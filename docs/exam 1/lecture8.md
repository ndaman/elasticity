<span>upcoming schedule</span>

-   Sep 18 - Exam Review, Homework 2 Due

-   Sep 20 - Exam 1

-   Sep 25 - Exam Return, Stress

-   Sep 27 - Stress

### outline

\[sections numbered\]

exam
====

<span>exam preparations</span>

-   Exam from 2015 is posted on Blackboard

-   This year’s exam will only be 5 problems

-   No equation sheet for the first exam, should remember things like coordinate transformation, Kronecker Delta

-   I do not expect you to remember things like invariants, the alternating symbol, or the strain transformation equations

<span>exam curve example</span>

-   I grade exams problem by problem to try to avoid any bias and keep grading consistent

-   Goal is to have an average of around 85-90 with standard deviation near 10%

-   In this example, average of 70, standard deviation of 15%

-   The high score (before curving) was 96 (this gets mapped to 100)

-   Next I take one exam that has a lower score (in this example let’s assume it’s 60), I look over the whole exam and see what grade I think that exam earned as a whole (with an eye to boosting average)

-   In this example, by mapping that exam to an 80 I get a formula of *y* = 0.56*x* + 46.7 (where *x* is the original score and *y* is the curved score), this change makes the class average an 85 and the deviation around 8.5%

<span>exam tips</span>

-   Don’t cheat

-   Don’t get hung up on one problem, be mindful of the time

-   If you do not know exactly how to calculate a problem, try to show that you understand the big picture

-   Even when you do understand how to calculate a problem, clearly illustrate the “big picture” in a way that is clear and easy to find

review
======

<span>topics</span>

-   Chapter 1

    -   Index notation

    -   Solving tensor equations

    -   Coordinate transformation

    -   Principal values

    -   Principal directions

    -   Tensor calculus

-   Chapter 2

    -   Deformations

    -   Deformation gradient

    -   Strain and rotation

    -   Strain transformation

    -   Principal strains

<span>index notation</span>

1.  Free indexes (subscript letters not repeated in a term)

2.  Dummy index (subscript letters repeated in a term)

3.  Rules

    1.  Indexes cannot repeat more than twice

    2.  Free indexes must match on either side of equation

    3.  Dummy index cannot be used as a free index

<span>converting to matrix math</span>

-   Sometimes our expression is more complex (involves more terms)

-   e.g. transformation of a matrix
    *a*<sub>*i**j*</sub><sup>′</sup> = *Q*<sub>*i**p*</sub>*Q*<sub>*j**q*</sub>*a*<sub>*p**q*</sub>

    1.  Re-arrange so dummy indexes are adjacent
        *Q*<sub>*i**p*</sub>*a*<sub>*p**q*</sub>*Q*<sub>*j**q*</sub>

    2.  Identify which (if any) tensors are transposed (dummy indexes should be on the inside of adjacent terms without a transpose)
        $$Q\_{ip} a\_{pq} \\alert{Q\_{jq}}$$
        \[*Q*\]\[*a*\]\[*Q*\]<sup>*T*</sup>

<span>example</span>

-   Convert the expression in index notation to Matrix notation
    *A*<sub>*i**k*</sub>*B*<sub>*j**l*</sub>*C*<sub>*m**l*</sub>*D*<sub>*m**k*</sub>

    1.  Re-arrange to so that dummy indexes are in adjacent terms
        *A*<sub>*i**k*</sub>*D*<sub>*m**k*</sub>*C*<sub>*m**l*</sub>*B*<sub>*j**l*</sub>

    2.  Identify which terms are transposed
        $$A\_{ik} \\alert{D\_{mk}} C\_{ml} \\alert{B\_{jl}}$$
        \[*A*\]\[*D*\]<sup>*T*</sup>\[*C*\]\[*B*\]<sup>*T*</sup>

<span>solving equations in index notation</span>

