<span>upcoming schedule</span>

-   Sep 25 - Exam Return, Stress and traction

-   Sep 27 - Stress transformation, Mohr’s circle

-   Oct 2 - Equilibrium

-   Oct 4 - Material Behavior

### outline

\[sections numbered\]

exam
====

<span>average</span>

-   Before the curve, the class average was 67.9% with a standard deviation of 14.0%

-   This was a pretty difficult exam, high score was 88% before the curve

-   After the curve, the class average was 85.3% with a standard deviation of 10.3%

-   Exam formula is Curved Score = 0.73\*(original score) + 35.61

-   Score in blackboard is curved

<span>problems</span>

-   Problem 1 had lowest average, followed by Problem 3

-   Problem 5 had the highest average, followed by Problem 3

-   Problem 2 is the only one on the exam that no one received full credit for

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


