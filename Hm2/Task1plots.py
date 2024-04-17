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

        def vel(f1,f2,t):
            return sqrt(derivative(f1,t,dx=1e-3)**2 + derivative(f2,t,dx=1e-3)**2 )
        def av(t):
            return vel(xA,yA,t)
        
        def bv(t):
            return vel(xB,yB,t)
        
        def cv(t):
            return vel(xC,yC,t)
        
        def dv(t):
            return vel(xD,yD,t)
        
        def ev(t):
            return vel(xE,yE,t)
        
        def fv(t):
            return vel(xF,yF,t)
        
        def gv(t):
            return vel(xG,yG,t)
        
        def hv(t):
            return vel(xH,yH,t)
        
        def angv(f1,f2,t):
        
            return abs(-f2(t) * derivative(f1,t,dx = 1e-3) + f1(t) * derivative(f2,t,dx = 1e-3)) / (f1(t)**2 + f2(t)**2)
        
        def angvA(t):
            return angv(xA,yA,t)
        
        def angvB(t):
            return angv(xB,yB,t)
        
        def angvC(t):
            return angv(xC,yC,t)
        
        def angvD(t):
            return angv(xD,yD,t)
        def angvE(t):
            return angv(xE,yE,t)
        def angvF(t):
            return angv(xF,yF,t)
        def angvG(t):
            return angv(xG,yG,t)
        def angvH(t):
            return angv(xH,yH,t)
        
        def accA(t):
            def vx(t1):
                return derivative(xA,t1,dx=1e-3)
            def vy(t1):
                return derivative(yA,t1,dx=1e-3)
            
            return sqrt(derivative(vx,t,dx=1e-6)**2 + derivative(vy,t,dx=1e-6)**2 )
        ax = Axes(
            x_range=[0, 10,1], y_range=[0, 0.2, 0.05], axis_config={"include_tip": False},
            x_length=11,y_length= 7
        ).add_coordinates()
        labels = ax.get_axis_labels(x_label="t", y_label="Acc A")
        graph = ax.plot(accA, color=MAROON)
        self.add(ax, labels, graph)
       

