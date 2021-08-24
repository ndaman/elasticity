# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
August 24, 2021

----
## upcoming schedule

-   Aug 24 - Principal Values
-   Aug 26 - Tensor Calculus
-   Aug 27 - Homework 1 Due
-   Aug 31 - Displacement and Strain
-   Sep 2 - Strain Transformation

----
## outline

<!-- vim-markdown-toc GFM -->

* group problems
* coordinate transformation
* examples
* principal directions
* examples

<!-- vim-markdown-toc -->

----
## office hours

-   My office - WH 200D
-   If you cannot make it to those hours just e-mail me to set an appointment

---
# principal directions

----
## principal directions

-   Principal directions are defined as
`$$(a_{ij} - \lambda \delta_{ij})n)j = 0$$`
-   `$\lambda$` are the principal values and `$n_{ij}$` are the principal directions
-   For each eigenvalue there will be a principal direction
-   We find the principal direction by substituting the solution for `$\lambda$` back into this equation

----
## example

`$$\begin{bmatrix}
	1-\lambda_1 & 2\\
	2 & 4-\lambda_1
	\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0$$`

-   This gives

`$$\begin{bmatrix}
	-4 & 2\\
	2 & -1
	\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0$$`

----
## example

-   We proceed to solve the equations using row-reduction, but we find

`$$\begin{bmatrix}
	2 & -1\\
	0 & 0
	\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0$$`

-   This means we cannot uniquely solve for `$n_j$`
-   We are only concerned with the direction, magnitude is not important
-   Choose `$n_2=1$`, solve for `$n_1$`
-   `$n^{(1)} = \langle \frac{1}{2}, 1 \rangle$`

----
## example

-   Similarly, for `$\lambda_2 = 0$`, we find

`$$\begin{bmatrix}
	1 & 2\\
	2 & 4
	\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0$$`

-   Which, after row-reduction, becomes

`$$\begin{bmatrix}
	1 & 2\\
	0 & 0
	\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0$$`

-   If we choose `$n_2=1$`, we find `$n_1 = -2$`
-   This gives `$n^{(2)} = \langle -2, 1 \rangle$`

----
## example

-   We can assemble a transformation matrix, `$Q_{ij}$`, from the principal directions
-   First we need to normalize them to unit vectors
-   `$||n^{(1)}|| = \sqrt{\frac{5}{4}}$`
-   `$\hat{n}^{(1)} = \frac{2}{\sqrt{5}} \langle \frac{1}{2}, 1 \rangle = \langle \frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}} \rangle$`
-   `$||n^{(2)}|| = \sqrt{5}$`
-   `$\hat{n}^{(2)} = \langle \frac{-2}{\sqrt{5}}, \frac{1}{\sqrt{5}} \rangle $`

----
## example

-   This gives

`$$Q_{ij} = \frac{1}{\sqrt{5}}\begin{bmatrix}
	1 & 2\\
	-2 & 1
\end{bmatrix}$$`

-   And we find

`$$A_{mn} = Q_{mi}Q_{nj}A_{ij}$$`

`$$A_{ij}^\prime = \begin{bmatrix}
	5 & 0 \\
	0 & 0
\end{bmatrix}$$`

---
# examples

----
## example

-   Find principal values, principal directions, and invariants for the tensor

`$$c_{ij} = \begin{bmatrix}
	8 & 0 & 0\\
	0 & 3 & 1\\
	0 & 1 & 3
\end{bmatrix}$$`

----
## example

-   Characteristic equation simplifies to
-   `$-\lambda^3 + 14\lambda^2 - 56\lambda + 64 = 0$`
-   Which has the solutions `$\lambda = 2, 4, 8$`

----
## example

-   To find the principal direction for `$\lambda_1 = 8$`

`$$\begin{bmatrix}
	8-8 & 0 & 0\\
	0 & 3-8 & 1\\
	0 & 1 & 3-8
	\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0$$`

----
## example

-   After row-reduction, we find

`$$\begin{bmatrix}
	0 & 0 & 0\\
	0 & 0 & -24\\
	0 & 1 & -5
	\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0$$`

