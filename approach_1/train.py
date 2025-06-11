from env import *
from hangman_agent import *
from config import *

def main():

    config = Config("./config.yaml")
    env = HangmanEnv()
    player = HangmanPlayer(env, config)


    player.fit()


if __name__ == '__main__':
    main()
