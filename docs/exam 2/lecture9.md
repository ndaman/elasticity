<span>upcoming schedule</span>

-   Sep 27 - Stress and Traction, Stress transformation, Mohr’s circle

-   Oct 2 - Equilibrium

-   Oct 4 - Material Behavior

### outline

\[sections numbered\]

traction vector and stress tensor
=================================

<span>traction</span>

<img src="../Figures/traction" alt="image" /> \[fig:traction\]

<span>traction</span>

-   The traction vector is defined as
    $$\\hat{t}^n(x,\\hat{n}) = \\lim\\limits\_{\\Delta A \\to 0} \\frac{\\Delta \\hat{f}}{\\Delta A}$$

-   By Newton’s third law (action-reaction principle)
    $$\\hat{t}^n(x,\\hat{n}) = -\\hat{t}^n(x,-\\hat{n})$$

<span>traction</span>

(0,0,0) – (2,0,0) – (2,2,0) – (0,2,0) – (0,0,0); (0,0,2) – (2,0,2) – (2,2,2) – (0,2,2) – (0,0,2); (2,0,0) – (2,0,2); (2,2,0) – (2,2,2); (0,2,0) – (0,2,2); (0,0,0) – (0,0,2); (1,1,2) – (1,1,3) node\[above\] <span>$\\hat{e}\_3$</span>; (2,1,1) – (3,1,1) node\[left\] <span>$\\hat{e}\_1$</span>; (1,2,1) – (1,3,1) node\[right\] <span>$\\hat{e}\_2$</span>; (1,1,2) – (2,1,4) node\[above\] <span>$\\hat{t}^{\\hat{e}\_3}$</span>; (2,1,1) – (3,2,2) node\[above\] <span>$\\hat{t}^{\\hat{e}\_1}$</span>; (1,2,1) – (1,4,2) node\[right\] <span>$\\hat{t}^{\\hat{e}\_2}$</span>;

<span>traction</span>

-   If we consider the special case where the normal vectors, $\\hat{n}$, align with the coordinate system ($\\hat{e}\_1$,$\\hat{e}\_2$,$\\hat{e}\_3$)

-   On the 1-face:
    $$\\begin{aligned}
            \\hat{n}&=\\hat{e}\_1: &\\quad \\hat{t}^n = t\_i^{(\\hat{e}\_1)} \\hat{e}\_i = t\_1^{(\\hat{e}\_1)} \\hat{e}\_1 + t\_2^{(\\hat{e}\_1)} \\hat{e}\_2 + t\_3^{(\\hat{e}\_1)} \\hat{e}\_3
            \\end{aligned}$$

-   On the 2-face:
    $$\\begin{aligned}
            \\hat{n}&=\\hat{e}\_2: &\\quad \\hat{t}^n = t\_i^{(\\hat{e}\_2)} \\hat{e}\_i = t\_1^{(\\hat{e}\_2)} \\hat{e}\_1 + t\_2^{(\\hat{e}\_2)} \\hat{e}\_2 + t\_3^{(\\hat{e}\_2)} \\hat{e}\_3
            \\end{aligned}$$

-   And on the 3-face:
    $$\\begin{aligned}
            \\hat{n}&=\\hat{e}\_3: &\\quad \\hat{t}^n = t\_i^{(\\hat{e}\_3)} \\hat{e}\_i = t\_1^{(\\hat{e}\_3)} \\hat{e}\_1 + t\_2^{(\\hat{e}\_3)} \\hat{e}\_2 + t\_3^{(\\hat{e}\_3)} \\hat{e}\_3
            \\end{aligned}$$

<span>stress tensor</span>

-   To simplify the notation, we introduce the stress tensor
    $$\\sigma\_{ij} = t\_j^{(\\hat{e}\_i)}$$

(0,0,0) – (2,0,0); (2,0,0) – (2,2,0) – (0,2,0); (0,2,0) – (0,0,0); (0,0,2) – (2,0,2) – (2,2,2) – (0,2,2) – (0,0,2); (2,0,0) – (2,0,2); (2,2,0) – (2,2,2); (0,2,0) – (0,2,2); (0,0,0) – (0,0,2); (1,1,2) – (1,1,3) node\[above\] <span>*σ*<sub>33</sub></span>; (1,1,2) – (2,1,2) node\[above\] <span>*σ*<sub>31</sub></span>; (1,1,2) – (1,2,2) node\[above\] <span>*σ*<sub>32</sub></span>; (2,1,1) – (3,1,1) node\[left\] <span>*σ*<sub>11</sub></span>; (2,1,1) – (2,1,2) node\[below left\] <span>*σ*<sub>13</sub></span>; (2,1,1) – (2,2,1) node\[above left\] <span>*σ*<sub>12</sub></span>; (1,2,1) – (1,3,1) node\[right\] <span>*σ*<sub>22</sub></span>; (1,2,1) – (2,2,1) node at (1.5,2,1.3) <span>*σ*<sub>21</sub></span>; (1,2,1) – (1,2,2) node\[below right\] <span>*σ*<sub>23</sub></span>;

