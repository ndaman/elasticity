<span>upcoming schedule</span>

-   Aug 28 - Coordinate Transformation, Principal Values

-   Aug 30 - Tensor Calculus

-   Sep 4 - Labor Day (No Class)

-   Sep 6 - Homework 1 Due, Displacement and Strain

Coordinate Transformation
=========================

<span>coordinate transformation in two dimensions</span>

(0,3) node (yaxis) \[above\] <span>*x*<sub>2</sub></span> |- (3,0) node (xaxis) \[right\] <span>*x*<sub>1</sub></span>; (0,0) – (-2.12,2.12) node (yprime) \[above left\] <span>*x*<sub>2</sub><sup>′</sup></span>; (0,0) – (2.12,2.12) node (xprime) \[above right\] <span>*x*<sub>1</sub><sup>′</sup></span>; (0,0) – (1.5,1.5) node (v) \[above left\] <span>*v*</span>;

<span>coordinate transformation in two dimensions</span>

-   The vector, *v*, remains fixed, but we transform our coordinate system

-   In the new coordinate system, the *x*<sub>2</sub><sup>′</sup> portion of *v* is zero.

-   To transform the coordinate system, we first define some unit vectors.

-   $\\hat{e}\_1$ is a unit vector in the direction of *x*<sub>1</sub>, while $\\hat{e}\_1^\\prime$ is a unit vector in the direction of *x*<sub>1</sub><sup>′</sup>

<span>coordinate transformation in two dimensions</span>

(0,3) node (yaxis) \[above\] <span>*x*<sub>2</sub></span> |- (3,0) node (xaxis) \[right\] <span>*x*<sub>1</sub></span>; (0,1) node (j) \[above right\] <span>$\\hat{e}\_2$</span> |- (1,0) node (i) \[below right\] <span>$\\hat{e}\_1$</span>; (0,0) – (-2.12,2.12) node (yprime) \[above left\] <span>*x*<sub>2</sub><sup>′</sup></span>; (0,0) – (2.12,2.12) node (xprime) \[above right\] <span>*x*<sub>1</sub><sup>′</sup></span>; (0,0) – (-.707,.707) node (jprime) \[above right\] <span>$\\hat{e}\_2^\\prime$</span>; (0,0) – (.707,.707) node (iprime) \[right\] <span>$\\hat{e}\_1^\\prime$</span>; (0,0) – (1.5,1.5) node (v) \[above left\] <span>*v*</span>; (0.5,0) arc (0:45:0.5) node (theta) \[below right = -0.1cm and 0.3cm\] <span>*θ*</span>;

<span>coordinate transformation in two dimensions</span>

-   For this example, let us assume *v* = ⟨2, 2⟩ and *θ* = 45<sup>∘</sup>

-   We can write the transformed unit vectors, $\\hat{e}\_1^\\prime$ and $\\hat{e}\_2^\\prime$ in terms of $\\hat{e}\_1$, $\\hat{e}\_2$ and the angle of rotation, *θ*.
    $$\\begin{aligned}
    \\hat{e}\_1^\\prime &= \\langle \\hat{e}\_1 \\cos \\theta , \\hat{e}\_2 \\sin \\theta\\rangle\\\\
    \\hat{e}\_2^\\prime &= \\langle -\\hat{e}\_1 \\sin \\theta , \\hat{e}\_2 \\cos \\theta \\rangle\\end{aligned}$$

<span>coordinate transformation in two dimensions</span>

-   We can write the vector, *v*, in terms of the unit vectors describing our axis system

-   $v = v\_1 \\hat{e}\_1 + v\_2 \\hat{e}\_2$

-   (note: $\\hat{e}\_1=\\langle 1, 0 \\rangle$ and $\\hat{e}\_2 = \\langle 0,1 \\rangle$)

-   *v* = ⟨2, 2⟩=2⟨1, 0⟩+2⟨0, 1⟩

<span>coordinate transformation in two dimensions</span>

-   When expressed in the transformed coordinate system, we refer to *v*<sup>′</sup>

-   *v*<sup>′</sup> = ⟨*v*<sub>1</sub>cos*θ* + *v*<sub>2</sub>sin*θ*, −*v*<sub>1</sub>sin*θ* + *v*<sub>2</sub>cos*θ*⟩

-   $v^\\prime = \\langle 2\\sqrt{2}, 0 \\rangle$

-   We can recover the original vector from the transformed coordinates:

-   $v = v\_1^\\prime \\hat{e}\_1^\\prime + v\_2^\\prime \\hat{e}\_2^\\prime$

