import pygame

from unittest import TestCase, mock, main
from src.paddle import Paddle
from src.GameArea import GameArea

class MockGameArea(mock.Mock):
    def get_rect():
        return pygame.Rect(0,0,100,100)

class TestBall(TestCase):
    def setUp(self):
        self.MOVE_GAP = 3
        self.paddle = Paddle(MockGameArea, move_gap=self.MOVE_GAP)
    
    
    def test_move_up(self):
        self.paddle.y = 10
        self.paddle.move_up()
        self.assertEqual(self.paddle.y, 7)
    
    def test_move_up_border(self):
        self.paddle.y = 0
        self.paddle.move_up()
        self.assertEqual(self.paddle.y, 0)
    
    def test_move_down(self):
        self.paddle.y = -10
        self.paddle.move_down()
        self.assertEqual(self.paddle.y, -7)
    
    def test_move_down_border(self):
        self.paddle.y = 0
        self.paddle.move_down()
        self.assertEqual(self.paddle.y, 0)
        