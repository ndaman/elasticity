# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
August 19, 2021

----
## upcoming schedule


-   Aug 19 - Coordinate Transformation
-   Aug 24 - Principal Values
-   Aug 26 - Tensor Calculus
-   Aug 31 - Displacement and Strain

----
## outline

<!-- vim-markdown-toc GFM -->

* review
* examples
* index notation algebra
* group problems
* coordinate transformation
* examples

<!-- vim-markdown-toc -->

---
# review

----
## office hours

-   Homework will generally be due on Fridays
-   Feel free to e-mail me for an appointment outside office hours if the time does not work for you

----
## homework

-   Homework 1 is available on Blackboard if you want to start working on it
-   Covers all of Chapter 1, relatively difficult, don’t wait until last minute
-   Study groups help a lot (but submit your own work)

----
## index notation

Free index vs. dummy index

<div class="left">

-  	is not repeated on any term
-		takes all values (1,2,3)
-   e.g. `$u_i = (u_1, u_2, u_3)$`
-		must match across terms in an express or equation

</div>

<div class="right">

-		is repeated on at least one term
-		indicates summation over all values
-   e.g. `$\sigma_{ii} = \sigma_{11} + \sigma_{22} + \sigma_{33}$`
-   can not be used more than twice in the same term (`$A_{ij}B_{jk}C_{kl}$` is good, `$A_{ij}B_{ij}C_{ij}$` is not)
	
</div>

----
## symmetry

-   Two types of symmetry: symmetry and antisymmetry
-   Symmetry: *a*<sub>*ij*</sub> = *a*<sub>*ji*</sub>
-   Anti-symmetry: *a*<sub>*ij*</sub> = −*a*<sub>*ji*</sub>

----
## symmetry

-   We can break any tensor up into symmetric and anti-symmetric portions
-   <!-- .element style="list-style-type: none" --> 
`$a_{ij} = \frac{1}{2} (a_{ij} + a_{ji}) + \frac{1}{2} (a_{ij} - a_{ji})$`

----
## example

-   Find symmetric and anti-symmetric portions of

`$$\begin{bmatrix}
1 & 4 & 3\\
2 & 1 & 5\\
4 & 3 & 6
\end{bmatrix}$$`

----
## example symmetric portion

`$$a_{(ij)} = \frac{1}{2}(a_{ij} + a_{ji})$$`

`$$a_{(ij)} = \frac{1}{2} \left (
\begin{bmatrix}
1 & 4 & 3\\
2 & 1 & 5\\
4 & 3 & 6
\end{bmatrix}+
\begin{bmatrix}
1 & 2 & 4\\
4 & 1 & 3\\
3 & 5 & 6
\end{bmatrix}\right)
= \begin{bmatrix}
1 & 3 & 3.5\\
3 & 1 & 4\\
3.5 & 4 & 6
\end{bmatrix}$$`

----
## example anti-symmetric portion

`$$a_{(ij)} = \frac{1}{2}(a_{ij} - a_{ji})$$`

`$$a_{(ij)} = \frac{1}{2} \left (
\begin{bmatrix}
1 & 4 & 3\\
2 & 1 & 5\\
4 & 3 & 6
\end{bmatrix}-
\begin{bmatrix}
1 & 2 & 4\\
4 & 1 & 3\\
3 & 5 & 6
\end{bmatrix}\right)
= \begin{bmatrix}
0 & 1 & -0.5\\
-1 & 0 & 1\\
0.5 & -1 & 0
\end{bmatrix}$$`

----
## special symbols

-   For convenience we define two symbols in index notation
-   *Kronecker delta* is a general tensor form of the Identity Matrix

`$$\delta_{ij} = \left\\{
\begin{array}{ll}
1& \text{if $i=j$}\\
0& \text{otherwise}
\end{array}
\right. = \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$$`

-   Is also used for higher order tensors

----
## Kronecker delta

-   `$\delta_{ij} = \delta_{ji}$`
-   `$\delta_{ij} = 3$`
-   `$\delta_{ij} a_j = a_i$`
-   `$\delta_{ij}a_{ij} = a_{ii}$`

----
## special symbols

