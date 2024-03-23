from unittest import TestCase, mock, main
from src.game import Game
from src.ball import Ball
import pygame


class MockScreen(mock.Mock):
    subsurface = mock.MagicMock()

    def get_width():
        return 100

    def get_height():
        return 100

    def fill(mock):
        pass

    def blit(mock1, mock2):
        pass


class MockEventBallOut(mock.Mock):
    type = "Ball Out"
    extra = True


class MockEvent(mock.Mock):
    type = "Mock Event"


class TestGame(TestCase):

    def setUp(self):
        self.game = Game(MockScreen, pygame.time.Clock(), 60, 10, 1, False)
        self.game.ball = mock.MagicMock(spec=Ball)
        self.game.ball.hit_box = mock.MagicMock()

    @mock.patch("pygame.event")
    @mock.patch("pygame.draw")
    @mock.patch("pygame.display")
    @mock.patch("pygame.font.Font")
    def test_execute_once(self, mock_event, mock_draw, mock_display, mock_font):
        execute_return = self.game.execute_once()
        self.assertTrue(execute_return)

    @mock.patch("pygame.event")
    @mock.patch("pygame.draw")
    @mock.patch("pygame.display")
    def test_ball_out(self, mock_event, mock_draw, mock_display):
        self.game.score[0] = 10
        event_return = self.game.handling_event(MockEventBallOut())
        self.assertFalse(event_return)

    @mock.patch("pygame.event")
    @mock.patch("pygame.draw")
    @mock.patch("pygame.display")
    def test_ball_in(self, mock_event, mock_draw, mock_display):
        event_return = self.game.handling_event(MockEvent())
        self.assertTrue(event_return)


if __name__ == "__main__":
    main()
