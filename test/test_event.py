from unittest import TestCase
from src.event import Event


class TestEvent(TestCase):
    def test_wrong_event_type(self):
        with self.assertRaises(TypeError):
            wrong_event_type = "mock_event_type"
            Event(wrong_event_type)
