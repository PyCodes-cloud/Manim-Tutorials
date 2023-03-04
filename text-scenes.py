"""
Text Objects in ManimCE!
"""

# Import Statement!
from manim import *

class TextScene(Scene):
    def construct(self):
        text = Text(
            text = "Welcome to Manim Tutorials!",
            font_size=70,
            font="Arial",
            color = BLUE
        )

        self.play(
            FadeIn(text)
        )
        self.wait()
