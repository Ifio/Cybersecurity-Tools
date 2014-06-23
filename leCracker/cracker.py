#Program that cracks a password via bruteforce for Unix crypt(),
# zipfiles and SHA-512 encryption algorithm*/
#/*By Jason Carcamo C. */
#/*June, 2014*/

import optparse
import os
import cryptMethod
import zipMethod
import shaMethod

#To chose the correct action for the given parameters
def getSalt(method, passwd):

    dicc ={
        1: cryptMethod.getSalt(passwd),
        2: cryptMethod.getSalt(passwd),
        3: shaMethod.getSalt(passwd)
    }
    return dicc[method]

#To chose the correct algorithm for the given parameters
def crack(method, passwd, word, salt, fileName):

    diccio = {
        1: cryptMethod.crypter(passwd, word, salt),
        2: zipMethod.extractZip(fileName, passwd),
        3: shaMethod.crypter(passwd, word, salt)
    }
    return diccio[method]

def select(encMethod, diccio, passwdFile, fileName):
    #To open file with passwords to crack
    p = open(passwdFile, "r")

    #To obtain the salt of every password in the file
    for line in p.readlines():
        thePassword = line.strip('\n')
        salt = getSalt(encMethod, thePassword)

        f = open(diccio, "r")
        #To compare every word with the given password
        for word in f.readlines():
            print crack(encMethod, thePassword, \
                        word.strip('\n'), salt, fileName)

def main():
    #To obtain console arguments, to be able to use them.
    parser = optparse.OptionParser("Usage%prog: " + \
                                   "[-h | ["
                                   "-m <encryption> -d <diccionary>" +\
                                   " -p <passwdfile> [ |-f <filename>]]")
    #To specify the meaning of the flags, and store the value.
    parser.add_option("-m", dest = "encMethod", type = "int", \
                      help = "(1) - crypt(), (2) - zipfile, (3) - shacrypt")
    parser.add_option("-d", dest = "diccio", type = "string", \
                      help = "file with common-password words")
    parser.add_option("-p", dest = "passwdFile", type = "string", \
                      help = "file with passwords")
    parser.add_option("-f", dest = "fileName", type = "string", \
                      help = "name of file to be cracked via zip method.")

    (options, args) = parser.parse_args()

    #To ensure that all parameters needed are given.
    if ((options.encMethod == None) | (options.diccio == None)
        | (options.passwdFile == None)):
        print parser.usage
        exit(1)
    else:
        encMethod = options.encMethod
        diccio = options.diccio
        passwdFile = options.passwdFile
        fileName = options.fileName

        #To verify the existence of the files and their permissions
        if not os.path.isfile(diccio):
            print "- " + diccio + " file does not exist."
            exit(0)
        elif not os.access(diccio, os.R_OK):
            print "- " + diccio + " acess denied."
            exit(0)
        elif not os.path.isfile(passwdFile):
            print "- " + passwdFile + " file does not exist."
            exit(0)
        elif not os.access(passwdFile, os.R_OK):
            print "- " + passwdFile + " access denied."
            exit(0)
        else:
            select(encMethod, diccio, passwdFile, fileName)

if __name__ == "__main__":
    main()
