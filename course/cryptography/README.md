# Cryptography

coursera course is recorded on 2012-06

如何在一个月内入门密码学 [zhihu-link](https://www.zhihu.com/question/36289177)

RSA: a simple and easy-to-read implementation (python recipe) [link](https://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/)

## coursera/cryptography

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
   * ideal cipher
   * DES challenge
   * meet in the middle attack: 2DES doesn't solve the exhasutive search problem
   * DESX
7. attack
   * side channel attacks: measure time/power to do encode and decode
   * fault attacks: computing errors in the last round expose the secret key
   * linear crypt-analysics
   * quantum attack
8. AES: Rijndael (Belgium), substitution-permutation network (SPN)
   * 128/192/256 bits key, 128 bits block
   * bytes substitution, shift row, mix column
   * Intel: `aesenc,aesenclast,aeskeygenassist`
   * best key  recovery attack `2^126`
   * related key attack on AES256 `2^99`
9. build pseudo random function (PRF) from pseudo random geneerator (PRG)
   * GGM's construction [wiki](https://en.wikipedia.org/wiki/Pseudorandom_function_family)
10. secure PRF
11. PRF switching lemma: any secure PRP is also a secure PRF, if $|X|$ is sufficiently large
12. one-time keys, many-time keys (chosen-plaintext security)
13. electronic code block (ECB), Deterministic counter mode
14. semantic security for many-time key
    * adversary's power: chosen plaintext attack (CPA)
    * randomized encryption
    * nonce-based encryption (nounce is never repeat)
      * nouce is a counter (packet counter)
15. cipher block chain (CBC) with random IV
16. random conunter mode
    * parallelizable

week3 message integrity

1. message integrity, no confidentiality
2. message authentication code (MAC)
   * signing algorithm $tag=S(k,m)$, verification algorithm $V(k,m,tag)=1/0$
   * chosen message attack
   * existential forgery
     * produce some new valid message tag pair (not necessarily the all message)
     * given $(m,t)$, attack cannot even produce $(m,t')$ for $t'\ne t$ (important when combining with encryption)
   * to defend sapping of authenticated data: include filename in the MACed area
3. CRC (cyclic redundancy check): designed to detect random error, NOT malicious error
4. any secure PRF is also a secure MAC
5. AES as MAC
   * convert small-MAC to big-MAC: CBC-MAC (banking, ANSI X9.9), HMAC (internet protocols, SSL, IPsec, SSH)
   * truncating MACs based on PRF
6. encrypted CBC-MAC
   * `k1,k2`
   * require PRP
   * raw CBC (1 key only) is not MAC secure
   * secure as long as $q\lleq |X|^{1/2}$
   * commonly used as an AES based MAC: CCM encryption mode (802.11i), NIST standard called CMAC
7. NMAC nested MAC
   * `k1,k2`
   * require PRF
   * raw NMAC (cascade function) is not MAC secure (extension attack)
   * secure as long as $q\lleq |K|^{1/2}$
   * not usually used with AES or 3DES: need to change AES key on every block (require AES key expansion)
   * the basis for HMAC
8. CBC-MAC padding: ISO pad with `10000...00`
9. CMAC (NIST standard)
   * `k,k1,k2`
   * no final encrption step: extension attack thwarted by last keyed xor
   * no dummy block: ambiguity resolved by use of `k1` or `k2`
10. PMAC
    * parallelizable
    * incremental
    * require $F$ PRP
    * block swapping attack
    * `k,k1`
11. one time MAC: secure against all attack, faster than PRF-based MAC
12. Carter-Wegman MAC:many time MAC
13. HMAC (hash-based MAC)
14. collision resistance
15. collision resistant function: if for al explicit efficient algorithm, the probability of finding a collision is negligible
    * no key needed (public verifiability)
    * require read-only space
    * generic birthday attack
16. SHA-1/256/512 (Secure Hash Algorithm)
    * 2017/02/23: SHA-1 collision found
17. Merkle-Damgard paradigm
    * padding block: include block length, maximum length $2^{64}$
    * compression function
    * MD collision resistance
18. compression function from a block cipher
    * Davies-Meyer compression function: given a block cipher $E:K\times \mathbb{F}_2^n\to\mathbb{F}_2^n$ $h(H,m)=E(m,H)\oplus H$
    * Miyaguchi-Preneel
19. SHA-256
    * Merkle-Damgard function
    * Davies-Meyer compression function
    * Block cipher: SHACAL-2, 512 bit key (message), 256 bit key (state $H$)
20. provable compression function
    * finding collision is as hard as solving "discrete log" modulo p
    * slow
21. HMAC
    * build a MAC from a hash function: $S(k,m)=H(k\oplus \mathrm{opad}, H(k\oplus \mathrm{ipad})||m)$
    * different from NMAC PRF: the so-called "k1,k2" in HMAC are dependent (only "k")
22. time attacks

week 4 anthenticated encryption (2000)

1. encrption secure against tampering (authenticated encryption)
   * confidentiality: eavesdropping, CPA-secure (Chosen Plaintext Attack)
   * integrity: existential unforgeability, chosen message attack, CBC-MAC, HMAC, PMAC, CW-MAC, NMAC
2. example
   * TCP/IP, IPsec, SSL, SSH
   * CBC with random IV does not provide integrity
3. authenticated encryption: a cipher $E: K\times M (\times N)\to C$, $D:K\times C(\times N)\to M\cup \bot$
   * security: semantic security, CPA-secure
   * ciphertext integrity
   * donot prevent replay attack
   * donot account for side channels (timing, power)
4. chosen ciphertext attack
   * can obtain the encryption of arbitrary messages of his choice
   * can decrypt any ciphertext of his choice, other than challenge ciphertext (from encoders)
5. combining MAC and encryption
   * MAC-then-encrypt (SSL): $E(k_E, m||S(k_I, m))$
     * may be insecure against chosen cypertext attack (CCA)
   * encrypt-then-MAC (IPsec): $E(k_E, m) || S(k_I, E(k_E, m))$
     * always correct
   * encrypt-and-MAC (SSH): $E(k_E, m) || S(k_I, m)$
     * not good: the output of the MAC signing algorithm might leak bits of the message
6. MAC-then-encrypt
   * when (E,D) is random-counter mode or random-CBC, then provides authenticated encryption
   * when (E,D) is random-counter mode, then one-time MAC is sufficient
7. standard: all are nounce based, all support AEAD (authenticated encryption with associated data)
   * (NIST) GCM (Galois counter mode): counter mode encrytion with CW-MAC
   * (NIST) CCM (CBC counter mode): CBC-MAC then counter mode encryption (802.11i)
   * EAX: counter mode encryption then CMAC
8. MAC security $(m,t)\not\Rightarrow(m,t')$
9. OCB: a direct construction from a PRP (patent issue)
10. the TLS record protocol
    * header
    * unidirectional keys: one key for each direction (send and receive)
    * stateful encryption: two `64bit` counters (against replay attack)
11. bugs in TLS older version (version `<1.1`)
    * (chained IV) IV for next record is last ciphertext block of current record, NOT CPA secure (BEAST attack)
    * padding oracle: alert `decryption_failed` and `bad_record_mac`. when decrption fails, do NOT explain why
    * TLS renegotiates key when an invalid record is received
    * IMAP over TLS
12. 802.11b WEP
    * two time pad
    * related PRG seeds
    * CRC checksum is linear: $\forall m,p, \mathrm{CRC}(m\oplus p)=\mathrm{CRC}(m)\oplus F(p)$
13. SSH binary packet protocol
    * encrypt-and-MAC: CBC encryption with chained IV
    * attack on the encryption length: non-atomic decryption, length field decrypted and used before authentication
    * solution: send the length field unencrypted, add a MAC of (sequence number, length field) right after the length field
14. key deriving
    * single source key (SK): hardware random number generator, key exchange protocol
    * key derivation function (KDF): derive multiple keys from SK
    * given a PRF $F$, $\mathrm{KDF}(SK,CTX,L)=F(SK,(CTX||0)) || F(SK,(CTX||1)) || \cdots || F(SK,(CTX||L))$
    * context (CTX): a string that identifies the purpose of the key, specific to application
15. extract-then-expand paradigm
    * computational extractor: indistinguishable from a random function
    * salt
16. HKDF: a KDF from HMAC
17. PBKDF: password-based KDF
    * password have insufficient entropy (vulnerable to dictionary attack)
    * salt, slow has function
    * `PKCS#5`
18. deterministic encryption
    * encrypted database: index, record
    * problem: deterministic encryption cannot be CPA secure
19. deterministic CPA security
    * CBC with fixed IV is not deterministic CPA secure
20. Synthetic IV (SIV)
    * given PRF `F`, `r <- F(k1,m), c <- E(k2,m,r)`
    * well suited for message longer than one AES block (16 bytes)
    * deterministic authenticated encryption (DAE)
21. PRP: deterministic CPA secure for 16 bytes messages
    * integrity: append `80bit` zero to the message, then PRP
22. construct PRP (DAE) for longer message space
    * EME: constructing a wide block PRP, performance can be 2 times slower than SIV
23. disk encrption: no expansion, PRP, deterministic encryption (no integrity)
    * master key, derived key using a PRF
24. tweakable encryption: $E,D:K\times T\times X\to X$
    * use sector number as the tweak
    * XTS tweakable block cipher: block-level PRP, not sector-level PRP
25. format preserving encryption
    * credit card format (around 42 bits): BIN number (first 6 digits), account number (next 9 digits), check digit (last digit)
    * Luby-Rackoff (truncate), Feistel construction

week5 public key cryptography

1. trusted 3rd parties
2. key exchange
3. online trusted 3rd party (TTP)
   * toy protocol: eavesdropping security, ticket
   * TTP: needed for every key exchange, know all session keys
   * example: kerberos system
   * insecure against replay attacks (active attack)
4. starting point of public key cryptography
   * 19974 Merkle
   * 1976 Diffie-Hellman
   * 1977 RSA
   * 2001 BF, ID-based encryption
   * 2011 BSW, functional encryption
5. Merkle puzzles
   * puzzles: problems that can be solved with some effort
   * Alice send $2^32$ puzzles to Bob: each puzzle $E(0^96||P_i, "Puzzle"||x_i||k_i)$, random $P_i\in \mathbb{F}_2^{32}$, $x_i,k_i\in \mathbb{F}_2^{128}$
   * Bob randomly solve a puzzle $P_j,x_j,k_j$, and send $x_j$ to Alice
   * Alice lookup puzzle with number $x_j$, use $k_j$ as shared secret
   * Alice's work $O(n)$ (here $n=2^{32}$), Bob's work $O(n)$, Eavesdropper's work $O(n^2)$
   * conclusion: roughly speaking, quadratic gap is best possible if we treat cipher as a black box oracle [arxiv-link](https://arxiv.org/abs/0801.3669v1)
6. Diffie-Hellman protocol (informally), arithmetic modulo of primes
   * fix a prime number $p$ (around 600 digits, 2000 bits) and an integer $g\in \mathbb{F}_p$
   * Alice random choose $a\in \mathbb{F}_p$ and send $A=g^a \pmod{p}$ to Bob
   * Bob random choose $b\in \mathbb{F}_p$ and send $B=g^b \pmod{p}$ to Alice
   * secret key $k=g^{ab}=B^a=A^b$
   * insecure against man-in-the-middle attack (active attack)
7. Diffie-Hellman function $\mathrm{DH}_g(g^a,g^b)=g^{ab} \pmod{p}$
   * suppose prime $p$ is $n$ bits long
   * best known algorithm, general number field sieve (GNFS): $exp(\tilde{O}(\sqrt[3]{n}))$
   * (cipher key size (bit), modulus size (bit)): `(80,1024), (128,3072), (256,15360)`
   * non-interactive properties
   * n-partite Diffie-Hellman problem: 3-partites (Joux algorithm [doi-link](https://doi.org/10.1007/s00145-004-0312-y)), 4-partites (open problem)
8. elliptic curve
   * (cipher key size (bit), modulus size (bit)): `(80,160), (128,256), (256,512)`
9. public key encryption: a triple of algorithm $G,E,D$
   * $G$: key generation algorithm (randomized algorithm), $G()$ outputs a pair of keys $(pk,sk)$
   * $E(pk,m)$: randomized algorithm
   * $D(sk,c)$: deterministic algorithm, output $m\in \mathcal{M}$ or $\bot$
   * insecure against man-in-the-middle attack
10. public key encryption semantic security
    * Challenger: $pk,sk\leftarrow G()$, give $pk$ to Adversary
    * Adversary: send $m_0,m_1\in\mathcal{M}$ with $|m_0|=|m_1|$
    * Challenge: send $c_b=E(pk,m_b)$ to Adversary
    * $EXP(b)$: Adversary's outputs for $c_b$
    * semantic secure: if advantange $Adv_{SS}[A,(G,E,D)]=|Pr[EXP(0)=1]-Pr[EXP(1)=1]|$ is negligible

Number theory

1. target: key exchange protocols, digital signatures, public key encryption
2. reference
   * victor Shoup's homepage [link](https://shoup.net/)
   * a computational introduction to number theory and algebra [link](https://shoup.net/ntb/)
3. notation
   * $\mathbb{Z}/n\mathbb{Z}=\left\{0,1,2,\cdots,n-1\right\}$
   * $\mathbb{Z}_n=\mathbb{Z}/n\mathbb{Z}$ (not strictly correct, but universal used)
   * $\mathbb{Z}_n^*=\left\{x\in\mathbb{Z}_n:\gcd(x,n)=1 \right\}$
   * $n=p^k$ where $p$ is a prime, then $\mathbb{Z}_n=\mathbb{F}_p^k$ is a finite (Galois) field
   * $\mathbb{P}$: prime number (not universal used)
4. modular arithmetic (ring algebra)
   * greatest common divisor (gcd)
   * extended Euclidean algorithm
   * $x\in\mathbb{Z}_n$ has an inverse iff $gcd(x,N)=1$
   * modular linear equations in $\mathbb{Z}_n$: $a\cdot x+b=0$, $x=-b\cdot a^{-1}$, run time $O(\log^2(n))$
5. Fermat's theorem (1640): $p\in\mathbb{P},\forall x\in\mathbb{Z}_p^*,x^{p-1}=1\pmod{p}$
6. Miller-Rabin test: generating random primes of length 1024bits
   * choose a random integer $p\in [2^1024,2^1025-1]$, test if $2^{p-1}==1\pmod{p}$, if yes, then $p$ is a prime
   * $Pr[p\notin \mathbb{P}]<2^{-60}$
   * not the best algorithm
   * round expectation: around several hundred
7. for $p\in\mathbb{P}$, $(\mathbb{Z}_p^*,\cdot)$ is a cyclic group
   * generator $g$, $\mathbb{Z}_p^*=\left\{1,g,g^2,\cdots,g^{p-2}\right\}=\langle g\rangle$
   * not every elemnent is a generator
   * $\mathrm{ord}_p(x)=|\langle x\rangle|$
   * Lagrange theorem: $\forall x\in\mathbb{Z}_p^*$, $\mathrm{ord}_p(x)$ divides $p-1$
8. Euler's generalization of Fermat (1736)
   * Euler's $\phi$ function: $n\in\mathbb{Z}^+$, $\phi(n)=|\mathbb{Z}_n^*|$
   * $p\in\mathbb{P}$, $\phi(p)=p-1$
   * $p,q\in\mathbb{P}$, $\phi(pq)=(p-1)(q-1)$
   * Euler theorem: $\forall x\in\mathbb{Z}_n^*,x^{\phi(n)}=1\pmod{n}$
9. modular e'th roots: $p\in\mathbb{P},c\in\mathbb{Z}_p$
   * e'th root: if $x^e=c\pmod{p}$, $x$ is called an e'th root of $c$
   * e'th root does not exist if $gcd(e,\phi(p))\neq 1$, e.g. $2^{1/2}$ in $\mathbb{Z}_{11}$
   * if $\gcd(e,p-1)=1$, $c^{1/e}$ always exists and easy to found
   * quadratic residue: if $x$ has a square root in $\mathbb{Z}_p$ (2-to-1 function)
   * Euler's theorem: iff $x^{(p-1)/2}=1\pmod{p}$
   * Legendre symbol of $x$ over $p$: $x^{(p-1)/2}$
   * extended Riemann hypothesis
   * computing e'th roots mod $n$ (composite number $n$, $e>1$) requires the factorization of $n$
10. repeated squaring algorithm (exponential)
11. $p\in \mathbb{P}$, polynomial $f(x)\in \mathbb{Z}_p[x]$, find $x\in \mathbb{Z}_p$ s.t. $f(x)=0$, running time is linear in degree of $f$
12. discrete logarithm problem: $p\in\mathbb{P},g\in\mathbb{Z}_p$ $\mathrm{Dlog}_g(g^x)=x$
13. discrete logarithm
    * cyclic group, generator
    * example: $Z_p^*$ for large $p$, elliptic curve groups mod $p$ (harder)
    * application: collision resistance hash function

week6

1. public key encryption
2. application: session setup, non-interactive application (email, require public key management)

## 知乎/稀有气体

1. link
   * 知乎/稀有气体 [zhihu-link](https://www.zhihu.com/column/c_1190932930565013504)
2. abbreviation
   * TXID: transaction ID
   * UTXO: unspent transaction output [wiki](https://en.wikipedia.org/wiki/Unspent_transaction_output)
3. concept
   * 椭圆加密方程
   * RSA
   * zero coin, zero cash
   * UTXO model versus account model
4. merkle tree, merkle proof [wiki-link](https://en.wikipedia.org/wiki/Merkle_tree) [csdn-link](https://blog.csdn.net/wo541075754/article/details/54632929)
   * second preimage attack
   * application
     * Lamport one-time signature, Merkle signature scheme
     * P2P network
     * trusted computing
     * Inter Planetary File System (IPFS)
     * BitCoin, Ethereum (Merkle Patricia Tree)
5. 匿名 anonymous, 假名 pseudonymous
6. bitcoin
   * 不足：交易链条分析 [Chainalysis](https://demo.chainalysis.com/)
   * CoinJoin: 要求交易额度相同，概率性匿名，
   * confidential transaction 私密交易：需要同态加密
   * Pedersen commitment:
     * 负数漏洞，range proof
     * 所有权漏洞, shielded transaction, world state (Ethereum)
7. blockchain scaling
   * 牺牲共识强度增加出块强度
   * 启用侧链
   * 类似于lightning的线下点对点通道
   * rollup

## homomorphic encryption

1. [secbit-blog-link](https://secbit.io/blog/2019/12/25/learn-zk-snark-from-zero-part-one/)
2. finite field $(\mathbb{Z}_q,+,\cdot)$ for $q=p^k,p\in\mathbb{P},k\in\mathbb{N}_1$
3. $a,g\in\mathbb{Z}_q$ denote public known values ($g$ might be generator of the $\mathbb{Z}_q$)
4. $x,y\in\mathbb{Z}_q$ denote private values

| operation | encrypted operation |
| :-: | :-: |
| $x$ | $E(x)=g^x$ |
| $x+y$ | $E(x)\cdot E(y)=g^{x+y}$ |
| $a\cdot x$ | $(E(x))^a=g^{a\cdot x}$ |
| $x\cdot y$ | NA |

## zero knowledge proof

1. link
   * 郭宇/零知识证明 [secbit-website](https://secbit.io/) [secbit-blog](https://secbit.io/blog/) [github/scebit](https://github.com/sec-bit)
   * Maksym Petkus [medium-link](https://medium.com/@imolfar)
   * Schwartz–Zippel lemma [wiki-link](https://en.wikipedia.org/wiki/Schwartz%E2%80%93Zippel_lemma)
2. abbreviation
   * SNARK: Succinct Non-interactive ARgument of Knowledge
   * ZKP: Zero Knowledge Proof
   * KEA: knowledge of exponent assumption
3. concept
   * zk-SNARK: zero knowledge proof protocol
   * ZKP: extractor
4. zk-SNARK应用
   * 证明关于隐私数据的声明：A的账余额多余`x`
   * 匿名认证：证明自己是某个群组的成员，而不需要透露自己的身份
   * 匿名支付：纳税而不透露收入
   * 外包计算（零信任计算）
5. zkp性质：称述statement, prover, verfier
   * 完整性：如果statement正确，prover总能说服verifier
   * 可靠性：如果statement错误，prover就不能说服verifier
   * 零知识：协议不泄露statement以外的信息
6. zkp protocol
   * 位检测协议
   * polynomial identity testing [wiki-link](https://en.wikipedia.org/wiki/Polynomial_identity_testing)
7. 加密多项式协议：prover (P) 要向verifier (V)证明$t(x)$是$p(x)$的因子而不暴露$p(x)$
   * 已知
     * finite field $(\mathbb{Z}_q,+,\cdot)$, generator $g\in\mathbb{Z}_q$
     * $p,t\in K[x]$ polynomial ring over field $\mathbb{Z}_q$
     * $E(x)=g^x:\mathbb{Z}_q\mapsto\mathbb{Z}_q$
     * $p(x)=p_0+p_1x+\cdots,p_d x^d$
     * $h(x)=p(x)/t(x)=h_0+h_1x+\cdots h_m x^m\in K[x]$, $m\leq d$
     * P privately holds $p(x)$ and $h(x)$
     * $t(x),g$ are public
   * V: $s\leftarrow_r \mathbb{Z}_q$
   * V: send $\left\{E(s^i):i=0,1,\cdots,d\right\}$ to P
   * P: evaulate $E(p(s))=\prod_i E(s^i)^{p_i}$
   * P: evaluate $E(h(s))=\prod_i E(s^i)^{h_i}$
   * P: send $E(p(s)),E(h(s))$ to V
   * V: verify $E(h(s))^{t(s)}=E(p(s))$

## Elliptic Curve Cryptography

1. link
   * andrea-corbellini-blog [link](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/)
   * ars-technica [blog-link](https://arstechnica.com/information-technology/2013/10/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/3/)
   * 知乎/椭圆曲线和国密算法 [zhihu-link](https://www.zhihu.com/column/c_125618851)
   * 知乎/隐私计算 [zhihu-link](https://www.zhihu.com/column/c_1433891764852158464)
2. abbreviation
   * ECC: elliptic curve cryptography
   * ECDH: elliptic curve Diffie-Hellman [wiki-link](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)
   * ECDSA: elliptic curve digital signature algorithm [wiki-link](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
   * ECDLP: elliptic curve discrete logarithm problem
3. elliptic curve
   * Weierstrass normal form: $y^2=x^3+ax+b$
   * $\left\{ (x,y)\in\mathbb{Z}_q^2:y^2=x^3+ax+b \pmod{q} \right\}\cup \left\{\infty\right\}$
   * $4a^3+27b^2\ne0 \pmod{q}$ (no singularities)
   * $\mathrm{char}(\mathbb{Z}_q)>3$
   * Schoof's algorithm [wiki](https://en.wikipedia.org/wiki/Schoof's_algorithm)
   * group operation of elliptic curves: Abelian group with $\infty$ as identity

## Post-Quantum Cryptography

Chris Peikert QIP2022 [youtube-link](https://youtu.be/dbP2cgTsrRo)

1. why PQC
   * we cannot wait until Big QCs are more imminent
   * harvesting attacks: store today's keys/ciphertexts to break later
   * rewriting history: forge signatures for old keys
   * deploy new cryptography at scale takes a long time
   * NIST PQC standardization process (2016)
2. concept
   * lattices, isogenies, multivariate quadratic
3. lattice-based cryptography advantage
   * efficient: linear, parallel operations
   * resists quantum attacks
   * security from mild worst-case assumptions
   * solutions to "holy grail" problems in crypto: FHE and related
4. lattice: full-rank additive subgroup
5. worst-case to average-case reduction
6. trapdoors for hard lattices and new cryptographic constructions [doi-link](https://doi.org/10.1145/1374376.1374407)
7. signatures in practice
   * Falcon: fast lattice-based compact signatures over NTRU [website](https://falcon-sign.info/)
   * dilithium: CRYSTALS-Dilithium Algorithm Specifications and Supporting Documentation [pdf](https://pq-crystals.org/dilithium/data/dilithium-specification-round3-20210208.pdf) [github-link](https://github.com/pq-crystals/dilithium)
8. public key encryption: LWE in paractice
   * Frodo (KEM)
