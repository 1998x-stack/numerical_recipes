#!/usr/bin/env python3

import os
from PyPDF2 import PdfReader, PdfWriter
import re


def sanitize_filename(filename):
    """Convert section title to a valid filename"""
    sanitized = re.sub(r'[^\w\s-]', '_', filename)
    sanitized = re.sub(r'[-\s]+', '_', sanitized)
    return sanitized.strip('_')


def split_pdf_by_sections():
    """Split the numerical recipes PDF into individual sections based on page numbers"""
    
    # Define the sections with their starting pages (with offset of 24 applied)
    sections = {
        # Chapter 2: Solution of Linear Algebraic Equations
        '2.1 Gauss-Jordan Elimination': {'start': 41+24, 'end': 45+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Gauss_Jordan_Elimination'},
        '2.2 Gaussian Elimination with Backsubstitution': {'start': 46+24, 'end': 47+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Gaussian_Elimination_with_Backsubstitution'},
        '2.3 LU Decomposition and Its Applications': {'start': 48+24, 'end': 55+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/LU_Decomposition_and_Its_Applications'},
        '2.4 Tridiagonal and Band-Diagonal Systems of Equations': {'start': 56+24, 'end': 60+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Tridiagonal_and_Band_Diagonal_Systems_of_Equations'},
        '2.5 Iterative Improvement of a Solution to Linear Equations': {'start': 61+24, 'end': 64+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Iterative_Improvement_of_a_Solution_to_Linear_Equations'},
        '2.6 Singular Value Decomposition': {'start': 65+24, 'end': 74+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Singular_Value_Decomposition'},
        '2.7 Sparse Linear Systems': {'start': 75+24, 'end': 92+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Sparse_Linear_Systems'},
        '2.8 Vandermonde Matrices and Toeplitz Matrices': {'start': 93+24, 'end': 99+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Vandermonde_Matrices_and_Toeplitz_Matrices'},
        '2.9 Cholesky Decomposition': {'start': 100+24, 'end': 101+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Cholesky_Decomposition'},
        '2.10 QR Decomposition': {'start': 102+24, 'end': 105+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/QR_Decomposition'},
        '2.11 Is Matrix Inversion an N3 Process': {'start': 106+24, 'end': 108+24, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Is_Matrix_Inversion_an_N3_Process'},
        
        # Chapter 3: Interpolation and Extrapolation
        '3.1 Preliminaries Searching a Ordered Table': {'start': 114+24, 'end': 117+24, 'folder': '3_Interpolation_and_Extrapolation/Preliminaries_Searching_a_Ordered_Table'},
        '3.2 Polynomial Interpolation and Extrapolation': {'start': 118+24, 'end': 119+24, 'folder': '3_Interpolation_and_Extrapolation/Polynomial_Interpolation_and_Extrapolation'},
        '3.3 Cubic Spline Interpolation': {'start': 120+24, 'end': 123+24, 'folder': '3_Interpolation_and_Extrapolation/Cubic_Spline_Interpolation'},
        '3.4 Rational Function Interpolation and Extrapolation': {'start': 124+24, 'end': 128+24, 'folder': '3_Interpolation_and_Extrapolation/Rational_Function_Interpolation_and_Extrapolation'},
        '3.5 Coefficients of the Interpolating Polynomial': {'start': 129+24, 'end': 131+24, 'folder': '3_Interpolation_and_Extrapolation/Coefficients_of_the_Interpolating_Polynomial'},
        '3.6 Interpolation on a Grid in Multidimensions': {'start': 132+24, 'end': 138+24, 'folder': '3_Interpolation_and_Extrapolation/Interpolation_on_a_Grid_in_Multidimensions'},
        '3.7 Interpolation on Scattered Data in Multidimensions': {'start': 139+24, 'end': 149+24, 'folder': '3_Interpolation_and_Extrapolation/Interpolation_on_Scattered_Data_in_Multidimensions'},
        '3.8 Laplace Interpolation': {'start': 150+24, 'end': 154+24, 'folder': '3_Interpolation_and_Extrapolation/Laplace_Interpolation'},
        
        # Chapter 4: Integration of Functions
        '4.1 Classical Formulas for Equally Spaced Abscissas': {'start': 156+24, 'end': 161+24, 'folder': '4_Integration_of_Functions/Classical_Formulas_for_Equally_Spaced_Abscissas'},
        '4.2 Elementary Algorithms': {'start': 162+24, 'end': 165+24, 'folder': '4_Integration_of_Functions/Elementary_Algorithms'},
        '4.3 Romberg Integration': {'start': 166+24, 'end': 166+24, 'folder': '4_Integration_of_Functions/Romberg_Integration'},
        '4.4 Improper Integrals': {'start': 167+24, 'end': 171+24, 'folder': '4_Integration_of_Functions/Improper_Integrals'},
        '4.5 Quadrature by Variable Transformation': {'start': 172+24, 'end': 178+24, 'folder': '4_Integration_of_Functions/Quadrature_by_Variable_Transformation'},
        '4.6 Gaussian Quadratures and Orthogonal Polynomials': {'start': 179+24, 'end': 193+24, 'folder': '4_Integration_of_Functions/Gaussian_Quadratures_and_Orthogonal_Polynomials'},
        '4.7 Adaptive Quadrature': {'start': 194+24, 'end': 195+24, 'folder': '4_Integration_of_Functions/Adaptive_Quadrature'},
        '4.8 Multidimensional Integrals': {'start': 196+24, 'end': 200+24, 'folder': '4_Integration_of_Functions/Multidimensional_Integrals'},
        
        # Chapter 5: Evaluation of Functions
        '5.1 Polynomials and Rational Functions': {'start': 201+24, 'end': 205+24, 'folder': '5_Evaluation_of_Functions/Polynomials_and_Rational_Functions'},
        '5.2 Evaluation of Continued Fractions': {'start': 206+24, 'end': 208+24, 'folder': '5_Evaluation_of_Functions/Evaluation_of_Continued_Fractions'},
        '5.3 Series and Their Convergence': {'start': 209+24, 'end': 218+24, 'folder': '5_Evaluation_of_Functions/Series_and_Their_Convergence'},
        '5.4 Recurrence Relations and Clenshaw\'s Recurrence Formula': {'start': 219+24, 'end': 224+24, 'folder': '5_Evaluation_of_Functions/Recurrence_Relations_and_Clushaws_Recurcence_Formula'},
        '5.5 Complex Arithmetic': {'start': 225+24, 'end': 226+24, 'folder': '5_Evaluation_of_Functions/Complex_Arithmetic'},
        '5.6 Quadratic and Cubic Equations': {'start': 227+24, 'end': 228+24, 'folder': '5_Evaluation_of_Functions/Quadratic_and_Cubic_Equations'},
        '5.7 Numerical Derivatives': {'start': 229+24, 'end': 232+24, 'folder': '5_Evaluation_of_Functions/Numerical_Derivatives'},
        '5.8 Chebyshev Approximation': {'start': 233+24, 'end': 239+24, 'folder': '5_Evaluation_of_Functions/Chebyshev_Approximation'},
        '5.9 Derivatives or Integrals of a Chebyshev-Approximated Function': {'start': 240+24, 'end': 240+24, 'folder': '5_Evaluation_of_Functions/Derivatives_or_Integrals_of_a_Chebyshev_Approximated_Function'},
        '5.10 Polynomial Approximation from Chebyshev Coefficients': {'start': 241+24, 'end': 242+24, 'folder': '5_Evaluation_of_Functions/Polynomial_Approximation_from_Chebyshev_Coefficients'},
        '5.11 Economization of Power Series': {'start': 243+24, 'end': 244+24, 'folder': '5_Evaluation_of_Functions/Economization_of_Power_Series'},
        '5.12 Padé Approximants': {'start': 245+24, 'end': 246+24, 'folder': '5_Evaluation_of_Functions/Pade_Approximants'},
        '5.13 Rational Chebyshev Approximation': {'start': 247+24, 'end': 250+24, 'folder': '5_Evaluation_of_Functions/Rational_Chebyshev_Approximation'},
        '5.14 Evaluation of Functions by Path Integration': {'start': 251+24, 'end': 254+24, 'folder': '5_Evaluation_of_Functions/Evaluation_of_Functions_by_Path_Integration'},
        
        # Chapter 6: Special Functions
        '6.1 Gamma Function Beta Function Factorials Binomial Coefficients': {'start': 256+24, 'end': 258+24, 'folder': '6_Special_Functions/Gamma_Function_Beta_Function_Factorials_Binomial_Coefficients'},
        '6.2 Incomplete Gamma Function and Error Function': {'start': 259+24, 'end': 265+24, 'folder': '6_Special_Functions/Incomplete_Gamma_Function_and_Error_Function'},
        '6.3 Exponential Integrals': {'start': 266+24, 'end': 269+24, 'folder': '6_Special_Functions/Exponential_Integrals'},
        '6.4 Incomplete Beta Function': {'start': 270+24, 'end': 273+24, 'folder': '6_Special_Functions/Incomplete_Beta_Function'},
        '6.5 Bessel Functions of Integer Order': {'start': 274+24, 'end': 282+24, 'folder': '6_Special_Functions/Bessel_Functions_of_Integer_Order'},
        '6.6 Bessel Functions of Fractional Order Airy Functions Spherical Bessel Functions': {'start': 283+24, 'end': 291+24, 'folder': '6_Special_Functions/Bessel_Functions_of_Fractional_Order_Airy_Functions_Spherical_Bessel_Functions'},
        '6.7 Spherical Harmonics': {'start': 292+24, 'end': 296+24, 'folder': '6_Special_Functions/Spherical_Harmonics'},
        '6.8 Fresnel Integrals Cosine and Sine Integrals': {'start': 297+24, 'end': 301+24, 'folder': '6_Special_Functions/Fresnel_Integrals_Cosine_and_Sine_Integrals'},
        '6.9 Dawson\'s Integral': {'start': 302+24, 'end': 303+24, 'folder': '6_Special_Functions/Dawsons_Integral'},
        '6.10 Generalized Fermi-Dirac Integrals': {'start': 304+24, 'end': 306+24, 'folder': '6_Special_Functions/Generalized_Fermi_Dirac_Integrals'},
        '6.11 Inverse of the Function xlogx': {'start': 307+24, 'end': 308+24, 'folder': '6_Special_Functions/Inverse_of_the_Function_xlogx'},
        '6.12 Elliptic Integrals and Jacobian Elliptic Functions': {'start': 309+24, 'end': 317+24, 'folder': '6_Special_Functions/Elliptic_Integrals_and_Jacobian_Elliptic_Functions'},
        '6.13 Hypergeometric Functions': {'start': 318+24, 'end': 319+24, 'folder': '6_Special_Functions/Hypergeometric_Functions'},
        '6.14 Statistical Functions': {'start': 320+24, 'end': 339+24, 'folder': '6_Special_Functions/Statistical_Functions'},
        
        # Chapter 7: Random Numbers
        '7.1 Uniform Deviates': {'start': 341+24, 'end': 357+24, 'folder': '7_Random_Numbers/Uniform_Deviates'},
        '7.2 Completely Hashing a Large Array': {'start': 358+24, 'end': 360+24, 'folder': '7_Random_Numbers/Completely_Hashing_a_Large_Array'},
        '7.3 Deviates from Other Distributions': {'start': 361+24, 'end': 377+24, 'folder': '7_Random_Numbers/Deviates_from_Other_Distributions'},
        '7.4 Multivariate Normal Deviates': {'start': 378+24, 'end': 379+24, 'folder': '7_Random_Numbers/Multivariate_Normal_Deviates'},
        '7.5 Linear Feedback Shift Registers': {'start': 380+24, 'end': 385+24, 'folder': '7_Random_Numbers/Linear_Feedback_Shift_Registers'},
        '7.6 Hash Tables and Hash Memories': {'start': 386+24, 'end': 396+24, 'folder': '7_Random_Numbers/Hash_Tables_and_Hash_Memories'},
        '7.7 Simple Monte Carlo Integration': {'start': 397+24, 'end': 402+24, 'folder': '7_Random_Numbers/Simple_Monte_Carlo_Integration'},
        '7.8 Quasi Random Sequences': {'start': 403+24, 'end': 409+24, 'folder': '7_Random_Numbers/Quasi_Random_Sequences'},
        '7.9 Adaptive and Recursive Monte Carlo Methods': {'start': 410+24, 'end': 418+24, 'folder': '7_Random_Numbers/Adaptive_and_Recursive_Monte_Carlo_Methods'},
        
        # Chapter 8: Sorting and Selection
        '8.1 Straight Insertion and Shells Method': {'start': 420+24, 'end': 422+24, 'folder': '8_Sorting_and_Selection/Straight_Insertion_and_Shells_Method'},
        '8.2 Quicksort': {'start': 423+24, 'end': 425+24, 'folder': '8_Sorting_and_Selection/Quicksort'},
        '8.3 Heapsort': {'start': 426+24, 'end': 427+24, 'folder': '8_Sorting_and_Selection/Heapsort'},
        '8.4 Indexing and Ranking': {'start': 428+24, 'end': 430+24, 'folder': '8_Sorting_and_Selection/Indexing_and_Ranking'},
        '8.5 Selecting the Mth Largest': {'start': 431+24, 'end': 438+24, 'folder': '8_Sorting_and_Selection/Selecting_the_Mth_Largest'},
        '8.6 Determination of Equivalence Classes': {'start': 439+24, 'end': 441+24, 'folder': '8_Sorting_and_Selection/Determination_of_Equivalence_Classes'},
        
        # Chapter 9: Root Finding and Nonlinear Sets of Equations
        '9.1 Bracketing and Bisection': {'start': 445+24, 'end': 448+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Bracketing_and_Bisection'},
        '9.2 Secant Method False Position Method and Ridders Method': {'start': 449+24, 'end': 453+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Secant_Method_False_Position_Method_and_Ridders_Method'},
        '9.3 Van Wijngaarden Dekker Brent Method': {'start': 454+24, 'end': 455+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Van_Wijngaarden_Dekker_Brent_Method'},
        '9.4 Newton Raphson Method Using Derivative': {'start': 456+24, 'end': 462+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Newton_Raphson_Method_Using_Derivative'},
        '9.5 Roots of Polynomials': {'start': 463+24, 'end': 472+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Roots_of_Polynomials'},
        '9.6 Newton Raphson Method for Nonlinear Systems of Equations': {'start': 473+24, 'end': 476+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Newton_Raphson_Method_for_Nonlinear_Systems_of_Equations'},
        '9.7 Globally Convergent Methods for Nonlinear Systems of Equations': {'start': 477+24, 'end': 486+24, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Globally_Convergent_Methods_for_Nonlinear_Systems_of_Equations'},
        
        # Chapter 10: Minimization or Maximization of Functions
        '10.1 Initially Bracketing a Minimum': {'start': 490+24, 'end': 491+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Initially_Bracketing_a_Minimum'},
        '10.2 Golden Section Search in One Dimension': {'start': 492+24, 'end': 495+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Golden_Section_Search_in_One_Dimension'},
        '10.3 Parabolic Interpolation and Brents Method in One Dimension': {'start': 496+24, 'end': 498+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Parabolic_Interpolation_and_Brents_Method_in_One_Dimension'},
        '10.4 One Dimensional Search with First Derivatives': {'start': 499+24, 'end': 501+24, 'folder': '10_Minimization_or_Maximization_of_Functions/One_Dimensional_Search_with_First_Derivatives'},
        '10.5 Downhill Simplex Method in Multidimensions': {'start': 502+24, 'end': 506+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Downhill_Simplex_Method_in_Multidimensions'},
        '10.6 Line Methods in Multidimensions': {'start': 507+24, 'end': 508+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Line_Methods_in_Multidimensions'},
        '10.7 Direction Set Powells Methods in Multidimensions': {'start': 509+24, 'end': 514+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Direction_Set_Powells_Methods_in_Multidimensions'},
        '10.8 Conjugate Gradient Methods in Multidimensions': {'start': 515+24, 'end': 520+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Conjugate_Gradient_Methods_in_Multidimensions'},
        '10.9 Quasi Newton or Variable Metric Methods in Multidimensions': {'start': 521+24, 'end': 525+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Quasi_Newton_or_Variable_Metric_Methods_in_Multidimensions'},
        '10.10 Linear Programming The Simplex Method': {'start': 526+24, 'end': 536+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Linear_Programming_The_Simplex_Method'},
        '10.11 Linear Programming Interior Point Methods': {'start': 537+24, 'end': 548+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Linear_Programming_Interior_Point_Methods'},
        '10.12 Simulated Annealing Methods': {'start': 549+24, 'end': 554+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Simulated_Annealing_Methods'},
        '10.13 Dynamic Programming': {'start': 555+24, 'end': 562+24, 'folder': '10_Minimization_or_Maximization_of_Functions/Dynamic_Programming'},
        
        # Chapter 11: Eigensystems
        '11.1 Jacobi Transformations of a Symmetric Matrix': {'start': 570+24, 'end': 575+24, 'folder': '11_Eigensystems/Jacobi_Transformations_of_a_Symmetric_Matrix'},
        '11.2 Real Symmetric Matrices': {'start': 576+24, 'end': 577+24, 'folder': '11_Eigensystems/Real_Symmetric_Matrices'},
        '11.3 Reduction of a Symmetric Matrix to Tridiagonal Form Givens and Householder Reductions': {'start': 578+24, 'end': 582+24, 'folder': '11_Eigensystems/Reduction_of_a_Symmetric_Matrix_to_Tridiagonal_Form_Givens_and_Householder_Reductions'},
        '11.4 Eigenvalues and Eigenvectors of a Tridiagonal Matrix': {'start': 583+24, 'end': 589+24, 'folder': '11_Eigensystems/Eigenvalues_and_Eigenvectors_of_a_Tridiagonal_Matrix'},
        '11.5 Hermitian Matrices': {'start': 590+24, 'end': 590+24, 'folder': '11_Eigensystems/Hermitian_Matrices'},
        '11.6 Real Nonsymmetric Matrices': {'start': 590+24, 'end': 595+24, 'folder': '11_Eigensystems/Real_Nonsymmetric_Matrices'},
        '11.7 The QR Algorithm for Real Hessenberg Matrices': {'start': 596+24, 'end': 596+24, 'folder': '11_Eigensystems/The_QR_Algorithm_for_Real_Hessenberg_Matrices'},
        '11.8 Improving Eigenvalues and or Finding Eigenvectors by Inverse Iteration': {'start': 597+24, 'end': 600+24, 'folder': '11_Eigensystems/Improving_Eigenvalues_and_or_Finding_Eigenvectors_by_Inverse_Iteration'},
        
        # Chapter 12: Fast Fourier Transform
        '12.1 Fourier Transform of Discretely Sampled Data': {'start': 605+24, 'end': 607+24, 'folder': '12_Fast_Fourier_Transform/Fourier_Transform_of_Discretely_Sampled_Data'},
        '12.2 Fast Fourier Transform FFT': {'start': 608+24, 'end': 616+24, 'folder': '12_Fast_Fourier_Transform/Fast_Fourier_Transform_FFT'},
        '12.3 FFT of Real Functions': {'start': 617+24, 'end': 619+24, 'folder': '12_Fast_Fourier_Transform/FFT_of_Real_Functions'},
        '12.4 Fast Sine and Cosine Transforms': {'start': 620+24, 'end': 626+24, 'folder': '12_Fast_Fourier_Transform/Fast_Sine_and_Cosine_Transforms'},
        '12.5 FFT in Two or More Dimensions': {'start': 627+24, 'end': 630+24, 'folder': '12_Fast_Fourier_Transform/FFT_in_Two_or_More_Dimensions'},
        '12.6 Fourier Transforms of Real Data in Two and Three Dimensions': {'start': 631+24, 'end': 636+24, 'folder': '12_Fast_Fourier_Transform/Fourier_Transforms_of_Real_Data_in_Two_and_Three_Dimensions'},
        '12.7 External Storage or Memory Local FFTs': {'start': 637+24, 'end': 639+24, 'folder': '12_Fast_Fourier_Transform/External_Storage_or_Memory_Local_FFTs'},
        
        # Chapter 13: Fourier and Spectral Applications
        '13.1 Convolution and Deconvolution Using the FFT': {'start': 641+24, 'end': 647+24, 'folder': '13_Fourier_and_Spectral_Applications/Convolution_and_Deconvolution_Using_the_FFT'},
        '13.2 Correlation and Autocorrelation Using the FFT': {'start': 648+24, 'end': 648+24, 'folder': '13_Fourier_and_Spectral_Applications/Correlation_and_Autocorrelation_Using_the_FFT'},
        '13.3 Optimal Wiener Filtering with the FFT': {'start': 649+24, 'end': 651+24, 'folder': '13_Fourier_and_Spectral_Applications/Optimal_Wiener_Filtering_with_the_FFT'},
        '13.4 Power Spectrum Estimation Using the FFT': {'start': 652+24, 'end': 666+24, 'folder': '13_Fourier_and_Spectral_Applications/Power_Spectrum_Estimation_using_the_FFT'},
        '13.5 Digital Filtering in the Time Domain': {'start': 667+24, 'end': 672+24, 'folder': '13_Fourier_and_Spectral_Applications/Digital_Filtering_in_the_Time_Domain'},
        '13.6 Linear Prediction and Linear Predictive Coding': {'start': 673+24, 'end': 680+24, 'folder': '13_Fourier_and_Spectral_Applications/Linear_Prediction_and_Linear_Predictive_Coding'},
        '13.7 Power Spectrum Estimation by the Maximum Entropy (All-Poles) Method': {'start': 681+24, 'end': 684+24, 'folder': '13_Fourier_and_Spectral_Applications/Power_Spectrum_Estimation_by_the_Maximum_Entropy_All_Poles_Method'},
        '13.8 Spectral Analysis of Unevenly Sampled Data': {'start': 685+24, 'end': 691+24, 'folder': '13_Fourier_and_Spectral_Applications/Spectral_Analysis_of_Unevenly_Sampled_Data'},
        '13.9 Computing Fourier Integrals Using the FFT': {'start': 692+24, 'end': 698+24, 'folder': '13_Fourier_and_Spectral_Applications/Computing_Fourier_Integrals_Using_the_FFT'},
        '13.10 Wavelet Transforms': {'start': 699+24, 'end': 716+24, 'folder': '13_Fourier_and_Spectral_Applications/Wavelet_Transforms'},
        '13.11 Numerical Use of the Sampling Theorem': {'start': 717+24, 'end': 719+24, 'folder': '13_Fourier_and_Spectral_Applications/Numerical_Use_of_the_Sampling_Theorem'},
        
        # Chapter 14: Statistical Description of Data
        '14.1 Moments of a Distribution: Mean, Variance, Skewness, and So Forth': {'start': 721+24, 'end': 725+24, 'folder': '14_Statistical_Description_of_Data/Moments_of_a_Distribution_Mean_Variance_Skewness_and_So_Forth'},
        '14.2 Do Two Distributions Have the Same Means or Variances?': {'start': 726+24, 'end': 729+24, 'folder': '14_Statistical_Description_of_Data/Do_Two_Distributions_Have_the_Same_Means_or_Variances'},
        '14.3 Are Two Distributions Different?': {'start': 730+24, 'end': 740+24, 'folder': '14_Statistical_Description_of_Data/Are_Two_Distributions_Different'},
        '14.4 Contingency Table Analysis of Two Distributions': {'start': 741+24, 'end': 744+24, 'folder': '14_Statistical_Description_of_Data/Contingency_Table_Analysis_of_Two_Distributions'},
        '14.5 Linear Correlation': {'start': 745+24, 'end': 747+24, 'folder': '14_Statistical_Description_of_Data/Linear_Correlation'},
        '14.6 Nonparametric or Rank Correlation': {'start': 748+24, 'end': 753+24, 'folder': '14_Statistical_Description_of_Data/Nonparametric_or_Rank_Correlation'},
        '14.7 Information-Theoretic Properties of Distributions': {'start': 754+24, 'end': 761+24, 'folder': '14_Statistical_Description_of_Data/Information_Theoretic_Properties_of_Distributions'},
        '14.8 Do Two-Dimensional Distributions Differ?': {'start': 762+24, 'end': 765+24, 'folder': '14_Statistical_Description_of_Data/Do_Two_Dimensional_Distributions_Differ'},
        '14.9 Savitzky-Golay Smoothing Filters': {'start': 766+24, 'end': 772+24, 'folder': '14_Statistical_Description_of_Data/Savitzky_Golay_Smoothing_Filters'},
        
        # Chapter 15: Modeling of Data
        '15.1 Least Squares as a Maximum Likelihood Estimator': {'start': 776+24, 'end': 779+24, 'folder': '15_Modeling_of_Data/Least_Squares_as_a_Maximum_Likelihood_Estimator'},
        '15.2 Fitting Data to a Straight Line': {'start': 780+24, 'end': 784+24, 'folder': '15_Modeling_of_Data/Fitting_Data_to_a_Straight_Line'},
        '15.3 Straight-Line Data with Errors in Both Coordinates': {'start': 785+24, 'end': 787+24, 'folder': '15_Modeling_of_Data/Straight_Line_Data_with_Errors_in_Both_Coordinates'},
        '15.4 General Linear Least Squares': {'start': 788+24, 'end': 798+24, 'folder': '15_Modeling_of_Data/General_Linear_Least_Squares'},
        '15.5 Nonlinear Models': {'start': 799+24, 'end': 806+24, 'folder': '15_Modeling_of_Data/Nonlinear_Models'},
        '15.6 Confidence Limits on Estimated Model Parameters': {'start': 807+24, 'end': 817+24, 'folder': '15_Modeling_of_Data/Confidence_Limits_on_Estimated_Model_Parameters'},
        '15.7 Robust Estimation': {'start': 818+24, 'end': 823+24, 'folder': '15_Modeling_of_Data/Robust_Estimation'},
        '15.8 Markov Chain Monte Carlo': {'start': 824+24, 'end': 835+24, 'folder': '15_Modeling_of_Data/Markov_Chain_Monte_Carlo'},
        '15.9 Gaussian Process Regression': {'start': 836+24, 'end': 839+24, 'folder': '15_Modeling_of_Data/Gaussian_Process_Regression'},
        
        # Chapter 16: Classification and Inference
        '16.1 Gaussian Mixture Models and k-Means Clustering': {'start': 842+24, 'end': 849+24, 'folder': '16_Classification_and_Inference/Gaussian_Mixture_Models_and_k_Means_Clustering'},
        '16.2 Viterbi Decoding': {'start': 850+24, 'end': 855+24, 'folder': '16_Classification_and_Inference/Viterbi_Decoding'},
        '16.3 Markov Models and Hidden Markov Modeling': {'start': 856+24, 'end': 867+24, 'folder': '16_Classification_and_Inference/Markov_Models_and_Hidden_Markov_Modeling'},
        '16.4 Hierarchical Clustering by Phylogenetic Trees': {'start': 868+24, 'end': 882+24, 'folder': '16_Classification_and_Inference/Hierarchical_Clustering_by_Phylogenetic_Trees'},
        '16.5 Support Vector Machines': {'start': 883+24, 'end': 898+24, 'folder': '16_Classification_and_Inference/Support_Vector_Machines'},
        
        # Chapter 17: Integration of Ordinary Differential Equations
        '17.1 Runge-Kutta Method': {'start': 907+24, 'end': 909+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Runge_Kutta_Method'},
        '17.2 Adaptive Stepsize Control for Runge-Kutta': {'start': 910+24, 'end': 920+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Adaptive_Stepsize_Control_for_Runge_Kutta'},
        '17.3 Richardson Extrapolation and the Bulirsch-Stoer Method': {'start': 921+24, 'end': 927+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Richardson_Extrapolation_and_the_Bulirsch_Stoer_Method'},
        '17.4 Second-Order Conservative Equations': {'start': 928+24, 'end': 930+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Second_Order_Conservative_Equations'},
        '17.5 Stiff Sets of Equations': {'start': 931+24, 'end': 941+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Stiff_Sets_of_Equations'},
        '17.6 Multistep, Multivalue, and Predictor-Corrector Methods': {'start': 942+24, 'end': 945+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Multistep_Multivalue_and_Predictor_Corrector_Methods'},
        '17.7 Stochastic Simulation of Chemical Reaction Networks': {'start': 946+24, 'end': 954+24, 'folder': '17_Integration_of_Ordinary_Differential_Equations/Stochastic_Simulation_of_Chemical_Reaction_Networks'},
        
        # Chapter 18: Two-Point Boundary Value Problems
        '18.1 The Shooting Method': {'start': 959+24, 'end': 961+24, 'folder': '18_Two_Point_Boundary_Value_Problems/The_Shooting_Method'},
        '18.2 Shooting to a Fitting Point': {'start': 962+24, 'end': 963+24, 'folder': '18_Two_Point_Boundary_Value_Problems/Shooting_to_a_Fitting_Point'},
        '18.3 Relaxation Methods': {'start': 964+24, 'end': 970+24, 'folder': '18_Two_Point_Boundary_Value_Problems/Relaxation_Methods'},
        '18.4 A Worked Example: Spheroidal Harmonics': {'start': 971+24, 'end': 980+24, 'folder': '18_Two_Point_Boundary_Value_Problems/A_Worked_Example_Spheroidal_Harmonics'},
        '18.5 Automated Allocation of Mesh Points': {'start': 981+24, 'end': 982+24, 'folder': '18_Two_Point_Boundary_Value_Problems/Automated_Allocation_of_Mesh_Points'},
        '18.6 Handling Internal Boundary Conditions or Singular Points': {'start': 983+24, 'end': 994+24, 'folder': '18_Two_Point_Boundary_Value_Problems/Handling_Internal_Boundary_Conditions_or_Singular_Points'},
        
        # Chapter 19: Integral Equations and Inverse Theory
        '19.1 Fredholm Equations of the Second Kind': {'start': 989+24, 'end': 991+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Fredholm_Equations_of_the_Second_Kind'},
        '19.2 Volterra Equations': {'start': 992+24, 'end': 994+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Volterra_Equations'},
        '19.3 Integral Equations with Singular Kernels': {'start': 995+24, 'end': 1000+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Integral_Equations_with_Singular_Kernels'},
        '19.4 Inverse Problems and the Use of A Priori Information': {'start': 1001+24, 'end': 1005+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Inverse_Problems_and_the_Use_of_A_Priori_Information'},
        '19.5 Linear Regularization Methods': {'start': 1006+24, 'end': 1013+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Linear_Regularization_Methods'},
        '19.6 Backus-Gilbert Method': {'start': 1014+24, 'end': 1015+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Backus_Gilbert_Method'},
        '19.7 Maximum Entropy Image Restoration': {'start': 1016+24, 'end': 1023+24, 'folder': '19_Integral_Equations_and_Inverse_Theory/Maximum_Entropy_Image_Restoration'},
        
        # Chapter 20: Partial Differential Equations
        '20.1 Flux-Conservative Initial Value Problems': {'start': 1031+24, 'end': 1042+24, 'folder': '20_Partial_Differential_Equations/Flux_Conservative_Initial_Value_Problems'},
        '20.2 Diffusive Initial Value Problems': {'start': 1043+24, 'end': 1048+24, 'folder': '20_Partial_Differential_Equations/Diffusive_Initial_Value_Problems'},
        '20.3 Initial Value Problems in Multidimensions': {'start': 1049+24, 'end': 1052+24, 'folder': '20_Partial_Differential_Equations/Initial_Value_Problems_in_Multidimensions'},
        '20.4 Fourier and Cyclic Reduction Methods for Boundary Value Problems': {'start': 1053+24, 'end': 1058+24, 'folder': '20_Partial_Differential_Equations/Fourier_and_Cyclic_Reduction_Methods_for_Boundary_Value_Problems'},
        '20.5 Relaxation Methods for Boundary Value Problems': {'start': 1059+24, 'end': 1065+24, 'folder': '20_Partial_Differential_Equations/Relaxation_Methods_for_Boundary_Value_Problems'},
        '20.6 Multigrid Methods for Boundary Value Problems': {'start': 1066+24, 'end': 1082+24, 'folder': '20_Partial_Differential_Equations/Multigrid_Methods_for_Boundary_Value_Problems'},
        '20.7 Spectral Methods': {'start': 1083+24, 'end': 1096+24, 'folder': '20_Partial_Differential_Equations/Spectral_Methods'},
        
        # Chapter 21: Computational Geometry
        '21.1 Points and Boxes': {'start': 1099+24, 'end': 1100+24, 'folder': '21_Computational_Geometry/Points_and_Boxes'},
        '21.2 KD Trees and Nearest-Neighbor Finding': {'start': 1101+24, 'end': 1110+24, 'folder': '21_Computational_Geometry/KD_Trees_and_Nearest_Neighbor_Finding'},
        '21.3 Triangles in Two and Three Dimensions': {'start': 1111+24, 'end': 1116+24, 'folder': '21_Computational_Geometry/Triangles_in_Two_and_Three_Dimensions'},
        '21.4 Lines, Line Segments, and Polygons': {'start': 1117+24, 'end': 1127+24, 'folder': '21_Computational_Geometry/Lines_Line_Segments_and_Polygons'},
        '21.5 Spheres and Rotations': {'start': 1128+24, 'end': 1130+24, 'folder': '21_Computational_Geometry/Spheres_and_Rotations'},
        '21.6 Triangulation and Delaunay Triangulation': {'start': 1131+24, 'end': 1140+24, 'folder': '21_Computational_Geometry/Triangulation_and_Delaunay_Triangulation'},
        '21.7 Applications of Delaunay Triangulation': {'start': 1141+24, 'end': 1148+24, 'folder': '21_Computational_Geometry/Applications_of_Delaunay_Triangulation'},
        '21.8 Quadtrees and Octrees: Storing Geometrical Objects': {'start': 1149+24, 'end': 1159+24, 'folder': '21_Computational_Geometry/Quadtrees_and_Octrees_Storing_Geometrical_Objects'},
        
        # Chapter 22: Less-Numerical Algorithms
        '22.1 Plotting Simple Graphs': {'start': 1160+24, 'end': 1162+24, 'folder': '22_Less_Numerical_Algorithms/Plotting_Simple_Graphs'},
        '22.2 Diagnosing Machine Parameters': {'start': 1163+24, 'end': 1165+24, 'folder': '22_Less_Numerical_Algorithms/Diagnosing_Machine_Parameters'},
        '22.3 Gray Codes': {'start': 1166+24, 'end': 1167+24, 'folder': '22_Less_Numerical_Algorithms/Gray_Codes'},
        '22.4 Cyclic Redundancy and Other Checksums': {'start': 1168+24, 'end': 1174+24, 'folder': '22_Less_Numerical_Algorithms/Cyclic_Redundancy_and_Other_Checksums'},
        '22.5 Huffman Coding and Compression of Data': {'start': 1175+24, 'end': 1180+24, 'folder': '22_Less_Numerical_Algorithms/Huffman_Coding_and_Compression_of_Data'},
        '22.6 Arithmetic Coding': {'start': 1181+24, 'end': 1184+24, 'folder': '22_Less_Numerical_Algorithms/Arithmetic_Coding'},
        '22.7 Arithmetic at Arbitrary Precision': {'start': 1185+24, 'end': 1194+24, 'folder': '22_Less_Numerical_Algorithms/Arithmetic_at_Arbitrary_Precision'},
    }

    # Load the main PDF
    with open("numerical_recipes.pdf", "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        # Split each section
        for section_name, section_info in sections.items():
            start_page = section_info['start'] - 1  # Convert to 0-indexed
            end_page = section_info['end'] - 1      # Convert to 0-indexed
            
            # Create a new PDF writer for this section
            output_writer = PdfWriter()
            
            # Add pages to the new PDF
            for page_num in range(start_page, end_page + 1):
                if page_num < len(pdf_reader.pages):
                    output_writer.add_page(pdf_reader.pages[page_num])
            
            # Create the target folder if it doesn't exist
            target_folder = section_info['folder']
            os.makedirs(target_folder, exist_ok=True)
            
            # Sanitize the section name for use as a filename
            sanitized_section_name = sanitize_filename(section_name)
            output_filename = f"{target_folder}/{sanitized_section_name}.pdf"
            
            # Write the section PDF to the file
            with open(output_filename, "wb") as output_pdf:
                output_writer.write(output_pdf)
                
            print(f"Created: {output_filename} (pages {section_info['start']}-{section_info['end']})")


if __name__ == "__main__":
    split_pdf_by_sections()