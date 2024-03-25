# number theory

1. link [youtube-link](https://www.youtube.com/playlist?list=PL22w63XsKjqxPO6pQ8wiZcIrtpTznGSre)
2. divisor: if $a$,$d$ is any integer, if $a=qd$ for some integer $q$, we say that $d$ is a divisor of $a$ written $d|a$
   * if $a|b$ and $b|c$, then $a|c$
3. greatest common divisor
   * let $a$ and $b$ be any two integers. Then an integer $d$ is called a common divisor of $a$ and $b$ if $d|a$ and $d|b$
   * Euclidean algorithm
   * linear combination: two integers $a,b$ (not both zero), if $d=gcd(a,b)$, then $d=ma+nb$ for some integers $m,n$ (possible non-unique)
4. [wiki/bezouts-identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)
5. relatively prime integers: **iff** $gcd(a,b)=1$
   * let $a,b$ be relatively prime integers and support $a|(bc)$ where $c$ is some integer, then $a|c$
   * integers $a,b,c$. suppose that $a,b$ are relatively prime and $a,c$ are relative prime. Then $a,bc$ are relatively prime
6. prime integers: let $p$ be an integer such that $p>1$, then $p$ is said to be prime if the only positive divisors are $1$ and $p$ itself
   * composite: not prime
7. Euclid's lemma: let $a$ and $b$ be any integers. if $p$ is prime and if $p|ab$, then either $p|a$ or $p|b$
8. fundamental theorem of arithmetic: suppose $n$ is an integer larger that $1$, then
   * $n$ is either a prime or a product of primes
   * the factorization of $n$ into a product of primes is unque except for the order of the factors
9. least common multiple (lcm)
   * $gcd(a,b)\cdot lcm(a,b)=ab$
10. modulo arithmetic
    * congruence modulo $n$: $a\equiv b ~mod~ n$
    * $14 ~mod~ 3 \equiv 2$, 14 mod 3 is congruent to 2
11. integers modulo n: addition, multiplication
12. [wiki-link](https://en.wikipedia.org/wiki/Integer_partition) integer partition
13. 费马小定理 Fermat's little theorem: 令$p$是一个素数，而$p\nmid a$, 则 $a^{p-1}\equiv 1 \bmod p$，等价的，$a^p\equiv a \bmod p$ [wiki](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
14. 欧拉定理 Euler's theorem: 令 $n\in \mathbb{N}_2$，而$gcd(a,n)=1$，则 $a^{\phi(n)}\equiv 1 \bmod n$ [wiki](https://en.wikipedia.org/wiki/Euler%27s_theorem)
    * 当$n$是素数，则退化为费马小定理
