To more precisely solve the example we discussed in class, we need to use the true strain, not the engineering strain, to find the deformation of the material. Recall the definition of the Poisson’s ratio:
$$\\nu = - \\frac{d \\epsilon\_{transverse}}{d \\epsilon\_{axial}} = - \\frac{d \\epsilon\_{y}}{d \\epsilon\_{x}}$$
 Also, the definition of true strain
$$d\\epsilon\_x = \\frac{1}{x}dx$$

We can re-write (1) to find
−*ν**d**ϵ*<sub>*x*</sub> = *d**ϵ*<sub>*y*</sub>
 And substitute (2) for both *ϵ*<sub>*x*</sub> and *ϵ*<sub>*y*</sub>
$$-\\nu \\frac{1}{x}dx = \\frac{1}{y}dy$$

We desire to find the *y*-displacement for some applied *x*-displacement, so we integrate this equation. If the material has an original length *L* in the *x*-direction, with a deformation of *Δ**L*, and a width of *W* in the *y*-direction, with a deformation of *Δ**W*, we write the integrals as
$$-\\nu \\int\_{L}^{1+\\Delta L}\\frac{1}{x}dx = \\int\_W^{W-\\Delta W}\\frac{1}{y}dy$$
 Performing the integral, we find
−*ν*\[ln(*L*+*Δ**L*)−ln(*L*)\] = ln(*W* − *Δ**W*)−ln(*W*)
 Using the rules of logarithms, we can re-write this as
$$-\\nu \\left\[\\ln\\left( \\frac{L+\\Delta L}{L} \\right) \\right\] = \\ln \\left( \\frac{W-\\Delta W}{W} \\right)$$
 Which simplifies to
$$-\\nu \\left\[\\ln\\left(1+\\frac{\\Delta L}{L}\\right) \\right\] = \\ln\\left(1-\\frac{\\Delta W}{W}\\right)$$
 We can take the exponential of both sides to find that
$$\\left(1+\\frac{\\Delta L}{L}\\right)^{-\\nu} = 1-\\frac{\\Delta W}{W}$$

For the incompressible example I did in class, with *ν* = 0.5, *L* = *W* = 1 and *Δ**L* = 1, we can calculate *Δ**W*
$$\\left(1+\\frac{1}{1}\\right)^{-0.5} = 1-\\frac{\\Delta W}{1}$$
$$\\Delta W = 1 - 2^{-0.5} = \\frac{2-\\sqrt{2}}{2}$$

The original volume is given by *V*<sub>0</sub> = *L**W*<sup>2</sup> (assuming a square cross-section and isotropic material), the deformed volume is given as *V* = (*L* + *Δ**L*)(*W* − *Δ**W*)<sup>2</sup>. The original volume is clearly 1, while the deformed volume is
$$V = (1+1)\\left(1-\\frac{2-\\sqrt{2}}{2}\\right)^2$$
 Which simplifies to
$$V = 2\\left(\\frac{\\sqrt{2}}{2}\\right)^2 = \\frac{4}{4} = 1$$
 Therefore the volume remains unchanged, representing an incompressible material.

As many of us suspected, the problem with my example in class was using engineering strain for a very large deformation, which resulted in an incorrect transverse deformation, but with the correct treatment of true strain, we find the result we expect.