-   Solve the following equation for *E*<sub>*k*</sub> in terms of *C*<sub>*i**j*</sub>, *V*<sub>*i**j*</sub>, and *a*<sub>*i*</sub>.

    *E*<sub>*k*</sub>*δ*<sub>*i**k*</sub> = *C*<sub>*k**j*</sub>(*V*<sub>*i**j*</sub>*a*<sub>*k*</sub> − *E*<sub>*k*</sub>*δ*<sub>*i**j*</sub>)

-   Solve the following equation for *U*<sub>*k*</sub> in terms of *a*<sub>*i*</sub> and *P*<sub>*j*</sub>
    $$\\mu \\left\\{\\delta\_{kj}a\_ia\_i + \\frac{1}{1-2\\nu}a\_ka\_j\\right\\}U\_k = P\_j$$
     **Hint:** First solve for *U*<sub>*k*</sub>*a*<sub>*k*</sub>, then substitute that relationship to solve for *U*<sub>*k*</sub>

-   Solve the following equation for *A*<sub>*i**j*</sub> in terms of *B*<sub>*i**j*</sub>
    *B*<sub>*i**j*</sub> = *A*<sub>*i**j*</sub> + *A*<sub>*k**k*</sub>*δ*<sub>*i**j*</sub>
     **Hint:** First solve for *A*<sub>*k**k*</sub> in terms of *B*<sub>*i**j*</sub>, then substitute that to solve for *A*<sub>*i**j*</sub>

<span>coordinate transformation</span>

-   We can express any tensor quantity in terms of a rotated coordinate system

-   The direction cosines help to find the coordinates in the transformed system
    *Q*<sub>*i**j*</sub> = cos(*x*<sub>*i*</sub><sup>′</sup>,*x*<sub>*j*</sub>)

-   Any-order tensor can be expressed in this form
    $$\\begin{aligned}
            a^\\prime &= a & \\text{zero order, scalar}\\\\
            a\_i^\\prime & = Q\_{ip} a\_p & \\text{first order, vector}\\\\
            a\_{ij}^\\prime & = Q\_{ip} Q\_{jq} a\_{pq} & \\text{second order, matrix}\\\\
            a\_{ijk}^\\prime & = Q\_{ip} Q\_{jq} Q\_{kr} a\_{pqr} & \\text{third order}\\\\
            a\_{ijkl}^\\prime & = Q\_{ip} Q\_{jq} Q\_{kr} Q\_{lo} a\_{pqro} & \\text{fourth order}
            \\end{aligned}$$

<span>principal values</span>

-   In the 2D coordinate transformation example, we were able to eliminate one value from a vector using coordinate transformation

-   For second-order tensors, we desire to find the “principal values” where all non-diagonal terms are zero

-   The direction determined by the unit vector, *n*<sub>*j*</sub>, is said to be the *principal direction* or *eigenvector* of the symmetric second-order tensor, *a*<sub>*i**j*</sub> if there exists a parameter, *λ*, such that
    *a*<sub>*i**j*</sub>*n*<sub>*j*</sub> = *λ**n*<sub>*i*</sub>

-   Where *λ* is called the *principal value* or *eigenvalue* of the tensor

<span>principal values</span>

-   We can re-write the equation
    (*a*<sub>*i**j*</sub> − *λ**δ*<sub>*i**j*</sub>)*n*<sub>*j*</sub> = 0

-   This system of equations has a non-trivial solution if and only if det\[*a*<sub>*i**j*</sub> − *λ**δ*<sub>*i**j*</sub>\]=0

-   This equation is known as the characteristic equation, and we solve it to find the principal values of a tensor

<span>example</span>

-   Find principal values, principal directions, and invariants for the tensor
    $$c\_{ij} = \\begin{bmatrix}
            1 & 0 & 2\\\\
            0 & 2 & 0\\\\
            2 & 0 & 4
            \\end{bmatrix}$$

