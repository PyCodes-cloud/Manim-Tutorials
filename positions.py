"""
Positioning Mobjects: Manim-Tutorials
"""

# Import Statement!
from manim import *

class Mobjects(Scene):
    def construct(self):
        circle = Circle(
            radius = 1,
            color=BLUE,
            stroke_width=2
        )

        square = Square(
            side_length=2,
            color=YELLOW,
            stroke_width=2
        )

        circle.to_edge(UP, buff=1)
        circle.to_edge(LEFT, buff=2)

        square.move_to([3, 1, 0])

        self.play(
            Create(circle),
            Create(square)
        )
        self.wait()