-   *alternating symbol* or *permutation symbol*

`$$\epsilon_{ijk} = \left \{
\begin{array}{rl}
1 & \text{if $ijk$ is an even permutation of 1,2,3}\\
-1 & \text{if $ijk$ is an odd permutation of 1,2,3}\\
0 & \text{otherwise}
\end{array}
\right.$$`

----
## permutation symbol

-   This symbol is not used as frequently as the *Kronecker delta*
-   For our uses in this course, it is enough to know that 123, 231, and 312 are even permutations
-   321, 132, 213 are odd permutations
-   all other indexes are zero
-   `$\epsilon_{ijk}\epsilon_{imn} = \delta_{jm} \delta_{kn} - \delta_{jn}\delta_{mk}$`

----
## determinant

-   We use the alternating symbol for writing determinants and cross-products

`$$\det[a_{ij}] = |a_{ij}| = \begin{vmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}
\end{vmatrix}
= \epsilon_{ijk}a_{i1} a_{j2} a_{k3}$$`

`$$\det[a_{ij}] = \frac{1}{6}\epsilon_{ijk} \epsilon_{pqr}a_{ip}a_{jq}a_{kr}$$`

----
## cross product

-   The cross-product can be written as a determinant:

`$$\hat{a} \times \hat{b} = \begin{vmatrix}
\hat{e}_1 & \hat{e}_2 & \hat{e}_3\\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}$$`

-   Or in index notation

`$$\hat{a} \times \hat{b} = \epsilon_{ijk} \hat{e}_i a_j b_k $$`

----
## partial derivative

-   We indicate (partial) derivatives using a comma
-   In three dimensions, we take the partial derivative with respect to each variable (*x*, *y*, *z* or *x*<sub>1</sub>, *x*<sub>2</sub>, *x*<sub>3</sub>)
-   For example a scalar property, such as density, can have a different value at any point in space
-   `$\rho = \rho(x_1, x_2, x_3)$`

`$$\rho_{,i} = \frac{\partial}{\partial x_i} \rho = \left\langle \frac{\partial \rho }{\partial x_1}, \frac{\partial \rho }{\partial x_2}, \frac{\partial \rho }{\partial x_3} \right\rangle$$`

----
## partial derivative

-   Similarly, if we take the partial derivative of a vector, it produces a matrix

`$$u_{i,j} = \frac{\partial}{\partial x_j} u_i = \begin{bmatrix}
\frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2} & \frac{\partial u_1}{\partial x_3}\\
\frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2} & \frac{\partial u_2}{\partial x_3}\\
\frac{\partial u_3}{\partial x_1} & \frac{\partial u_3}{\partial x_2} & \frac{\partial u_3}{\partial x_3}
\end{bmatrix}$$`

---
# examples

----
## example 1

-   Write the following in conventional notation
    *T*<sub>*ij*, *j*</sub> + *F*<sub>*i*</sub> = 0
-   <!-- .element class="fragment" --> The comma indicates a partial derivative
-   <!-- .element class="fragment" --> The first index, 
_i_, is not repeated in any terms, so it is a “free index”
    -   This means in a 3D coordinate system, we will have at least three equations
-   <!-- .element class="fragment" --> The second index, 
_j_, is repeated in the first term, indicating summation.
    -   We will have exactly three equations

----
## example 1 (solution)

*T*<sub>*ij*, *j*</sub> + *F*<sub>*i*</sub> = 0

`$$\begin{aligned}
\frac{\partial T_{11}}{\partial x_1} + \frac{\partial T_{12}}{\partial x_2} + \frac{\partial T_{13}}{\partial x_3} + F_1= 0\\
\frac{\partial T_{21}}{\partial x_1} + \frac{\partial T_{22}}{\partial x_2} + \frac{\partial T_{23}}{\partial x_3} + F_2= 0\\
\frac{\partial T_{31}}{\partial x_1} + \frac{\partial T_{32}}{\partial x_2} + \frac{\partial T_{33}}{\partial x_3} + F_3= 0\\\end{aligned}$$`

----
## example 2

