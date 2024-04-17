from manim import *
from math import *
class simulation2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-100, 100,25], y_range=[-100, 100, 25], axis_config={"include_tip": False},
            x_length=7,y_length= 7
        ).add_coordinates()
        labels = ax.get_axis_labels(x_label="x", y_label="y(x)")

        t = ValueTracker(0)

        def xx(t):
            return 25 * cos(t)
        
        def yy(t):
            return 25 * sin(t)
        initial_point = [ax.coords_to_point(xx(t.get_value()), yy((t.get_value())))]
        textA = Text("A",font_size=20,color=RED)
        textB = Text("B",font_size=20,color=GREEN)
        textC = Text("C",font_size=20,color=BLUE)
        dotA = Dot(point=initial_point,radius = 0.08,color=RED)
        dotB = Dot(point=initial_point,radius = 0.08,color=GREEN)
        dotC = Dot(point=initial_point,radius = 0.08,color=BLUE)
        lineAB = Line(start=dotA.get_center(),end=dotB.get_center())
        def pointupdater(x,func1,func2):    
            val = t.get_value()
            x.move_to(ax.c2p(func1(val), func2(val)))
        def aupdater(x):
            def func1(t):
                return 25 * cos(t)
            def func2(t):
                return 25 * sin(t)
            pointupdater(x,func1,func2)
            textA.next_to(x)
        
        def bUpdater(x):
            def func1(t):
                return 3/8 * (50 * sin(t) / sqrt(3) + 50 * cos(t) - sqrt((- 50 * sin(t) / sqrt(3) - 50 * cos(t) + 50 / sqrt(3)) ** 2 - 16/3 * (-1250 * sin(t)- 5775)) - 50 / sqrt(3))
            def func2(t):
                return func1(t) * sqrt(3) / 3 + 25
            pointupdater(x,func1,func2)
            textB.next_to(x)
        
        def cUpdater(x):
            def func1(t):
                xB = 3/8 * (50 * sin(t) / sqrt(3) + 50 * cos(t) - sqrt((- 50 * sin(t) / sqrt(3) - 50 * cos(t) + 50 / sqrt(3)) ** 2 - 16/3 * (-1250 * sin(t)- 5775)) - 50 / sqrt(3))
                xA = 25 * cos(t)
                return (xB - xA) / 80 * 20 + xA
            def func2(t):
                yB = 3/8 * (50 * sin(t) / sqrt(3) + 50 * cos(t) - sqrt((- 50 * sin(t) / sqrt(3) - 50 * cos(t) + 50 / sqrt(3)) ** 2 - 16/3 * (-1250 * sin(t)- 5775)) - 50 / sqrt(3))
                yB = yB * sqrt(3) / 3 + 25
                yA = 25 * sin(t)
                return (yB - yA) / 80 * 20 + yA
            pointupdater(x,func1,func2)
            textC.next_to(x)
        def lineUpdater(x):
            x.put_start_and_end_on(dotA.get_center(),dotB.get_center())
        dotA.add_updater(aupdater)
        dotB.add_updater(bUpdater)
        dotC.add_updater(cUpdater)
        lineAB.add_updater(lineUpdater)
        self.add(ax, labels, dotA,dotB,lineAB,textA,textB,dotC,textC)
        self.play(t.animate.set_value(20),run_time = 15)
 
        self.wait()