from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  
        circle.set_fill(PINK, opacity=0.5)   

        square = Square()
        square2= Square()  
        square.rotate(PI / 4) 
        self.play(Create(square))  
        self.play(Transform(square, circle))  
        self.play(FadeOut(square))  
        self.play(Create(square)) 
        self.play(Transform(square, square2))
        self.remove(square)
        self.play(Rotate(square2),angle = 180)
        self.remove(square2)
        text1 = Text("Aditya Chouhan", font_size=144)
        text2=Text("Raina Girish", font_size=160) 
        self.play(Write(text1))
        self.play(Transform(text1,text2))
        self.wait(2)