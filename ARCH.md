# Numerical Recipes Project Architecture

## Overview
This project organizes the algorithms and methods from "Numerical Recipes" into a structured directory hierarchy. Each chapter and section from the book has its own folder containing relevant source code, documentation, and associated resources.

## Directory Structure

### Chapter 2: Solution of Linear Algebraic Equations
- **Start Page:** 37
- **Sections:**
  - 2.1 Gauss-Jordan Elimination (pages 65-69)
  - 2.2 Gaussian Elimination with Backsubstitution (pages 70-71)
  - 2.3 LU Decomposition and Its Applications (pages 72-79)
  - 2.4 Tridiagonal and Band-Diagonal Systems of Equations (pages 80-84)
  - 2.5 Iterative Improvement of a Solution to Linear Equations (pages 85-88)
  - 2.6 Singular Value Decomposition (pages 89-98)
  - 2.7 Sparse Linear Systems (pages 99-116)
  - 2.8 Vandermonde Matrices and Toeplitz Matrices (pages 117-123)
  - 2.9 Cholesky Decomposition (pages 124-125)
  - 2.10 QR Decomposition (pages 126-129)
  - 2.11 Is Matrix Inversion an N³ Process? (pages 130-132)

### Chapter 3: Interpolation and Extrapolation
- **Start Page:** 110
- **Sections:**
  - 3.1 Preliminaries: Searching a Ordered Table (pages 138-141)
  - 3.2 Polynomial Interpolation and Extrapolation (pages 142-143)
  - 3.3 Cubic Spline Interpolation (pages 144-147)
  - 3.4 Rational Function Interpolation and Extrapolation (pages 148-152)
  - 3.5 Coefficients of the Interpolating Polynomial (pages 153-155)
  - 3.6 Interpolation on a Grid in Multidimensions (pages 156-162)
  - 3.7 Interpolation on Scattered Data in Multidimensions (pages 163-173)
  - 3.8 Laplace Interpolation (pages 174-178)

### Chapter 4: Integration of Functions
- **Start Page:** 155
- **Sections:**
  - 4.1 Classical Formulas for Equally Spaced Abscissas (pages 180-185)
  - 4.2 Elementary Algorithms (pages 186-189)
  - 4.3 Romberg Integration (pages 190-190)
  - 4.4 Improper Integrals (pages 191-195)
  - 4.5 Quadrature by Variable Transformation (pages 196-202)
  - 4.6 Gaussian Quadratures and Orthogonal Polynomials (pages 203-217)
  - 4.7 Adaptive Quadrature (pages 218-219)
  - 4.8 Multidimensional Integrals (pages 220-224)

### Chapter 5: Evaluation of Functions
- **Start Page:** 201
- **Sections:**
  - 5.1 Polynomials and Rational Functions (pages 225-229)
  - 5.2 Evaluation of Continued Fractions (pages 230-232)
  - 5.3 Series and Their Convergence (pages 233-242)
  - 5.4 Recurrence Relations and Clenshaw's Recurrence Formula (pages 243-248)
  - 5.5 Complex Arithmetic (pages 249-250)
  - 5.6 Quadratic and Cubic Equations (pages 251-252)
  - 5.7 Numerical Derivatives (pages 253-256)
  - 5.8 Chebyshev Approximation (pages 257-263)
  - 5.9 Derivatives or Integrals of a Chebyshev-Approximated Function (pages 264-264)
  - 5.10 Polynomial Approximation from Chebyshev Coefficients (pages 265-266)
  - 5.11 Economization of Power Series (pages 267-268)
  - 5.12 Padé Approximants (pages 269-270)
  - 5.13 Rational Chebyshev Approximation (pages 271-274)
  - 5.14 Evaluation of Functions by Path Integration (pages 275-278)

