# Numerical Recipes Project Architecture

## Overview
This project organizes the algorithms and methods from "Numerical Recipes" into a structured directory hierarchy. Each chapter and section from the book has its own folder containing relevant source code, documentation, and associated resources.

## Directory Structure

### Chapter 2: Solution of Linear Algebraic Equations
- **Start Page:** 37
- **Sections:**
  - 2.1 Gauss-Jordan Elimination (pages 41-45)
  - 2.2 Gaussian Elimination with Backsubstitution (pages 46-47)
  - 2.3 LU Decomposition and Its Applications (pages 48-55)
  - 2.4 Tridiagonal and Band-Diagonal Systems of Equations (pages 56-60)
  - 2.5 Iterative Improvement of a Solution to Linear Equations (pages 61-64)
  - 2.6 Singular Value Decomposition (pages 65-74)
  - 2.7 Sparse Linear Systems (pages 75-92)
  - 2.8 Vandermonde Matrices and Toeplitz Matrices (pages 93-99)
  - 2.9 Cholesky Decomposition (pages 100-101)
  - 2.10 QR Decomposition (pages 102-105)
  - 2.11 Is Matrix Inversion an N³ Process? (pages 106-108)

### Chapter 3: Interpolation and Extrapolation
- **Start Page:** 110
- **Sections:**
  - 3.1 Preliminaries: Searching a Ordered Table (pages 114-117)
  - 3.2 Polynomial Interpolation and Extrapolation (pages 118-119)
  - 3.3 Cubic Spline Interpolation (pages 120-123)
  - 3.4 Rational Function Interpolation and Extrapolation (pages 124-128)
  - 3.5 Coefficients of the Interpolating Polynomial (pages 129-131)
  - 3.6 Interpolation on a Grid in Multidimensions (pages 132-138)
  - 3.7 Interpolation on Scattered Data in Multidimensions (pages 139-149)
  - 3.8 Laplace Interpolation (pages 150-154)

### Chapter 4: Integration of Functions
- **Start Page:** 155
- **Sections:**
  - 4.1 Classical Formulas for Equally Spaced Abscissas (pages 156-161)
  - 4.2 Elementary Algorithms (pages 162-165)
  - 4.3 Romberg Integration (pages 166-166)
  - 4.4 Improper Integrals (pages 167-171)
  - 4.5 Quadrature by Variable Transformation (pages 172-178)
  - 4.6 Gaussian Quadratures and Orthogonal Polynomials (pages 179-193)
  - 4.7 Adaptive Quadrature (pages 194-195)
  - 4.8 Multidimensional Integrals (pages 196-200)

### Chapter 5: Evaluation of Functions
- **Start Page:** 201
- **Sections:**
  - 5.1 Polynomials and Rational Functions (pages 201-205)
  - 5.2 Evaluation of Continued Fractions (pages 206-208)
  - 5.3 Series and Their Convergence (pages 209-218)
  - 5.4 Recurrence Relations and Clenshaw's Recurrence Formula (pages 219-224)
  - 5.5 Complex Arithmetic (pages 225-226)
  - 5.6 Quadratic and Cubic Equations (pages 227-228)
  - 5.7 Numerical Derivatives (pages 229-232)
  - 5.8 Chebyshev Approximation (pages 233-239)
  - 5.9 Derivatives or Integrals of a Chebyshev-Approximated Function (pages 240-240)
  - 5.10 Polynomial Approximation from Chebyshev Coefficients (pages 241-242)
  - 5.11 Economization of Power Series (pages 243-244)
  - 5.12 Padé Approximants (pages 245-246)
  - 5.13 Rational Chebyshev Approximation (pages 247-250)
  - 5.14 Evaluation of Functions by Path Integration (pages 251-254)

### Chapter 6: Special Functions
- **Start Page:** 255
- **Sections:**
  - 6.1 Gamma Function, Beta Function, Factorials, Binomial Coefficients (pages 256-258)
  - 6.2 Incomplete Gamma Function and Error Function (pages 259-265)
  - 6.3 Exponential Integrals (pages 266-269)
  - 6.4 Incomplete Beta Function (pages 270-273)
  - 6.5 Bessel Functions of Integer Order (pages 274-282)
  - 6.6 Bessel Functions of Fractional Order, Airy Functions, Spherical Bessel Functions (pages 283-291)
  - 6.7 Spherical Harmonics (pages 292-296)
  - 6.8 Fresnel Integrals, Cosine and Sine Integrals (pages 297-301)
  - 6.9 Dawson's Integral (pages 302-303)
  - 6.10 Generalized Fermi-Dirac Integrals (pages 304-306)
  - 6.11 Inverse of the Function xlog(x) (pages 307-308)
  - 6.12 Elliptic Integrals and Jacobian Elliptic Functions (pages 309-317)
  - 6.13 Hypergeometric Functions (pages 318-319)
  - 6.14 Statistical Functions (pages 320-339)

