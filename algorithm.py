import  re

keyword = ["if", "read", "then", "else", "write", "repeat", "until", "end"]
symbols = {"+":"Plus sign", "-":"minus sign", "*":"Multiply sign", "/":"Devision sign", ":":"Assign", \
    "=":"Equal", "<":"Less than sign", "(":"left bracket", ")":"right bracket", ";":"Semicolon"}
spaces = ["\n","\t"," "]
def scanner(string):
        myout = ""
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
                    elif string[iterator+1] in symbols or string[iterator+1] in spaces:
                        if token in keyword :
                            myout += token + " , " + token.upper()+"\n"
                            token=''
                        else:
                           myout += token + " , identifier\n"
                           token = ''
                    else:
                        myout += "ERROR"
                        return myout

                elif  re.match(("[0-9]" ),i):
                    token += i
                    if re.match(("[0-9]"), string[iterator + 1]):
                        continue
                    elif string[iterator+1] in symbols or string[iterator+1] in spaces:
                        myout += token + " , number\n"
                        token = ''
                    else:
                        myout +="ERROR"
                        return myout
                elif i in symbols:
                    if i is ':' and string[iterator+1] is '=':
                        myout += i + "=" + " , " + symbols[i] +"\n"
                    elif i is not ':':
                        myout += i + " , " + symbols[i] +"\n"
                elif i is not " " and i is not "\n":
                    myout +="ERROR"
                    return myout
            elif comment_flag is False:
                if i is '}':
                    comment_flag = True
                else:
                    continue
        if comment_flag is False: #openning an { and didn't fold it }
            myout +="ERROR"
            return myout
        return myout
