# TAI content
def c_peg ():
 return "O"
def c_empty ():
 return "_"
def c_blocked ():
 return "X"
def is_empty (e):
 return e == c_empty()
def is_peg (e):
 return e == c_peg()
def is_blocked (e):
 return e == c_blocked() 

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
 return (l, c)
def pos_l (pos):
 return pos[0]
def pos_c (pos):
 return pos[1] 

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
 return [i, f]
def move_initial (move):
 return move[0]
def move_final (move):
 return move[1] 

""" funcao auxiliar. pega nas linhas e colunas e forma tuplos. coloca-os na lista"""
def create_possible_move(line_current,column_current,line_possible,column_possible):
    current = make_pos(line_current,column_current)
    possible = make_pos(line_possible,column_possible)
    lst = []
    lst.append(current)
    lst.append(possible)
    return lst
b1 = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]] 
def board_moves(board):
    line_len = len(board[0]) #tamanho de uma linha
    res = []
    l = 0
    c = 0
    
    while l < line_len:
        while c < line_len:
            if(is_peg(board[l][c])):
                if (l > 1): #limite superior do tabuleiro
                    if (is_empty(board[l-2][c])):
                        res.append(create_possible_move( l, c, l-2, c))
                if (l < line_len - 2 ): #limite inferior tabuleiro
                    if (is_empty(board[l+2][c])):
                        res.append(create_possible_move( l, c, l+2, c))
                if (c > 1): #limite da esquerda do tabuleiro
                    if (is_empty(board[l][c-2])):
                        res.append(create_possible_move(l,c,l,c-2))
                if (c < line_len - 2): #limite da direita do tabuleiro
                    if (is_empty(board[l][c+2])):
                        res.append(create_possible_move(l, c, l, c+2))
            c = c + 1
        l = l + 1
    print res
    return res

board_moves(b1)

def board_perform_move(board,move):
    res = board
    res[pos_l(move_initial(move))][pos_c(move_initial(move))] = c_empty()
    res[pos_l(move_final(move))][pos_c(move_final(move))] = c_peg()
    print res
    return res

board_perform_move(b1,[(0,2),(0,0)])