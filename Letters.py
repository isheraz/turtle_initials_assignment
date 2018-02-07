# author : Sheraz Ahmed
import turtle

# Class Definition for drawing Alphabets
class DrawableAlphabets:
    # function to Draw A
    @classmethod
    def draw_a(cls,letter):
        letter.left(75)
        letter.forward(200)
        letter.left(35)
        letter.backward(200)
        letter.left(30)
        letter.color('#000')
        letter.forward(130)
        letter.color('#fff')
        letter.right(140)
        letter.forward(80)

    # function to Draw S
    @classmethod
    def draw_s(cls,letter):
        for i in range(1, 4):
            letter.forward(100)
            letter.left(90)

        letter.backward(100)
        letter.left(90)
        letter.forward(100)

    #function to draw initials SA
    # def draw_art(self, character):
    @classmethod
    def draw_my_initials(cls):

        window = turtle.Screen()
        window.bgcolor("#000000")

        aplhabet = turtle.Turtle()
        aplhabet.shape('turtle')
        aplhabet.speed(1)
        aplhabet.color('#fff')
        DrawableAlphabets.draw_gap(aplhabet,'backward',120)
        DrawableAlphabets.draw_s(aplhabet)
        DrawableAlphabets.draw_gap(aplhabet,'forward',50)
        DrawableAlphabets.draw_a(aplhabet)

        window.exitonclick()

# gap between letters
    @classmethod
    def draw_gap(cls, aplhabet,dir,steps):
        aplhabet.color('#000')
        aplhabet.home()
        if dir == 'backward':
            aplhabet.backward(steps)
        if dir == 'forward':
            aplhabet.forward(steps)
        aplhabet.color('#fff')
        pass


# Code Run
initials = DrawableAlphabets()
initials.draw_my_initials()
