import pygame
from pygame.locals import *


class Piece:
    def __init__(self, piece_color, piece_position):
        self.has_moved = False
        self.piece_color = piece_color
        self.direction = 1 if self.piece_color == 'light_white_square' else -1
        self.piece_position = piece_position
        self.color_of_opponents_pieces = 'dark_black_square' if self.piece_color == 'light_white_square' else 'light_white_square'

    def is_opponent(self, piece):
        return piece.piece_color == self.color_of_opponents_pieces

    def diagonal_moves(self, board):
        moves = []
        curr_pos = self.piece_position[0] + 1, self.piece_position[1] + 1
        while curr_pos[1] <= 7 and curr_pos[0] <= 7:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0] + 1, curr_pos[1] + 1

        curr_pos = self.piece_position[0] + 1, self.piece_position[1] - 1
        while curr_pos[1] >= 0 and curr_pos[0] <= 7:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0] + 1, curr_pos[1] - 1

        curr_pos = self.piece_position[0] - 1, self.piece_position[1] + 1
        while curr_pos[0] >= 0 and curr_pos[1] <= 7:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0] - 1, curr_pos[1] + 1

        curr_pos = self.piece_position[0] - 1, self.piece_position[1] - 1
        while curr_pos[1] >= 0 and curr_pos[0] >= 0:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0] - 1, curr_pos[1] - 1

        return moves

    def line_moves(self, board):
        moves = []
        curr_pos = self.piece_position[0], self.piece_position[1] + 1
        while curr_pos[1] <= 7:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0], curr_pos[1] + 1

        curr_pos = self.piece_position[0], self.piece_position[1] - 1
        while curr_pos[1] >= 0:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0], curr_pos[1] - 1

        curr_pos = self.piece_position[0] + 1, self.piece_position[1]
        while curr_pos[0] <= 7:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0] + 1, curr_pos[1]

        curr_pos = self.piece_position[0] - 1, self.piece_position[1]
        while curr_pos[0] >= 0:
            piece = board[curr_pos[0]][curr_pos[1]]
            if not piece:
                moves.append(curr_pos)
            elif self.is_opponent(piece):
                moves.append(curr_pos)
                break
            else:
                break

            curr_pos = curr_pos[0] - 1, curr_pos[1]

        return moves

    def pieces_move(self, piece_move):
        self.piece_position = piece_move

    def is_it_possible_to_move_piece(self, move, board):
        return move in self.moves(board)

    def moves(self, board):
        return []


class PieceBishop(Piece):
    def __init__(self, piece_color, piece_position):
        self.name = 'Bishop'
        super(PieceBishop, self).__init__(piece_color, piece_position)
        if self.piece_color == 'light_white_square':
            self.image = 'images/white_bishop.png'
        else:
            self.image = 'images/black_bishop.png'

    def moves(self, board):
        return self.diagonal_moves(board)


class PieceKing(Piece):
    def __init__(self, piece_color, piece_position):
        self.name = 'King'
        super(PieceKing, self).__init__(piece_color, piece_position)
        if self.piece_color == 'light_white_square':
            self.image = 'images/white_king.png'
        else:
            self.image = 'images/black_king.png'

    def moves(self, board):
        moves = []
        for i in range(-1, 2):
            for e in range(-1, 2):
                space = self.piece_position[0] + e, self.piece_position[1] + i
                if space[0] < 0 or space[0] > 7 or space[1] < 0 or space[1] > 7:
                    continue
                piece = board[space[0]][space[1]]
                if not piece or self.is_opponent(piece):
                    moves.append(space)

        return moves

    def is_opponent(self, piece):
        return piece.piece_color == self.color_of_opponents_pieces


class PieceKnight(Piece):
    def __init__(self, piece_color, piece_position):
        self.name = 'Knight'
        super(PieceKnight, self).__init__(piece_color, piece_position)
        if self.piece_color == 'light_white_square':
            self.image = 'images/white_knight.png'
        else:
            self.image = 'images/black_knight.png'

    def moves(self, board):
        poss_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        moves = []
        for move in poss_moves:
            pos = self.piece_position[0] + move[0], self.piece_position[1] + move[1]
            if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
                continue
            piece = board[pos[0]][pos[1]]
            if not piece or self.is_opponent(piece):
                moves.append(pos)
        return moves


