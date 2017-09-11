#####################################################################
# Dart app used to keep track of a game of darts
#####################################################################

from text_interface import TextInterface


class DartApp(object):

    def __int__(self, interface):
        self.interface = interface
        self.game = self.interface.get_game()  # returns selected game class

    def run(self):

        self.interface.print_intro()  # intro and game instructions
        n = self.interface.number_of_players()

        players = self.game.set_game_vars(n)

        player = 0

        while True:
            darts = throw_round(players[player].get_name())
            score_round(players, darts, player)
            if game_over(player, players):
                break
            player = next_player(player, n)
        self.interface.close()





def main():

    inter = TextInterface()

    g = DartApp(inter)

    g.run()
    
if __name__ == '__main__':
    main()

    