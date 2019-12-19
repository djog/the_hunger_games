from pygame.math import Vector2


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
        self.location.x, self.location.y = offset

    def action(self, atype: str, arguments: tuple):
        self.action_queue.append(
            Action(atype, arguments)
        )

    def update(self):
        for action in self.action_queue:
            try:
                self.actions[action.type](action.args)
            except KeyError:
                print("No such action: {}".format(action.type))
