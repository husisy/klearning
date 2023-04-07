# Cryptography

1. link
   * [cousera-link](https://www.coursera.org/learn/crypto/home/week/1)
   * a graduate course in applied cryptography [link](https://toc.cryptobook.us/)
   * a computational introduction to number theory and algebra [link](https://open.umn.edu/opentextbooks/textbooks/187)
2. concept
   * stream cipher
   * public key cryptography
   * key exchange
   * zero-knowledge, privacy mechanism
   * crypto primitives
   * cypertext only attack
3. application
   * web traffic: https (SSL/TLS)
   * wireless traffic: wifi (802.11i WPA2), well phone (GSM), bluetooth
   * encryption files on disk: EFS, TrueCrypt
   * content protection: DVD (CSS), Blue-ray (AACS)
   * user authentication
4. role
   * Alice: client
   * Bob: server
   * Eve: eavesdroping (confidentiality), tampering (integrity)
5. secure sockets layer (SSL) / TLS
   * handshake protocol: establish shared secret key using public-key cryptography
   * record layer: transmit data using shared secret key
6. symmetric encryption system
   * only secret key (e.g. 128 bits) is secret initialy, the encryption algorithm is publicly known
   * message `m`, secret key `k`, cipher `E,D`
   * `D(E(m,k),k)=m`
   * never use a proprietary cipher
7. one time key (encrypted email) and multi use key (encrypted file)
8. usage
   * secret key establishment
   * secure communication
   * digital signature
   * anonymous communication
   * anonymous digital cash
   * secure multi-party computation: election, private auctions
   * privately outsourcing computation
   * zero knowledge (proof of knowledge)
9. three steps
   * precisely specify threat model
   * propose a construction
   * prove that breaking construction under threat model will solve an underlying hard problem
10. history
    * @book the code breakers (1996), by David Kahn
    * substitution cipher
    * Caesar cipher
    * Vigener cipher
    * rotor machines (1870-1943)
    * the Enigma
    * 1974 data encryption standard (DES)
    * 2001 AES
    * 2008 Salsa20
11. descrete probability
    * [wikibook](https://en.wikibooks.org/wiki/High_School_Mathematics_Extensions/Discrete_Probability)
    * uniform distribution
    * point distribution
    * distribution vector
    * evenets: subset of universe
    * the union bound $P[A_1\cup A_2]\leq P[A_1] + P[A_2]$
    * (definition) random variable is a function $\mathrm{Pr}[X=v]:=\mathrm{Pr}[X^{-1}(v)]$
    * randomized algorithm
    * xor
    * theoremm: $Y$ a random variable over $\mathbb{F}_2^n$, $X$ an independent uniform random variable over $\mathbb{F}_2^n$, then $Y\oplus X$ is also a uniform random variable over $\mathbb{F}_2^n$
    * the birthday problem [wiki](https://en.wikipedia.org/wiki/Birthday_problem)
12. cipher: a pair of efficient algorithm $E,D$, key, message, ciphertext
    * message space $\mathcal{M}$, key space $\mathcal{K}$, ciphertext space $\mathcal{C}$
    * consistent equation: $\forall m\in\mathcal{M},k\in\mathcal{K}, D(k,E(k,m))=m$
    * $E$ is often randomized, $D$ is always deterministic
13. the one time pad (OTP) (Vernam 1917)
    * $E(k,m)=k\oplus m$
    * $D(k,c)=k\oplus c$
    * very fast to encrypt and decrypt
    * but long key
    * OTP has perfect secrecy
14. information theoretic security (Shannon 1949)
    * CT (ciphertext) should reveal no information about the PT (plaintext)
    * definition: TODO
    * perfect secrecy: $\forall m_0,m_1\in \mathcal{M},|m_0|=|m_1|,\forall c\in\mathcal{C}$, $k$ is a random varialbe, $\mathrm{Pr}[E(k,m_0)=c]=\mathrm{Pr}[E(k,m_1)=c]$
    * perfect secrecy: key length $|k|$ is at least as long as the message length $|m|$
    * no CT only attack
    * malleable (no integrity)
15. PRG (pesudo random generator)
    * must be unpredictable: no efficient algorithm can predict $i+1$ bit given the first $i$ bits, $\forall i$
    * linear congurence generator: bad, `glibc random()`
16. negligible and non-negligible
    * practically: $\epsilon\geq 2^{-30}$, $\epsilon\leq 2^{-80}$
    * theoretically $\epsilon:\; \mathbb{Z}^{\geq 0} \mapsto \mathbb{R}^{\geq 0}$
      * non-negligible: $\exists d, \epsilon(\lambda)\geq {\lambda^{-d}}$
      * negligible: $\forall d,\lambda\geq\lambda_d, \epsilon(\lambda)\leq {\lambda^{-d}}$
17. two time pad attack
    * example: project Venona (1941-1946), MS-PPTP (Windows NT, point-to-point tunneling protocol), 802.11b WEP, WEP (RC4)
    * network trafic: negotiate new key for every session (TLS)
    * disk encryption: typically do not use a stream cipher
18. stream ciphers
    * cannot have perfect secrey
    * RC4 (1987)
    * content scrambling system (CSS), linear feedback shift register (LFSR)
    * eStream, Salsa20
19. Yao's Principle [wiki](https://en.wikipedia.org/wiki/Yao%27s_principle)
20. semantically secure

## week2 block ciphers

1. block ciphers
   * 3DES (k=168 bits, m=64 bits, 48 rounds), AES (k=128/192/256 bits, m=128 bits, 10 rounds), Blowfish, Twofish
   * round function
   * pseudo random function $F:K\times X\to Y$
   * pseudo random permutation $E:K\times X\to X$, efficient inversion algorithm
2. pseudo random function is secure if a random function in $\mathrm{Funcs}[X,Y]$ is indistinguishable from a random function in $S_F$
3. given a pseudo random function $F:K\times \mathbb{F}_2^n\to \mathbb{F}_2^n$, then $G:K\times \mathbb{F}_2^n\to \mathbb{F}_2^{nt}$ is a secure PRG
   * $G(k)=F(k,0) | F(k,1) | \cdots | F(k,k) $
   * parallelizable
4. data encryption standard (DES)
   * 1970 IBM, Lucifer, key length 128 bits, block length 128 bits
   * 1973 IBM block cipher proposal
   * 1976 DES key length 56 bits, block length 64 bits
   * 2000 AES Rijndael
5. Feistel network
   * invertible
   * $f_1,f_2,\cdots,f_n$
   * each $f_i$ need indepdent key
6. exhaustive search
