import pygame

from src.game import game
from src.window import root


def main():
    game.run(root)


if __name__ == "__main__":
    while True:
        try:
            main()
        except IndexError:
            ...
