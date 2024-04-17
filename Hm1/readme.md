# Task 1
![](https://i.imgur.com/D16bLIR.png)

All code used for this task may be found in the subdirectory Hm1/Task 1/

To use the code locally, please follow these instructions to install the required libraries:
https://github.com/manimCommunity/manim

## Solution


$$ y(x) = \frac{4}{9} x^2 + 1$$

![](https://i.imgur.com/ZBK1hav.png)

<center>Plot of y(x) generated by plot1.py</center>

$$ \vec{v} = \begin{pmatrix}
     \frac{dx}{dt} \\ 
     \frac{dy}{dt} \\
 \end{pmatrix} = \begin{pmatrix}
     3\\ 
     8t + 1 \\
 \end{pmatrix}
$$

![](https://i.imgur.com/CGMCPUq.png)

<center>Plot of v(t) generated by plot2.py</center>

$$ \vec{a} = 
     \frac{d\vec{v}}{dt}= \begin{pmatrix}
     0\\ 
     8 \\
 \end{pmatrix}
 $$
 
 ![](https://i.imgur.com/pasBwNt.png)
 
<center>Plot of a(t) generated by plot3.py</center>

 $$\vec{a_\tau} = \frac{\vec{a}.\vec{v}}{\vec{v}.\vec{v}} = \begin{pmatrix}\frac{12(8t+1)}{32t^2+8t+5} \\ \frac{4(8t+1)^2}{32t^2+8t+5}\end{pmatrix}$$
 
 ![](https://i.imgur.com/XtI5uKb.png)

 <center>Plot of tangential acceleration generated by plot4.py</center>

 $$\vec{a_n} = \vec{a} - \vec{a_\tau} = \begin{pmatrix}-\frac{12\left(8t+1\right)}{32t^2+8t+5}\\ \frac{36}{32t^2+8t+5}\end{pmatrix}$$
 
 ![](https://i.imgur.com/pWE7Yhb.png)
 
 <center>Plot of tangential normal generated by plot5.py</center>
 
 $$k = \frac{48}{(256t^2+9)^{\frac{3}{2}}}$$
 
![](https://i.imgur.com/n5efPie.png)

 <center>Plot of curvature generated by plot6.py</center>
 
 ### Simulation of the mecanism generated by Task1.py:
 
 https://drive.google.com/file/d/1RggzZzjrQX4xarAy9qIBX4iiAtd0wpkm/view?usp=share_link
 
 # Task 2
 
![](https://i.imgur.com/UP3BRr9.png)

All code used for this task may be found in the subdirectory Hm1/Task 2/

To use the code locally, please follow these instructions to install the required libraries:
https://github.com/manimCommunity/manim
## Solution
$$x_A(t) = 25cos(t)$$
$$y_A(t) = 25sin(t)$$
Point B is in the straight line BP which makes a 60 degrees angle with the y-axis.
Therefore, $$y_B(t) = \frac{\sqrt{3}}{3}x_B(t) + 25$$

Distance AB = constant = 80, we can write:
$$(x_A - x_B) ^ 2 + (y_A - y_B)^2 = AB^2$$ such that $$x_A > x_B$$
From these information and after substitution we find that:
$$x_B(t) = \frac{3}{8}(\frac{50sin(t)}{\sqrt{3}} + 50cos(t) - \sqrt{(-\frac{50sin(t)}{\sqrt{3}} - 50 cos(t) + \frac{50}{\sqrt{3}})^2 - \frac{16}{3}(-1250sin(t)-5775)} - \frac{50}{\sqrt{3}})$$
and $$y_B(t) = \frac{\sqrt{3}}{3}x_B(t) + 25$$

Since C is in AB, We can obtain the coordinates of C from the rule:
$$\vec{AC} = \frac{\vec{AB}}{AB} AC$$
We get:
$$x_C(t) = x_A(t) + \frac{1}{4}(x_B(t) - x_A(t)) $$
$$y_C(t) = y_A(t) + \frac{1}{4}(y_B(t) - y_A(t))$$

### Simulation of the mecanism generated by Task2.py:
https://drive.google.com/file/d/1z7NqgXVTFAnYDQ9tCHSI3ihYYaYHifs_/view?usp=sharing