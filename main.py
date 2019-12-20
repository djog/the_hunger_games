from graphics.pygame_manager import Graphics

if __name__ == "__main__":
    print("Hello SNEK")

    p = Graphics((600, 600), 15)

    while p.Running:
        p.parse_events()
        p.draw()

    p.close()