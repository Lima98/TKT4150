#import "@preview/dvdtyp:1.0.1": *

#show: dvdtyp.with(
  title: "Exercise 0",
  subtitle: [TKT4150 - Biomechanics],
  author: "Jan-Øivind Lima",
  accent: highlight,
)

#show link: underline
#show link: set text(fill: highlight)

#set math.mat(delim: "[")

#outline(depth: none)

== Preliminaries
This section was only lots of recap of earlier courses, there did not seem to be any exercised to be completed here.

== Linear Algebra and Matrix analysis
Given $A = mat(1,2,3;4,5,6;7,8,9), bold(a)=mat(1,2,3)^T,$ and $ bold(b)=mat(4,5,6)^T$

=== Calculate trA, detA, the Frobenius norm ∥A∥,$A bold(a), bold(a)^T bold(b)$ and $bold(b)^T bold(a)$. 

 trA is given formualicly as trA$ = sum_(i=1)^(n) a_(i i)$
 We can simply state this as the sum of the diagonal elements of the matrix A. 
 Which gives us: trA = 1 + 5 + 9 = *15*

detA is simply calculated as:\
$det(A) &= 1 dot 5 dot 9 + 2 dot 6 dot 7 + 3 dot 4 dot 8 - 3 dot 5 dot 7 - 2 dot 4 dot 9 - 1 dot 6 dot 8 \
&= 45 + 84 + 96 - 21 - 32 - 48 = bold(0)$

The Forbenius norm is the square root of the sum of all the elements squared. It is defined and caluclated as follows:\
$||A||_F &= sqrt(sum_(i=1)^(m) sum_(j=1)^(n) |a_(i j)|^2) \
&= sqrt(1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 + 9^2) \
&= sqrt(285) approx bold(16.88)$

Calculating $A bold(a)$ we get:\
$A bold(a) = mat(1,2,3;4,5,6;7,8,9) mat(1;2;3) = mat(1 dot 1 + 2 dot 2 + 3 dot 3;4 dot 1 + 5 dot 2 + 6 dot 3;7 dot 1 + 8 dot 2 + 9 dot 3) = bold(mat(14;32;50))$

Calculating $bold(a)^T bold(b)$ we get:\
$bold(a)^T bold(b) = mat(1,2,3) mat(4;5;6) = 1 dot 4 + 2 dot 5 + 3 dot 6 = bold(32)$

Calculating $bold(b)^T bold(a)$ we get:\
$bold(b)^T bold(a) = mat(4,5,6) mat(1;2;3) = 4 dot 1 + 5 dot 2 + 6 dot 3 = bold(32)$

#pagebreak()

=== A and B are 3x3 matrices. a and b are 3x1 matrices (i.e. vectors). Prove the following implications:

- If $bold(a)^T A bold(b) = 0$ for all $bold(a)$ and $bold(b)$, then $A = 0$.

Assuming that $bold(a)$ and $bold(b)$ are non-zero vectors, we can prove this by contradiction.\
Assume that $A$ is not the zero matrix, meaning that at least one element of $A$ is non-zero.\
Let $A = mat(a_(11), a_(12), a_(13); a_(21), a_(22), a_(23); a_(31), a_(32), a_(33))$ where at least one $a_(i j) eq.not 0$.\
We can choose specific vectors for $bold(a)$ and $bold(b)$ to make $bold(a)^T A bold(b) eq.not 0$.\
For example, if we choose $bold(a) = mat(1;0;0)$ and $bold(b) = mat(1;0;0)$, then:\
$ bold(a)^T A bold(b) = mat(1,0,0) mat(a_(11), a_(12), a_(13); a_(21), a_(22), a_(23); a_(31), a_(32), a_(33)) mat(1;0;0) = a_(11) $\
If $a_(11) eq.not 0$, then $bold(a)^T A bold(b) eq.not 0$, which contradicts our assumption that $bold(a)^T A bold(b) = 0$ for all $bold(a)$ and $bold(b)$.\
Therefore, our assumption that $A$ is not the zero matrix must be false, and we conclude that $A = 0$.
 
- $A^T = -A <=> bold(a)^T A bold(a) = 0$ for all $bold(a)$

  Assume that $A^T = -A$. Then, for any vector $bold(a)$, we have:\
  $ bold(a)^T A bold(a) = bold(a)^T (-A^T) bold(a) = - (bold(a)^T A^T bold(a)) = - (bold(a)^T A bold(a)) $\
  This implies that $ bold(a)^T A bold(a) = - (bold(a)^T A bold(a)) $ which can only be true if $ bold(a)^T A bold(a) = 0 $ Therefore, if $ A^T = -A $ then $ bold(a)^T A bold(a) = 0 $ for all $bold(a)$.

- If $bold(a)^T A bold(a)=a^T B bold(a)$ for all $bold(a)$, then $A + A^T = B + B^T$.
  
  We start with the given condition:\
  $ bold(a)^T A bold(a) = bold(a)^T B bold(a) $ for all $bold(a)$\
  This can be rewritten as:\
  $ bold(a)^T (A - B) bold(a) = 0 $ for all $bold(a)$\
  Let $C = A - B$. Then we have:\
  $ bold(a)^T C bold(a) = 0 $ for all $bold(a)$\
  This implies that C is a skew-symmetric matrix, meaning that $C^T = -C$. Therefore, we have:\
  $ (A - B)^T = -(A - B) $\
  Expanding this gives us:\
  $ A^T - B^T = -A + B $\
  Rearranging terms, we get:\
  $ A + A^T = B + B^T $\
  Thus, if $ bold(a)^T A bold(a) = bold(a)^T B bold(a) $ for all $bold(a)$, then it follows that $ A + A^T = B + B^T $