<span>traction</span>

-   We can find some interesting information about the traction vector by considering an arbitrary tetrahedron with some traction $\\hat{t}^{(n)}$ applied to the surface

    (2,0,0) – (3,0,0) node\[below left\] <span>*x*<sub>1</sub></span>; (0,1.5,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub></span>; (0,0,1.5) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (2,0,0) – (0,0,0) – (0,1.5,0); (0,0,0) – (0,0,1.5); (2,0,0) – (0,1.5,0) – (0,0,1.5) – (2,0,0); (1,.75,.75) – (2,1.5,1.5) node\[above\] <span>$\\hat{n}$</span>; (1,.75,.75) – (1,2,1) node \[right\] <span>$\\hat{t}^{(n)}$</span>;

<span>traction</span>

-   If we consider the balance of forces in the *x*<sub>1</sub>-direction
    *t*<sub>1</sub>*d**A* − *σ*<sub>11</sub>*d**A*<sub>1</sub> − *σ*<sub>21</sub>*d**A*<sub>2</sub> − *σ*<sub>31</sub>*d**A*<sub>3</sub> + *b*<sub>1</sub>*ρ**d**V* = 0

-   The area components are:
    $$\\begin{aligned}
            dA\_1 &= n\_1 dA\\\\
            dA\_2 &= n\_2 dA\\\\
            dA\_3 &= n\_3 dA\\\\
            \\end{aligned}$$

-   And $dV = \\frac{1}{3}h dA$.

<span>traction</span>
$$t\_1 dA - \\sigma\_{11} n\_1 dA - \\sigma\_{21} n\_2 dA - \\sigma\_{31} n\_3 dA + b\_1 \\rho \\frac{1}{3}h dA = 0$$

-   If we let *h* → 0 and divide by *d**A*
    *t*<sub>1</sub> = *σ*<sub>11</sub>*n*<sub>1</sub> + *σ*<sub>21</sub>*n*<sub>2</sub> + *σ*<sub>31</sub>*n*<sub>3</sub>

-   We can write this in index notation as
    *t*<sub>1</sub> = *σ*<sub>*i*1</sub>*n*<sub>*i*</sub>

-   We find, similarly
    $$\\begin{aligned}
            t\_2 &= \\sigma\_{i2} n\_i\\\\
            t\_3 &= \\sigma\_{i3} n\_i\\\\
            \\end{aligned}$$

<span>traction</span>

-   We can further combine these results in index notation as
    *t*<sub>*j*</sub> = *σ*<sub>*i**j*</sub>*n*<sub>*i*</sub>

-   This means with knowledge of the nine components of *σ*<sub>*i**j*</sub>, we can find the traction vector at any point on any surface

<span>example</span>

-   Consider a block of material with a uniformly distributed force acting on the 1-face. Find the tractions on an arbitrary interior plane

    (0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (3,3) – (4,1) – (1,1); (1,2) – (0.5,2) node\[left\] <span>*P*</span>; (5,2) – (5.5,2) node\[right\] <span>*P*</span>; (3,3) – (5,3) – (5,1) – (4,1); (3.5,2) – (4,2.25) node at (4.1,2.3) <span>$\\hat{n}$</span>; (3.5,2) – (4,2.8) node at (4.3,2.8) <span>$\\hat{t}^{(n)}$</span>; (4,1) – (4.75,1.375); (4.5,1) arc (0:26.6:0.5) node at (4.6,1.15) <span>*θ*</span>;

<span>example</span>

-   First we consider a vertical cut on the interior 1-face (*n*<sub>*i*</sub> = ⟨1, 0, 0⟩)

-   Next we represent the force *P* as a vector, *p*<sub>*i*</sub> = ⟨*P*, 0, 0⟩

-   Balancing forces yields
    *t*<sub>*i*</sub>*A* − *p*<sub>*i*</sub> = 0

-   We find $t\_1 = \\frac{P}{A} = \\sigma\_{11}$, *t*<sub>2</sub> = 0 = *σ*<sub>12</sub> and *t*<sub>3</sub> = 0 = *σ*<sub>13</sub>

-   No force is applied in the other directions, so it is trivial to find the rest of the stress tensor
    $$\\sigma\_{ij} = \\begin{bmatrix}
            P/A & 0 & 0\\\\
            0 & 0 & 0\\\\
            0 & 0 & 0
            \\end{bmatrix}$$

<span>example</span>

-   We can now consider any arbitrary angle of interior cut.

-   The normal for a cut as shown in the diagram will be *n*<sub>*i*</sub> = ⟨cos*θ*, sin*θ*, 0⟩.

-   We can again use *t*<sub>*j*</sub> = *σ*<sub>*i**j*</sub>*n*<sub>*i*</sub> to find *t*<sub>*j*</sub> for any angle *θ*.
    $$\\begin{aligned}
            t\_1 &= \\frac{P}{A} \\cos \\theta \\\\
            t\_2 &= 0\\\\
            t\_3 &= 0
            \\end{aligned}$$

Stress Transformation
=====================

<span>stress transformation</span>

-   Stress transformation equations are identical to the strain transformation equations

-   Both stress and strain are tensor, and transform in the same fashion

-   Rotation about z-axis gives
    $$Q\_{ij} = \\begin{bmatrix}
            \\cos \\theta & \\cos (90-\\theta) & \\cos 90\\\\
            \\cos (90+\\theta) & \\cos \\theta & \\cos 90\\\\
            \\cos 90 & \\cos 90 & \\cos 0\\\\
            \\end{bmatrix} = \\begin{bmatrix}
            \\cos \\theta & \\sin \\theta & 0\\\\
            -\\sin \\theta & \\cos \\theta & 0\\\\
            0 & 0 & 1\\\\
            \\end{bmatrix}$$

<span>stress transformation</span>

-   We recall that
    *σ*<sub>*i**j*</sub><sup>′</sup> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*Q*<sub>*m**n*</sub>

-   Which gives
    $$\\begin{aligned}
            \\sigma^\\prime\_x &= \\sigma\_x \\cos ^2 \\theta + \\sigma\_y \\sin^2 \\theta + 2 \\tau\_{xy} \\sin \\theta \\cos \\theta \\\\
            \\sigma^\\prime\_y &= \\sigma\_x \\sin ^2 \\theta + \\sigma\_y \\cos^2 \\theta - 2 \\tau\_{xy} \\sin \\theta \\cos \\theta \\\\
            \\tau^\\prime\_{xy} &= -\\sigma\_x \\sin \\theta \\cos \\theta + \\sigma\_y \\sin \\theta \\cos \\theta + \\tau\_{xy} (\\cos^2 \\theta - \\sin^2 \\theta)
            \\end{aligned}$$

<span>stress transformation</span>

-   As with the strain transformation equations, these are often re-written using the double-angle formulae.
    $$\\begin{aligned}
            \\sigma^\\prime\_x &= \\frac{\\sigma\_x + \\sigma\_y}{2} + \\frac{\\sigma\_x - \\sigma\_y}{2}\\cos 2\\theta + \\tau\_{xy} \\sin 2\\theta \\\\
            \\sigma^\\prime\_y &= \\frac{\\sigma\_x + \\sigma\_y}{2} - \\frac{\\sigma\_x - \\sigma\_y}{2}\\cos 2\\theta - \\tau\_{xy} \\sin 2\\theta \\\\
            \\tau^\\prime\_{xy} &= \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin 2\\theta + \\tau\_{xy} \\cos 2\\theta
            \\end{aligned}$$

Principal Stresses
==================

<span>principal stresses</span>

-   Principal stresses can be found in the same fashion as principal values and principal strains
    det\[*σ*<sub>*i**j*</sub> − *σ**δ*<sub>*i**j*</sub>\]=0

<span>tractions</span>

-   We can use what we know about principal values to find some interesting things about the tractions

-   Consider the traction vector on an arbitrary internal face, and decompose into Normal and Shear components.

    <img src="../Figures/potato" alt="image" /> \[fig:potato\]

<span>tractions</span>

-   The normal component can be found using the dot product
    $$N = \\hat{T}^n \\cdot \\hat{n}$$

-   The shear component can be found using the Pythagorean theorem
    $$S^2 = |\\hat{T}^n|^2 - N^2$$

<span>tractions</span>

-   We now use the stress tensor in the principal direction to simplify the calculations
    $$\\begin{aligned}
            N &= \\hat{T}^n \\cdot \\hat{n}\\\\
            &= T^n\_i n\_i \\\\
            &= \\sigma\_{ji} n\_j n\_i\\\\
            &= \\sigma\_1 n\_1^2 + \\sigma\_2 n\_2^2 + \\sigma\_3 n\_3^2
            \\end{aligned}$$

<span>tractions</span>

-   We also know that
    $$\\begin{aligned}
            |\\hat{T}^n|^2 &= \\hat{T}^n \\cdot \\hat{T}^n\\\\
            &= T\_i^n T\_i^n \\\\
            &= \\sigma\_{ji} n\_j \\sigma\_{ki} n\_k\\\\
            &= \\sigma\_1^2 n\_1^2 + \\sigma\_2^2 n\_2^2 + \\sigma\_3^2 n\_3^2
            \\end{aligned}$$

<span>mohr’s circle</span>

-   If we constrain the normal vector to be a unit vector we can formulate the following inequalities
    $$\\begin{aligned}
            S^2 + (N-\\sigma\_2)(N-\\sigma\_3) &\\ge 0\\\\
            S^2 + (N-\\sigma\_3)(N-\\sigma\_1) &\\le 0\\\\
            S^2 + (N-\\sigma\_1)(N-\\sigma\_2) &\\ge 0\\\\
            \\end{aligned}$$

-   These inequalities form what is known as Mohr’s circle

<span>mohr’s circle</span>

<img src="../Figures/mohr" alt="image" /> \[fig:mohr\]

Maximum Shear Stress
====================

<span>maximum shear stress</span>

-   From Mohr’s circle, we can find the maximum shear stress in terms of the principal stresses
    *S*<sub>*m**a**x*</sub> = (*σ*<sub>1</sub> − *σ*<sub>3</sub>)/2

<span>maximum shear stress</span>

-   For plane stress problems, we can also use the stress transformation equations to find the maximum shear stress

-   We desire to maximize this equation:
    $$\\tau^\\prime\_{xy} = \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin 2\\theta + \\tau\_{xy} \\cos 2\\theta$$

<span>maximum shear stress</span>

-   Taking the derivative with respect to *θ* gives
    $$\\frac{\\partial}{\\partial \\theta} (\\tau^\\prime\_{xy}) = (\\sigma\_y-\\sigma\_x)\\cos 2\\theta - 2\\tau\_{xy} \\sin 2\\theta = 0$$

-   Which we can use to find 2*θ*
    $$2\\theta = \\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)$$

<span>maximum shear stress</span>

-   Substituting back into the original equation gives
    $$\\tau^\\prime\_{max} = \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin \\left\[\\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)\\right\] + \\tau\_{xy} \\cos \\left\[\\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)\\right\]$$

