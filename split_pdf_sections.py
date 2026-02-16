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
    
    # Define the sections with their starting pages
    sections = {
        # Chapter 2: Solution of Linear Algebraic Equations
        '2.1 Gauss-Jordan Elimination': {'start': 41, 'end': 45, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Gauss_Jordan_Elimination'},
        '2.2 Gaussian Elimination with Backsubstitution': {'start': 46, 'end': 47, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Gaussian_Elimination_with_Backsubstitution'},
        '2.3 LU Decomposition and Its Applications': {'start': 48, 'end': 55, 'folder': '2_Solution_of_Linear_Algebraic_Equations/LU_Decomposition_and_Its_Applications'},
        '2.4 Tridiagonal and Band-Diagonal Systems of Equations': {'start': 56, 'end': 60, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Tridiagonal_and_Band_Diagonal_Systems_of_Equations'},
        '2.5 Iterative Improvement of a Solution to Linear Equations': {'start': 61, 'end': 64, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Iterative_Improvement_of_a_Solution_to_Linear_Equations'},
        '2.6 Singular Value Decomposition': {'start': 65, 'end': 74, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Singular_Value_Decomposition'},
        '2.7 Sparse Linear Systems': {'start': 75, 'end': 92, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Sparse_Linear_Systems'},
        '2.8 Vandermonde Matrices and Toeplitz Matrices': {'start': 93, 'end': 99, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Vandermonde_Matrices_and_Toeplitz_Matrices'},
        '2.9 Cholesky Decomposition': {'start': 100, 'end': 101, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Cholesky_Decomposition'},
        '2.10 QR Decomposition': {'start': 102, 'end': 105, 'folder': '2_Solution_of_Linear_Algebraic_Equations/QR_Decomposition'},
        '2.11 Is Matrix Inversion an N3 Process': {'start': 106, 'end': 108, 'folder': '2_Solution_of_Linear_Algebraic_Equations/Is_Matrix_Inversion_an_N3_Process'},
        
        # Chapter 3: Interpolation and Extrapolation
        '3.1 Preliminaries Searching a Ordered Table': {'start': 114, 'end': 117, 'folder': '3_Interpolation_and_Extrapolation/Preliminaries_Searching_a_Ordered_Table'},
        '3.2 Polynomial Interpolation and Extrapolation': {'start': 118, 'end': 119, 'folder': '3_Interpolation_and_Extrapolation/Polynomial_Interpolation_and_Extrapolation'},
        '3.3 Cubic Spline Interpolation': {'start': 120, 'end': 123, 'folder': '3_Interpolation_and_Extrapolation/Cubic_Spline_Interpolation'},
        '3.4 Rational Function Interpolation and Extrapolation': {'start': 124, 'end': 128, 'folder': '3_Interpolation_and_Extrapolation/Rational_Function_Interpolation_and_Extrapolation'},
        '3.5 Coefficients of the Interpolating Polynomial': {'start': 129, 'end': 131, 'folder': '3_Interpolation_and_Extrapolation/Coefficients_of_the_Interpolating_Polynomial'},
        '3.6 Interpolation on a Grid in Multidimensions': {'start': 132, 'end': 138, 'folder': '3_Interpolation_and_Extrapolation/Interpolation_on_a_Grid_in_Multidimensions'},
        '3.7 Interpolation on Scattered Data in Multidimensions': {'start': 139, 'end': 149, 'folder': '3_Interpolation_and_Extrapolation/Interpolation_on_Scattered_Data_in_Multidimensions'},
        '3.8 Laplace Interpolation': {'start': 150, 'end': 154, 'folder': '3_Interpolation_and_Extrapolation/Laplace_Interpolation'},
        
        # Chapter 4: Integration of Functions
        '4.1 Classical Formulas for Equally Spaced Abscissas': {'start': 156, 'end': 161, 'folder': '4_Integration_of_Functions/Classical_Formulas_for_Equally_Spaced_Abscissas'},
        '4.2 Elementary Algorithms': {'start': 162, 'end': 165, 'folder': '4_Integration_of_Functions/Elementary_Algorithms'},
        '4.3 Romberg Integration': {'start': 166, 'end': 166, 'folder': '4_Integration_of_Functions/Romberg_Integration'},
        '4.4 Improper Integrals': {'start': 167, 'end': 171, 'folder': '4_Integration_of_Functions/Improper_Integrals'},
        '4.5 Quadrature by Variable Transformation': {'start': 172, 'end': 178, 'folder': '4_Integration_of_Functions/Quadrature_by_Variable_Transformation'},
        '4.6 Gaussian Quadratures and Orthogonal Polynomials': {'start': 179, 'end': 193, 'folder': '4_Integration_of_Functions/Gaussian_Quadratures_and_Orthogonal_Polynomials'},
        '4.7 Adaptive Quadrature': {'start': 194, 'end': 195, 'folder': '4_Integration_of_Functions/Adaptive_Quadrature'},
        '4.8 Multidimensional Integrals': {'start': 196, 'end': 200, 'folder': '4_Integration_of_Functions/Multidimensional_Integrals'},
        
        # Chapter 5: Evaluation of Functions
        '5.1 Polynomials and Rational Functions': {'start': 201, 'end': 205, 'folder': '5_Evaluation_of_Functions/Polynomials_and_Rational_Functions'},
        '5.2 Evaluation of Continued Fractions': {'start': 206, 'end': 208, 'folder': '5_Evaluation_of_Functions/Evaluation_of_Continued_Fractions'},
        '5.3 Series and Their Convergence': {'start': 209, 'end': 218, 'folder': '5_Evaluation_of_Functions/Series_and_Their_Convergence'},
        '5.4 Recurrence Relations and Clenshaw\'s Recurrence Formula': {'start': 219, 'end': 224, 'folder': '5_Evaluation_of_Functions/Recurrence_Relations_and_Clushaws_Recurcence_Formula'},
        '5.5 Complex Arithmetic': {'start': 225, 'end': 226, 'folder': '5_Evaluation_of_Functions/Complex_Arithmetic'},
        '5.6 Quadratic and Cubic Equations': {'start': 227, 'end': 228, 'folder': '5_Evaluation_of_Functions/Quadratic_and_Cubic_Equations'},
        '5.7 Numerical Derivatives': {'start': 229, 'end': 232, 'folder': '5_Evaluation_of_Functions/Numerical_Derivatives'},
        '5.8 Chebyshev Approximation': {'start': 233, 'end': 239, 'folder': '5_Evaluation_of_Functions/Chebyshev_Approximation'},
        '5.9 Derivatives or Integrals of a Chebyshev-Approximated Function': {'start': 240, 'end': 240, 'folder': '5_Evaluation_of_Functions/Derivatives_or_Integrals_of_a_Chebyshev_Approximated_Function'},
        '5.10 Polynomial Approximation from Chebyshev Coefficients': {'start': 241, 'end': 242, 'folder': '5_Evaluation_of_Functions/Polynomial_Approximation_from_Chebyshev_Coefficients'},
        '5.11 Economization of Power Series': {'start': 243, 'end': 244, 'folder': '5_Evaluation_of_Functions/Economization_of_Power_Series'},
        '5.12 Padé Approximants': {'start': 245, 'end': 246, 'folder': '5_Evaluation_of_Functions/Pade_Approximants'},
        '5.13 Rational Chebyshev Approximation': {'start': 247, 'end': 250, 'folder': '5_Evaluation_of_Functions/Rational_Chebyshev_Approximation'},
        '5.14 Evaluation of Functions by Path Integration': {'start': 251, 'end': 254, 'folder': '5_Evaluation_of_Functions/Evaluation_of_Functions_by_Path_Integration'},
        
        # Chapter 6: Special Functions
        '6.1 Gamma Function Beta Function Factorials Binomial Coefficients': {'start': 256, 'end': 258, 'folder': '6_Special_Functions/Gamma_Function_Beta_Function_Factorials_Binomial_Coefficients'},
        '6.2 Incomplete Gamma Function and Error Function': {'start': 259, 'end': 265, 'folder': '6_Special_Functions/Incomplete_Gamma_Function_and_Error_Function'},
        '6.3 Exponential Integrals': {'start': 266, 'end': 269, 'folder': '6_Special_Functions/Exponential_Integrals'},
        '6.4 Incomplete Beta Function': {'start': 270, 'end': 273, 'folder': '6_Special_Functions/Incomplete_Beta_Function'},
        '6.5 Bessel Functions of Integer Order': {'start': 274, 'end': 282, 'folder': '6_Special_Functions/Bessel_Functions_of_Integer_Order'},
        '6.6 Bessel Functions of Fractional Order Airy Functions Spherical Bessel Functions': {'start': 283, 'end': 291, 'folder': '6_Special_Functions/Bessel_Functions_of_Fractional_Order_Airy_Functions_Spherical_Bessel_Functions'},
        '6.7 Spherical Harmonics': {'start': 292, 'end': 296, 'folder': '6_Special_Functions/Spherical_Harmonics'},
        '6.8 Fresnel Integrals Cosine and Sine Integrals': {'start': 297, 'end': 301, 'folder': '6_Special_Functions/Fresnel_Integrals_Cosine_and_Sine_Integrals'},
        '6.9 Dawson\'s Integral': {'start': 302, 'end': 303, 'folder': '6_Special_Functions/Dawsons_Integral'},
        '6.10 Generalized Fermi-Dirac Integrals': {'start': 304, 'end': 306, 'folder': '6_Special_Functions/Generalized_Fermi_Dirac_Integrals'},
        '6.11 Inverse of the Function xlogx': {'start': 307, 'end': 308, 'folder': '6_Special_Functions/Inverse_of_the_Function_xlogx'},
        '6.12 Elliptic Integrals and Jacobian Elliptic Functions': {'start': 309, 'end': 317, 'folder': '6_Special_Functions/Elliptic_Integrals_and_Jacobian_Elliptic_Functions'},
        '6.13 Hypergeometric Functions': {'start': 318, 'end': 319, 'folder': '6_Special_Functions/Hypergeometric_Functions'},
        '6.14 Statistical Functions': {'start': 320, 'end': 339, 'folder': '6_Special_Functions/Statistical_Functions'},
        
        # Chapter 7: Random Numbers
        '7.1 Uniform Deviates': {'start': 341, 'end': 357, 'folder': '7_Random_Numbers/Uniform_Deviates'},
        '7.2 Completely Hashing a Large Array': {'start': 358, 'end': 360, 'folder': '7_Random_Numbers/Completely_Hashing_a_Large_Array'},
        '7.3 Deviates from Other Distributions': {'start': 361, 'end': 377, 'folder': '7_Random_Numbers/Deviates_from_Other_Distributions'},
        '7.4 Multivariate Normal Deviates': {'start': 378, 'end': 379, 'folder': '7_Random_Numbers/Multivariate_Normal_Deviates'},
        '7.5 Linear Feedback Shift Registers': {'start': 380, 'end': 385, 'folder': '7_Random_Numbers/Linear_Feedback_Shift_Registers'},
        '7.6 Hash Tables and Hash Memories': {'start': 386, 'end': 396, 'folder': '7_Random_Numbers/Hash_Tables_and_Hash_Memories'},
        '7.7 Simple Monte Carlo Integration': {'start': 397, 'end': 402, 'folder': '7_Random_Numbers/Simple_Monte_Carlo_Integration'},
        '7.8 Quasi Random Sequences': {'start': 403, 'end': 409, 'folder': '7_Random_Numbers/Quasi_Random_Sequences'},
        '7.9 Adaptive and Recursive Monte Carlo Methods': {'start': 410, 'end': 418, 'folder': '7_Random_Numbers/Adaptive_and_Recursive_Monte_Carlo_Methods'},
        
        # Chapter 8: Sorting and Selection
        '8.1 Straight Insertion and Shells Method': {'start': 420, 'end': 422, 'folder': '8_Sorting_and_Selection/Straight_Insertion_and_Shells_Method'},
        '8.2 Quicksort': {'start': 423, 'end': 425, 'folder': '8_Sorting_and_Selection/Quicksort'},
        '8.3 Heapsort': {'start': 426, 'end': 427, 'folder': '8_Sorting_and_Selection/Heapsort'},
        '8.4 Indexing and Ranking': {'start': 428, 'end': 430, 'folder': '8_Sorting_and_Selection/Indexing_and_Ranking'},
        '8.5 Selecting the Mth Largest': {'start': 431, 'end': 438, 'folder': '8_Sorting_and_Selection/Selecting_the_Mth_Largest'},
        '8.6 Determination of Equivalence Classes': {'start': 439, 'end': 441, 'folder': '8_Sorting_and_Selection/Determination_of_Equivalence_Classes'},
        
        # Chapter 9: Root Finding and Nonlinear Sets of Equations
        '9.1 Bracketing and Bisection': {'start': 445, 'end': 448, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Bracketing_and_Bisection'},
        '9.2 Secant Method False Position Method and Ridders Method': {'start': 449, 'end': 453, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Secant_Method_False_Position_Method_and_Ridders_Method'},
        '9.3 Van Wijngaarden Dekker Brent Method': {'start': 454, 'end': 455, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Van_Wijngaarden_Dekker_Brent_Method'},
        '9.4 Newton Raphson Method Using Derivative': {'start': 456, 'end': 462, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Newton_Raphson_Method_Using_Derivative'},
        '9.5 Roots of Polynomials': {'start': 463, 'end': 472, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Roots_of_Polynomials'},
        '9.6 Newton Raphson Method for Nonlinear Systems of Equations': {'start': 473, 'end': 476, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Newton_Raphson_Method_for_Nonlinear_Systems_of_Equations'},
        '9.7 Globally Convergent Methods for Nonlinear Systems of Equations': {'start': 477, 'end': 486, 'folder': '9_Root_Finding_and_Nonlinear_Sets_of_Equations/Globally_Convergent_Methods_for_Nonlinear_Systems_of_Equations'},
        
        # Chapter 10: Minimization or Maximization of Functions
        '10.1 Initially Bracketing a Minimum': {'start': 490, 'end': 491, 'folder': '10_Minimization_or_Maximization_of_Functions/Initially_Bracketing_a_Minimum'},
        '10.2 Golden Section Search in One Dimension': {'start': 492, 'end': 495, 'folder': '10_Minimization_or_Maximization_of_Functions/Golden_Section_Search_in_One_Dimension'},
        '10.3 Parabolic Interpolation and Brents Method in One Dimension': {'start': 496, 'end': 498, 'folder': '10_Minimization_or_Maximization_of_Functions/Parabolic_Interpolation_and_Brents_Method_in_One_Dimension'},
        '10.4 One Dimensional Search with First Derivatives': {'start': 499, 'end': 501, 'folder': '10_Minimization_or_Maximization_of_Functions/One_Dimensional_Search_with_First_Derivatives'},
        '10.5 Downhill Simplex Method in Multidimensions': {'start': 502, 'end': 506, 'folder': '10_Minimization_or_Maximization_of_Functions/Downhill_Simplex_Method_in_Multidimensions'},
        '10.6 Line Methods in Multidimensions': {'start': 507, 'end': 508, 'folder': '10_Minimization_or_Maximization_of_Functions/Line_Methods_in_Multidimensions'},
        '10.7 Direction Set Powells Methods in Multidimensions': {'start': 509, 'end': 514, 'folder': '10_Minimization_or_Maximization_of_Functions/Direction_Set_Powells_Methods_in_Multidimensions'},
        '10.8 Conjugate Gradient Methods in Multidimensions': {'start': 515, 'end': 520, 'folder': '10_Minimization_or_Maximization_of_Functions/Conjugate_Gradient_Methods_in_Multidimensions'},
        '10.9 Quasi Newton or Variable Metric Methods in Multidimensions': {'start': 521, 'end': 525, 'folder': '10_Minimization_or_Maximization_of_Functions/Quasi_Newton_or_Variable_Metric_Methods_in_Multidimensions'},
        '10.10 Linear Programming The Simplex Method': {'start': 526, 'end': 536, 'folder': '10_Minimization_or_Maximization_of_Functions/Linear_Programming_The_Simplex_Method'},
        '10.11 Linear Programming Interior Point Methods': {'start': 537, 'end': 548, 'folder': '10_Minimization_or_Maximization_of_Functions/Linear_Programming_Interior_Point_Methods'},
        '10.12 Simulated Annealing Methods': {'start': 549, 'end': 554, 'folder': '10_Minimization_or_Maximization_of_Functions/Simulated_Annealing_Methods'},
        '10.13 Dynamic Programming': {'start': 555, 'end': 562, 'folder': '10_Minimization_or_Maximization_of_Functions/Dynamic_Programming'},
        
        # Chapter 11: Eigensystems
        '11.1 Jacobi Transformations of a Symmetric Matrix': {'start': 570, 'end': 575, 'folder': '11_Eigensystems/Jacobi_Transformations_of_a_Symmetric_Matrix'},
        '11.2 Real Symmetric Matrices': {'start': 576, 'end': 577, 'folder': '11_Eigensystems/Real_Symmetric_Matrices'},
        '11.3 Reduction of a Symmetric Matrix to Tridiagonal Form Givens and Householder Reductions': {'start': 578, 'end': 582, 'folder': '11_Eigensystems/Reduction_of_a_Symmetric_Matrix_to_Tridiagonal_Form_Givens_and_Householder_Reductions'},
        '11.4 Eigenvalues and Eigenvectors of a Tridiagonal Matrix': {'start': 583, 'end': 589, 'folder': '11_Eigensystems/Eigenvalues_and_Eigenvectors_of_a_Tridiagonal_Matrix'},
        '11.5 Hermitian Matrices': {'start': 590, 'end': 590, 'folder': '11_Eigensystems/Hermitian_Matrices'},
        '11.6 Real Nonsymmetric Matrices': {'start': 590, 'end': 595, 'folder': '11_Eigensystems/Real_Nonsymmetric_Matrices'},
        '11.7 The QR Algorithm for Real Hessenberg Matrices': {'start': 596, 'end': 596, 'folder': '11_Eigensystems/The_QR_Algorithm_for_Real_Hessenberg_Matrices'},
        '11.8 Improving Eigenvalues and or Finding Eigenvectors by Inverse Iteration': {'start': 597, 'end': 600, 'folder': '11_Eigensystems/Improving_Eigenvalues_and_or_Finding_Eigenvectors_by_Inverse_Iteration'},
        
        # Chapter 12: Fast Fourier Transform
        '12.1 Fourier Transform of Discretely Sampled Data': {'start': 605, 'end': 607, 'folder': '12_Fast_Fourier_Transform/Fourier_Transform_of_Discretely_Sampled_Data'},
        '12.2 Fast Fourier Transform FFT': {'start': 608, 'end': 616, 'folder': '12_Fast_Fourier_Transform/Fast_Fourier_Transform_FFT'},
        '12.3 FFT of Real Functions': {'start': 617, 'end': 619, 'folder': '12_Fast_Fourier_Transform/FFT_of_Real_Functions'},
        '12.4 Fast Sine and Cosine Transforms': {'start': 620, 'end': 626, 'folder': '12_Fast_Fourier_Transform/Fast_Sine_and_Cosine_Transforms'},
        '12.5 FFT in Two or More Dimensions': {'start': 627, 'end': 630, 'folder': '12_Fast_Fourier_Transform/FFT_in_Two_or_More_Dimensions'},
        '12.6 Fourier Transforms of Real Data in Two and Three Dimensions': {'start': 631, 'end': 636, 'folder': '12_Fast_Fourier_Transform/Fourier_Transforms_of_Real_Data_in_Two_and_Three_Dimensions'},
        '12.7 External Storage or Memory Local FFTs': {'start': 637, 'end': 639, 'folder': '12_Fast_Fourier_Transform/External_Storage_or_Memory_Local_FFTs'},
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