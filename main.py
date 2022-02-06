sml_fce_tme = 1
basic.show_icon(IconNames.HAPPY)
music.set_built_in_speaker_enabled(True)
soundExpression.hello.play_until_done()
sml_fce_tme = 0
num1 = 0
equ = 0
num2 = 0
phs = 1
symbol = [images.create_image("""
. . # . .
. . # . .
# # # # #
. . # . .
. . # . .
"""), images.create_image("""
. . . . .
. . . . .
# # # # #
. . . . .
. . . . .
"""), images.create_image("""
# . . . #
. # . # .
. . # . .
. # . # .
# . . . #
"""), images.create_image("""
. . . . #
. . . # .
. . # . .
. # . . .
# . . . .
""")]
def on_forever():
    if sml_fce_tme == 0:
        if phs == 1:
            basic.show_number(num1)
        else:
            if phs == 2:
                symbol[equ].show_image(0)
            else:
                if phs == 3:
                    basic.show_number(num2)
                else:
                    if phs == 4:
                        if equ == 0:
                            basic.show_number(num1 + num2)
                        else:
                            if equ == 1:
                                basic.show_number(num1 - num2)
                            else:
                                if equ == 2:
                                    basic.show_number(num1 * num2)
                                else:
                                    if equ == 3:
                                        basic.show_number(num1 / num2)
basic.forever(on_forever)
def on_button_pressed_a():
    global num1, equ, num2
    soundExpression.happy.play_until_done()
    if phs == 1:
        num1 += 1
    else:
        if phs == 2:
            equ += 1
        else:
            if phs == 3:
                num2 += 1
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    soundExpression.sad.play_until_done()
    global num1, equ, num2
    if phs == 1:
        num1 += 1
    else:
        if phs == 2:
            equ += 1
        else:
            if phs == 3:
                num2 += 1   
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_ab():
    global phs
    soundExpression.slide.play_until_done()
    phs += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)