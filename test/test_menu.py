from unittest import TestCase, mock, main
from src import menu


class TestMenu(TestCase):

    @mock.patch("pygame.display")
    @mock.patch("pygame_menu.Menu")
    def test_start_menu(self, mock_pygame_menu, mock_display):
        mock_width = 100
        mock_height = 100
        menu.start_menu(mock_width, mock_height)
        expected_calls = [
            mock.call("Pong eternal", mock_width, mock_height, theme=mock.ANY),
            mock.call().add.selector("Mode :", mock.ANY),
            mock.call().add.selector("Score maximal :", mock.ANY, onchange=mock.ANY),
            mock.call().add.selector("Graphisme :", mock.ANY, default=1),
            mock.call().add.button("Jouer", mock.ANY),
            mock.call().add.button("Quitter", mock.ANY),
            mock.call().mainloop(mock.ANY),
        ]
        self.assertEqual(expected_calls, mock_pygame_menu.mock_calls)

    def test_menu_too_small(self):
        with self.assertRaises(ValueError):
            menu.start_menu(1, 1)
