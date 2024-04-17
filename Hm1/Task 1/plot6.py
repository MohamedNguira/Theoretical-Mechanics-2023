from manim import *

class plot6(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5], y_range=[0, 2,0.5], axis_config={"include_tip": False},
            x_axis_config={
                "numbers_to_include": np.arange(-5, 5.1, 1),

            },
             y_axis_config={
                "numbers_to_include": np.arange(0, 2.1, 0.5),

            },
        )
        labels = ax.get_axis_labels(x_label="t", y_label="k(t)")

        def func(t):
            return 48  / (256 * t * t + 9) ** 1.5
        
        graph = ax.plot(func, color=MAROON)
        self.add(ax, labels, graph)