-   (note: $\\hat{e}\_1^\\prime=\\langle \\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle$ and $\\hat{e}\_2^\\prime = \\langle -\\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle$)

-   $v = 2\\sqrt{2}\\langle \\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle, 0 \\langle -\\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle = \\langle 2, 2 \\rangle$

<span>general coordinate transformation</span>

-   Coordinate transformation can become much more complicated in three dimensions, and with higher-order tensors

-   It is convenient to define a general form of the coordinate transformation in index notation

-   We define *Q*<sub>*i**j*</sub> as the cosine of the angle between the *x*<sub>*i*</sub><sup>′</sup> axis and the *x*<sub>*j*</sub> axis.

-   This is also referred to as the “direction cosine”
    *Q*<sub>*i**j*</sub> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)

<span>general coordinate transformation</span>

-   We can use this form on our 2D transformation example
    $$\\begin{aligned}
    Q\_{ij} &= \\cos (x\_i^\\prime, x\_j)\\\\ &= \\begin{bmatrix}
    \\cos (x\_1^\\prime, x\_1) & \\cos (x\_1^\\prime, x\_2)\\\\
    \\cos (x\_2^\\prime, x\_1) & \\cos (x\_2^\\prime, x\_2)
    \\end{bmatrix}\\\\ &= \\begin{bmatrix}
    \\cos \\theta & \\cos (90-\\theta)\\\\
    \\cos (90+\\theta) & \\cos \\theta
    \\end{bmatrix} \\\\ &= \\begin{bmatrix}
    \\cos \\theta & \\sin \\theta \\\\
    -\\sin \\theta & \\cos \\theta
    \\end{bmatrix}\\end{aligned}$$

<span>general coordinate transformation</span>

-   We can transform any-order tensor using *Q*<sub>*i**j*</sub>

-   Vectors (first-order tensors): *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*i**j*</sub>*v*<sub>*j*</sub>

-   Matrices (second-order tensors): *σ*<sub>*m**n*</sub><sup>′</sup> = *Q*<sub>*m**i*</sub>*Q*<sub>*n**j*</sub>*σ*<sub>*i**j*</sub>

-   Fourth-order tensors: *C*<sub>*i**j**k**l*</sub><sup>′</sup> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*Q*<sub>*k**o*</sub>*Q*<sub>*l**p*</sub>*C*<sub>*m**n**o**p*</sub>

<span>general coordinate transformation</span>

-   We can similarly use *Q*<sub>*i**j*</sub> to find tensors in the original coordinate system

-   Vectors (first-order tensors): *v*<sub>*i*</sub> = *Q*<sub>*j**i*</sub>*v*<sub>*j*</sub><sup>′</sup>

-   Matrices (second-order tensors): *σ*<sub>*m**n*</sub> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*σ*<sub>*i**j*</sub><sup>′</sup>

-   Fourth-order tensors: *C*<sub>*i**j**k**l*</sub> = *Q*<sub>*m**i*</sub>*Q*<sub>*n**j*</sub>*Q*<sub>*o**k*</sub>*Q*<sub>*p**l*</sub>*C*<sub>*m**n**o**p*</sub><sup>′</sup>

<span>general coordinate transformation</span>

-   We can derive some interesting properties of the transformation tensor, *Q*<sub>*i**j*</sub>

-   We know that *v*<sub>*i*</sub> = *Q*<sub>*j**i*</sub>*v*<sub>*j*</sub><sup>′</sup> and that *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*i**j*</sub>*v*<sub>*j*</sub>

-   If we substitute (changing the appropriate indexes) we find:

-   *v*<sub>*i*</sub> = *Q*<sub>*j**i*</sub>*Q*<sub>*j**k*</sub>*v*<sub>*k*</sub>

-   We can now use the Kronecker Delta to substitute *v*<sub>*i*</sub> = *δ*<sub>*i**k*</sub>*v*<sub>*k*</sub> which gives

-   *δ*<sub>*i**k*</sub>*v*<sub>*k*</sub> = *Q*<sub>*j**i*</sub>*Q*<sub>*j**k*</sub>*v*<sub>*k*</sub>

Examples
========

<span>example</span>

(0,0,0) – (3,0,0) node\[below left\] <span>*x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>;

-   Find *Q*<sub>*i**j*</sub><sup>1</sup> for rotation of 60<sup>∘</sup> about *x*<sub>2</sub>

