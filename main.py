#! /usr/bin/python

import hillcipher
import logging

def main():
    # setup simple logging
    logging.basicConfig(level = logging.DEBUG,
                        format = '%(levelname)s : %(message)s',
                        filename = './hillcipher.log',
                        filemode = 'w')

    logging.info('Starting main')
    """ Interface to work with the Hill Cipher module."""
    hc = hillcipher.HillCipher()
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

    ciphertext = hc.encryptText(plaintext)
    print "Decrypting a ciphertext: '{0}':".format(ciphertext)
    print hc.decryptText(ciphertext)

    plaintext = "hithere|howareyou|iamfine|sendmanymenttothebatteredplainstonight|theambushisabouttogodown|" 
    ciphertext = hc.encryptText(plaintext)
    hillcipher.cryptanalyzer.cryptanalyzeHillcipher(plaintext, ciphertext)
    logging.info('Ending main')

if __name__ == "__main__":
    main()
