# author: Rafayel Gardishyan
from logics.agent import Agent


def function(a, b):
    return a + 2 * b


def test_test():
    assert function(3, 5) == 13


def test_agent():
    a = Agent()
    a.action("MOV", (5, 2))
    a.update()
    assert a.location.x, a.location.y == (5, 2)
