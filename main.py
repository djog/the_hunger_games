from graphics.pygame_manager import Graphics
from logics.agent import Agent

if __name__ == "__main__":
    print("Hello SNEK")

    p = Graphics((600, 600), 15)
    a = Agent()

    while p.Running:
        p.parse_events()
        a.update()
        p.draw(a)

    p.close()