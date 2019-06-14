from level.rooms.room import Room
from utilities.color import Color
from entities.geometry.rectangle import Rectangle


class SpecialRoom(Room):
    "A bigger room with no stairs"

    def __init__(self, building_id):
        super(SpecialRoom, self).__init__(building_id)

    def create_bounds(self):
        self.bounds = Rectangle(0, 0, 12 * 16, 6 * 16)

    def make_exits(self):
        self.exits.append(Rectangle(self.bounds.x + self.bounds.width / 2 - 16,
                                    self.bounds.y + self.bounds.height - 16, 32, 16, color=Color.BLACK))

    def update(self, delta_time):
        pass