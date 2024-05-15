from termcolor import colored, cprint
import numpy as np

board = [
    # . 1 2 3 4 5 6 7 8 9 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # C
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # E
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # G
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # H
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # J
]

board_dict = {
    "A1": (0, 0),
    "A2": (0, 1),
    "A3": (0, 2),
    "A4": (0, 3),
    "A5": (0, 4),
    "A6": (0, 5),
    "A7": (0, 6),
    "A8": (0, 7),
    "A9": (0, 8),
    "A10": (0, 9),
    "B1": (1, 0),
    "B2": (1, 1),
    "B3": (1, 2),
    "B4": (1, 3),
    "B5": (1, 4),
    "B6": (1, 5),
    "B7": (1, 6),
    "B8": (1, 7),
    "B9": (1, 8),
    "B10": (1, 9),
    "C1": (2, 0),
    "C2": (2, 1),
    "C3": (2, 2),
    "C4": (2, 3),
    "C5": (2, 4),
    "C6": (2, 5),
    "C7": (2, 6),
    "C8": (2, 7),
    "C9": (2, 8),
    "C10": (2, 9),
    "D1": (3, 0),
    "D2": (3, 1),
    "D3": (3, 2),
    "D4": (3, 3),
    "D5": (3, 4),
    "D6": (3, 5),
    "D7": (3, 6),
    "D8": (3, 7),
    "D9": (3, 8),
    "D10": (3, 9),
    "E1": (4, 0),
    "E2": (4, 1),
    "E3": (4, 2),
    "E4": (4, 3),
    "E5": (4, 4),
    "E6": (4, 5),
    "E7": (4, 6),
    "E8": (4, 7),
    "E9": (4, 8),
    "E10": (4, 9),
    "F1": (5, 0),
    "F2": (5, 1),
    "F3": (5, 2),
    "F4": (5, 3),
    "F5": (5, 4),
    "F6": (5, 5),
    "F7": (5, 6),
    "F8": (5, 7),
    "F9": (5, 8),
    "F10": (5, 9),
    "G1": (6, 0),
    "G2": (6, 1),
    "G3": (6, 2),
    "G4": (6, 3),
    "G5": (6, 4),
    "G6": (6, 5),
    "G7": (6, 6),
    "G8": (6, 7),
    "G9": (6, 8),
    "G10": (6, 9),
    "H1": (7, 0),
    "H2": (7, 1),
    "H3": (7, 2),
    "H4": (7, 3),
    "H5": (7, 4),
    "H6": (7, 5),
    "H7": (7, 6),
    "H8": (7, 7),
    "H9": (7, 8),
    "H10": (7, 9),
    "I1": (8, 0),
    "I2": (8, 1),
    "I3": (8, 2),
    "I4": (8, 3),
    "I5": (8, 4),
    "I6": (8, 5),
    "I7": (8, 6),
    "I8": (8, 7),
    "I9": (8, 8),
    "I10": (8, 9),
    "J1": (9, 0),
    "J2": (9, 1),
    "J3": (9, 2),
    "J4": (9, 3),
    "J5": (9, 4),
    "J6": (9, 5),
    "J7": (9, 6),
    "J8": (9, 7),
    "J9": (9, 8),
    "J10": (9, 9),
}

#                        offense_view , user_input which will look like A1
def coordinate_translator(coordinate):
    j, i = board_dict[coordinate]
    return [j, i]

def array_translator(array):
    for key in board_dict:
        if np.array_equal(board_dict[key], array):
            return key

def printBoard(header, border, board, footer):
    print(header, end="")
    print(border, end="")
    colored_board = ""
    board_array = board.split("\n")
    for i, line in enumerate(board_array):
        if "||" in line:  # Check if || is in the line
            row_label, board_content = line.split("||", 1)
            colored_board += row_label + "||"
            for char in board_content:
                if char in ["X", "#", "!", "0", "D", "F", "G", "H", "I", "J", "C", "B", "P", "S"]:
                    # Add color to char and append it to colored_board
                    if char == "D" or char == "C" or char == "B" or char == "P" or char == "S":
                        colored_board += colored(char, "red")
                    if char == "X":
                        colored_board += colored(char, "white")
                    elif char == "#":
                        colored_board += colored(char, "yellow")
                    elif char == "!":
                        colored_board += colored(
                            char, "red", attrs=["concealed"], on_color="on_light_red"
                        )
                    elif char == "0":
                        colored_board += colored(char, "blue", "on_blue")
                else:
                    colored_board += char
            if i != len(board_array) - 1:  # If the current line is not the last line
                colored_board += "\n"
        else:
            colored_board += line
            if i != len(board_array) - 1:  # If the current line is not the last line
                colored_board += "\n"
    print(colored_board, end="")
    print(footer, end="")

def is_index_in_range(array, row_index, col_index):
    return 0 <= row_index < len(array) and 0 <= col_index < len(array[0])

