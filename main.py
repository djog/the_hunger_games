import time

from graphics.pygame_manager import Graphics
from logics.agent import Agent

if __name__ == "__main__":
    print("Hello SNEK")

    p = Graphics((600, 600), (120, 120))

    p.world.add_agent(Agent())

    while p.Running:
        p.parse_events()
        p.world.update()
        p.draw()

        p.world.agents[0].action("MOV", (1, 1))
        time.sleep(.1)

    p.close()