class PieceRook(Piece):
    def __init__(self, piece_color, piece_position):
        self.name = 'Rook'
        super(PieceRook, self).__init__(piece_color, piece_position)
        if self.piece_color == 'light_white_square':
            self.image = 'images/white_rook.png'
        else:
            self.image = 'images/black_rook.png'

    def moves(self, board):
        return self.line_moves(board)


class PiecePawn(Piece):
    def __init__(self, piece_color, piece_position):
        self.name = 'Pawn'
        super(PiecePawn, self).__init__(piece_color, piece_position)
        if self.piece_color == 'light_white_square':
            self.image = 'images/white_pawn.png'
        else:
            self.image = 'images/black_pawn.png'

    def moves(self, board):
        moves = []

        if not self.is_piece_in_front(board):
            moves.append((self.piece_position[0], self.piece_position[1] + self.direction))

            if (not self.has_moved) and (
                    not board[self.piece_position[0]][self.piece_position[1] + 2 * self.direction]):
                moves.append((self.piece_position[0], self.piece_position[1] + 2 * self.direction))

        if self.piece_position[0] < 7:
            right_diagonal = board[self.piece_position[0] + 1][self.piece_position[1] + self.direction]
            if right_diagonal and self.is_opponent(right_diagonal):
                moves.append(right_diagonal.piece_position)

        if self.piece_position[0] > 0:
            left_diagonal = board[self.piece_position[0] - 1][self.piece_position[1] + self.direction]
            if left_diagonal and self.is_opponent(left_diagonal):
                moves.append(left_diagonal.piece_position)

        return moves

    def is_piece_in_front(self, board):
        return board[self.piece_position[0]][self.piece_position[1] + self.direction]

    def is_opponent_piece_diagonal(self, board, left_side):
        side = -1 if left_side else 1
        return board[self.piece_position[0] + side][
            self.piece_position[1] + self.direction].piece_color == self.color_of_opponents_pieces


class PieceQueen(Piece):

    def __init__(self, piece_color, piece_position):
        self.name = 'Queen'
        super(PieceQueen, self).__init__(piece_color, piece_position)
        if self.piece_color == 'light_white_square':
            self.image = 'images/white_queen.png'
        else:
            self.image = 'images/black_queen.png'

    def moves(self, board):
        return self.line_moves(board) + self.diagonal_moves(board)