-   Identify whether the following expressions represent a scalar, vector, or matrix
-   If index notation is used incorrectly, give a reason why
-   *A*<sub>*i*</sub> = *B*<sub>*i*</sub>
-   *A*<sub>*i*</sub> = *B*<sub>*i*</sub> + *C*<sub>*i*</sub>*D*<sub>*i*</sub>
-   `$\delta_{ij}A_iB_j$`
-   `$\phi = \frac{\partial F_i}{\partial x_i}$`

----
## example 2 (solution)

-   Vector equation
-   Incorrect use of index notation, *i* used as both free and dummy index
-   Scalar value (both indexes are dummy indexes)
-   Scalar value (could also be written *F*<sub>*i*, *i*</sub>)

---
# index notation algebra

----
## substitution

-   When solving tensor equations, we often need to manipulate expressions
-   We need to make sure the correct indexes are used when substituting, for example
-   *a*<sub>*i*</sub> = *U*<sub>*im*</sub>*b*<sub>*m*</sub>
-   *b*<sub>*i*</sub> = *V*<sub>*im*</sub>*c*<sub>*m*</sub>
-   To substitute the second into the first, we need to change indexes

----
## substitution

-   We need to change the free index, *i*, to *m* in the second equation
-   Since *m* is already used as the dummy index, we need to change that too
-   *b*<sub>*m*</sub> = *V*<sub>*mj*</sub>*c*<sub>*j*</sub>
-   We can now make the substitution
-   *a*<sub>*i*</sub> = *U*<sub>*im*</sub>*V*<sub>*mj*</sub>*c*<sub>*j*</sub>

----
## multiplication

-   We need to be careful with indexes when multiplying expressions
-   `$p = a_m b_m$` and `$q = c_m d_m$`
-   We can express, *pq*, but remember the dummy index cannot be repeated more than once
-   `$pq \ne a_m b_m c_m d_m$`
-   Instead we must change the dummy index in one of the expressions first
-   `$pq = a_m b_m c_n d_n$`

----
## factoring

-   In the following expression, we would like to factor out *n*, but it has different indexes
-   `$T_{ij}n_j - \lambda n_i = -$`
-   Recall `$\delta_{ij}a_j = a_i$`, we can rewrite `$n_i = \delta_{ij}n_j$`
-   `$T_{ij}n_j = \lambda \delta_{ij}n_j = -$`
-   `$T_{ij} - \lambda \delta_{ji})n_j = 0$`

----
## contraction

-   `$T_{ii}$` is the contraction of `$T_{ij}$`
-   This can often be a useful tool in solving tensor equations
-   `$T_{ij} = \lambda \Delta \delta_{ij} + 2\mu E_{ij}$`
-   `$T_{ii} = \lambda \Delta \delta_{ii} + 2\mu E_{ii}$`

----
## example

-   Solve the equation below for *U*<sub>*k*</sub> in terms of *P*<sub>*i*</sub> and *a*<sub>*i*</sub>.
-   <!-- .element style="list-style-type: none" --> 
`$$\mu \left[ \delta_{kj} a_i a_i + \frac{1}{1-2\nu} a_k a_j \right] U_k = P_j$$`
-   <!-- .element class="fragment" --> Multiply both sides by 
_a_<sub>*j*</sub>
-		<!-- .element style="list-style-type: none", class="fragment" --> 
`$$\mu \left[ a_j \delta_{kj} a_i a_i + \frac{1}{1-2\nu} a_k a_j a_j \right] U_k = P_j a_j$$`
-   <!-- .element class="fragment" -->The dummy indexes can be changed
-		<!-- .element style="list-style-type: none", class="fragment" --> 
`$$\mu \left[ a_j \delta_{kj} a_i a_i + \frac{1}{1-2\nu} a_k a_i a_i \right] U_k = P_j a_j$$`

----
## example

-   *a*<sub>*j*</sub>*δ*<sub>*kj*</sub> = *a*<sub>*k*</sub>
-		<!-- .element style="list-style-type: none" --> 
$$\mu U_k \left[ a_k a_i a_i + \frac{1}{1-2\nu} a_k a_i a_i \right] = P_j a_j$$
-   <!-- .element class="fragment" -->Factoring
-		<!-- .element style="list-style-type: none", class="fragment" --> 
$$\mu U_k a_k a_i a_i \left[ 1 + \frac{1}{1-2\nu} \right] = P_j a_j$$
-   <!-- .element class="fragment" -->Simplifying
-		<!-- .element style="list-style-type: none", class="fragment" --> 
$$\mu U_k a_k a_i a_i \left[ \frac{2(1-\nu)}{1-2\nu} \right] = P_j a_j$$

