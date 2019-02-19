class Player:
    def __init__(self):
        self.username = ""
        self.lives = 0
        self.player_number = 0

    def enter_name(self):
        self.username = input('Please enter your username : \n')
        print('Thanks you {0}, next step,'.format(self.username))

    def set_lives(self):
        self.lives = int(input('Please, set your lives number : \n'))
        if self.lives > 5:
            print('Awww, a little baby boy. Ready to set the game ? \n')
        else:
            print('Ouch ! You like challenge, i see. Ready to set the game ? \n')

    def set_player_number(self):
        self.player_number = int(input('Try to catch the random number :\n'))



# if __name__ == '__main