def view_render(array):
    string1 = """
    |                         ||  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10                              |"""
    string2= """
    | ________________________________________________________________________________________________________________  |
    |                                                                                                                   |"""

    string3= """
    |                       A ||  {a1}  |  {a2}  |  {a3}  |  {a4}  |  {a5}  |  {a6}  |  {a7}  |  {a8}  |  {a9}  |  {a10}  ||                           |
    |                       B ||  {b1}  |  {b2}  |  {b3}  |  {b4}  |  {b5}  |  {b6}  |  {b7}  |  {b8}  |  {b9}  |  {b10}  ||                           |
    |                       C ||  {c1}  |  {c2}  |  {c3}  |  {c4}  |  {c5}  |  {c6}  |  {c7}  |  {c8}  |  {c9}  |  {c10}  ||                           |
    |                       D ||  {d1}  |  {d2}  |  {d3}  |  {d4}  |  {d5}  |  {d6}  |  {d7}  |  {d8}  |  {d9}  |  {d10}  ||                           |
    |                       E ||  {e1}  |  {e2}  |  {e3}  |  {e4}  |  {e5}  |  {e6}  |  {e7}  |  {e8}  |  {e9}  |  {e10}  ||                           |
    |                       F ||  {f1}  |  {f2}  |  {f3}  |  {f4}  |  {f5}  |  {f6}  |  {f7}  |  {f8}  |  {f9}  |  {f10}  ||                           |
    |                       G ||  {g1}  |  {g2}  |  {g3}  |  {g4}  |  {g5}  |  {g6}  |  {g7}  |  {g8}  |  {g9}  |  {g10}  ||                           |
    |                       H ||  {h1}  |  {h2}  |  {h3}  |  {h4}  |  {h5}  |  {h6}  |  {h7}  |  {h8}  |  {h9}  |  {h10}  ||                           |
    |                       I ||  {i1}  |  {i2}  |  {i3}  |  {i4}  |  {i5}  |  {i6}  |  {i7}  |  {i8}  |  {i9}  |  {i10}  ||                           |
    |                       J ||  {j1}  |  {j2}  |  {j3}  |  {j4}  |  {j5}  |  {j6}  |  {j7}  |  {j8}  |  {j9}  |  {j10}  ||                           |""".format(
        a1 = array[0][0],
        a2 = array[0][1],
        a3 = array[0][2],
        a4 = array[0][3],
        a5 = array[0][4],
        a6 = array[0][5],
        a7 = array[0][6],
        a8 = array[0][7],
        a9 = array[0][8],
        a10 = array[0][9],
        b1 = array[1][0],
        b2 = array[1][1],
        b3 = array[1][2],
        b4 = array[1][3],
        b5 = array[1][4],
        b6 = array[1][5],
        b7 = array[1][6],
        b8 = array[1][7],
        b9 = array[1][8],
        b10 = array[1][9],
        c1 = array[2][0],
        c2 = array[2][1],
        c3 = array[2][2],
        c4 = array[2][3],
        c5 = array[2][4],
        c6 = array[2][5],
        c7 = array[2][6],
        c8 = array[2][7],
        c9 = array[2][8],
        c10 = array[2][9],
        d1 = array[3][0],
        d2 = array[3][1],
        d3 = array[3][2],
        d4 = array[3][3],
        d5 = array[3][4],
        d6 = array[3][5],
        d7 = array[3][6],
        d8 = array[3][7],
        d9 = array[3][8],
        d10 = array[3][9],
        e1 = array[4][0],
        e2 = array[4][1],
        e3 = array[4][2],
        e4 = array[4][3],
        e5 = array[4][4],
        e6 = array[4][5],
        e7 = array[4][6],
        e8 = array[4][7],
        e9 = array[4][8],
        e10 = array[4][9],
        f1 = array[5][0],
        f2 = array[5][1],
        f3 = array[5][2],
        f4 = array[5][3],
        f5 = array[5][4],
        f6 = array[5][5],
        f7 = array[5][6],
        f8 = array[5][7],
        f9 = array[5][8],
        f10 = array[5][9],
        g1 = array[6][0],
        g2 = array[6][1],
        g3 = array[6][2],
        g4 = array[6][3],
        g5 = array[6][4],
        g6 = array[6][5],
        g7 = array[6][6],
        g8 = array[6][7],
        g9 = array[6][8],
        g10 = array[6][9],
        h1 = array[7][0],
        h2 = array[7][1],
        h3 = array[7][2],
        h4 = array[7][3],
        h5 = array[7][4],
        h6 = array[7][5],
        h7 = array[7][6],
        h8 = array[7][7],
        h9 = array[7][8],
        h10 = array[7][9],
        i1 = array[8][0],
        i2 = array[8][1],
        i3 = array[8][2],
        i4 = array[8][3],
        i5 = array[8][4],
        i6 = array[8][5],
        i7 = array[8][6],
        i8 = array[8][7],
        i9 = array[8][8],
        i10 = array[8][9],
        j1 = array[9][0],
        j2 = array[9][1],
        j3 = array[9][2],
        j4 = array[9][3],
        j5 = array[9][4],
        j6 = array[9][5],
        j7 = array[9][6],
        j8 = array[9][7],
        j9 = array[9][8],
        j10 = array[9][9],
    )
    string4 = """
    |___________________________________________________________________________________________________________________|"""
    printBoard(string1, string2, string3, string4)
