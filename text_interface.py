

class TextInterface(object):

    """Text interface for testing CricketGame"""

    def collect_throw(self, name):

        legal = ['15', '16', '17', '18', '19', '20', 'b']

        darts = [roundInput.strip() for roundInput in
                 input("Enter round for {:10} ".format(name + ':')).lower().split(',')]

        round_full = []

        for dart in darts:
            if 'x' in dart:
                multi = dart.split('x')
                [round_full.append(multi[0]) for _ in range(int(multi[1]))]
            else:
                round_full.append(dart)

        return [x for x in round_full if x in legal]

    def get_game_inputs(self):

        names = [''] * 2

        for i in range(2):
            names[i] = input('Name of player {}: '.format(i + 1))
            if names[i] == '':
                names[i] = 'Player{}'.format(i + 1)

        return names

    def print_board(self, players, points):
        """ Receive copy of players.getboard list as players and list of
            each players points as points"""

        symbol = {0: 'O', 1: 'X', 2: '/', 3: ' '}
        target = ['20', '19', '18', '17', '16', '15', 'B']

        print()
        print('{}\t\t\t\t{}'.format(points[0], points[1]))

        for i in range(7):
            print('\t{}\t{}\t{}'.format(
                symbol[players[0][6-i]], target[i], symbol[players[1][6-i]]))

        print()