-   Find *Q*<sub>*i**j*</sub><sup>2</sup> for rotation of 30<sup>∘</sup> about *x*<sub>3</sub><sup>′</sup>

-   Find *e*<sub>*i*</sub><sup>′′</sup> after both rotations

<span>example</span>

(0,0,0) – (3,0,0) node\[below left\] <span>*x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub>, *x*<sub>2</sub><sup>′</sup></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (0,0,0) – (2.6,0,1.5) node\[above\] <span>*x*<sub>3</sub><sup>′</sup></span>; (0,0,0) – (1.5,0,-2.6) node\[below left\] <span>*x*<sub>1</sub><sup>′</sup></span>; <span>above left</span><span>*θ*<sub>1</sub></span> <span>below left</span><span>*θ*<sub>1</sub></span>

<span>example</span>

(0,0,0) – (3,0,0) node\[below left\] <span>*x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub>, *x*<sub>2</sub><sup>′</sup></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (0,0,0) – (2.6,0,1.5) node\[above\] <span>*x*<sub>3</sub><sup>′</sup>, *x*<sub>3</sub><sup>′′</sup></span>; (0,0,0) – (1.5,0,-2.6) node\[below left\] <span>*x*<sub>1</sub><sup>′</sup></span>; <span>above left</span><span>*θ*<sub>1</sub></span> <span>below left</span><span>*θ*<sub>1</sub></span>; ; (0,0,0) – (2.6,1.5,0) node\[below right\] <span>*x*<sub>1</sub><sup>′′</sup></span>; (0,0,0) – (-1.5,2.6,0) node\[below right\] <span>*x*<sub>2</sub><sup>′′</sup></span>; ; ;

<span>example</span>

-   *Q*<sub>*i**j*</sub><sup>1</sup> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)

-   *Q*<sub>*i**j*</sub><sup>2</sup> = cos(*x*<sub>*i*</sub><sup>′′</sup>, *x*<sub>*j*</sub><sup>′</sup>)
    $$Q\_{ij}^1 = \\begin{bmatrix}
    \\cos 60 & \\cos 90 & \\cos 150\\\\
    \\cos 90 & \\cos 0 & \\cos 90\\\\
    \\cos 30 & \\cos 90 & \\cos 60
    \\end{bmatrix}$$
    $$Q\_{ij}^2 = \\begin{bmatrix}
    \\cos 30 & \\cos 60 & \\cos 90\\\\
    \\cos 120 & \\cos 30 & \\cos 90\\\\
    \\cos 90 & \\cos 90 & \\cos 0
    \\end{bmatrix}$$

<span>example</span>

-   We now use *Q*<sub>*i**j*</sub> to find $\\hat{e}\_i^\\prime$ and $\\hat{e}\_i^{\\prime \\prime}$

-   First, we need to write $\\hat{e}\_i$ in a manner more consistent with index notation

-   We will indicate axis direction with a superscript, e.g. $\\hat{e}\_1 = e\_i^1$

-   *e*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*i**j*</sub><sup>1</sup>*e*<sub>*j*</sub>

-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*i**j*</sub><sup>2</sup>*e*<sub>*j*</sub><sup>′</sup>

-   How do we find *e*<sub>*i*</sub><sup>′′</sup> in terms of *e*<sub>*i*</sub>?

-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*i**j*</sub><sup>2</sup>*Q*<sub>*j**k*</sub><sup>1</sup>*e*<sub>*k*</sub>

Principal Directions
====================

<span>principal directions</span>

-   We defined principal directions earlier
    (*a*<sub>*i**j*</sub> − *λ**δ*<sub>*i**j*</sub>)*n*<sub>*j*</sub> = 0

-   *λ* are the principal values and *n*<sub>*j*</sub> are the principal directions

-   For each eigenvalue there will be a principal direction

-   We find the principal direction by substituting the solution for *λ* back into this equation

<span>example</span>

-   Find the principal directions for the earlier principal values example

-   Recall *λ* = 0, 5, let us say *λ*<sub>1</sub> = 5, we find *n*<sub>*j*</sub><sup>(1)</sup> by
    $$\\begin{bmatrix}
    1-\\lambda\_1 & 2\\\\
    2 & 4-\\lambda\_1
    \\end{bmatrix} \\begin{Bmatrix}
    n\_1 \\\\ n\_2
    \\end{Bmatrix} = 0$$

-   This gives
    $$\\begin{bmatrix}
    -4 & 2\\\\
    2 & -1
    \\end{bmatrix} \\begin{Bmatrix}
    n\_1 \\\\ n\_2
    \\end{Bmatrix} = 0$$

