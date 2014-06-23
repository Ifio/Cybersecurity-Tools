#/*By Jason Carcamo C. */
#/*June, 2014*/

import zipfile

def extractZip(zfile, passwd):
    try:
        #To extract the file if the password is correct
        zfile.extractall(pwd = passwd)
        return "Password --> " + passwd
    except:
        #To keep testing passwords in case one fails
        return "Password missmatch."
        pass
