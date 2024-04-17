from manim import *

class plot1(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-16, 16], y_range=[0, 102, 10], axis_config={"include_tip": False},
            x_axis_config={
                "numbers_to_include": np.arange(-16, 16.01, 3),

            },
             y_axis_config={
                "numbers_to_include": np.arange(0, 102, 15),

            },
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y(x)")

        def func(x):
            return 4/9 * x * x + 1
        
        graph = ax.plot(func, color=MAROON)
        self.add(ax, labels, graph)