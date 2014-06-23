LeCracker
=========

LeCracker is an small python program, to introduce bruteforce password cracking.

For unix crypt(), zipfiles and sha-512 encryption algorithm.

    Author: Jason Cárcamo C.
    Date: June 22nd.

Version
----
1.0

Usage
-----------

    usage: python cracker.py [-h | {args}]
    args = [ -m <encryption> -d <diccionary> -p <passwdfile> [ |-f <filename>] ]
            -m ENCMETHOD   (1) - Crypt(), (2) - ZipFiles, (3) - SHA-512
            -d DICCIO      file with common-password words
            -p PASSWDFILE  file with passwords
            -f FILENAME    name of file to be cracked via zip method.

Example
-----
    1. Python cracker.py -m 1 -d passdiccio.txt -p passwdFile.txt
    2. Python cracker.py -m 2 -d passdiccio.txt -p passwdFile.txt -f zipped.zip

License
------------
This python program is an introduction to bruteforce password cracking.
Some of this code is based on **TJ. O’Connor, Violent Python:
A Cookbook for Hackers, Forensic Analysts,
Penetration Testers and Security Engineers.**

Permission is hereby granted, free of charge, to any person who wants to test,
modify and improve the script.