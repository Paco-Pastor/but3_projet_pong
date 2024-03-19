import threading
import time

from unittest import TestCase, mock, main
from src import game
import threading
import time



class TestGame(TestCase):

    @mock.patch("src.game.pygame.display")
    @mock.patch("src.game.GameArea")
    def test_start(self, mock_display, mock_game_area):
        # game.start()
        # FIXME dont infinite loop
        pass

if __name__ == "__main__":
    main()
