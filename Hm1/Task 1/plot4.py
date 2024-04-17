from manim import *

class plot4(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5], y_range=[0, 10,1], axis_config={"include_tip": False},
            x_axis_config={
                "numbers_to_include": np.arange(-5, 5.1, 1),

            },
             y_axis_config={
                "numbers_to_include": np.arange(0, 10.1, 1),

            },
        )
        labels = ax.get_axis_labels(x_label="t", y_label="a_{T}(t)")

        def func(t):
            x = 12 * (8 * t + 1) / (32 * t * t + 8 * t + 5)
            y = 4 * ((8 * t + 1) ** 2) / (32 * t * t + 8 * t + 5)
            return (x * x + y * y) ** 0.5
        
        graph = ax.plot(func, color=MAROON)
        self.add(ax, labels, graph)