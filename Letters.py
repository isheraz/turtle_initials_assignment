import turtle


class DrawableAlphabets:
    def draw_a(letter):
        letter.right(45)
        letter.backward(200)

    def draw_s(letter):
        letter.forward(100)
        letter.left(90)
        letter.forward(100)
        letter.left(90)
        letter.forward(100)
        letter.left(90)
        letter.backward(100)
        letter.left(90)
        letter.forward(100)

    def draw_art(self, character):
        window = turtle.Screen()
        window.bgcolor("#000000")

        aplhabet = turtle.Turtle()
        aplhabet.shape('turtle')
        aplhabet.speed(1)
        aplhabet.color('#fff')

        if character == 'a':
            DrawableAlphabets.draw_a(aplhabet)
        if character == 's':
            DrawableAlphabets.draw_s(aplhabet)
        window.exitonclick()


initials = DrawableAlphabets()
initials.draw_art('s')
initials.draw_art('a')