class ChessBoard:
    def __init__(self):
        self.curr_player = 'light_white_square'
        self.board = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            self.board[i][1] = PiecePawn('light_white_square', (i, 1))
            self.board[i][6] = PiecePawn('dark_black_square', (i, 6))

        self.board[6][0] = PieceKnight('light_white_square', (6, 0))
        self.board[4][7] = PieceKing('dark_black_square', (4, 7))
        self.board[0][0] = PieceRook('light_white_square', (0, 0))
        self.board[2][7] = PieceBishop('dark_black_square', (2, 7))
        self.board[3][0] = PieceQueen('light_white_square', (3, 0))
        self.board[7][7] = PieceRook('dark_black_square', (7, 7))
        self.board[4][0] = PieceKing('light_white_square', (4, 0))
        self.board[5][0] = PieceBishop('light_white_square', (5, 0))
        self.board[6][7] = PieceKnight('dark_black_square', (6, 7))
        self.board[1][0] = PieceKnight('light_white_square', (1, 0))
        self.board[3][7] = PieceQueen('dark_black_square', (3, 7))
        self.board[7][0] = PieceRook('light_white_square', (7, 0))
        self.board[0][7] = PieceRook('dark_black_square', (0, 7))
        self.board[1][7] = PieceKnight('dark_black_square', (1, 7))
        self.board[2][0] = PieceBishop('light_white_square', (2, 0))
        self.board[5][7] = PieceBishop('dark_black_square', (5, 7))

    def pieces_of_chess_enjoyer(self):
        pieces = []
        for piece in self.get_all_pieces():
            if piece.piece_color == self.curr_player:
                pieces.append(piece)
        return pieces

    def moves(self, piece):
        if piece.name != 'King':
            return piece.moves(self.board)
        else:
            return piece.moves(self.board) + self.moving_castle_piece_moves()

    def position_of_current_piece(self, space):
        return self.board[space[0]][space[1]]

    def players_pieses_type_list(self, piece_name, player):
        pieces = []
        for row in self.board:
            for space in row:
                if space and space.name == piece_name and space.piece_color == player:
                    pieces.append(space)
        return pieces

    def piece_move(self, piece, new_position):
        pos = piece.piece_position
        piece.pieces_move(new_position)
        self.board[new_position[0]][new_position[1]] = piece
        self.board[pos[0]][pos[1]] = None
        if not piece.has_moved:
            piece.has_moved = True

    def extra_move(self, piece, new_position):
        pos = piece.piece_position
        piece.pieces_move(new_position)
        self.board[new_position[0]][new_position[1]] = piece
        self.board[pos[0]][pos[1]] = None

    def moving_castle_piece_moves(self):
        castles = []
        king = self.players_pieses_type_list('King', self.curr_player)[0]
        y = 0 if self.curr_player == 'light_white_square' else 7
        b = self.board
        if b[0][y] and not b[0][y].has_moved and b[4][y] and not b[4][y].has_moved:
            if all(not b[x][y] for x in range(1, 4)):
                    castles.append((2, y))

        if b[7][y] and not b[7][y].has_moved and b[4][y] and not b[4][y].has_moved:
            if all(not b[x][y] for x in range(5, 7)):
                    castles.append((6, y))

        for move in castles:
            self.extra_moves_of_king(king, move)
            castles.remove(move)
            self.undo_extra_moves_of_king(king)

        return castles

    def king_of_chess(self, king, new_king_position):
        corresponding_rook = {(2, 0): (1, 0), (6, 0): (7, 0), (2, 7): (1, 7), (6, 7): (7, 7)}
        corresponding_rook_move = {(2, 0): (3, 0), (6, 0): (5, 0), (2, 7): (3, 7), (6, 7): (5, 7)}
        rook_pos = corresponding_rook[new_king_position]
        rook = self.board[rook_pos[0]][rook_pos[1]]
        self.piece_move(king, new_king_position)
        self.piece_move(rook, corresponding_rook_move[new_king_position])

    def extra_moves_of_king(self, king, new_king_position):

        corresponding_rook = {(2, 0): (1, 0), (6, 0): (7, 0), (2, 7): (1, 7), (6, 7): (7, 7)}
        corresponding_rook_move = {(2, 0): (3, 0), (6, 0): (5, 0), (2, 7): (3, 7), (6, 7): (5, 7)}
        rook_pos = corresponding_rook[new_king_position]
        rook = self.board[rook_pos[0]][rook_pos[1]]
        self.extra_move(king, new_king_position)
        self.extra_move(rook, corresponding_rook_move[new_king_position])

    def undo_extra_moves_of_king(self, king):
        corresponding_rook = {(2, 0): (3, 0), (6, 0): (5, 0), (2, 7): (3, 7), (6, 7): (5, 7)}
        corresponding_rook_move = {(2, 0): (0, 0), (6, 0): (7, 0), (2, 7): (0, 7), (6, 7): (7, 7)}
        rook_pos = corresponding_rook[king.piece_position]
        rook = self.board[rook_pos[0]][rook_pos[1]]
        self.extra_move(rook, corresponding_rook_move[king.piece_position])
        self.extra_move(king, (4, king.piece_position[1]))


    def is_curr_player_in_check(self, piece, moves):
        king = self.players_pieses_type_list('King', self.curr_player)[0]
        b = self.board
        piece_original_pos = piece.piece_position

        poss_moves = []

        for move in moves:
            piece_at_move_pos = self.board[move[0]][move[1]]
            self.extra_move(piece, move)

            poss_moves.append(move)

            self.extra_move(piece, piece_original_pos)
            self.board[move[0]][move[1]] = piece_at_move_pos

        return poss_moves

    def get_all_pieces(self):
        pieces = []
        for x in range(8):
            for y in range(8):
                if self.board[x][y]:
                    pieces.append(self.board[x][y])
        return pieces


def x_y_coordinates(position):
    return position[0] * 75 + 200, (7 - position[1]) * 75


