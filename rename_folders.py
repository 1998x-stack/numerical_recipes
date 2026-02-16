#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Define the mapping from folder names to chapter.section numbers
folder_mapping = {
    # Chapter 2 mappings
    "Gauss_Jordan_Elimination": "2_1",
    "Gaussian_Elimination_with_Backsubstitution": "2_2",
    "LU_Decomposition_and_Its_Applications": "2_3", 
    "Tridiagonal_and_Band_Diagonal_Systems_of_Equations": "2_4",
    "Iterative_Improvement_of_a_Solution_to_Linear_Equations": "2_5",
    "Singular_Value_Decomposition": "2_6",
    "Sparse_Linear_Systems": "2_7",
    "Vandermonde_Matrices_and_Toeplitz_Matrices": "2_8",
    "Cholesky_Decomposition": "2_9",
    "QR_Decomposition": "2_10",
    "Is_Matrix_Inversion_an_N3_Process": "2_11",
    
    # Chapter 3 mappings
    "Preliminaries_Searching_a_Ordered_Table": "3_1",
    "Polynomial_Interpolation_and_Extrapolation": "3_2",
    "Cubic_Spline_Interpolation": "3_3",
    "Rational_Function_Interpolation_and_Extrapolation": "3_4",
    "Coefficients_of_the_Interpolating_Polynomial": "3_5",
    "Interpolation_on_a_Grid_in_Multidimensions": "3_6",
    "Interpolation_on_Scattered_Data_in_Multidimensions": "3_7",
    "Laplace_Interpolation": "3_8",
    
    # Chapter 4 mappings
    "Classical_Formulas_for_Equally_Spaced_Abscissas": "4_1",
    "Elementary_Algorithms": "4_2",
    "Romberg_Integration": "4_3",
    "Improper_Integrals": "4_4",
    "Quadrature_by_Variable_Transformation": "4_5",
    "Gaussian_Quadratures_and_Orthogonal_Polynomials": "4_6",
    "Adaptive_Quadrature": "4_7",
    "Multidimensional_Integrals": "4_8",
    
    # Chapter 5 mappings
    "Polynomials_and_Rational_Functions": "5_1",
    "Evaluation_of_Continued_Fractions": "5_2",
    "Series_and_Their_Convergence": "5_3",
    "Recurrence_Relations_and_Clushaws_Recurcence_Formula": "5_4",
    "Complex_Arithmetic": "5_5",
    "Quadratic_and_Cubic_Equations": "5_6",
    "Numerical_Derivatives": "5_7",
    "Chebyshev_Approximation": "5_8",
    "Derivatives_or_Integrals_of_a_Chebyshev_Approximated_Function": "5_9",
    "Polynomial_Approximation_from_Chebyshev_Coefficients": "5_10",
    "Economization_of_Power_Series": "5_11",
    "Padé_Approximants": "5_12",
    "Rational_Chebyshev_Approximation": "5_13",
    "Evaluation_of_Functions_by_Path_Integration": "5_14",
    
    # Chapter 6 mappings
    "Gamma_Function_Beta_Function_Factorials_Binomial_Coefficients": "6_1",
    "Incomplete_Gamma_Function_and_Error_Function": "6_2",
    "Exponential_Integrals": "6_3",
    "Incomplete_Beta_Function": "6_4",
    "Bessel_Functions_of_Integer_Order": "6_5",
    "Bessel_Functions_of_Fractional_Order_Airy_Functions_Spherical_Bessel_Functions": "6_6",
    "Spherical_Harmonics": "6_7",
    "Fresnel_Integrals_Cosine_and_Sine_Integrals": "6_8",
    "Dawson_s_Integral": "6_9",
    "Generalized_Fermi_Dirac_Integrals": "6_10",
    "Inverse_of_the_Function_xlogx": "6_11",
    "Elliptic_Integrals_and_Jacobian_Elliptic_Functions": "6_12",
    "Hypergeometric_Functions": "6_13",
    "Statistical_Functions": "6_14",
    
    # Chapter 7 mappings
    "Uniform_Deviates": "7_1",
    "Completely_Hashing_a_Large_Array": "7_2",
    "Deviates_from_Other_Distributions": "7_3",
    "Multivariate_Normal_Deviates": "7_4",
    "Linear_Feedback_Shift_Registers": "7_5",
    "Hash_Tables_and_Hash_Memories": "7_6",
    "Simple_Monte_Carlo_Integration": "7_7",
    "Quasi_Random_Sequences": "7_8",
    "Adaptive_and_Recursive_Monte_Carlo_Methods": "7_9",
    
    # Chapter 8 mappings
    "Straight_Insertion_and_Shells_Method": "8_1",
    "Quicksort": "8_2",
    "Heapsort": "8_3",
    "Indexing_and_Ranking": "8_4",
    "Selecting_the_Mth_Largest": "8_5",
    "Determination_of_Equivalence_Classes": "8_6",
    
    # Chapter 9 mappings
    "Bracketing_and_Bisection": "9_1",
    "Secant_Method_False_Position_Method_and_Ridders_Method": "9_2",
    "Van_Wijngaarden_Dekker_Brent_Method": "9_3",
    "Newton_Raphson_Method_Using_Derivative": "9_4",
    "Roots_of_Polynomials": "9_5",
    "Newton_Raphson_Method_for_Nonlinear_Systems_of_Equations": "9_6",
    "Globally_Convergent_Methods_for_Nonlinear_Systems_of_Equations": "9_7",
    
    # Chapter 10 mappings
    "Initially_Bracketing_a_Minimum": "10_1",
    "Golden_Section_Search_in_One_Dimension": "10_2",
    "Parabolic_Interpolation_and_Brents_Method_in_One_Dimension": "10_3",
    "One_Dimensional_Search_with_First_Derivatives": "10_4",
    "Downhill_Simplex_Method_in_Multidimensions": "10_5",
    "Line_Methods_in_Multidimensions": "10_6",
    "Direction_Set_Powells_Methods_in_Multidimensions": "10_7",
    "Conjugate_Gradient_Methods_in_Multidimensions": "10_8",
    "Quasi_Newton_or_Variable_Metric_Methods_in_Multidimensions": "10_9",
    "Linear_Programming_The_Simplex_Method": "10_10",
    "Linear_Programming_Interior_Point_Methods": "10_11",
    "Simulated_Annealing_Methods": "10_12",
    "Dynamic_Programming": "10_13",
    
    # Chapter 11 mappings
    "Jacobi_Transformations_of_a_Symmetric_Matrix": "11_1",
    "Real_Symmetric_Matrices": "11_2",
    # Note: 11_3 already exists with correct naming
    "Eigenvalues_and_Eigenvectors_of_a_Tridiagonal_Matrix": "11_4",
    "Hermitian_Matrices": "11_5",
    "Real_Nonsymmetric_Matrices": "11_6",
    "The_QR_Algorithm_for_Real_Hessenberg_Matrices": "11_7",
    "Improving_Eigenvalues_and_or_Finding_Eigenvectors_by_Inverse_Iteration": "11_8",
    
    # Chapter 12 mappings
    "Fourier_Transform_of_Discretely_Sampled_Data": "12_1",
    "Fast_Fourier_Transform_FFT": "12_2",
    "FFT_of_Real_Functions": "12_3",
    "Fast_Sine_and_Cosine_Transforms": "12_4",
    "FFT_in_Two_or_More_Dimensions": "12_5",
    "Fourier_Transforms_of_Real_Data_in_Two_and_Three_Dimensions": "12_6",
    "External_Storage_or_Memory_Local_FFTs": "12_7",
    
    # Chapter 13 mappings
    "Convolution_and_Deconvolution_Using_the_FFT": "13_1",
    "Correlation_and_Autocorrelation_Using_the_FFT": "13_2",
    "Optimal_Wiener_Filtering_with_the_FFT": "13_3",
    "Power_Spectrum_Estimation_Using_the_FFT": "13_4",
    "Digital_Filtering_in_the_Time_Domain": "13_5",
    "Linear_Prediction_and_Linear_Predictive_Coding": "13_6",
    "Power_Spectrum_Estimation_by_the_Maximum_Entropy_All_Poles_Method": "13_7",
    "Spectral_Analysis_of_Unevenly_Sampled_Data": "13_8",
    "Computing_Fourier_Integrals_Using_the_FFT": "13_9",
    "Wavelet_Transforms": "13_10",
    "Numerical_Use_of_the_Sampling_Theorem": "13_11",
    
    # Chapter 14 mappings
    "Moments_of_a_Distribution_Mean_Variance_Skewness_and_So_Forth": "14_1",
    "Do_Two_Distributions_Have_the_Same_Means_or_Variances": "14_2",
    "Are_Two_Distributions_Different": "14_3",
    "Contingency_Table_Analysis_of_Two_Distributions": "14_4",
    "Linear_Correlation": "14_5",
    "Nonparametric_or_Rank_Correlation": "14_6",
    "Information_Theoretic_Properties_of_Distributions": "14_7",
    "Do_Two_Dimensional_Distributions_Differ": "14_8",
    "Savitzky_Golay_Smoothing_Filters": "14_9",
    
    # Chapter 15 mappings
    "Least_Squares_as_a_Maximum_Likelihood_Estimator": "15_1",
    "Fitting_Data_to_a_Straight_Line": "15_2",
    "Straight_Line_Data_with_Errors_in_Both_Coordinates": "15_3",
    "General_Linear_Least_Squares": "15_4",
    "Nonlinear_Models": "15_5",
    "Confidence_Limits_on_Estimated_Model_Parameters": "15_6",
    "Robust_Estimation": "15_7",
    "Markov_Chain_Monte_Carlo": "15_8",
    "Gaussian_Process_Regression": "15_9",
    
    # Chapter 16 mappings
    "Gaussian_Mixture_Models_and_k_Means_Clustering": "16_1",
    "Viterbi_Decoding": "16_2",
    "Markov_Models_and_Hidden_Markov_Modeling": "16_3",
    "Hierarchical_Clustering_by_Phylogenetic_Trees": "16_4",
    "Support_Vector_Machines": "16_5",
    
    # Chapter 17 mappings
    "Runge_Kutta_Method": "17_1",
    "Adaptive_Stepsize_Control_for_Runge_Kutta": "17_2",
    "Richardson_Extrapolation_and_the_Bulirsch_Stoer_Method": "17_3",
    "Second_Order_Conservative_Equations": "17_4",
    "Stiff_Sets_of_Equations": "17_5",
    "Multistep_Multivalue_and_Predictor_Corrector_Methods": "17_6",
    "Stochastic_Simulation_of_Chemical_Reaction_Networks": "17_7",
    
    # Chapter 18 mappings
    "The_Shooting_Method": "18_1",
    "Shooting_to_a_Fitting_Point": "18_2",
    "Relaxation_Methods": "18_3",
    "A_Worked_Example_Spheroidal_Harmonics": "18_4",
    "Automated_Allocation_of_Mesh_Points": "18_5",
    "Handling_Internal_Boundary_Conditions_or_Singular_Points": "18_6",
    
    # Chapter 19 mappings
    "Fredholm_Equations_of_the_Second_Kind": "19_1",
    "Volterra_Equations": "19_2",
    "Integral_Equations_with_Singular_Kernels": "19_3",
    "Inverse_Problems_and_the_Use_of_A_Priori_Information": "19_4",
    "Linear_Regularization_Methods": "19_5",
    "Backus_Gilbert_Method": "19_6",
    "Maximum_Entropy_Image_Restoration": "19_7",
    
    # Chapter 20 mappings
    "Flux_Conservative_Initial_Value_Problems": "20_1",
    "Diffusive_Initial_Value_Problems": "20_2",
    "Initial_Value_Problems_in_Multidimensions": "20_3",
    "Fourier_and_Cyclic_Reduction_Methods_for_Boundary_Value_Problems": "20_4",
    "Relaxation_Methods_for_Boundary_Value_Problems": "20_5",
    "Multigrid_Methods_for_Boundary_Value_Problems": "20_6",
    "Spectral_Methods": "20_7",
    
    # Chapter 21 mappings
    "Points_and_Boxes": "21_1",
    "KD_Trees_and_Nearest_Neighbor_Finding": "21_2",
    "Triangles_in_Two_and_Three_Dimensions": "21_3",
    "Lines_Line_Segments_and_Polygons": "21_4",
    "Spheres_and_Rotations": "21_5",
    "Triangulation_and_Delaunay_Triangulation": "21_6",
    "Applications_of_Delaunay_Triangulation": "21_7",
    "Quadtrees_and_Octrees_Storing_Geometrical_Objects": "21_8",
    
    # Chapter 22 mappings
    "Plotting_Simple_Graphs": "22_1",
    "Diagnosing_Machine_Parameters": "22_2",
    "Gray_Codes": "22_3",
    "Cyclic_Redundancy_and_Other_Checksums": "22_4",
    "Huffman_Coding_and_Compression_of_Data": "22_5",
    "Arithmetic_Coding": "22_6",
    "Arithmetic_at_Arbitrary_Precision": "22_7",
}

def rename_subfolders():
    base_path = Path(".")
    
    for chapter_dir in base_path.iterdir():
        if chapter_dir.is_dir() and re.match(r'^\d+_.*', chapter_dir.name):
            for subfolder in chapter_dir.iterdir():
                if subfolder.is_dir():
                    subfolder_name = subfolder.name
                    
                    if re.match(r'^\d+_\d+_.*', subfolder_name):
                        print(f"Skipping {subfolder_name} - already has correct prefix")
                        continue
                    
                    if subfolder_name in folder_mapping:
                        chapter_section = folder_mapping[subfolder_name]
                        
                        new_name = f"{chapter_section}_{subfolder_name}"
                        new_path = subfolder.parent / new_name
                        
                        print(f"Renaming: {subfolder_name} -> {new_name}")
                        
                        try:
                            subfolder.rename(new_path)
                            print(f"  Renamed successfully!")
                        except OSError as e:
                            print(f"  Error renaming {subfolder_name}: {e}")
                    else:
                        print(f"Warning: No mapping found for {subfolder_name}")
                        
if __name__ == "__main__":
    rename_subfolders()