### Chapter 6: Special Functions
- **Start Page:** 255
- **Sections:**
  - 6.1 Gamma Function, Beta Function, Factorials, Binomial Coefficients (pages 280-282)
  - 6.2 Incomplete Gamma Function and Error Function (pages 283-289)
  - 6.3 Exponential Integrals (pages 290-293)
  - 6.4 Incomplete Beta Function (pages 294-297)
  - 6.5 Bessel Functions of Integer Order (pages 298-306)
  - 6.6 Bessel Functions of Fractional Order, Airy Functions, Spherical Bessel Functions (pages 307-315)
  - 6.7 Spherical Harmonics (pages 316-320)
  - 6.8 Fresnel Integrals, Cosine and Sine Integrals (pages 321-325)
  - 6.9 Dawson's Integral (pages 326-327)
  - 6.10 Generalized Fermi-Dirac Integrals (pages 328-330)
  - 6.11 Inverse of the Function xlog(x) (pages 331-332)
  - 6.12 Elliptic Integrals and Jacobian Elliptic Functions (pages 333-341)
  - 6.13 Hypergeometric Functions (pages 342-343)
  - 6.14 Statistical Functions (pages 344-363)

### Chapter 7: Random Numbers
- **Start Page:** 340
- **Sections:**
  - 7.1 Uniform Deviates (pages 365-381)
  - 7.2 Completely Hashing a Large Array (pages 382-384)
  - 7.3 Deviates from Other Distributions (pages 385-401)
  - 7.4 Multivariate Normal Deviates (pages 402-403)
  - 7.5 Linear Feedback Shift Registers (pages 404-409)
  - 7.6 Hash Tables and Hash Memories (pages 410-420)
  - 7.7 Simple Monte Carlo Integration (pages 421-426)
  - 7.8 Quasi- (that is, Sub-) Random Sequences (pages 427-433)
  - 7.9 Adaptive and Recursive Monte Carlo Methods (pages 434-442)

### Chapter 8: Sorting and Selection
- **Start Page:** 419
- **Sections:**
  - 8.1 Straight Insertion and Shell's Method (pages 444-446)
  - 8.2 Quicksort (pages 447-449)
  - 8.3 Heapsort (pages 450-451)
  - 8.4 Indexing and Ranking (pages 452-454)
  - 8.5 Selecting the Mth Largest (pages 455-462)
  - 8.6 Determination of Equivalence Classes (pages 463-465)

### Chapter 9: Root Finding and Nonlinear Sets of Equations
- **Start Page:** 442
- **Sections:**
  - 9.1 Bracketing and Bisection (pages 469-472)
  - 9.2 Secant Method, False Position Method, and Ridders' Method (pages 473-477)
  - 9.3 Van Wijngaarden-Dekker-Brent Method (pages 478-479)
  - 9.4 Newton-Raphson Method Using Derivative (pages 480-486)
  - 9.5 Roots of Polynomials (pages 487-496)
  - 9.6 Newton-Raphson Method for Nonlinear Systems of Equations (pages 497-500)
  - 9.7 Globally Convergent Methods for Nonlinear Systems of Equations (pages 501-510)

