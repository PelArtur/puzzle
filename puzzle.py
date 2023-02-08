def validate_board(board):
    '''board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]'''
    flag = [f'{x}' for x in range(1, 10)]
    flag2 = [f'{x}' for x in range(1, 10)]
    for i in range(9):
        for j in range(9):
            if board[i][j] in flag:
                flag.remove(board[i][j])
            elif board[i][j] != '*' and board[i][j] != ' ':
                return False
            if board[j][i] in flag2:
                flag2.remove(board[j][i])
            elif board[j][i] != '*' and board[j][i] != ' ':
                return False
        flag = [f"{x}" for x in range(1, 10)]
        flag2 = [f"{x}" for x in range(1, 10)]
    return True



print(validate_board(board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   2  **",
 "  8  2***",
 "  2  ****"
]))