def x_y_space_position(x, y):
    return (x - 200) // 75, 7 - y // 75


class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((1000, 650))
        pygame.display.set_caption('Chess')

        self.settings = {'board_image': 'images/board.png'}
        self.board_image = pygame.image.load(self.settings['board_image'])

        self.chess_board = ChessBoard()

        self.choosen_piece = None
        self.moves_of_player = []
        self.every_possible_moves = self.all_moves_possible()

        self.start_gaming()

    def start_gaming(self):
        while True:
            self.window_of_game_draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_clicks()

    def change_current_player(self):
        if self.chess_board.curr_player != 'dark_black_square':
            self.chess_board.curr_player = 'dark_black_square'
        else:
            self.chess_board.curr_player = 'light_white_square'

    def deselect_piece(self):
        self.choosen_piece = None
        self.moves_of_player = None

    def handle_mouse_clicks(self):
        x, y = pygame.mouse.get_pos()
        if y > 600:
            pass
        elif x < 200:
            pass
        elif x > 800:
            pass
        else:
            selected_space = x_y_space_position(x, y)
            if not self.choosen_piece:

                if self.is_piece_of_current_player(selected_space):
                    self.select_piece(selected_space)

            else:
                if selected_space == self.choosen_piece.piece_position:
                    self.deselect_piece()

                elif selected_space in self.moves_of_player:
                    if self.choosen_piece.name == 'King' and selected_space in self.chess_board.moving_castle_piece_moves():
                        self.chess_board.king_of_chess(self.choosen_piece, selected_space)

                    else:
                        self.move_piece(self.choosen_piece, selected_space)
                        if self.choosen_piece.name == 'Pawn' and selected_space[1] == 0 or selected_space[1] == 7:
                            self.chess_board.board[selected_space[0]][selected_space[1]] = None
                            self.chess_board.board[selected_space[0]][selected_space[1]] = PieceQueen(
                                self.chess_board.curr_player, selected_space)

                    self.deselect_piece()
                    self.change_current_player()

                    self.every_possible_moves = self.all_moves_possible()


                elif selected_space in [piece.position for piece in self.chess_board.pieces_of_chess_enjoyer()]:
                    self.select_piece(selected_space)

                else:
                    self.deselect_piece()

    def draw_chess_board(self):
        self.game_display.blit(self.board_image, (200, 0))

        for piece in self.chess_board.get_all_pieces():
            image_position = piece.piece_position
            image_position = 200 + image_position[0] * 75, (7 - image_position[1]) * 75
            piece_image = pygame.image.load(piece.image)
            self.game_display.blit(piece_image, image_position)

        if self.choosen_piece:
            box_x, box_y = x_y_coordinates(self.choosen_piece.piece_position)
            pygame.draw.rect(self.game_display, blue, Rect((box_x, box_y), (75, 75)), 5)
            for move in self.moves_of_player:
                box1_x, box1_y = x_y_coordinates(move)
                pygame.draw.rect(self.game_display, red, Rect((box1_x, box1_y), (75, 75)), 5)

    def is_piece_of_current_player(self, space):
        for piece in self.chess_board.pieces_of_chess_enjoyer():
            if space == piece.piece_position:
                return True

    def window_of_game_draw(self):
        self.game_display.fill(white)
        self.draw_chess_board()
        pygame.display.update()

    def all_moves_possible(self):
        moves = {}
        pieces = self.chess_board.pieces_of_chess_enjoyer()
        for piece in pieces:
            p_moves = self.chess_board.moves(piece)
            moves[piece.piece_position] = self.chess_board.is_curr_player_in_check(piece, p_moves)
        return moves

    def moves_of_current_all_possibilities(self):
        return self.every_possible_moves[self.choosen_piece.piece_position]

    def select_piece(self, new_space):
        self.choosen_piece = self.chess_board.position_of_current_piece(new_space)
        self.moves_of_player = self.moves_of_current_all_possibilities()

    def move_piece(self, piece, new_position):
        self.chess_board.piece_move(piece, new_position)


if __name__ == '__main__':
    black = (0, 0, 0)
    blue = (34, 0, 255)
    white = (255, 255, 255)
    red = (209, 9, 9)
    Game()
