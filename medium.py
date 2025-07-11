import numpy as np
import random
import pygame
import sys
import math

#RGB value
BLUE = (0,131, 184)  
BLACK = (0,0,0)
RED = (255, 22, 44)
YELLOW= (254, 211, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


PLAYER = 0 
AI =1 

PLAYER_PIECE = 1
AI_PIECE = 2
EMPTY = 0

WINDOW_LENGTH = 4

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row] [col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1] [col] == 0

def get_next_open_row(board, col):
    for r in range (ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):#check horizontal location for win 
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board [r] [c+1] == piece and board [r][c+2] == piece and board [r][c+3] == piece:
                return True
            
    #check vertical location for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board [r+1] [c] == piece and board [r+2][c] == piece and board [r+3][c] == piece:
                return True
            
    #check positively sloped diagonals
    for c in range(COLUMN_COUNT -3 ):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board [r+1] [c+1] == piece and board [r+2][c+2] == piece and board [r+3][c+3] == piece:
                return True

    #Check negatively sloped diagonals
    for c in range(COLUMN_COUNT -3 ):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board [r-1] [c+1] == piece and board [r-2][c+2] == piece and board [r-3][c+3] == piece:
                return True

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE
        
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5
        
    if window.count(piece) == 3 and window.count(EMPTY) == 1:
        score -= 8
             
    return score 
   
 #Score Position
def score_position(board, piece):
    score = 0
    #Horizontal
    for r in range (ROW_COUNT):
        row_array =[int(i) for i in list(board[r, :])]
        
        for c in range(COLUMN_COUNT -3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)
                
                
    ## Score vertical
    for c in range (COLUMN_COUNT):
        col_array = [int(i) for i in  list (board[:,c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r +WINDOW_LENGTH]
            score += evaluate_window(window, piece)
                

    ##Score +ve slope diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3 ):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)
                
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)
            
    return score

def get_valid_locations(board):
    valid_location = []
    for col in range (COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_location.append(col)
    return valid_location

#pick best move
def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = 0
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
            
    return best_col
            
    


    
 #draw board     
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE,(c* SQUARESIZE, r* SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+ SQUARESIZE/2), int(r* SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] ==PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+ SQUARESIZE/2), height - int(r* SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] ==AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+ SQUARESIZE/2), height - int(r* SQUARESIZE+SQUARESIZE/2)), RADIUS)      
    pygame.display.update()         
                

board = create_board()
print_board(board)
game_over= False

pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT *SQUARESIZE
height =(ROW_COUNT +1 ) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE/2 -5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


myfont = pygame.font.SysFont("serif", 63)    #Font

turn = random.randint(PLAYER, AI)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            posx = event.pos[0]
            if turn ==PLAYER:
                pygame.draw.circle(screen, RED,(posx, int(SQUARESIZE/2)), RADIUS)
            
        pygame.display.update()
            
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0,width, SQUARESIZE))
            #print(event.pos)
            #Ask for player 1 Input
            if turn == PLAYER:
                posx= event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)
                    
                    if winning_move(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 Wins!Congrats!!!", 1, RED)
                        screen.blit(label,(40,10)) #update that specific part of screen
                        game_over = True
                        
                    turn +=1
                    turn = turn %2
                    print_board(board)
                    draw_board(board)

    #Ask for player  2 input
    if turn == AI and not game_over:
        #col = random.randint(0, COLUMN_COUNT - 1)
        col = pick_best_move(board, AI_PIECE)
                
        if is_valid_location(board, col):
            pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)
                
            if winning_move(board, AI_PIECE):
                label = myfont.render("Game Over! Better Luck:)", 1, YELLOW)
                screen.blit(label,(40,10)) #update that specific part of screen
                game_over = True

            print_board(board)
            draw_board(board)
            
            turn +=1
            turn = turn %2
            
    if game_over:pygame.time.wait(3000) #3 second delay