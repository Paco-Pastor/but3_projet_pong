class Event:
    # True si la balle sort par la gauche, false si elle sort par la droite
    BALL_OUT = 'Ball Out'
    def __init__(self, event_type, extra=None):
        ok = False
        if event_type is Event.BALL_OUT:
            if type(extra) == bool:
                self.type = event_type
                self.extra = extra
                ok = True

        if not ok:
            raise TypeError('Invalid input')


    def __repr__(self):
        return f'{self.type}: {self.extra}'