<span>example</span>
$$\\begin{vmatrix}
        1-\\lambda & 0 & 2\\\\
        0 & 2-\\lambda & 0\\\\
        2 & 0 & 4-\\lambda
        \\end{vmatrix} = 0$$

<span>example</span>
$$\\begin{aligned}
    (1-\\lambda)\[(2-\\lambda)(4-\\lambda)-0\]-0+2\[0-2(2-\\lambda)\] &= 0 \\\\
    (1-\\lambda)(2-\\lambda)(4-\\lambda)-4(2-\\lambda) &= 0
    \\end{aligned}$$
$$\\begin{aligned}
    (2-\\lambda)\[(1-\\lambda)(4-\\lambda)-4\] &= 0 \\\\
    (1-\\lambda)(4-\\lambda)-4 &= 0\\\\
    \\lambda^2 -5\\lambda = 0
    \\end{aligned}$$
*λ* = 5, 2, 0

<span>example</span>

-   To find the principal direction for *λ*<sub>1</sub> = 5
    $$\\begin{bmatrix}
            1-5 & 0 & 2\\\\
            0 & 2-5 & 0\\\\
            2 & 0 & 4-5
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$
    $$\\begin{bmatrix}
            -4 & 0 & 2\\\\
            0 & -3 & 0\\\\
            2 & 0 & -1
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

<span>example</span>

-   To row-reduce, we can multiply row 3 by 2
    $$\\begin{bmatrix}
            -4 & 0 & 2\\\\
            0 & -3 & 0\\\\
            \\alert{2} & \\alert{0} & \\alert{-1}
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   Now we add this to row 1, which cancels all terms in row 1
    $$\\begin{bmatrix}
            \\alert{0} & \\alert{0} & \\alert{0}\\\\
            0 & -3 & 0\\\\
            2 & 0 & -1
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

<span>example</span>

-   We are now left with only two equations
    $$\\begin{aligned}
            -3 n\_2 &= 0\\\\
            2 n\_1 -n\_3 &= 0\\\\
            \\end{aligned}$$

-   We know that *n*<sub>2</sub> = 0. If we let *n*<sub>3</sub> = 1, we find $n\_1 = \\frac{1}{2}$
    $$n^1 = \\langle \\frac{1}{2}, 0, 1 \\rangle$$

<span>example</span>

-   To find the principal direction for *λ*<sub>2</sub> = 2
    $$\\begin{bmatrix}
            1-2 & 0 & 2\\\\
            0 & 2-2 & 0\\\\
            2 & 0 & 4-2
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$
    $$\\begin{bmatrix}
            -1 & 0 & 2\\\\
            0 & 0 & 0\\\\
            2 & 0 & 2
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

<span>example</span>

-   To row-reduce, we can multiply row 1 by 2
    $$\\begin{bmatrix}
            \\alert{-1} & \\alert{0} & \\alert{2}\\\\
            0 & 0 & 0\\\\
            2 & 0 & 2
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   Now we add this to row 3, which cancels the first term
    $$\\begin{bmatrix}
            -1 & 0 & 2\\\\
            0 & 0 & 0\\\\
            0 & 0 & 4
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

<span>example</span>

-   We are left with two equations
    $$\\begin{aligned}
            -n\_1 + 2n\_3 &= 0\\\\
            4 n\_3 &= 0
            \\end{aligned}$$

-   We know that *n*<sub>3</sub> = 0, this also gives *n*<sub>1</sub> = 0.

-   *n*<sub>2</sub> can be any value, we choose *n*<sub>2</sub> = 1
    *n*<sup>2</sup> = ⟨0, 1, 0⟩

<span>example</span>

-   The third principal direction can be found two ways

-   We can either use the same method or use the cross-product *n*<sup>3</sup> = *n*<sup>1</sup> × *n*<sup>2</sup>
    $$\\begin{bmatrix}
            1 & 0 & 2\\\\
            0 & 2 & 0\\\\
            2 & 0 & 4
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   After row-reduction
    $$\\begin{bmatrix}
            1 & 0 & 2\\\\
            0 & 2 & 0\\\\
            0 & 0 & 0
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   *n*<sup>3</sup> = ⟨ − 2, 0, 1⟩

