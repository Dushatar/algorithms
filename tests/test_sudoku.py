from algorithms.matrix import (
    bomb_enemy,
    copy_transform,
    crout_matrix_decomposition,
    cholesky_matrix_decomposition,
    matrix_exponentiation,
    matrix_inversion,
    multiply,
    rotate_image,
    sparse_dot_vector,
    spiral_traversal,
    sudoku_validator,
    sum_sub_squares,
)

import unittest


class TestSudokuValidator(unittest.TestCase):
    """[summary]
    Test for the file sudoku_validator.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_sudoku_validator(self):
        self.assertTrue(
            sudoku_validator.valid_solution(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))

        self.assertTrue(
            sudoku_validator.valid_solution_hashtable(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))

        self.assertTrue(
            sudoku_validator.valid_solution_set(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))

        self.assertFalse(
            sudoku_validator.valid_solution(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ]))

        self.assertFalse(
            sudoku_validator.valid_solution_hashtable(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ]))

        self.assertFalse(
            sudoku_validator.valid_solution_set(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 0, 3, 4, 9],
                    [1, 0, 0, 3, 4, 2, 5, 6, 0],
                    [8, 5, 9, 7, 6, 1, 0, 2, 0],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 0, 1, 5, 3, 7, 2, 1, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 0, 0, 4, 8, 1, 1, 7, 9]
                ]))
        
        
        #MIN EGNA!!!! TESTAR COLUMNER 
        self.assertFalse(
            sudoku_validator.valid_solution_set(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9],
                ]))
        
        #MIN EGNA!!!! TESTAR RUTOR
        self.assertFalse(
            sudoku_validator.valid_solution_set(
                [
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 7, 4, 2, 5, 6, 3],
                    [8, 5, 9, 3, 6, 1, 4, 2, 7],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]
                ]))
        
        
        """
        #self.assertTrue(sudoku_validator.return_thingy())
        print("For 1 in", sudoku_validator.return_thingy(0))
        print("For 1 not in", sudoku_validator.return_thingy(1))
        print("If 1 in", sudoku_validator.return_thingy(2))
        print("If 1 not in", sudoku_validator.return_thingy(3))
        print("For 2 in", sudoku_validator.return_thingy(4))
        print("For 2 not in", sudoku_validator.return_thingy(5))
        print("If 2 in", sudoku_validator.return_thingy(6))
        print("If 2 not in", sudoku_validator.return_thingy(7))
        print("For 3 in", sudoku_validator.return_thingy(8))
        print("For 3 not in", sudoku_validator.return_thingy(9))
        print("For 4 in", sudoku_validator.return_thingy(10))
        print("For 4 not in", sudoku_validator.return_thingy(11))
        print("If 3 in", sudoku_validator.return_thingy(12))
        print("If 3 not in", sudoku_validator.return_thingy(13))
        
        count = 0
        for i in range(14):
            if sudoku_validator.return_thingy(i) == 1:
                count = count +1
        
        print()
        print("VI GÅR IGENOM ", count, "BRANCHES")
        """

class TestSumSubSquares(unittest.TestCase):
    """[summary]
    Test for the file sum_sub_squares.py

    Arguments:
        unittest {[type]} -- [description]
    """

    def test_sum_sub_squares(self):
        mat = [[1, 1, 1, 1, 1],
               [2, 2, 2, 2, 2],
               [3, 3, 3, 3, 3],
               [4, 4, 4, 4, 4],
               [5, 5, 5, 5, 5]]
        self.assertEqual(sum_sub_squares.sum_sub_squares(mat, 3),
                         [[18, 18, 18], [27, 27, 27], [36, 36, 36]])

if __name__ == "__main__":
    unittest.main()