### Chapter 10: Minimization or Maximization of Functions
- **Start Page:** 487
- **Sections:**
  - 10.1 Initially Bracketing a Minimum (pages 514-515)
  - 10.2 Golden Section Search in One Dimension (pages 516-519)
  - 10.3 Parabolic Interpolation and Brent's Method in One Dimension (pages 520-522)
  - 10.4 One-Dimensional Search with First Derivatives (pages 523-525)
  - 10.5 Downhill Simplex Method in Multidimensions (pages 526-530)
  - 10.6 Line Methods in Multidimensions (pages 531-532)
  - 10.7 Direction Set (Powell's) Methods in Multidimensions (pages 533-538)
  - 10.8 Conjugate Gradient Methods in Multidimensions (pages 539-544)
  - 10.9 Quasi-Newton or Variable Metric Methods in Multidimensions (pages 545-549)
  - 10.10 Linear Programming: The Simplex Method (pages 550-560)
  - 10.11 Linear Programming: Interior-Point Methods (pages 561-572)
  - 10.12 Simulated Annealing Methods (pages 573-578)
  - 10.13 Dynamic Programming (pages 579-586)

### Chapter 11: Eigensystems
- **Start Page:** 563
- **Sections:**
  - 11.1 Jacobi Transformations of a Symmetric Matrix (pages 594-599)
  - 11.2 Real Symmetric Matrices (pages 600-601)
  - 11.3 Reduction of a Symmetric Matrix to Tridiagonal Form: Givens and Householder Reductions (pages 602-606)
  - 11.4 Eigenvalues and Eigenvectors of a Tridiagonal Matrix (pages 607-613)
  - 11.5 Hermitian Matrices (pages 614-614)
  - 11.6 Real Nonsymmetric Matrices (pages 614-619)
  - 11.7 The QR Algorithm for Real Hessenberg Matrices (pages 620-620)
  - 11.8 Improving Eigenvalues and/or Finding Eigenvectors by Inverse Iteration (pages 621-624)

### Chapter 12: Fast Fourier Transform
- **Start Page:** 600
- **Sections:**
  - 12.1 Fourier Transform of Discretely Sampled Data (pages 629-631)
  - 12.2 Fast Fourier Transform (FFT) (pages 632-640)
  - 12.3 FFT of Real Functions (pages 641-643)
  - 12.4 Fast Sine and Cosine Transforms (pages 644-650)
  - 12.5 FFT in Two or More Dimensions (pages 651-654)
  - 12.6 Fourier Transforms of Real Data in Two and Three Dimensions (pages 655-660)
  - 12.7 External Storage or Memory-Local FFTs (pages 661-663)

## Chapter 13: Fourier and Spectral Applications
- **Start Page:** 640
- **Sections:**
  - 13.1 Convolution and Deconvolution Using the FFT (pages 665-671)
  - 13.2 Correlation and Autocorrelation Using the FFT (pages 672-672)
  - 13.3 Optimal Wiener Filtering with the FFT (pages 673-675)
  - 13.4 Power Spectrum Estimation Using the FFT (pages 676-690)
  - 13.5 Digital Filtering in the Time Domain (pages 691-696)
  - 13.6 Linear Prediction and Linear Predictive Coding (pages 697-704)
  - 13.7 Power Spectrum Estimation by the Maximum Entropy (All-Poles) Method (pages 705-708)
  - 13.8 Spectral Analysis of Unevenly Sampled Data (pages 709-715)
  - 13.9 Computing Fourier Integrals Using the FFT (pages 716-722)
  - 13.10 Wavelet Transforms (pages 723-740)
  - 13.11 Numerical Use of the Sampling Theorem (pages 741-743)

## Chapter 14: Statistical Description of Data
- **Start Page:** 720
- **Sections:**
  - 14.1 Moments of a Distribution: Mean, Variance, Skewness, and So Forth (pages 745-749)
  - 14.2 Do Two Distributions Have the Same Means or Variances? (pages 750-753)
  - 14.3 Are Two Distributions Different? (pages 754-764)
  - 14.4 Contingency Table Analysis of Two Distributions (pages 765-768)
  - 14.5 Linear Correlation (pages 769-771)
  - 14.6 Nonparametric or Rank Correlation (pages 772-777)
  - 14.7 Information-Theoretic Properties of Distributions (pages 778-785)
  - 14.8 Do Two-Dimensional Distributions Differ? (pages 786-789)
  - 14.9 Savitzky-Golay Smoothing Filters (pages 790-796)

## Chapter 15: Modeling of Data
- **Start Page:** 773
- **Sections:**
  - 15.1 Least Squares as a Maximum Likelihood Estimator (pages 800-803)
  - 15.2 Fitting Data to a Straight Line (pages 804-808)
  - 15.3 Straight-Line Data with Errors in Both Coordinates (pages 809-811)
  - 15.4 General Linear Least Squares (pages 812-822)
  - 15.5 Nonlinear Models (pages 823-830)
  - 15.6 Confidence Limits on Estimated Model Parameters (pages 831-841)
  - 15.7 Robust Estimation (pages 842-847)
  - 15.8 Markov Chain Monte Carlo (pages 848-859)
  - 15.9 Gaussian Process Regression (pages 860-863)

## Chapter 16: Classification and Inference
- **Start Page:** 840
- **Sections:**
  - 16.1 Gaussian Mixture Models and k-Means Clustering (pages 866-873)
  - 16.2 Viterbi Decoding (pages 874-879)
  - 16.3 Markov Models and Hidden Markov Modeling (pages 880-891)
  - 16.4 Hierarchical Clustering by Phylogenetic Trees (pages 892-906)
  - 16.5 Support Vector Machines (pages 907-922)

## Chapter 17: Integration of Ordinary Differential Equations
- **Start Page:** 899
- **Sections:**
  - 17.1 Runge-Kutta Method (pages 931-933)
  - 17.2 Adaptive Stepsize Control for Runge-Kutta (pages 934-944)
  - 17.3 Richardson Extrapolation and the Bulirsch-Stoer Method (pages 945-951)
  - 17.4 Second-Order Conservative Equations (pages 952-954)
  - 17.5 Stiff Sets of Equations (pages 955-965)
  - 17.6 Multistep, Multivalue, and Predictor-Corrector Methods (pages 966-969)
  - 17.7 Stochastic Simulation of Chemical Reaction Networks (pages 970-978)

## Chapter 18: Two-Point Boundary Value Problems
- **Start Page:** 955
- **Sections:**
  - 18.1 The Shooting Method (pages 983-985)
  - 18.2 Shooting to a Fitting Point (pages 986-987)
  - 18.3 Relaxation Methods (pages 988-994)
  - 18.4 A Worked Example: Spheroidal Harmonics (pages 995-1004)
  - 18.5 Automated Allocation of Mesh Points (pages 1005-1006)
  - 18.6 Handling Internal Boundary Conditions or Singular Points (pages 1007-1018)

## Chapter 19: Integral Equations and Inverse Theory
- **Start Page:** 986
- **Sections:**
  - 19.1 Fredholm Equations of the Second Kind (pages 1013-1015)
  - 19.2 Volterra Equations (pages 1016-1018)
  - 19.3 Integral Equations with Singular Kernels (pages 1019-1024)
  - 19.4 Inverse Problems and the Use of A Priori Information (pages 1025-1029)
  - 19.5 Linear Regularization Methods (pages 1030-1037)
  - 19.6 Backus-Gilbert Method (pages 1038-1039)
  - 19.7 Maximum Entropy Image Restoration (pages 1040-1047)

## Chapter 20: Partial Differential Equations
- **Start Page:** 1024
- **Sections:**
  - 20.1 Flux-Conservative Initial Value Problems (pages 1055-1066)
  - 20.2 Diffusive Initial Value Problems (pages 1067-1072)
  - 20.3 Initial Value Problems in Multidimensions (pages 1073-1076)
  - 20.4 Fourier and Cyclic Reduction Methods for Boundary Value Problems (pages 1077-1082)
  - 20.5 Relaxation Methods for Boundary Value Problems (pages 1083-1089)
  - 20.6 Multigrid Methods for Boundary Value Problems (pages 1090-1106)
  - 20.7 Spectral Methods (pages 1107-1120)

## Chapter 21: Computational Geometry
- **Start Page:** 1097
- **Sections:**
  - 21.1 Points and Boxes (pages 1123-1124)
  - 21.2 KD Trees and Nearest-Neighbor Finding (pages 1125-1134)
  - 21.3 Triangles in Two and Three Dimensions (pages 1135-1140)
  - 21.4 Lines, Line Segments, and Polygons (pages 1141-1151)
  - 21.5 Spheres and Rotations (pages 1152-1154)
  - 21.6 Triangulation and Delaunay Triangulation (pages 1155-1164)
  - 21.7 Applications of Delaunay Triangulation (pages 1165-1172)
  - 21.8 Quadtrees and Octrees: Storing Geometrical Objects (pages 1173-1183)

## Chapter 22: Less-Numerical Algorithms
- **Start Page:** 1160
- **Sections:**
  - 22.1 Plotting Simple Graphs (pages 1184-1186)
  - 22.2 Diagnosing Machine Parameters (pages 1187-1189)
  - 22.3 Gray Codes (pages 1190-1191)
  - 22.4 Cyclic Redundancy and Other Checksums (pages 1192-1198)
  - 22.5 Huffman Coding and Compression of Data (pages 1199-1204)
  - 22.6 Arithmetic Coding (pages 1205-1208)
  - 22.7 Arithmetic at Arbitrary Precision (pages 1209-1218)

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