<span>partial derivatives</span>

-   We usually omit the (*x*<sub>*i*</sub>), but most variables we deal with are functions of *x*<sub>*i*</sub>

-   These are referred to as field variables. e.g.
    $$\\begin{aligned}
    {2}
            a &= a(x\_1, x\_2, x\_3) & &= a(x\_i) \\\\
            a\_i &= a\_i(x\_1, x\_2, x\_3) & &= a\_i(x\_i) \\\\
            a\_{ij} &= a\_{ij}(x\_1, x\_2, x\_3) & &= a\_{ij}(x\_i)
            \\end{aligned}$$

<span>partial derivatives</span>

-   We can use comma notation to simplify taking partial derivatives of field variables
    $$\\begin{aligned}
            a\_{,i} &= \\frac{\\partial}{\\partial x\_i} a \\\\
            a\_{i,j} &= \\frac{\\partial}{\\partial x\_j} a\_i \\\\
            a\_{ij,k} &= \\frac{\\partial}{\\partial x\_k} a\_{ij} \\\\
            \\end{aligned}$$

<span>tensor calculus</span>

-   Let *f* be a scalar-valued function such that $f(x\_i) = \\sqrt{x\_i x\_i}$. Find *f*<sub>,*k*</sub>

-   We can use the chain rule to differentiate

-   $f\_{,k} = \\frac{1}{2}(x\_i x\_i)^{-\\frac{1}{2}} (x\_i x\_i)\_{,k}$

-   Using the chain rule again to compute (*x*<sub>*i*</sub>*x*<sub>*i*</sub>)<sub>,*k*</sub> we find

-   $f\_{,k} = \\frac{1}{2}(x\_i x\_i)^{-\\frac{1}{2}} (x\_i x\_{i,k} + x\_{i,k} x\_i )$

-   Simplifying $f\_{,k} = (x\_i x\_i)^{-\\frac{1}{2}} (x\_i x\_{i,k})$

-   The partial derivative, $\\frac{\\partial x\_i}{\\partial x\_k} = \\delta\_{ik}$

-   Substituting $f\_{,k} = (x\_i x\_i)^{-\\frac{1}{2}} (x\_i \\delta\_{ik})$

-   We also know that *x*<sub>*i*</sub>*δ*<sub>*i**k*</sub> = *x*<sub>*k*</sub>, and we can also substitute $f = \\sqrt{x\_i x\_i}$ to find

-   $f\_{,k} = \\frac{x\_k}{f}$

<span>deformation</span>

-   A *deformation* is a comparison of two states. The deformation of a material point is expressed as
    $$\\begin{gathered}
            x\_i = x\_i(x\_1^0, x\_2^0, x\_3^0) \\quad \\text{or} \\quad x\_i^0 = x\_i^0(x\_1, x\_2, x\_3)
            \\end{gathered}$$

-   For example, consider the 2D deformation
    $$\\begin{gathered}
            \\begin{Bmatrix}
            x\_1 \\\\ x\_2
            \\end{Bmatrix} =
            \\begin{Bmatrix}
            2 x\_1^0 \\\\ x\_2^0
            \\end{Bmatrix} \\quad \\text{or} \\quad
            \\begin{Bmatrix}
            x\_1^0 \\\\ x\_2^0
            \\end{Bmatrix}
            = \\begin{Bmatrix}
            \\frac{1}{2} x\_1 \\\\ x\_2
            \\end{Bmatrix}
            \\end{gathered}$$

    (0,0) – (0,2); (0,0) – (3,0); (0,0) – (1,0) node\[below\] <span>*x*<sub>1</sub><sup>0</sup></span> – (1,1) – (0,1) node\[left\] <span>*x*<sub>2</sub><sup>0</sup></span> – (0,0); (1,1) – (2,1) node\[right\] <span>*x*<sub>2</sub></span> – (2,0) node\[below\] <span>*x*<sub>1</sub></span>;

