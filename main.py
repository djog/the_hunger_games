from graphics.pygame_manager import Graphics
from logics.agent import Agent

if __name__ == "__main__":
    print("Hello SNEK")

    p = Graphics((600, 600), (30, 30))

    p.world.add_agent(Agent())

    while p.Running:
        p.parse_events()
        p.world.update()
        p.draw()

    p.close()
