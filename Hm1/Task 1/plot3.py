from manim import *

class plot3(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5], y_range=[0, 50,5], axis_config={"include_tip": False},
            x_axis_config={
                "numbers_to_include": np.arange(-5, 5.1, 1),

            },
             y_axis_config={
                "numbers_to_include": np.arange(0, 50.1, 5),

            },
        )
        labels = ax.get_axis_labels(x_label="t", y_label="a(t)")

        def func(t):
            x = 3
            y = 8
            return (x * x + y * y) ** 0.5
        
        graph = ax.plot(func, color=MAROON)
        self.add(ax, labels, graph)