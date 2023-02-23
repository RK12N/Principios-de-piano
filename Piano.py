import keyboard
from playsound import playsound
import pygame


pygame.init()
class piano:
    def Do(): 
        sound = pygame.mixer.Sound("Do.wav")
        sound.play()
        return
    def Re():
        sound = pygame.mixer.Sound("Re.wav")
        sound.play()
        return
    def Mi():
        sound = pygame.mixer.Sound("Mi.wav")
        sound.play()
        return
    def Fa():
        sound = pygame.mixer.Sound("Fa.wav")
        sound.play()
        return
    
    def Sol():
        sound = pygame.mixer.Sound("Sol.wav")
        sound.play()
        return
        
    def La():
        sound = pygame.mixer.Sound("La.wav")
        sound.play()
        return
        
    def Si():
        sound = pygame.mixer.Sound("Si.wav")
        sound.play()
        return
    


keyboard.add_hotkey('a',piano.Do)
keyboard.add_hotkey('s',piano.Re)
keyboard.add_hotkey('d',piano.Mi)
keyboard.add_hotkey('f',piano.Fa)
keyboard.add_hotkey('g',piano.Sol)
keyboard.add_hotkey('h',piano.La)
keyboard.add_hotkey('j',piano.Si)

keyboard.wait()