<span>displacement</span>

-   Displacement is the shortest distance traveled when a particle moves from one location to another

-   It is identical in Eulerian and Lagrangian descriptions
    $$\\begin{aligned}
            u\_i &= (x\_i - x\_i^0)\\\\
            \\begin{Bmatrix}
            u \\\\ v \\\\ w
            \\end{Bmatrix} &= \\begin{Bmatrix}
            x - x^0\\\\
            y - y^0\\\\
            z - z^0
            \\end{Bmatrix}
            \\end{aligned}$$

<span>deformation gradients</span>

-   In index notation we write displacements as *u*<sub>*i*</sub>

-   The deformation gradient can be written in this notation as
    $$F = u\_{i,j} = \\begin{bmatrix}
            \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2} & \\frac{\\partial u\_1}{\\partial x\_3}\\\\
            \\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2} & \\frac{\\partial u\_2}{\\partial x\_3}\\\\
            \\frac{\\partial u\_3}{\\partial x\_1} & \\frac{\\partial u\_3}{\\partial x\_2} & \\frac{\\partial u\_3}{\\partial x\_3}
            \\end{bmatrix}$$

<span>strain definition</span>

-   We can separate the deformation gradient into symmetric and antisymmetric parts
    *u*<sub>*i*, *j*</sub> = *e*<sub>*i**j*</sub> + *ω*<sub>*i**j*</sub>

-   Where
    $$\\begin{aligned}
                e\_{ij} &= \\frac{1}{2}(u\_{i,j} + u\_{j,i})\\\\
                \\omega\_{ij} &= \\frac{1}{2}(u\_{i,j} - u\_{j,i})
            \\end{aligned}$$

-   *e*<sub>*i**j*</sub> is known as the strain tensor

-   *ω*<sub>*i**j*</sub> is known as the rotation tensor

<span>example</span>

-   Find the displacements given the following strain tensor
    $$e\_{ij} = \\begin{bmatrix}
            yz & xz & xy\\\\
            xz & 2y & \\frac{1}{2}x^2\\\\
            xy & \\frac{1}{2}x^2 & 3z^2
            \\end{bmatrix}$$

-   We start by integrating the diagonal terms
    *u* = ∫*y**z**d**x* = *x**y**z* + *f*(*y*, *z*)
    *v* = ∫2*y**d**y* = *y*<sup>2</sup> + *g*(*x*, *z*)
    *w* = ∫3*z*<sup>2</sup>*d**z* = *z*<sup>3</sup> + *h*(*x*, *y*)

<span>example</span>

-   Next we need to find the shear terms
    $$\\begin{aligned}
            e\_{xy} &= \\frac{1}{2}(u\_{,y}+v\_{,x})\\\\
            xz &= \\frac{1}{2}(xz + f\_{,y} + g\_{,x})
            \\end{aligned}$$
    $$\\begin{aligned}
            e\_{xz} &= \\frac{1}{2}(u\_{,z}+w\_{,x})\\\\
            xy &= \\frac{1}{2}(xy + f\_{,z} + h\_{,x})
            \\end{aligned}$$
    $$\\begin{aligned}
            e\_{yz} &= \\frac{1}{2}(v\_{,z}+w\_{,y})\\\\
            \\frac{1}{2}x^2 &= \\frac{1}{2}(g\_{,z} + h\_{,y})
            \\end{aligned}$$

<span>example</span>

-   Note that we cannot uniquely solve this (any arbitrary rotation *ω*<sub>*i**j*</sub> can be added and will still produce a valid strain)