----
## example

-   Solve for *U*<sub>*k*</sub>*a*<sub>*k*</sub>
-		<!-- .element style="list-style-type: none" --> 
$$U_k a_k = \frac{P_j a_j(1-2\nu)}{2\mu a_i a_i (1-\nu) }$$
-   <!-- .element class="fragment" -->This is a scalar equation, we need to find 
_U_<sub>*j*</sub>, but we substitute this back into the original equation.
-   <!-- .element class="fragment" -->First, expand the original equation
-		<!-- .element style="list-style-type: none", class="fragment" --> 
$$\mu U_k \delta_{kj} a_i a_i + \mu U_k \frac{1}{1-2\nu} a_k a_j = P_j$$

----
## example

-   After substitution, we find
-		<!-- .element style="list-style-type: none" -->
$$\mu U_j a_i a_i + \mu \frac{1}{1-2\nu} \frac{P_j a_j(1-2\nu)}{2\mu a_i a_i (1-\nu) } a_j = P_j$$
-   <!-- .element class="fragment" -->
The index *j* is repeated too many times, so we need to change *P*<sub>*j*</sub>*a*<sub>*j*</sub> to a different index
-		<!-- .element style="list-style-type: none", class="fragment" --> 
$$\mu U_j a_i a_i + \frac{P_k a_k}{2 a_i a_i (1-\nu) } a_j = P_j$$
-   <!-- .element class="fragment" -->
We can now solve for *U*<sub>*j*</sub>
-		<!-- .element style="list-style-type: none", class="fragment" --> 
$$U_j  = \frac{1}{\mu a_i a_i} \left[P_j - \frac{P_k a_k}{2 a_i a_i (1-\nu) } a_j\right]$$


---
# group problems

----
## group 1 

Identify the dummy and free indexes in each of the following expressions. Indicate the tensor order of the expression. If index notation is used incorrectly, identify why it is used incorrectly and propose a correction.

1.  *a*<sub>*i*</sub>*b*<sub>*j*</sub>*c*<sub>*k*</sub> + *d*<sub>*ijk*</sub>
2.  *a*<sub>*ii*</sub>*b*<sub>*k*</sub> + *c*<sub>*kk*</sub>*d*<sub>*j*</sub>
3.  *C*<sub>*ijkl*</sub>*ϵ*<sub>*kl*</sub>

----
## group 2 

Is it possible to factor *n*<sub>*i*</sub> from the following equation? If so, factor it.

*T*<sub>*ij*</sub>*n*<sub>*j*</sub> − *λn*<sub>*i*</sub> = 0

----
## group 3 

Find the symmetric, *S*<sub>*ij*</sub>, and anti-symmetric, *A*<sub>*ij*</sub>, portions of *T*<sub>*ij*</sub>. 
Verify that *S*<sub>*ij*</sub> + *A*<sub>*ij*</sub> = *T*<sub>*ij*</sub>

$$T_{ij} = \begin{bmatrix}
      1 & 0 & 3\\
      0 & 1 & 2\\
      3 & 0 & 3
  \end{bmatrix}$$

---
# coordinate transformation

----
## two dimensions

![2D axis to illustrate coordinate transformation](../images/transform2D.png) <!-- .element width="80%" -->

----
## dimensions

-   The vector, *v*, remains fixed, but we transform our coordinate system
-   In the new coordinate system, the *x*<sub>2</sub><sup>′</sup> portion of *v* is zero.
-   To transform the coordinate system, we first define some unit vectors.
-   $\hat{e}_1$ is a unit vector in the direction of *x*<sub>1</sub>, while $\hat{e}_1^\prime$ is a unit vector in the direction of *x*<sub>1</sub><sup>′</sup>

----
## two dimensions

