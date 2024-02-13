import sys
import time
import pandas as pd

def parse_arguments():
    if len(sys.argv) != 3:
        print("ERROR: Not enough/too many/illegal input arguments.")
        sys.exit(1)

    mode = int(sys.argv[1])
    filename = sys.argv[2]

    return mode, filename

def load_sudoku_board(filename):
    sudoku_input = pd.read_csv(filename, header=None)
    return sudoku_input.values

def display_sudoku_board(board):
    for row in board:
        print(",".join(map(str, row)))

def is_consistent(board):
    for i in range(9):
        row_set = set()
        col_set = set()
        grid_set = set()

        for j in range(9):
            if board[i, j] != 'X' and board[i, j] in row_set:
                return False
            row_set.add(board[i, j])

            if board[j, i] != 'X' and board[j, i] in col_set:
                return False
            col_set.add(board[j, i])

            grid_row = 3 * (i // 3) + j // 3
            grid_col = 3 * (i % 3) + j % 3

            if board[grid_row, grid_col] != 'X' and board[grid_row, grid_col] in grid_set:
                return False
            grid_set.add(board[grid_row, grid_col])

    return True

def assignment_is_complete(assignment):
    return len(assignment) == 81

def select_unassigned_variable(csp, assignment):
    for i in range(9):
        for j in range(9):
            if (i, j) not in assignment:
                return (i, j)
    return None

def order_domain_values(csp, var, assignment):
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def value_is_consistent(value, assignment):
    return all(value != assignment[var] for var in assignment)

def add_assignment(assignment, var, value):
    return {**assignment, var: value}

def remove_assignment(assignment, var):
    return {key: val for key, val in assignment.items() if key != var}

def inference(csp, var, assignment):
    return None  # Since inference is not implemented, return None

def add_inferences(csp, inferences):
    return None  # Since adding inferences is not implemented, return None

def remove_inferences(csp, inferences):
    return None  # Since removing inferences is not implemented, return None

def brute_force_search(board):
    assignment = {}
    result = recursive_brute_force(board, assignment)
    if result is not None:
        return result
    else:
        print("No solution found.")
        return None

def recursive_brute_force(board, assignment):
    if assignment_is_complete(assignment):
        return assignment

    var = select_unassigned_variable(board, assignment)
    for value in order_domain_values(board, var, assignment):
        if value_is_consistent(value, assignment):
            new_assignment = add_assignment(assignment, var, value)
            result = recursive_brute_force(board, new_assignment)
            if result is not None:
                return result

    return None

if __name__ == "__main__":
    mode, filename = parse_arguments()
    sudoku_board = load_sudoku_board(filename)

    print("Last Name, First Name, AXXXXXXXX solution:")
    print(f"Input file: {filename}")
    print("Algorithm: ALGO_NAME")

    print("\nInput puzzle:")
    display_sudoku_board(sudoku_board)

    if mode == 1:
        # Brute Force Search
        start_time = time.time()
        solution = brute_force_search(sudoku_board)
        end_time = time.time()

        if solution is not None:
            print("\nSolved puzzle:")
            display_sudoku_board(solution)
            print(f"Number of search tree nodes generated: {0}")  # Not implemented
            print(f"Search time: {end_time - start_time} seconds")
    elif mode == 2:
        # Backtracking Search
        nodes_generated = [0]
        start_time = time.time()
        solution = recursive_brute_force(sudoku_board, {}, nodes_generated)
        end_time = time.time()

        if solution is not None:
            print("\nSolved puzzle:")
            display_sudoku_board(solution)
            print(f"Number of search tree nodes generated: {nodes_generated[0]}")
            print(f"Search time: {end_time - start_time} seconds")
    elif mode == 3:
        # MRV and Forward-Checking
        nodes_generated = [0]
        start_time = time.time()
        solution = mrv_and_forward_checking(sudoku_board, nodes_generated)
        end_time = time.time()

        if solution is not None:
            print("\nSolved puzzle:")
            display_sudoku_board(solution)
            print(f"Number of search tree nodes generated: {nodes_generated[0]}")
            print(f"Search time: {end_time - start_time} seconds")
    elif mode == 4:
        # Test Completed Puzzle
        test_completed_puzzle(sudoku_board)
    else:
        print("ERROR: Invalid mode.")
