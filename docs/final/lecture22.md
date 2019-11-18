<span>upcoming schedule</span>

-   Nov 15 - Airy Stress Functions

-   Nov 20 - Airy Stress Functions, HW 7 Due

-   Nov 22 - No Class (Thanksgiving Break)

-   Nov 27 - Airy Stress Functions, Special Topics

-   Nov 29 - Special Topics

-   Dec 4 - Final Exam Review, HW 8 Due

-   Dec 6 - Final Exam Review

### outline

\[sections numbered\]

Polynomial Solutions
====================

<span>airy stress function solutions</span>

-   To solve a problem using Airy stress functions, we need to solve this biharmonic equation
    $$\\frac{\\partial^4 \\phi}{\\partial x^4} + 2\\frac{\\partial^4 \\phi}{\\partial x^2 \\partial y^2} + \\frac{\\partial^4 \\phi}{\\partial y^4} = 0$$

-   One solution to this is the power series
    $$\\phi(x,y) = \\sum\_{m=0}^{\\infty} \\sum\_{n=0}^{\\infty} A\_{mn} x^m y^n$$

<span>power series solution</span>

-   Note that terms for *m* + *n* ≤ 1 do not contribute to the stress, and can be neglected

-   Also note that for *m* + *n* ≤ 3 compatibility is automatically satisfied

-   For *m* + *n* ≥ 4 the coefficients must be related for compatibility to be satisfied

<span>example</span>

<img src="tension" alt="image" /> \[fig:tension\]

<span>example</span>

-   What are the boundary conditions in terms of the stress tensor?
    $$\\begin{aligned}
            \\sigma\_x (\\pm l,y) &= T\\\\
            \\sigma\_y (x, \\pm c) &= 0\\\\
            \\tau\_{xy} (\\pm l, y) &= \\tau\_{xy} (x, \\pm c) = 0
            \\end{aligned}$$

-   What is the simplest form of polynomial stress function that would satisfy these boundary conditions?
    $$\\begin{aligned}
            \\sigma\_{xx} &= \\frac{\\partial^2 \\phi}{\\partial y^2} + V\\\\
            \\sigma\_{yy} &= \\frac{\\partial^2 \\phi}{\\partial x^2} + V\\\\
            \\tau\_{xy} &= -\\frac{\\partial^2 \\phi}{\\partial x \\partial y}
            \\end{aligned}$$

<span>saint venant’s principle</span>

-   Some boundary conditions are cumbersome to model exactly

-   In this case we can use Saint Venant’s principle to express a statically equivalent version of the boundary conditions

<span>example</span>

<img src="bending" alt="image" /> \[fig:bending\]

<span>example</span>

-   Locally along the ends, there will be some tractions in order to apply the bending moment

-   These tractions will cancel out, however, so we can use Saint Venant’s principle to avoid modeling them explicitly
    $$\\begin{aligned}
            \\sigma\_y (x, \\pm c) &= 0\\\\
            \\tau\_{xy} (x, \\pm c) &= \\tau\_{xy} (\\pm L, y) = 0\\\\
            \\int\_{-c}^{c}\\sigma\_x (\\pm l,y)dy &= 0\\\\
            \\int\_{-c}^{c}\\sigma\_x (\\pm l,y)ydy &= -M
            \\end{aligned}$$

<span>example</span>

-   What is the simplest form of polynomial stress function that would satisfy these boundary conditions?
    $$\\begin{aligned}
            \\sigma\_{xx} &= \\frac{\\partial^2 \\phi}{\\partial y^2} + V\\\\
            \\sigma\_{yy} &= \\frac{\\partial^2 \\phi}{\\partial x^2} + V\\\\
            \\tau\_{xy} &= -\\frac{\\partial^2 \\phi}{\\partial x \\partial y}
            \\end{aligned}$$

<span>example</span>

<img src="distributed" alt="image" /> \[fig:distributed\]

<span>example</span>

-   In this case we can write the boundary conditions as
    $$\\begin{aligned}
            \\tau\_{xy}(x, \\pm c) &= 0\\\\
            \\sigma\_y (x,c) &= 0\\\\
            \\sigma\_y (x,-c) &= -w\\\\
            \\int\_{-c}^{c} \\sigma\_x (\\pm l, y) dy &= 0\\\\
            \\int\_{-c}^{c} \\sigma\_x (\\pm l, y) ydy &= 0\\\\
            \\int\_{-c}^{c} \\tau\_{xy} (\\pm l, y) dy &= \\mp wl\\\\
            \\end{aligned}$$

<span>example</span>

-   And find that the stress function
    $$\\phi = Ax^2 + Bx^2 y + Cx^2 y^3 + Dy^3 - \\frac{1}{5}C y^5$$

-   Can satisfy the boundary conditions as well as compatibility

Examples
========

<span>end-loaded cantilever beam</span>

; ; ; (0,-0.5) – (0,0.5) – (6,0.5) – (6,-0.5) – (0,-0.5); \[-90\]; \[-90\]\[1\]; node at (6.5,0.5) <span>*P*</span>; (0,1) node\[above\] <span>*y*</span> – (0,0) – (2,0) node\[right\] <span>*x*</span>; (2.7,-1) node\[right\] <span>*L*</span> – (0,-1); (3.3,-1) – (6,-1); (3,0.25) node\[below\] <span>2*c*</span> – (3,0.5); (3,-0.25) – (3,-0.5);

<span>baseball problem II</span>

-   Solve the problem of a baseball with an incompressible core under remote pressure using the Airy Stress method