<span>example</span>

-   We proceed to solve the equations using row-reduction, but we find
    $$\\begin{bmatrix}
    2 & -1\\\\
    0 & 0
    \\end{bmatrix} \\begin{Bmatrix}
    n\_1 \\\\ n\_2
    \\end{Bmatrix} = 0$$

-   This means we cannot uniquely solve for *n*<sub>*j*</sub>

-   We are only concerned with the direction, magnitude is not important

-   Choose *n*<sub>2</sub> = 1, solve for *n*<sub>1</sub>

-   $n^{(1)} = \\langle \\frac{1}{2}, 1 \\rangle$

<span>example</span>

-   Similarly, for *λ*<sub>2</sub> = 0, we find
    $$\\begin{bmatrix}
    1 & 2\\\\
    2 & 4
    \\end{bmatrix} \\begin{Bmatrix}
    n\_1 \\\\ n\_2
    \\end{Bmatrix} = 0$$

-   Which, after row-reduction, becomes
    $$\\begin{bmatrix}
    1 & 2\\\\
    0 & 0
    \\end{bmatrix} \\begin{Bmatrix}
    n\_1 \\\\ n\_2
    \\end{Bmatrix} = 0$$

-   If we choose *n*<sub>2</sub> = 1, we find *n*<sub>1</sub> = −2

-   This gives *n*<sup>(2)</sup> = ⟨ − 2, 1⟩

<span>example</span>

-   We can assemble a transformation matrix, *Q*<sub>*i**j*</sub>, from the principal directions

-   First we need to normalize them to unit vectors

-   $||n^{(1)}|| = \\sqrt{\\frac{5}{4}}$

-   $\\hat{n}^{(1)} = \\frac{2}{\\sqrt{5}} \\langle \\frac{1}{2}, 1 \\rangle = \\langle \\frac{1}{\\sqrt{5}}, \\frac{2}{\\sqrt{5}} \\rangle$

-   $||n^{(2)}|| = \\sqrt{5}$

-   $\\hat{n}^{(2)} = \\langle \\frac{-2}{\\sqrt{5}}, \\frac{1}{\\sqrt{5}} \\rangle $

<span>example</span>

-   This gives
    $$Q\_{ij} = \\frac{1}{\\sqrt{5}}\\begin{bmatrix}
    1 & 2\\\\
    -2 & 1
    \\end{bmatrix}$$

-   And we find
    *A*<sub>*m**n*</sub><sup>′</sup> = *Q*<sub>*m**i*</sub>*Q*<sub>*n**j*</sub>*A*<sub>*i**j*</sub>
    $$A\_{ij}^\\prime = \\begin{bmatrix}
    5 & 0 \\\\
    0 & 0
    \\end{bmatrix}$$

Examples
========

<span>example</span>

-   Find principal values, principal directions, and invariants for the tensor
    $$c\_{ij} = \\begin{bmatrix}
    8 & 0 & 0\\\\
    0 & 3 & 1\\\\
    0 & 1 & 3
    \\end{bmatrix}$$

<span>example</span>

-   Characteristic equation simplifies to

-   −*λ*<sup>3</sup> + 14*λ*<sup>2</sup> − 56*λ* + 64 = 0

-   Which has the solutions *λ* = 2, 4, 8

<span>example</span>

-   To find the principal direction for *λ*<sub>1</sub> = 8
    $$\\begin{bmatrix}
    8-8 & 0 & 0\\\\
    0 & 3-8 & 1\\\\
    0 & 1 & 3-8
    \\end{bmatrix}\\begin{Bmatrix}
    n\_1 \\\\ n\_2 \\\\ n\_3
    \\end{Bmatrix} = 0$$

<span>example</span>

-   After row-reduction, we find
    $$\\begin{bmatrix}
            0 & 0 & 0\\\\
            0 & 0 & -24\\\\
            0 & 1 & -5
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   This means that *n*<sub>3</sub> = 0 and, as a result, *n*<sub>2</sub> = 0.

-   *n*<sub>1</sub> can be any value, we choose *n*<sub>1</sub> = 1 to give a unit vector.

-   *n*<sup>(1)</sup> = ⟨1, 0, 0⟩

<span>example</span>

-   To find the principal direction for *λ*<sub>2</sub> = 4
    $$\\begin{bmatrix}
            8-4 & 0 & 0\\\\
            0 & 3-4 & 1\\\\
            0 & 1 & 3-4
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

<span>example</span>

