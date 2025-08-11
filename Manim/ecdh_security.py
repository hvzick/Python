from manim import *

class ECDHSecurity(Scene):
    def construct(self):
        title = Text("Why is ECDH Secure?", font_size=36, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))

        # Security points
        security_points = VGroup(
            Text("• Public keys A and B are shared openly", font_size=20),
            Text("• Private keys a and b remain secret", font_size=20),
            Text("• Computing a from A requires solving ECDLP", font_size=20),
            Text("• Elliptic Curve Discrete Logarithm Problem is hard", font_size=20),
            Text("• Even with A and B, attackers can't find shared secret", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        security_points.move_to(ORIGIN)

        for point in security_points:
            self.play(Write(point))
            self.wait(1)

        self.wait(2)

        # Highlight the key point
        key_point = Text(
            "The security relies on the difficulty of the ECDLP!",
            font_size=24,
            color=GREEN
        ).move_to(DOWN * 2.5)
        
        highlight_box = Rectangle(
            width=10, height=1, color=GREEN, stroke_width=3
        ).move_to(DOWN * 2.5)
        
        self.play(Create(highlight_box))
        self.play(Write(key_point))
        self.wait(3)
