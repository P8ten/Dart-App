from text_interface import TextInterface


class Cricketeer(object):

    board = {}
    points = 0
    qp = 0

    def __init__(self, name):
        self.name = name
        self.reset_board()
        self.reset_stat()

    def get_board(self):
        return list(self.board.values())

    def get_value(self, mark):
        return self.board[mark]

    def mark_board(self, mark):
        self.board[mark] -= 1

    def get_points(self):
        return self.points

    def mark_points(self, mark):
        if mark == 'b':
            self.points += 25
        else:
            self.points += int(mark)

    def get_name(self):
        return self.name

    def player_qp(self):
        self.qp += 1

    def reset_board(self):
        self.board = {'b': 3, '15': 3, '16': 3, '17': 3, '18': 3, '19': 3, '20': 3}

    def reset_stat(self):
        self.qp = 0

    def mark_open(self, mark):
        if self.get_value(mark):
            return False
        else:
            return True


class CricketGame(object):

    """
        This program will facilitate keeping score for a round of cricket between 2-4 players.
        The score for each player should be entered in one line separated by commas.
        Non scoring darts can be entered or skipped.
        Doubles or Triples can be entered one at a time or with the point value followed by a x2 or x3
        e.g. If player one throws a triple 20, double 19, and a 14,
        the round can be entered as 20, 20, 20, 19, 19, 14 or could also be entered 20x3, 19x2
        Bulls should be entered as "B" or "b"
    """

    def __init__(self, interface):
        self.players = [''] * 2
        self.interface = interface

    def set_game_vars(self, names):
        for i in range(2):
            self.players[i] = Cricketeer(names[i])

        return self.players

    def throw_round(self, name):

        return self.interface.collect_throw(name)

    def score_round(self, players, darts, player):

        for dart in darts:
            if players[player].get_value(dart):
                players[player].mark_board(dart)
            elif players[player].mark_open(dart) and not players[player].get_value(dart):
                players[player].mark_points(dart)

    def game_over(self, player, players):

        if sum(players[player].get_board()) != 0:
            return False

        for n in range(len(players)):
            if players[n].get_points() > players[player].get_points():
                return False

        return True

    def play(self):

        # print_intro()  # intro and game instructions
        names = self.interface.get_game_inputs()  # players names
        players = self.set_game_vars(names)

        player = 0

        while True:
            darts = self.throw_round(players[player].get_name())
            self.score_round(players, darts, player)
            self.interface.print_board([players[0].get_board(), players[1].get_board()],
                                       [players[0].get_points(), players[1].get_points()])
            if self.game_over(player, players):
                break

            if player == 0:
                player += 1
            else:
                player = 0


def main():
    inter = TextInterface()
    g = CricketGame(inter)
    g.play()


if __name__ == '__main__':
    main()