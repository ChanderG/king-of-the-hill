#! /usr/bin/python

import hillcipher

def main():
    """ Interface to work with the Hill Cipher module."""
    hc = hillcipher.HillCipher()
    print "WIP."
    print "Init Key being used: \n{0}".format(hc.getKey())

    print "Setting random key of size 3:"
    hc.setRandomKey(3)
    print "New key is:"
    print hc.getKey()

if __name__ == "__main__":
    main()