### Chapter 7: Random Numbers
- **Start Page:** 340
- **Sections:**
  - 7.1 Uniform Deviates (pages 341-357)
  - 7.2 Completely Hashing a Large Array (pages 358-360)
  - 7.3 Deviates from Other Distributions (pages 361-377)
  - 7.4 Multivariate Normal Deviates (pages 378-379)
  - 7.5 Linear Feedback Shift Registers (pages 380-385)
  - 7.6 Hash Tables and Hash Memories (pages 386-396)
  - 7.7 Simple Monte Carlo Integration (pages 397-402)
  - 7.8 Quasi- (that is, Sub-) Random Sequences (pages 403-409)
  - 7.9 Adaptive and Recursive Monte Carlo Methods (pages 410-418)

### Chapter 8: Sorting and Selection
- **Start Page:** 419
- **Sections:**
  - 8.1 Straight Insertion and Shell's Method (pages 420-422)
  - 8.2 Quicksort (pages 423-425)
  - 8.3 Heapsort (pages 426-427)
  - 8.4 Indexing and Ranking (pages 428-430)
  - 8.5 Selecting the Mth Largest (pages 431-438)
  - 8.6 Determination of Equivalence Classes (pages 439-441)

### Chapter 9: Root Finding and Nonlinear Sets of Equations
- **Start Page:** 442
- **Sections:**
  - 9.1 Bracketing and Bisection (pages 445-448)
  - 9.2 Secant Method, False Position Method, and Ridders' Method (pages 449-453)
  - 9.3 Van Wijngaarden-Dekker-Brent Method (pages 454-455)
  - 9.4 Newton-Raphson Method Using Derivative (pages 456-462)
  - 9.5 Roots of Polynomials (pages 463-472)
  - 9.6 Newton-Raphson Method for Nonlinear Systems of Equations (pages 473-476)
  - 9.7 Globally Convergent Methods for Nonlinear Systems of Equations (pages 477-486)

### Chapter 10: Minimization or Maximization of Functions
- **Start Page:** 487
- **Sections:**
  - 10.1 Initially Bracketing a Minimum (pages 490-491)
  - 10.2 Golden Section Search in One Dimension (pages 492-495)
  - 10.3 Parabolic Interpolation and Brent's Method in One Dimension (pages 496-498)
  - 10.4 One-Dimensional Search with First Derivatives (pages 499-501)
  - 10.5 Downhill Simplex Method in Multidimensions (pages 502-506)
  - 10.6 Line Methods in Multidimensions (pages 507-508)
  - 10.7 Direction Set (Powell's) Methods in Multidimensions (pages 509-514)
  - 10.8 Conjugate Gradient Methods in Multidimensions (pages 515-520)
  - 10.9 Quasi-Newton or Variable Metric Methods in Multidimensions (pages 521-525)
  - 10.10 Linear Programming: The Simplex Method (pages 526-536)
  - 10.11 Linear Programming: Interior-Point Methods (pages 537-548)
  - 10.12 Simulated Annealing Methods (pages 549-554)
  - 10.13 Dynamic Programming (pages 555-562)

### Chapter 11: Eigensystems
- **Start Page:** 563
- **Sections:**
  - 11.1 Jacobi Transformations of a Symmetric Matrix (pages 570-575)
  - 11.2 Real Symmetric Matrices (pages 576-577)
  - 11.3 Reduction of a Symmetric Matrix to Tridiagonal Form: Givens and Householder Reductions (pages 578-582)
  - 11.4 Eigenvalues and Eigenvectors of a Tridiagonal Matrix (pages 583-589)
  - 11.5 Hermitian Matrices (pages 590-590)
  - 11.6 Real Nonsymmetric Matrices (pages 590-595)
  - 11.7 The QR Algorithm for Real Hessenberg Matrices (pages 596-596)
  - 11.8 Improving Eigenvalues and/or Finding Eigenvectors by Inverse Iteration (pages 597-600)

### Chapter 12: Fast Fourier Transform
- **Start Page:** 600
- **Sections:**
  - 12.1 Fourier Transform of Discretely Sampled Data (pages 605-607)
  - 12.2 Fast Fourier Transform (FFT) (pages 608-616)
  - 12.3 FFT of Real Functions (pages 617-619)
  - 12.4 Fast Sine and Cosine Transforms (pages 620-626)
  - 12.5 FFT in Two or More Dimensions (pages 627-630)
  - 12.6 Fourier Transforms of Real Data in Two and Three Dimensions (pages 631-636)
  - 12.7 External Storage or Memory-Local FFTs (pages 637-639)

## File Organization

Each section folder contains:

- **Python Implementation:** `.py` file with the core algorithm implementation
- **Documentation:** `.md` file with explanation of the algorithm
- **Source PDF:** Extracted pages from the original Numerical Recipes book
- **Additional Resources:** Any supplementary materials needed for implementation

## Implementation Status

- ✅ Directory structure created
- ✅ Source PDFs split and organized by section
- ✅ Architecture document created
- 🔄 Implementation of algorithms in progress

## Usage

To implement a specific algorithm:

1. Navigate to the appropriate chapter/section directory
2. Review the source PDF for the algorithm specification
3. Implement the algorithm in the provided Python file
4. Document your implementation in the markdown file
5. Add tests as needed

## References

- Press, W.H., Teukolsky, S.A., Vetterling, W.T., & Flannery, B.P. (2007). *Numerical Recipes: The Art of Scientific Computing* (3rd ed.). Cambridge University Press. ISBN 0-521-88068-8.