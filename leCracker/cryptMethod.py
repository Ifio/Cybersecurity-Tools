#/*By Jason Carcamo C. */
#/*June, 2014*/

import crypt

def getSalt(passwd):
    return passwd[:2]

def crypter(passwd, word, salt):
    #To encrypt the passwdcompString with the given salt
    encrypt = crypt.crypt(word, salt)
    #To compare the password with the diccionary word
    if encrypt == passwd:
        return "Password match! \n \t The password for " + passwd + \
            " is : " + word
    else:
        return "Password missmatch."
