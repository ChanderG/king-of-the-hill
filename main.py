#! /usr/bin/python

import hillcipher

def main():
    """ Interface to work with the Hill Cipher module."""
    hc = hillcipher.HillCipher()
    print "WIP."
    print "Init Key being used: \n{0}".format(hc.getKey())

    """
    print "Setting random key of size 2:"
    hc.setRandomKey(2)
    print "New key is:"
    print hc.getKey()
    """

    plaintext = 'july'
    print "Encrypting a plaintext: '{0}':".format(plaintext)
    print hc.encryptText(plaintext)

if __name__ == "__main__":
    main()
