from copy import copy


class List(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, index, value):
        if value > 255:
            value = 255
        elif value < 0:
            value = 0
        list.__setitem__(self, index, value)

    def copy(self):
        return copy(self)