![2D axis with unit vectors along the axes to illustrate coordinate transformation](../images/transform2D-unit.png) <!-- .element width="80%" --> 

----
## two dimensions

-   For this example, let us assume *v* = ⟨2, 2⟩ and *θ* = 45<sup>∘</sup>
-   We can write the transformed unit vectors, $\hat{e}_1^\prime$ and $\hat{e}_2^\prime$ in terms of $\hat{e}_1$, $\hat{e}_2$ and the angle of rotation, *θ*.

$$\begin{aligned}
\hat{e}_1^\prime &= \langle \hat{e}_1 \cos \theta , \hat{e}_2 \sin \theta\rangle\\
\hat{e}_2^\prime &= \langle -\hat{e}_1 \sin \theta , \hat{e}_2 \cos \theta \rangle\end{aligned}$$

----
## two dimensions

-   We can write the vector, *v*, in terms of the unit vectors describing our axis system
-   $v = v_1 \hat{e}_1 + v_2 \hat{e}_2$
-   (note: $\hat{e}_1=\langle 1, 0 \rangle$ and $\hat{e}_2 = \langle 0,1 \rangle$)
-   *v* = ⟨2, 2⟩=2⟨1, 0⟩+2⟨0, 1⟩

----
## two dimensions

-   When expressed in the transformed coordinate system, we refer to *v*<sup>′</sup>
-   *v*<sup>′</sup> = ⟨*v*<sub>1</sub>cos*θ* + *v*<sub>2</sub>sin*θ*, −*v*<sub>1</sub>sin*θ* + *v*<sub>2</sub>cos*θ*⟩
-   $v^\prime = \langle 2\sqrt{2}, 0 \rangle$
-   We can recover the original vector from the transformed coordinates:
-   $v = v_1^\prime \hat{e}_1^\prime + v_2^\prime \hat{e}_2^\prime$
-   (note: $\hat{e}_1^\prime=\langle \frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle$ and $\hat{e}_2^\prime = \langle -\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle$)
-   $v = 2\sqrt{2}\langle \frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle, 0 \langle -\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle = \langle 2, 2 \rangle$

----
## general 

-   Coordinate transformation can become much more complicated in three dimensions, and with higher-order tensors
-   It is convenient to define a general form of the coordinate transformation in index notation
-   We define *Q*<sub>*ij*</sub> as the cosine of the angle between the *x*<sub>*i*</sub><sup>′</sup> axis and the *x*<sub>*j*</sub> axis.
-   This is also referred to as the “direction cosine”
    *Q*<sub>*ij*</sub> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)

----
## general 

-   We can use this form on our 2D transformation example

$$\begin{aligned}
Q_{ij} &= \cos (x_i^\prime, x_j)\\ &= \begin{bmatrix}
\cos (x_1^\prime, x_1) & \cos (x_1^\prime, x_2)\\
\cos (x_2^\prime, x_1) & \cos (x_2^\prime, x_2)
\end{bmatrix}\\ &= \begin{bmatrix}
\cos \theta & \cos (90-\theta)\\
\cos (90+\theta) & \cos \theta
\end{bmatrix} \\ &= \begin{bmatrix}
\cos \theta & \sin \theta \\
-\sin \theta & \cos \theta
\end{bmatrix}\end{aligned}$$

----
## general 

-   We can transform any-order tensor using *Q*<sub>*ij*</sub>
-   Vectors (first-order tensors): *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*ij*</sub>*v*<sub>*j*</sub>
-   Matrices (second-order tensors): *σ*<sub>*mn*</sub><sup>′</sup> = *Q*<sub>*mi*</sub>*Q*<sub>*nj*</sub>*σ*<sub>*ij*</sub>
-   Fourth-order tensors: *C*<sub>*ijkl*</sub><sup>′</sup> = *Q*<sub>*im*</sub>*Q*<sub>*jn*</sub>*Q*<sub>*ko*</sub>*Q*<sub>*lp*</sub>*C*<sub>*mnop*</sub>

----
## general 

