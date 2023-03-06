"""
Creating LaTeX Formulas!
"""

from manim import *

class FormulaOne(Scene):
    def construct(self):
        formula_one = MathTex(
            "c^{2} = a^{2} + b^{2}",
            color = BLUE,
            font_size=80
        )
        self.play(
            Write(formula_one)
        )
        self.wait(2)

class FormulaTwo(Scene):
    def construct(self):
        formula_two = MathTex(
            r"\frac{\mathrm{d} }{\mathrm{d} x} (u.v) = u.\frac{\mathrm{d} v}{\mathrm{d} x} + v.\frac{\mathrm{d} u}{\mathrm{d} x}",
            color = YELLOW,
            font_size=60
        )
        self.play(
            FadeIn(formula_two)
        )
        self.wait(2)
