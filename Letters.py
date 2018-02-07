import turtle


class DrawableAlphabets:
    def draw_a(letter):
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


    def draw_s(letter):
        for i in range(1, 4):
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


# initials_s = DrawableAlphabets()
initials_a = DrawableAlphabets()
# initials_s.draw_art('s')
initials_a.draw_art('a')
