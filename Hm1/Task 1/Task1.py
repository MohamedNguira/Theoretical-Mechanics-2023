from manim import *

class simulation1(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-16, 16,4], y_range=[0, 120, 20], axis_config={"include_tip": False},
            x_axis_config={
                "numbers_to_include": np.arange(-16, 16.1, 4),

            },
             y_axis_config={
                "numbers_to_include": np.arange(0, 120.1, 20),

            },
        )
        labels = ax.get_axis_labels(x_label="x", y_label="y(x)")

        t = ValueTracker(-5)

        acctext = MathTex(r'\vec{a}',font_size = 26,color = BLUE) 
        vtext = MathTex(r'\vec{v}',font_size = 26,color = WHITE) 
        accntext = MathTex(r'\vec{a}_n',font_size = 26,color = GREEN) 
        accttext = MathTex(r'\vec{a}_{\tau}',font_size = 26,color = YELLOW) 

        def func(x):
            return 4/9 * x * x + 1
        
        def xx(t):
            return 3* t
        
        def yy(t):
            return 4 * t* t + 1
        initial_point = [ax.coords_to_point(xx(t.get_value()), yy((t.get_value())))]
        dot = Dot(point=initial_point,radius = 0.04)
        def pointupdater(x):
            val = t.get_value()
            x.move_to(ax.c2p(xx(val), yy(val)))

        def vectorupdater(x,func1,func2):
            val = t.get_value()
            end = Dot(ax.c2p(func1(val) + xx(val),  yy(val) +func2(val)))
            x.put_start_and_end_on(dot.get_center(),end.get_center())

        def velocityupdater(x):

            def func1(t):
                return 3
            def func2(t):
                return 8 * t + 1
            vectorupdater(x,func1,func2)
            vtext.next_to(velocity,RIGHT)
        
        def accupdater(x):
            def func1(t):
                return 0
            def func2(t):
                return 8 
            vectorupdater(x,func1,func2)
            acctext.next_to(acc,RIGHT)
        
        def accnupdater(x):
            def func1(t):
                return -12 * (8 * t + 1) / (32 * t * t + 8 * t + 5)
            def func2(t):
                return 36 / (32 * t * t + 8 * t + 5)
            vectorupdater(x,func1,func2)
            accntext.next_to(accn,RIGHT)

        def acctupdater(x):
            def func1(t):
                return 12 * (8 * t + 1) / (32 * t * t + 8 * t + 5)
            def func2(t):
                return 4 * ((8 * t + 1) ** 2) / (32 * t * t + 8 * t + 5)
            vectorupdater(x,func1,func2)
            accttext.next_to(acct,RIGHT)
        
        velocity = Vector([1,1],stroke_width = 3,max_tip_length_to_length_ratio = 0.1,max_stroke_width_to_length_ratio=100)

        acc = velocity.copy()
        acc.color = BLUE
        accn = velocity.copy()
        accn.color = GREEN
        acct = velocity.copy()
        acct.color = YELLOW
        graph = ax.plot(func, color=MAROON)

        dot.add_updater(pointupdater)
        velocity.add_updater(velocityupdater)
        acc.add_updater(accupdater)
        accn.add_updater(accnupdater)
        acct.add_updater(acctupdater)

        

        self.add(ax, labels, graph, dot, velocity,acc,accn,acct,acctext,vtext,accntext,accttext)
        self.play(t.animate.set_value(5),run_time = 20)
 
        self.wait()