-   Note that
    $$\\begin{aligned}
            \\sin (\\tan ^{-1} (x)) &= \\frac{x}{\\sqrt{1+x^2}}\\\\
            \\cos (\\tan ^{-1} (x)) &= \\frac{1}{\\sqrt{1+x^2}}\\\\
            \\end{aligned}$$

<span>maximum shear stress</span>

-   We note that
    $$\\sqrt{1+ \\left(\\frac{\\sigma\_y - \\sigma\_x}{2 \\tau\_{xy}}\\right)^2} = \\frac{\\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}}{2\\tau\_{xy}}$$

-   And thus we find
    $$\\tau\_{max} = \\frac{(\\sigma\_y-\\sigma\_x)^2}{2 \\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}} + \\frac{4\\tau\_{xy}^2}{2 \\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}}$$

<span>maximum shear stress</span>

-   Adding the terms and simplifying, we find
    $$\\tau\_{max} = \\sqrt{\\left(\\frac{\\sigma\_y-\\sigma\_x}{2}\\right)^2+\\tau\_{xy}^2}$$

group problems
==============

<span>group one</span>

-   The stress state in a rectangle under biaxial loading is
    $$\\sigma\_{ij} = \\begin{bmatrix} X & 0 & 0\\\\
          0 & Y & 0\\\\
          0 & 0 & 0\\end{bmatrix}$$

-   Find the traction vector, as well as the normal and shearing stresses on some oblique plane, *S*

(0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (5,3) – (5,1) – (1,1); (1.5,1.5) – (2.5,2.5); node at (1.7,2.5) <span>*S*</span>; (2.35,1.5) arc (0:45:0.85) node\[right\] <span>*θ*</span>;

<span>group two</span>

-   For the figure shown, what must the traction be on the other faces for the stress to be uniform and in equilibrium?

(0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (3,3) – (3,1) – (1,1); (3,2) – (4,3) node\[right\] <span>*t*<sub>*i*</sub> = *σ*<sub>0</sub>⟨1, 1⟩</span>;

<span>group three</span>

-   For the figure shown, find the (uniform) stress tensor. What must the traction be on the last face?

(0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (3,1) – (1,1); (2,2) – (3,2) node\[right\] <span>$t\_i=\\frac{\\sigma\_0}{\\sqrt{2}} \\langle 1, 0\\rangle$</span>; (2,1) – (2.5,0.5) node\[right\] <span>$t\_i=\\frac{\\sigma\_0}{2} \\langle 1, -1 \\rangle$</span>;
