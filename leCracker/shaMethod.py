#/*By Jason Carcamo C. */
#/*June, 2014*/

import crypt

def crypter(passwd, word, salt):
    #To encrypt in using sha512 encryption ($6$)
    encrypt = crypt.crypt(word, "$6$"+salt)

    if passwd == encrypt:
        return "Password match! \n\t the password for : " + passwd + \
            ", is: " + word
    else:
        return "Password missmatch."

def getSalt(passwd):
    #To substring the salt from the password
    start = passwd.find("$6$")
    nextSign = passwd.find("$", start + 3)
    salt = passwd[start + 3:nextSign]
    return salt
