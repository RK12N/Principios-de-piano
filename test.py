import keyboard

def on_press(event):
    print("Hola")

def on_release(event):
    print("Adiós")
    if event.name == 'esc': # Si se libera la tecla "esc", se detiene la detección del teclado.
        return False

keyboard.on_press(on_press)
keyboard.on_release(on_release)
keyboard.wait() # Espera hasta que se presione una tecla.
