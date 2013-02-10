import sys

def count_clears(board, c):
    cc = c*5
    ret = 0
    for i in range(len(board)):
        ret += cc == board[i:][:5]
        ret += cc == board[i::21][:5]
        ret += cc == board[i::20][:5]
        ret += cc == board[i::19][:5]
    return ret

def check_last(board, c):
    for i in range(len(board)):
        ba = bytearray(board)
        ba[i] = b'.'
        if not count_clears(ba, c):
            return True
    return False

def check():
    YES = 'YES'
    NO = 'NO'
    board = ','.join([sys.stdin.readline().strip() for _ in range(19)])

    no = board.count('o')
    nx = board.count('x')
    nd = no - nx
    if not (0 <= nd <= 1):
        return NO

    last, before = 'ox' if nd == 1 else 'xo'
    if count_clears(board, before):
        return NO
    if not count_clears(board, last):
        return YES
    if check_last(board, last):
        return YES
    return NO

print check()
