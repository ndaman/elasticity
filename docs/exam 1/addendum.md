# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
August 29, 2019

----
## upcoming schedule

-   Aug 28 - Tensor Calculus
-   Sep 2 - Labor Day
-   Sep 4 - Displacement and Strain, Homework 1 Due
-   Sep 9 - Strain Transformation
-   Sep 11 - Exam 1 Review

---
# principal values

----
## principal values

-   In the 2D coordinate transformation example, we were able to eliminate one value from a vector using coordinate transformation
-   For second-order tensors, we desire to find the “principal values” where all non-diagonal terms are zero

----
## principal directions

-   The direction determined by the unit vector, *n*<sub>*j*</sub>, is said to be the *principal direction* or *eigenvector* of the symmetric second-order tensor, *a*<sub>*ij*</sub> if there exists a parameter, *λ*, such that
    *a*<sub>*ij*</sub>*n*<sub>*j*</sub> = *λn*<sub>*i*</sub>
-   Where *λ* is called the *principal value* or *eigenvalue* of the tensor

----
## principal values

-   We can re-write the equation
    (*a*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>)*n*<sub>*j*</sub> = 0

-   This system of equations has a non-trivial solution if and only if det[*a*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>]=0
-   This equation is known as the characteristic equation, and we solve it to find the principal values of a tensor

----
## example

-   Find the principal values of the tensor

$$A\_{ij} = \\begin{bmatrix}
	1 & 2\\\\
	2 & 4
\\end{bmatrix}$$

-   From the characteristic equation, we know that det[*A*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>]=0, or

$$\\begin{vmatrix}
	1-\\lambda & 2\\\\
	2 & 4 - \\lambda
\\end{vmatrix} = 0$$

----
## example

-   Calculating the determinant gives
    (1 − *λ*)(4 − *λ*)−4 = 0

-   Multiplying out and simplifying, we find
    *λ*<sup>2</sup> − 5*λ* = *λ*(*λ* − 5)=0

-   This has the solution *λ* = 0, 5

---
# invariants

----
## invariants

-   Every tensor has some invariants which do not change with coordinate transformation
-   These are known as *fundamental invariants*
-   The characteristic equation for a tensor in 3D can be written in terms of the invariants
    det[*a*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>]= − *λ*<sup>3</sup> + *I*<sub>*α*</sub>*λ*<sup>2</sup> − *II*<sub>*α*</sub>*λ* + *III*<sub>*α*</sub> = 0

----
## invariants

-   The invariants can be found by the following equations
$$\\begin{aligned}
	I\_\\alpha &= a\_{ii}\\\\
	II\_\\alpha &= \\frac{1}{2}(a\_{ii} a\_{jj} - a\_{ij}a\_{ij})\\\\
	III\_\\alpha &= \\det \[ a\_{ij}\]\\end{aligned}$$

----
## invariants

-   In the principal direction, *a*<sub>*ij*</sub><sup>′</sup> will be

$$a\_{ij}^\\prime = \\begin{bmatrix}
	\\lambda\_1 & 0 & 0\\\\
	0 & \\lambda\_2 & 0\\\\
	0 & 0 & \\lambda\_3
\\end{bmatrix}$$

-   Since invariants do not change with coordinate systems, we can also write the invariants as

$$\\begin{aligned}
	I\_\\alpha &= \\lambda\_1 + \\lambda\_2 + \\lambda\_3\\\\
	II\_\\alpha &= \\lambda\_1\\lambda\_2 + \\lambda\_2 \\lambda\_3 + \\lambda\_3 \\lambda\_1\\\\
	III\_\\alpha &= \\lambda\_1 \\lambda\_2 \\lambda\_3\\end{aligned}$$


