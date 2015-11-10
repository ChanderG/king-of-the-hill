""" Main Cryptanalysis module."""

import helpers
import numpy as np

def attackHillCipher(ptnos, ctnos, key_size):
    """ Hill Cipher attack helper.

    INPUT
    ---------
    ptnos -- plaintext converted to numbers
    ctnos -- ciphertext converted to numbers
    key_size -- attack size

    OUPUT
    --------
    None if attack fails.
    The Key if successful.

    """

    # obtain candidates to create the matrix
    ptcand = ptnos[:key_size*key_size]
    ctcand = ctnos[:key_size*key_size]

    ptmat = np.matrix(ptcand)
    ptmat = np.reshape(ptmat, (key_size, key_size))

    ctmat = np.matrix(ctcand)
    ctmat = np.reshape(ctmat, (key_size, key_size))

    invptmat = helpers.inversematrix(ptmat, 29) 
    if invptmat == None:
        return None

    invptmat = helpers.takeMod(invptmat, 29)
    key = invptmat*ctmat
    key = helpers.takeMod(key, 29)

    ptcheck = ptnos[key_size*key_size:key_size*key_size + key_size]
    ctcheck = ctnos[key_size*key_size:key_size*key_size + key_size]

    ptcheckmat = np.matrix(ptcheck)

    ctcheckmat = ptcheckmat*key
    ctcheckmat = helpers.takeMod(ctcheckmat, 29)
    ctcheckmat = ctcheckmat.tolist()[0]

    if ctcheckmat == ctcheck:
        return key
    return None

def cryptanalyzeHillcipher(plaintext, ciphertext):
    """ Cryptanalyze the Hill Cipher.

    Runs a known plaintext attack.

    INPUT
    --------
    plaintext -- the known plaintext
    ciphertext -- the corresponding ciphertext
    
    Outputs the Key of the cipher.
    
    Works only for key sizes upto 5x5.
    """

    # sanity check for plaintext/ciphertext
    if len(plaintext) != len(ciphertext):
        print "Length of plaintext/ciphertext pair does not match."
        return 

    # naive check for amount of text input
    # we need k*k + k amount of data
    # check for upperbound -> at least 30
    if len(plaintext) < 30:
        print "Not enough plaintext/ciphertext to launch attack."
        print "Need 30 characters or more."
        return

    # convert text to numerical array
    ptchars = list(plaintext)
    ptnos = map(lambda x: ord(x) - ord('a'),ptchars)

    ctchars = list(ciphertext)
    ctnos = map(lambda x: ord(x) - ord('a'),ctchars)

    suspect_key_size = 2 
    res = None
    while True:
        res = attackHillCipher(ptnos, ctnos, suspect_key_size)
        if res == None:
            suspect_key_size += 1
            if suspect_key_size == 6:
                break
        else:
            break

    if res == None:
        print "Unable to break the cipher."
    else:
        print "Successfully cracked the cipher: "
        print res