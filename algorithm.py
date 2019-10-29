import  re

keyword = ["if", "read", "then", "else", "write", "repeat", "until", "end"]
symbols = ["+", "-", "*", "/", ":", "=", "<", "(", ")", ";"]
def scanner(string):
        #read_file = open("code.txt","r")
        write_file = open("output.txt","w+")
        #string = read_file.read()
        comment_flag = True
        string += " "
        token = ""
        iterator = -1
        for i in string :
            iterator+=1
            if i is '{':
                comment_flag = False
            if comment_flag is True :
                if  re.match(("[a-z|A-Z]" ),i):
                    token += i
                    if re.match(("[a-z|A-Z]" ),string[iterator+1]):
                       continue
                    elif string[iterator+1] in symbols or string[iterator+1] is " " or string[iterator+1] is '\t'or string[iterator+1] is '\n':
                       if token in keyword :
                          write_file.write(token)
                          write_file.write(" , ")
                          write_file.write(token.upper())
                          write_file.write("\n")
                          token=''
                       else:
                           write_file.write(token)
                           write_file.write(" , identifier\n")
                           token = ''
                    else:
                        write_file.write("ERROR")
                        return

                elif  re.match(("[0-9]" ),i):
                    token += i
                    if re.match(("[0-9]"), string[iterator + 1]):
                        continue
                    elif string[iterator+1] in symbols or string[iterator+1] is " " or string[iterator+1] is '\t'or string[iterator+1] is '\n':
                        write_file.write(token)
                        write_file.write(" , number\n")
                        token = ''
                    else:
                        write_file.write("ERROR")
                        return
                elif i in symbols:
                    if i is '+':
                        write_file.write(i)
                        write_file.write(" , Plus sign\n")
                    elif i is '-':
                        write_file.write(i)
                        write_file.write(" , minus sign\n")
                    elif i is '*':
                        write_file.write(i)
                        write_file.write(" , Multiply sign\n")
                    elif i is '/':
                        write_file.write(i)
                        write_file.write(" , Division sign\n")
                    elif i is ':' and string[iterator+1] is '=':
                        write_file.write(i+'=')
                        write_file.write(" , Assign\n")
                    elif i is '=' and string[iterator-1] is not ':' and iterator is not 0:
                        write_file.write(i)
                        write_file.write(" , Equal\n")
                    elif i is '<':
                        write_file.write(i)
                        write_file.write(" , Less than sign\n")
                    elif i is '(':
                        write_file.write(i)
                        write_file.write(" , left bracket\n")
                    elif i is ')':
                        write_file.write(i)
                        write_file.write(" , Right bracket\n")
                    elif i is ';':
                        write_file.write(i)
                        write_file.write(" , Semicolon\n")
                elif i is not " " and i is not "\n":
                    write_file.write("ERROR")
                    return
            elif comment_flag is False:
                if i is '}':
                    comment_flag = True
                else:
                    continue
        if comment_flag is False: #openning an { and didn't fold it }
            write_file.write('ERROR')
            return
        #read_file.close()
        write_file.close()
