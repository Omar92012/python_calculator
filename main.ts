let sml_fce_tme = 1
basic.showIcon(IconNames.Happy)
music.setBuiltInSpeakerEnabled(true)
soundExpression.hello.playUntilDone()
sml_fce_tme = 0
let num1 = 0
let equ = 0
let num2 = 0
let phs = 1
let symbol = [images.createImage(`
. . # . .
. . # . .
# # # # #
. . # . .
. . # . .
`), images.createImage(`
. . . . .
. . . . .
# # # # #
. . . . .
. . . . .
`), images.createImage(`
# . . . #
. # . # .
. . # . .
. # . # .
# . . . #
`), images.createImage(`
. . . . #
. . . # .
. . # . .
. # . . .
# . . . .
`)]
basic.forever(function on_forever() {
    if (sml_fce_tme == 0) {
        if (phs == 1) {
            basic.showNumber(num1)
        } else if (phs == 2) {
            symbol[equ].showImage(0)
        } else if (phs == 3) {
            basic.showNumber(num2)
        } else if (phs == 4) {
            if (equ == 0) {
                basic.showNumber(num1 + num2)
            } else if (equ == 1) {
                basic.showNumber(num1 - num2)
            } else if (equ == 2) {
                basic.showNumber(num1 * num2)
            } else if (equ == 3) {
                basic.showNumber(num1 / num2)
            }
            
        }
        
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    soundExpression.happy.playUntilDone()
    if (phs == 1) {
        num1 += 1
    } else if (phs == 2) {
        equ += 1
    } else if (phs == 3) {
        num2 += 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    soundExpression.sad.playUntilDone()
    
    if (phs == 1) {
        num1 += 1
    } else if (phs == 2) {
        equ += 1
    } else if (phs == 3) {
        num2 += 1
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    soundExpression.slide.playUntilDone()
    phs += 1
})
