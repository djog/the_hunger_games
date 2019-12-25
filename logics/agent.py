from pygame.math import Vector2

from logics.world import World


class Action:

    def __init__(self, type, args):
        self.type = type
        self.args = args


class Agent(object):

    def __init__(self):
        self.lifetime = 0
        self.location = Vector2()
        self.location.x, self.location.y = 0, 0

        self.action_queue: list = []  # Of type Action

        self.actions = {
            "MOV": self.move
        }

    def move(self, offset: tuple):
        self.location.x += offset[0]
        self.location.y += offset[1]

    def action(self, atype: str, arguments: tuple):
        self.action_queue.append(
            Action(atype, arguments)
        )

    def update(self, parent: World):
        # Use to get other variables from the world
        print(parent)
        for i in range(len(self.action_queue)):
            action = self.action_queue.pop()
            try:
                self.actions[action.type](action.args)
            except KeyError:
                print("No such action: {}".format(action.type))
