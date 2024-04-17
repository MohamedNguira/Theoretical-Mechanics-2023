from manim import *
from math import *
from scipy.misc import derivative
omega = 1
phi = 52
a = 32
b = 4
c = 39
d = 19
e = 32
O1A = 12
O2D = 32
O3E = 18
AB = 46
AD = 29
GH = 14
DE = 53
GF = 25
FH = 14
O4G = 20
class simulation2(Scene):

    def construct(self):
        def circleintersection(xa,ya,xb,yb,AC,BC):
            d = sqrt((xa-xb)**2 +(ya-yb)**2)
            a = (AC**2 - BC**2 + d**2) / (2 * d)
            h = sqrt(AC**2 - a**2)
            x3 = xa + a/d*(xb -xa)
            y3 = ya + a/d*(yb - ya)
            sol1 = [x3 + h/d*(yb - ya),y3 - h/d * (xb-xa)]
            sol2 = [x3 - h/d*(yb - ya),y3 + h/d * (xb-xa)]
            if sol2[1] > sol1[1]:
                return sol2
            else: 
                return sol1
        def deriv(f,x):
            h = 10**-5
            return (f(x+h) - f(h)) / h
        def xA(t):
            return O1A * cos(omega * t + phi)
        def yA(t):
            return O1A * sin(omega * t + phi)
        def xB(t):
            return 0
        def yB(t):
            xa = xA(t)
            ya = yA(t)
            return ya + (AB**2 - xa**2)**0.5
        def xC(t):
            xa = xA(t)
            xb = xB(t)
            return (xb - xa) * 2/ 3 + xa
        
        def yC(t):
            ya = yA(t)
            yb = yB(t)
            return (yb - ya) * 2/ 3 + ya
        
        def xD(t):
            xa = xA(t)
            ya = yA(t)
            xo = a + b
            yo = -d
            return circleintersection(xa,ya,xo,yo,AD,O2D)[0]
            
            
        def yD(t):
            xa = xA(t)
            ya = yA(t)
            xo = a + b
            yo = -d
            return circleintersection(xa,ya,xo,yo,AD,O2D)[1]
        
        def xE(t):
            xa = xD(t)
            ya = yD(t)
            xo = a + b+c
            yo = e
            return circleintersection(xa,ya,xo,yo,DE,O3E)[0]
            
        def yE(t):
            xa = xD(t)
            ya = yD(t)
            xo = a + b+c
            yo = e
            return circleintersection(xa,ya,xo,yo,DE,O3E)[1]
            
        def xF(t):
            xd = xD(t)
            xe = xE(t)
            return (xe - xd) * 3/ 5 + xd
        
        def yF(t):
            yd = yD(t)
            ye = yE(t)
            return (ye - yd) * 3/ 5 + yd
        
        def xG(t):
            xa = xF(t)
            ya = yF(t)
            xo = a
            yo = e
            return circleintersection(xa,ya,xo,yo,GF,O4G)[0]
        def yG(t):
            xa = xF(t)
            ya = yF(t)
            xo = a
            yo = e
            return circleintersection(xa,ya,xo,yo,GF,O4G)[1]
        
        def xH(t):   
            xa = xF(t)
            ya = yF(t)
            xo = xG(t) 
            yo = yG(t)
            return circleintersection(xa,ya,xo,yo,FH,GH)[0]
        
        def yH(t):
            xa = xF(t)
            ya = yF(t)
            xo = xG(t) 
            yo = yG(t)
            return circleintersection(xa,ya,xo,yo,FH,GH)[1]

        ax = Axes(
            x_range=[-20, 110,10], y_range=[-30, 60, 10], axis_config={"include_tip": False},
            x_length=11,y_length= 7
        ).add_coordinates()
        labels = ax.get_axis_labels(x_label="x", y_label="y")

        t = ValueTracker(0)

        initial_point = [ax.coords_to_point(xA(t.get_value()), yB((t.get_value())))]

        textA = Text("A",font_size=20,color=RED)
        textB = Text("B",font_size=20,color=GREEN)
        textC = Text("C",font_size=20,color=BLUE)
        textD = Text("D",font_size=20,color=YELLOW)
        textE = Text("E",font_size=20,color=ORANGE)
        textF = Text("F",font_size=20,color=LIGHT_BROWN)
        textH = Text("H",font_size=20,color=PURPLE)
        textG = Text("G",font_size=20,color=PINK)

        textO1 = Text("O1",font_size=20,color=WHITE)
        textO2 = Text("O2",font_size=20,color=WHITE)
        textO3 = Text("O3",font_size=20,color=WHITE)
        textO4 = Text("O4",font_size=20,color=WHITE)

        textva = MathTex(r'\vec{v}_A',font_size = 26,color = RED) 
        textvb = MathTex(r'\vec{v}_B',font_size = 26,color = GREEN)
        textvc = MathTex(r'\vec{v}_C',font_size = 26,color = BLUE)
        textvd = MathTex(r'\vec{v}_D',font_size = 26,color = YELLOW)
        textve = MathTex(r'\vec{v}_E',font_size = 26,color = ORANGE)
        textvf = MathTex(r'\vec{v}_F',font_size = 26,color = LIGHT_BROWN)
        textvg = MathTex(r'\vec{v}_G',font_size = 26,color = PURPLE)
        textvh = MathTex(r'\vec{v}_H',font_size = 26,color = PINK)

        dotA = Dot(point=initial_point,radius = 0.08,color=RED)
        dotB = Dot(point=initial_point,radius = 0.08,color=GREEN)
        dotC = Dot(point=initial_point,radius = 0.08,color=BLUE)
        dotD = Dot(point=initial_point,radius = 0.08,color=YELLOW)
        dotE = Dot(point=initial_point,radius = 0.08,color=ORANGE)
        dotF = Dot(point=initial_point,radius = 0.08,color=LIGHT_BROWN)
        dotH = Dot(point=initial_point,radius = 0.08,color=PURPLE)
        dotG = Dot(point=initial_point,radius = 0.08,color=PINK)

        dotO1 = Dot(point = [ax.coords_to_point(0,0)],color = WHITE)
        dotO2 = Dot(point = [ax.coords_to_point(a+b,-d)],color = WHITE)
        dotO3 = Dot(point = [ax.coords_to_point(a+b+c,e)],color = WHITE)
        dotO4 = Dot(point = [ax.coords_to_point(a,e)],color = WHITE)

        textO1.next_to(dotO1)
        textO2.next_to(dotO2)
        textO3.next_to(dotO3)
        textO4.next_to(dotO4)

        lineAB = Line(start=dotA.get_center(),end=dotB.get_center())
        lineAB.add_updater(lambda x : x.put_start_and_end_on(ax.c2p(xA(t.get_value()),yA(t.get_value())),ax.c2p(xB(t.get_value()),yB(t.get_value()))))
       
        lineAO1 = Line(start=dotA.get_center(),end=dotO1.get_center())
        lineAO1.add_updater(lambda x : x.put_start_and_end_on(dotO1.get_center(),ax.c2p(xA(t.get_value()),yA(t.get_value()))))
       
        lineAD = Line(start=dotA.get_center(),end=dotD.get_center())
        lineAD.add_updater(lambda x : x.put_start_and_end_on(ax.c2p(xA(t.get_value()),yA(t.get_value())),ax.c2p(xD(t.get_value()),yD(t.get_value()))))
       
        lineDO2 = Line(start=dotD.get_center(),end=dotO2.get_center())
        lineDO2.add_updater(lambda x : x.put_start_and_end_on(dotO2.get_center(),ax.c2p(xD(t.get_value()),yD(t.get_value()))))

        lineDE = Line(start=dotD.get_center(),end=dotE.get_center())
        lineDE.add_updater(lambda x : x.put_start_and_end_on(ax.c2p(xD(t.get_value()),yD(t.get_value())),ax.c2p(xE(t.get_value()),yE(t.get_value()))))
      
        lineEO3 = Line(start=dotE.get_center(),end=dotO3.get_center())
        lineEO3.add_updater(lambda x : x.put_start_and_end_on(dotO3.get_center(),ax.c2p(xE(t.get_value()),yE(t.get_value()))))

        lineGO4 = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineGO4.add_updater(lambda x : x.put_start_and_end_on(dotO4.get_center(),ax.c2p(xG(t.get_value()),yG(t.get_value()))))

        lineFG = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineFG.add_updater(lambda x : x.put_start_and_end_on(ax.c2p(xF(t.get_value()),yF(t.get_value())),ax.c2p(xG(t.get_value()),yG(t.get_value()))))

        lineGH = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineGH.add_updater(lambda x : x.put_start_and_end_on(ax.c2p(xG(t.get_value()),yG(t.get_value())),ax.c2p(xH(t.get_value()),yH(t.get_value()))))

        lineFH = Line(start=dotG.get_center(),end=dotO4.get_center())
        lineFH.add_updater(lambda x : x.put_start_and_end_on(ax.c2p(xF(t.get_value()),yF(t.get_value())),ax.c2p(xH(t.get_value()),yH(t.get_value()))))

        av = Vector([1,1],buff = 0,color=RED,stroke_width = 3,max_tip_length_to_length_ratio = 0.1,max_stroke_width_to_length_ratio=100)
        bv = av.copy().set_color(GREEN)
        cv = av.copy().set_color(BLUE)
        dv = av.copy().set_color(YELLOW)
        ev = av.copy().set_color(ORANGE)
        fv = av.copy().set_color(LIGHT_BROWN)
        gv = av.copy().set_color(PINK)
        hv = av.copy().set_color(PURPLE)

        def vectorupdater(x,f1,f2):
            t1 = t.get_value()
            start = ax.c2p(f1(t1),f2(t1))
            end = ax.c2p(f1(t1) + derivative(f1,t1,dx=1e-3),f2(t1) + derivative(f2,t1,dx=1e-3) )
            x.put_start_and_end_on(start,end)

        av.add_updater(lambda x: vectorupdater(x,xA,yA))
        bv.add_updater(lambda x: vectorupdater(x,xB,yB))
        cv.add_updater(lambda x: vectorupdater(x,xC,yC))
        dv.add_updater(lambda x: vectorupdater(x,xD,yD))
        ev.add_updater(lambda x: vectorupdater(x,xE,yE))
        fv.add_updater(lambda x: vectorupdater(x,xF,yF))
        gv.add_updater(lambda x: vectorupdater(x,xG,yG))
        hv.add_updater(lambda x: vectorupdater(x,xH,yH))

        textva.add_updater(lambda x: x.next_to(av,RIGHT))
        textvb.add_updater(lambda x: x.next_to(bv,RIGHT))
        textvc.add_updater(lambda x: x.next_to(cv,RIGHT))
        textvd.add_updater(lambda x: x.next_to(dv,RIGHT))
        textve.add_updater(lambda x: x.next_to(ev,RIGHT))
        textvf.add_updater(lambda x: x.next_to(fv,RIGHT))
        textvg.add_updater(lambda x: x.next_to(gv,RIGHT))
        textvh.add_updater(lambda x: x.next_to(hv,RIGHT))

        def pointupdater(x,func1,func2):    
            val = t.get_value()
            x.move_to(ax.c2p(func1(val), func2(val)))

        def aupdater(x):
            pointupdater(x,xA,yA)
            textA.next_to(x)          
        
        def bUpdater(x):
            pointupdater(x,xB,yB)
            textB.next_to(x)

        
        def cUpdater(x):
            pointupdater(x,xC,yC)
            textC.next_to(x)
        def dUpdater(x):
            pointupdater(x,xD,yD)
            textD.next_to(x)
        def eUpdater(x):
            pointupdater(x,xE,yE)
            textE.next_to(x)
        def fUpdater(x):
            pointupdater(x,xF,yF)
            textF.next_to(x)

        
        def gUpdater(x):
            pointupdater(x,xG,yG)
            textG.next_to(x)
        
        def hUpdater(x):
            pointupdater(x,xH,yH)
            textH.next_to(x)
       
        dotA.add_updater(aupdater)
        dotB.add_updater(bUpdater)
        dotC.add_updater(cUpdater)

        dotD.add_updater(dUpdater)
        dotE.add_updater(eUpdater)
        dotF.add_updater(fUpdater)
        dotG.add_updater(gUpdater)
        dotH.add_updater(hUpdater)
        textD.add_updater(lambda x: x.next_to(dotD.get_center()))
        self.add(ax,av,bv,cv,dv,ev,fv,gv,hv,textO4,dotO4, textD,lineFG,textE,textF,textG,textH,lineFH,lineGH,lineFH,labels,dotF,dotG,dotH,lineGO4, dotE,dotO3,lineEO3,lineDE,textO3,textE,dotA,dotB,textA,textB,lineAB,dotC,textC,dotO1,lineAO1,textO1,dotD,lineDO2,lineAD,dotO2,textO2)
        self.add(textva,textvb,textvc,textvd,textve,textvf,textvg,textvh)
        self.play(t.animate.set_value(10),run_time = 10)
 
        self.wait()