-   This means that `$n_3=0$` and, as a result, `$n_2 = 0$`. 
-   `$n_1$` can be any value, we choose `$n_1 = 1$` to give a unit vector.
-   `$n^{(1)} = \langle 1, 0, 0 \rangle$`

----
## example

-   To find the principal direction for `$\lambda_2 = 4$`

`$$\begin{bmatrix}
	8-4 & 0 & 0\\
	0 & 3-4 & 1\\
	0 & 1 & 3-4
	\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0$$`

----
## example

-   After row-reduction, we find

`$$\begin{bmatrix}
	4 & 0 & 0\\
	0 & -1 & 1\\
	0 & 0 & 0
	\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0$$`

-   This means that `$n_1 = 0$`
-   We also know that `$n_2 = n_3$` so we choose `$n_2 = n_3 = 1$`
-   This gives `$n^{(2)} = \frac{1}{\sqrt{2}}\langle 0, 1, 1 \rangle$` after normalization

----
## example

-   To find the principal direction for `$\lambda_3 = 2$`

`$$\begin{bmatrix}
	8-2 & 0 & 0\\
	0 & 3-2 & 1\\
	0 & 1 & 3-2
	\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0$$`

----
## example

-   After row-reduction, we find

`$$\begin{bmatrix}
	6 & 0 & 0\\
	0 & 1 & 1\\
	0 & 0 & 0
	\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0$$`

-   This means that `$n_1 = 0$`
-   We also know that `$n_2 = -n_3$`, so we choose `$n_2 = 1$` and `$n_1 = -1$`
-   This gives `$n^{(3)} = \frac{1}{\sqrt{2}}\langle 0, 1, -1 \rangle$` after normalization

----
## example

-   In summary, for `$c_{ij}$` we have:
-   `$\lambda_1 = 8$` and `$n^{(1)} = \langle 1, 0, 0 \rangle$`
-   `$\lambda_2 = 4$` and `$n^{(2)} = \langle 0, 1, 1 \rangle$`
-   `$\lambda_3 = 2$` and `$n^{(3)} = \langle 0, 1, -1 \rangle$`
-   We can assemble `$n^{(i)}$` into a transformation tensor

`$$Q_{ij} = \frac{1}{\sqrt{2}}\begin{bmatrix}
	\sqrt{2} & 0 & 0\\
	0 & 1 & 1\\
	0 & 1 & -1
\end{bmatrix}$$`

----
## example

-   What is `$c_{ij}^\prime$`?
-   `$c_{ij}^\prime = Q_{im}Q_{jn}c_{mn}$`

`$$c_{ij}^\prime = \begin{bmatrix}
	8 & 0 & 0 \\
	0 & 4 & 0 \\
	0 & 0 & 2
\end{bmatrix}$$`

----
## example

-   We can also find the invariants for

`$$c_{ij} = \begin{bmatrix}
	8 & 0 & 0\\
	0 & 3 & 1\\
	0 & 1 & 3
\end{bmatrix}$$`

-   Recall:

`$$\begin{aligned}
	I_\alpha &= a_{ii}\\
	II_\alpha &= \frac{1}{2}(a_{ii} a_{jj} - a_{ij}a_{ij})\\
	III_\alpha &= \det [ a_{ij}]
\end{aligned}$$`

----
## example

-   First invariant

`$$I_\alpha = a_{ii} = 8 + 3 + 3 = 14$$`

-   Second invariant

`$$II_\alpha = \frac{1}{2}(a_{ii} a_{jj} - a_{ij}a_{ij})$$`
`$$a_{ii} a_{jj} = 14 \times 14$$`
`$$a_{ij}a_{ij} = a_{11} a_{11} + a_{12}a_{12} + a_{13}a_{13} + ... + a_{33}a_{33}$$`
`$$II_\alpha = \frac{1}{2}(196 - 84) = 56$$`

----
## example

-   Third invariant

`$$III_\alpha = \det [a_{ij}]$$`
`$$III_\alpha = 8 (3 \times 3 - 1 \times 1) = 64$$`

