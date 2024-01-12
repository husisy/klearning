# cryptography

## cryptography - Cyrill Gossi

Fundamental cryptography in theory and python

[youtube-link](https://www.youtube.com/playlist?list=PLWjMI9CAmVU4--SmpzgswTvxLkZqC9QWn)

[github-link](https://github.com/cgossi/fundamental_cryptography_with_python)

1. TOC
   * confidentiality
     * symmetric encryption: AES, ECB/CBC mode
     * asymmetric encryption: RSA
     * hybrid encryption
     * key exchange: EDH, ECDHE
   * integrity: hash function (MD5, SHA1)
   * authenticity: HMAC, encrypt-then-MAC
   * non-repudiation: digital signature
2. abbreviation
   * AES: advanced encryption standard (2001)
   * NIST: National Institute of Standards and Technology
   * AEAD: authenticated encryption with associated data
3. concept
   * cryptology, cryptography, cryptanalysis
   * plaintext
   * ciphertext
4. goal
   * confidentiality: information is only accessible to an authorized party
   * integrity: conrrectness and completeness of information can be verified
   * authenticity: source of information can be verified by a receiving party
   * non-repudiation: source of information can be verified by any third party
5. Symmetric encryption: AES
   * key length `128` bits
   * block cipher
   * confidentiality only mode: ECB (electronic codebook), CBC (cipher block chaining), PCBC (propagating CBC), CTR (counter), CFB (cipher feedback), OFB (output feedback)
   * AEAD mode: GCM (Galois/counter), SIV (synthetic intialization vector), CCM (counter with CBC-MAC), EAX (encrypt-then-authenticate-then-translate)
