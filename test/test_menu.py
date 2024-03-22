from unittest import TestCase, mock, main
from src import menu


class TestMenu(TestCase):

    @mock.patch("pygame.display")
    @mock.patch("pygame_menu.Menu")
    def test_start_menu(self, mock_pygame_menu, mock_display):
        menu.start_menu(100, 100)
        expected_calls = [
            mock.call().add.selector("Mode :", [("1 joueur", 1), ("2 joueurs", 2)]),
            mock.call().add.button('Jouer', mock.ANY),
            mock.call().add.button('Quitter', mock.ANY),
            mock.call().mainloop(mock.ANY)
        ]
        self.assertIn(expected_calls, mock_pygame_menu.mock_calls)

    def test_menu_too_small(self):
        with self.assertRaises(ValueError):
            menu.start_menu(1, 1)
