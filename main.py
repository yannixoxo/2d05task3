count = 0

def on_button_pressed_a():
    global count
    count = 9
    for index in range(count + 1):
        basic.show_number(count)
        basic.pause(100)
        count += -1
    basic.pause(2000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . # . # .
                # . . . #
                . . . . .
                # . . . #
                . # . # .
    """)
    basic.show_leds("""
        # . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