-   After row-reduction, we find
    $$\\begin{bmatrix}
            4 & 0 & 0\\\\
            0 & -1 & 1\\\\
            0 & 0 & 0
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   This means that *n*<sub>1</sub> = 0

-   We also know that *n*<sub>2</sub> = *n*<sub>3</sub>, so we choose *n*<sub>2</sub> = *n*<sub>1</sub> = 1

-   This gives $n^{(2)} = \\frac{1}{\\sqrt{2}}\\langle 0, 1, 1 \\rangle$ after normalization

<span>example</span>

-   To find the principal direction for *λ*<sub>3</sub> = 2
    $$\\begin{bmatrix}
            8-2 & 0 & 0\\\\
            0 & 3-2 & 1\\\\
            0 & 1 & 3-2
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

<span>example</span>

-   After row-reduction, we find
    $$\\begin{bmatrix}
            6 & 0 & 0\\\\
            0 & 1 & 1\\\\
            0 & 0 & 0
            \\end{bmatrix}\\begin{Bmatrix}
            n\_1 \\\\ n\_2 \\\\ n\_3
            \\end{Bmatrix} = 0$$

-   This means that *n*<sub>1</sub> = 0

-   We also know that *n*<sub>2</sub> = −*n*<sub>3</sub>, so we choose *n*<sub>2</sub> = 1 and *n*<sub>1</sub> = −1

-   This gives $n^{(3)} = \\frac{1}{\\sqrt{2}}\\langle 0, 1, -1 \\rangle$ after normalization

<span>example</span>

-   In summary, for *c*<sub>*i**j*</sub> we have:

-   *λ*<sub>1</sub> = 8 and *n*<sup>(1)</sup> = ⟨1, 0, 0⟩

-   *λ*<sub>2</sub> = 4 and $n^{(2)} = \\frac{1}{\\sqrt{2}}\\langle 0, 1, 1 \\rangle$

-   *λ*<sub>3</sub> = 2 and $n^{(3)} = \\frac{1}{\\sqrt{2}}\\langle 0, 1, -1 \\rangle$

-   We can assemble *n*<sup>(*i*)</sup> into a transformation tensor
    $$Q\_{ij} = \\frac{1}{\\sqrt{2}}\\begin{bmatrix}
            \\sqrt{2} & 0 & 0\\\\
            0 & 1 & 1\\\\
            0 & 1 & -1
            \\end{bmatrix}$$

<span>example</span>

-   What is *c*<sub>*i**j*</sub><sup>′</sup>?

-   *c*<sub>*i**j*</sub><sup>′</sup> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*c*<sub>*m**n*</sub>
    $$c\_{ij}^\\prime = \\begin{bmatrix}
            8 & 0 & 0 \\\\
            0 & 4 & 0 \\\\
            0 & 0 & 2
            \\end{bmatrix}$$

<span>example</span>

-   We can also find the invariants for
    $$c\_{ij} = \\begin{bmatrix}
            8 & 0 & 0\\\\
            0 & 3 & 1\\\\
            0 & 1 & 3
            \\end{bmatrix}$$

-   Recall:
    $$\\begin{aligned}
            I\_\\alpha &= a\_{ii}\\\\
            II\_\\alpha &= \\frac{1}{2}(a\_{ii} a\_{jj} - a\_{ij}a\_{ij})\\\\
            III\_\\alpha &= \\det \[ a\_{ij}\]
            \\end{aligned}$$

<span>example</span>

-   First invariant
    *I*<sub>*α*</sub> = *a*<sub>*i**i*</sub> = 8 + 3 + 3 = 14

-   Second invariant
    $$II\_\\alpha = \\frac{1}{2}(a\_{ii} a\_{jj} - a\_{ij}a\_{ij})$$
    *a*<sub>*i**i*</sub>*a*<sub>*j**j*</sub> = 14 × 14
    *a*<sub>*i**j*</sub>*a*<sub>*i**j*</sub> = *a*<sub>11</sub>*a*<sub>11</sub> + *a*<sub>12</sub>*a*<sub>12</sub> + *a*<sub>13</sub>*a*<sub>13</sub> + ... + *a*<sub>33</sub>*a*<sub>33</sub>
    $$II\_\\alpha = \\frac{1}{2}(196 - 84) = 56$$

<span>example</span>

-   Third invariant
    *I**I**I*<sub>*α*</sub> = det\[*a*<sub>*i**j*</sub>\]
    *I**I**I*<sub>*α*</sub> = 8 × (3 × 3 − 1 × 1)=64


