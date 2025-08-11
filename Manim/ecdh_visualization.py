from manim import *
import numpy as np

class ECDHVisualization(Scene):
    def construct(self):
        # Title
        title = Text("ECDH: Visual Representation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Create a simplified elliptic curve
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": GREY}
        )
        
        # Elliptic curve function (simplified for visualization)
        def elliptic_curve(x):
            return np.sqrt(np.abs(x**3 - x + 1))
        
        # Create the curve (upper and lower parts)
        curve_upper = axes.plot(
            lambda x: elliptic_curve(x),
            x_range=[-1.5, 2.5],
            color=WHITE,
            stroke_width=3
        )
        
        curve_lower = axes.plot(
            lambda x: -elliptic_curve(x),
            x_range=[-1.5, 2.5],
            color=WHITE,
            stroke_width=3
        )

        self.play(Create(axes))
        self.play(Create(curve_upper), Create(curve_lower))

        # Generator point
        G = Dot(axes.coords_to_point(1, elliptic_curve(1)), color=YELLOW, radius=0.1)
        G_label = Text("G", font_size=20, color=YELLOW).next_to(G, UR, buff=0.1)
        
        self.play(Create(G), Write(G_label))
        self.wait(1)

        # Alice's private key multiplication
        alice_point = Dot(axes.coords_to_point(-0.5, elliptic_curve(-0.5)), color=BLUE, radius=0.1)
        alice_label = Text("A = a·G", font_size=16, color=BLUE).next_to(alice_point, UL, buff=0.1)
        
        # Bob's private key multiplication
        bob_point = Dot(axes.coords_to_point(0.5, -elliptic_curve(0.5)), color=RED, radius=0.1)
        bob_label = Text("B = b·G", font_size=16, color=RED).next_to(bob_point, DR, buff=0.1)

        self.play(
            Create(alice_point),
            Write(alice_label),
            Create(bob_point),
            Write(bob_label)
        )
        self.wait(2)

        # Shared secret point
        shared_point = Dot(axes.coords_to_point(1.5, elliptic_curve(1.5)), color=GREEN, radius=0.12)
        shared_label = Text("Shared Secret", font_size=16, color=GREEN).next_to(shared_point, UR, buff=0.1)
        
        # Draw lines showing the computation
        line_alice = Line(alice_point.get_center(), shared_point.get_center(), color=BLUE, stroke_width=2)
        line_bob = Line(bob_point.get_center(), shared_point.get_center(), color=RED, stroke_width=2)
        
        self.play(Create(line_alice), Create(line_bob))
        self.play(Create(shared_point), Write(shared_label))
        
        # Pulsing animation for the shared secret
        self.play(
            shared_point.animate.set_color(GREEN).scale(1.5),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(3)
