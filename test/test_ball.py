from unittest import TestCase, mock, main
from src.ball import Ball


class TestBall(TestCase):
    def setUp(self):
        self.ball = Ball(mock.Mock())

    def test_update_image(self):
        old_image = self.ball.image
        self.ball.update_image()
        self.assertNotEqual(self.ball.image, old_image)

    def test_start(self):
        self.ball.start()
        self.assertEqual(self.ball.direction, self.ball.orientation)

    def test_movement(self):
        self.ball.movement()
        expected_x = self.ball.x + self.ball.speed * 0
        expected_y = self.ball.y + self.ball.speed * 0
        self.assertEqual(self.ball.x, expected_x)
        self.assertEqual(self.ball.y, expected_y)

    def test_rotate(self):
        expected_orientation = (self.ball.orientation + 1) % 360
        self.ball.rotate()
        self.assertEqual(self.ball.orientation, expected_orientation)

    # TODO test display


if __name__ == "__main__":
    main()