-   Assume *ω*<sub>*i**j*</sub> = 0
    $$\\begin{aligned}
            \\frac{1}{2}(u\_{,y} - v\_{,x}) &= 0 \\\\
            xz + f\_{,y} - g\_{,x} &= 0 \\\\
            f\_{,y} &= g\_{,x} - xz
            \\end{aligned}$$

<span>example</span>

-   We can now substitute this in the *e*<sub>*x**y*</sub> expression
    $$\\begin{aligned}
            e\_{xy} &= \\frac{1}{2}(u\_{,y}+v\_{,x})\\\\
            xz &= \\frac{1}{2}(xz + f\_{,y} + g\_{,x})\\\\
            2 xz &= xz + g\_{,x} - xz + g\_{,x})\\\\
            2g\_{,x} &= 2xz \\\\
            g(x,z) &= \\frac{1}{2}x^2z + g\_2(z)
            \\end{aligned}$$

-   We can substitute this into the rotation expression to find *f*<sub>,*y*</sub>
    $$\\begin{aligned}
            f\_{,y} &= g\_{,x} - xz\\\\
            f\_{,y} &= xz - xz\\\\
            f(y,z) &= f\_2(z)
            \\end{aligned}$$

<span>example</span>

-   Next we consider *ω*<sub>*x**z*</sub>
    $$\\begin{aligned}
            \\frac{1}{2}(u\_{,z} - w\_{,x}) &= 0 \\\\
            xy + f\_{,z} - h\_{,x} &= 0\\\\
            h\_{,x} &= xy + f\_{,z}
            \\end{aligned}$$

-   Substituting this into *e*<sub>*x**z*</sub> gives
    $$\\begin{aligned}
            e\_{xz} &= \\frac{1}{2}(xy+f\_{,z}+xy + f\_{,z})\\\\
            xy &= xy + f\_{,z}\\\\
            f\_{,z} &= 0\\\\
            f\_2(z) &= 0
            \\end{aligned}$$

<span>example</span>

-   Substituting back into *ω*<sub>*x**z*</sub> we find
    $$\\begin{aligned}
            h\_{,x} &= xy + f\_{,z}\\\\
            h\_{,x} &= xy\\\\
            h(x,y) &= \\frac{1}{2}x^2 y + h\_2(y)
            \\end{aligned}$$

-   The last term to consider is *ω*<sub>*y**z*</sub>
    $$\\begin{aligned}
            \\frac{1}{2}(v\_{,z}-w\_{,y}) &= 0\\\\
            \\frac{1}{2}x^2 + g\_{2,z} - (\\frac{1}{2}x^2 + h\_{2,y}) &= 0\\\\
            \\frac{1}{2}x^2 + g\_{2,z} &= \\frac{1}{2}x^2 + h\_{2,y}
            \\end{aligned}$$

<span>example</span>

-   Substituting into *e*<sub>*y**z*</sub>
    $$\\begin{aligned}
            e\_{yz} &= \\frac{1}{2}(v\_{,z}+w\_{,y})\\\\
            \\frac{1}{2}x^2 &= \\frac{1}{2}(\\frac{1}{2}x^2 + g\_{2,z} + \\frac{1}{2}x^2 + h\_{2,y})\\\\
            \\frac{1}{2}x^2 &= \\frac{1}{2}x^2 + g\_{2,z}\\\\
            g\_{2,z} &= 0\\\\
            g(x,z) &= \\frac{1}{2} x^2 z
            \\end{aligned}$$

-   And substituting back into *ω*<sub>*y**z*</sub>
    $$\\begin{aligned}
            \\frac{1}{2}x^2 &= \\frac{1}{2}x^2 + h\_{2,y}\\\\
            h\_(2,y) &= 0\\\\
            h\_2(y) &= 0
            \\end{aligned}$$

<span>example</span>
$$\\begin{aligned}
    u &= xyz\\\\
    v &= y^2 + \\frac{1}{2}x^2z\\\\
    w &= z^3 + \\frac{1}{2}x^2y
    \\end{aligned}$$

