from unittest import TestCase, mock, main
from src.GameArea import GameArea

import pygame


class MockScreen(mock.Mock):
    subsurface = mock.MagicMock()

    def get_width():
        return 100

    def get_height():
        return 100

    def fill(mock):
        pass


class MockEventBallOut(mock.Mock):
    type = "Ball Out"
    extra = True


class MockEvent(mock.Mock):
    type = "Mock Event"


class TestGameArea(TestCase):

    def setUp(self):
        self.game_area = GameArea(MockScreen, pygame.time.Clock(), 60, 10, 1)

    @mock.patch("pygame.event")
    @mock.patch("pygame.draw")
    @mock.patch("pygame.display")
    def test_execute_once(self, mock_event, mock_draw, mock_display):
        execute_return = self.game_area.execute_once()
        self.assertTrue(execute_return)

    @mock.patch("pygame.event")
    @mock.patch("pygame.draw")
    @mock.patch("pygame.display")
    def test_ball_out(self, mock_event, mock_draw, mock_display):
        self.game_area.score[0] = 10
        event_return = self.game_area.handling_event(MockEventBallOut())
        self.assertFalse(event_return)

    @mock.patch("pygame.event")
    @mock.patch("pygame.draw")
    @mock.patch("pygame.display")
    def test_ball_in(self, mock_event, mock_draw, mock_display):
        event_return = self.game_area.handling_event(MockEvent())
        self.assertTrue(event_return)


if __name__ == "__main__":
    main()
