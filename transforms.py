"""
Transformations: Manim Tutorials
"""

from manim import *

class Transforms(Scene):
    def construct(self):
        # Circle Mobject!
        circle = Circle(color=YELLOW, radius=1.5, stroke_width=2.0).to_edge(UL, buff=1)

        # Square Mobject!
        square = Square(color=BLUE, side_length=2.5, stroke_width=2.0).to_edge(UR, buff=1)

        formula_one = MathTex(
            r"\lim_{\theta \rightarrow a} \frac{ \sin{\theta} }{\theta} = 1",
            color = ORANGE,
            font_size=60
        ).to_edge(DL, buff=1)

        formula_two = MathTex(
            r"\lim_{\theta \rightarrow a} \frac{ \tan{\theta} }{\theta} = 1",
            color=ORANGE,
            font_size=60
        ).to_edge(DR, buff=1)

        # <------ Fade To Color ------>
        self.play(
            Write(formula_one)
        )
        self.wait(2)

        self.play(
            FadeToColor(formula_one, color=YELLOW),
            run_time=1.5
        )

        # <----- Fade Transform ------------->
        self.play(
            FadeIn(circle)
        )
        self.wait(2)

        self.play(
            FadeTransform(circle, square),
            run_time=1.5
        )
        self.wait(2)

        # <------- Replacement Transform ------->
        self.play(
            FadeIn(formula_one)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(formula_one.copy(), formula_two),
            run_time=1.5
        )
        self.wait(2)

        # <----- Scale in Place ------------>
        self.play(
            FadeIn(circle)
        )
        self.wait()

        circle.save_state()

        self.play(
            ScaleInPlace(circle, scale_factor=2)
        )
        self.wait()

        # <----------- Restore --------->
        self.play(
            Restore(circle)
        )
        self.wait(2)
