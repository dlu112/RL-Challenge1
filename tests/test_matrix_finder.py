# Unit testing Matrix Finder with unittest
import unittest
from matrix_finder import MatrixFinder

class TestMatrixFinder(unittest.TestCase):
    # Initialize test matrices and matrix finders
    def setUp(self):
        debug = True

        self.test_matrix = [[0, 3.5, 6, 9],
                            [10, 13.5, 16, 19],
                            [20, 23.5, 26, 29],
                            [30, 33.5, 36, 39],
                            [40, 43.5, 46, 49],
                            [50, 53.5, 56, 59]]
        self.test_matrix_finder = MatrixFinder(self.test_matrix, debug)

        self.test_matrix_2 = [[0, 3],
                              [10, "apple", 13],
                              [20, 23]]
        self.test_matrix_finder_2 = MatrixFinder(self.test_matrix_2, debug)

        self.test_matrix_3 = [[0, 3],
                              [5, 6],
                              [7, 8],
                              ["banana", 10, 13],
                              [15, 16],
                              [20, 23]]
        self.test_matrix_finder_3 = MatrixFinder(self.test_matrix_3, debug)

        self.test_matrix_4 = [[1],
                              [3],
                              [5],
                              [7],
                              [9]]
        self.test_matrix_finder_4 = MatrixFinder(self.test_matrix_4, debug)

        self.test_matrix_5 = [[1, 3, 5, 7, 9]]
        self.test_matrix_finder_5 = MatrixFinder(self.test_matrix_5, debug)

        self.test_matrix_6 = [[5]]
        self.test_matrix_finder_6 = MatrixFinder(self.test_matrix_6, debug)

    # MatrixFinder gets the correct number of rows
    def test_rows(self):
        self.assertEqual(self.test_matrix_finder._m, 6, "Incorrect number of rows")

    # MatrixFinder gets the correct number of columns
    def test_cols(self):
        self.assertEqual(self.test_matrix_finder._n, 4, "Incorrect number of columns")

    # Each row is the correct length
    def test_row_lengths(self):
        for row in self.test_matrix_finder._matrix:
            self.assertEqual(len(row), 4, "A row in the matrix has the wrong length")

    # Finds target correctly
    def test_find_target(self):
        self.assertTrue(self.test_matrix_finder.find(36), "Fails to find target in matrix")

    # Fails to find target correctly
    def test_fails_target(self):
        self.assertFalse(self.test_matrix_finder.find(37), "Finds target not in matrix")
    
    # Finds target when target is in matrix[0][0]
    def test_find_first_target(self):
        self.assertTrue(self.test_matrix_finder.find(0), "Fails to find target in matrix located at [0][0]")

    # Finds target when target is in matrix[m][n]
    def test_find_last_target(self):
        self.assertTrue(self.test_matrix_finder.find(59), "Fails to find target in matrix located at [m][n]")

    # Fails when target is less than matrix[0][0]
    def test_target_too_small(self):
        self.assertFalse(self.test_matrix_finder.find(-1), "Finds target smaller than smallest value in matrix")

    # Fails when target is greater than highest value in matrix
    def test_target_too_big(self):
        self.assertFalse(self.test_matrix_finder.find(60), "Finds target larger than highest value in matrix")

    # Fails when target is wrong type
    def test_target_type_error(self):
        self.assertFalse(self.test_matrix_finder.find("10"), "Fails to handle TypeError in target")

    # Succeeds when TypeError is in matrix but not interacted with
    def test_avoid_matrix_type_error(self):
        self.assertTrue(self.test_matrix_finder_2.find(3), "Fails to avoid TypeError in matrix row")
    
    # Fails when TypeError is in selected target row
    def test_handle_matrix_type_error(self):
        self.assertFalse(self.test_matrix_finder_2.find(13), "Fails to handle TypeError in matrix")

    # Succeeds when TypeError is in first column of matrix and not interacted with
    def test_avoid_matrix_type_error_col_1(self):
        self.assertTrue(self.test_matrix_finder_3.find(0), "Fails to avoid TypeError in first column of matrix")

    # Fails when TypeError is in first column of matrix and interacted with
    def test_handle_matrix_type_error_col_1(self):
        self.assertFalse(self.test_matrix_finder_3.find(15), "Fails to handle TypeError in first column of matrix")

    # Successfully finds value when matrix has n = 1
    def test_find_target_n_1(self):
        self.assertTrue(self.test_matrix_finder_4.find(3), "Fails to find target in one column matrix")

    # Successfully fails to finds value when matrix has n = 1
    def test_fails_target_n_1(self):
        self.assertFalse(self.test_matrix_finder_4.find(2), "Find target not in in one column matrix")

    # Successfully finds value when matrix has m = 1
    def test_find_target_n_1(self):
        self.assertTrue(self.test_matrix_finder_5.find(3), "Fails to find target in one row matrix")

    # Successfully fails to finds value when matrix has m = 1
    def test_fails_target_n_1(self):
        self.assertFalse(self.test_matrix_finder_5.find(2), "Find target not in in one row matrix")

    # Successfully finds value when matrix s of dimension 1 x 1
    def test_find_target_1x1(self):
        self.assertTrue(self.test_matrix_finder_6.find(5), "Fails to find target in 1x1 matrix")

    # Successfully fails to finds value when matrix is of dimension 1 x 1
    def test_fails_target_1x1(self):
        self.assertFalse(self.test_matrix_finder_6.find(4), "Find target not in in 1x1 matrix")
    
if __name__ == "__main__":
    unittest.main()
