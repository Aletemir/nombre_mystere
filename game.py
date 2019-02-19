import random
from player import Player
import sqlite3


class Game:
    def __init__(self):
        self.number = 0
        self.score = 0
        self.round = 0
        self.player = Player()


    def random_number(self):
        range_min = int(input('Enter min range : \n'))
        range_max = int(input('Enter max range : \n'))
        self.number = random.randint(range_min, range_max)
        print('you choose to begin at {0} and to stop at {1}'.format(range_min, range_max))

    def play(self):
        self.player.enter_name()
        self.player.set_lives()
        self.random_number()
        while self.player.player_number != self.number and self.player.lives > 0:
            self.player.set_player_number()
            if self.player.player_number > self.number:
                print('Oops, not that, it\'s to high.')
                self.player.lives -= 1
                self.round += 1
            elif self.player.player_number < self.number:
                print('Arf, not enough.')
                self.player.lives -= 1
                self.round += 1
            else:
                print('Wouhou ! You find it {2}. You still have {0} and you got the number in {1} round'
                      .format(self.player.lives, self.round, self.player.username))
                self.score += 1
        if self.player.lives == 0:
            print('Game over')

    def save_score(self):
        try:
            cx = sqlite3.connect('mystery_number.db3')
            cur = cx.cursor()

            cur.execute("CREATE TABLE if not exists players (rowid integer primary key, name text, score integer)")

            cur.execute("insert into players (name, score) values (?,?)",
                        (self.player.username, self.round))

            cx.commit()

            print('Top 3 des joueurs :')
            cur.execute("select name, score from players order by score desc limit 3")
            for row in cur:
                print(row[0], row[1])
        except Exception as e:

            print(e)


if __name__ == '__main__':
    game = Game()
    game.play()
