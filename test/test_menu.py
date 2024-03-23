from unittest import TestCase, mock, main
from src import menu
import pygame
import pygame_menu


class TestMenu(TestCase):

    def mock_loop(self, screen):
        pass

    @mock.patch.object(pygame_menu.Menu, "mainloop", new=mock_loop)
    def test_start_menu(self):
        menu_instance = menu.Menu("Mock menu", 100, 100, pygame_menu.themes.Theme())
        expected_widgets = {
            pygame_menu.widgets.Selector: 2,
            pygame_menu.widgets.Button: 2,
        }
        actual_widgets = {
            pygame_menu.widgets.Selector: 0,
            pygame_menu.widgets.Button: 0,
        }
        for widget in menu_instance._widgets:
            actual_widgets[type(widget)] += 1

        self.assertEqual(expected_widgets, actual_widgets)

    def test_menu_too_small(self):
        with self.assertRaises(ValueError):
            menu.start_menu(1, 1)

    def test_menu_negative_values(self):
        with self.assertRaises(pygame.error):
            menu.start_menu(-1, -1)