-   We can similarly use *Q*<sub>*ij*</sub> to find tensors in the original coordinate system
-   Vectors (first-order tensors): *v*<sub>*i*</sub> = *Q*<sub>*ji*</sub>*v*<sub>*j*</sub><sup>′</sup>
-   Matrices (second-order tensors): *σ*<sub>*mn*</sub> = *Q*<sub>*im*</sub>*Q*<sub>*jn*</sub>*σ*<sub>*ij*</sub><sup>′</sup>
-   Fourth-order tensors: *C*<sub>*ijkl*</sub> = *Q*<sub>*mi*</sub>*Q*<sub>*nj*</sub>*Q*<sub>*ok*</sub>*Q*<sub>*pl*</sub>*C*<sub>*mnop*</sub><sup>′</sup>

----
## mental/emotional health warning

-		Some texts flip the definition of *Q*<sub>*ij*</sub>, and then flip their transformation law accordingly
-		Any time you use tensor transformation, make sure you are following a consistent set of transformation laws

----
## general 

-   We can derive some interesting properties of the transformation tensor, *Q*<sub>*ij*</sub>
-   We know that *v*<sub>*i*</sub> = *Q*<sub>*ji*</sub>*v*<sub>*j*</sub><sup>′</sup> and that *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*ij*</sub>*v*<sub>*j*</sub>
-   If we substitute (changing the appropriate indexes) we find:
-   *v*<sub>*i*</sub> = *Q*<sub>*ji*</sub>*Q*<sub>*jk*</sub>*v*<sub>*k*</sub>
-   We can now use the Kronecker Delta to substitute *v*<sub>*i*</sub> = *δ*<sub>*ik*</sub>*v*<sub>*k*</sub> which gives
-   *δ*<sub>*ik*</sub>*v*<sub>*k*</sub> = *Q*<sub>*ji*</sub>*Q*<sub>*jk*</sub>*v*<sub>*k*</sub>

---
# examples

----
## example

<div class="left">

![empty 3D coordinate system with axes labeled for example problem](../images/example-a.png)
</div>

<div class="right">

-   Find *Q*<sub>*ij*</sub><sup>1</sup> for rotation of 60<sup>∘</sup> about *x*<sub>2</sub> 
-   Find *Q*<sub>*ij*</sub><sup>2</sup> for rotation of 30<sup>∘</sup> about *x*<sub>3</sub><sup>′</sup> 
-   Find *e*<sub>*i*</sub><sup>′′</sup> after both rotations 

</div>

----
## example

![3d coordinate system after first rotation](../images/example-b.png) <!-- .element width="50%" --> 

----
## example

![3d coordinate system after second rotation](../images/example-c.png)<!-- .element width="50%" --> 

----
## example

-   *Q*<sub>*ij*</sub><sup>1</sup> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)
-   *Q*<sub>*ij*</sub><sup>2</sup> = cos(*x*<sub>*i*</sub><sup>′′</sup>, *x*<sub>*j*</sub><sup>′</sup>)

$$Q_{ij}^1 = \begin{bmatrix}
\cos 60 & \cos 90 & \cos 150\\
\cos 90 & \cos 0 & \cos 90\\
\cos 30 & \cos 90 & \cos 60
\end{bmatrix}$$
$$Q_{ij}^2 = \begin{bmatrix}
\cos 30 & \cos 60 & \cos 90\\
\cos 120 & \cos 30 & \cos 90\\
\cos 90 & \cos 90 & \cos 0
\end{bmatrix}$$

----
## example

-   We now use *Q*<sub>*ij*</sub> to find $\hat{e}_i^\prime$ and $\hat{e}_i^{\prime \prime}$
-   First, we need to write $\hat{e}_i$ in a manner more consistent with index notation
-   We will indicate axis direction with a superscript, e.g. $\hat{e}_1 = e_i^1$
-   *e*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*ij*</sub><sup>1</sup>*e*<sub>*j*</sub>
-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*ij*</sub><sup>2</sup>*e*<sub>*j*</sub><sup>′</sup>
-   How do we find *e*<sub>*i*</sub><sup>′′</sup> in terms of *e*<sub>*i*</sub>?
-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*ij*</sub><sup>2</sup>*Q*<sub>*jk*</sub><sup>1</sup>*e*<sub>*k*</sub>


