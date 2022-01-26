import pyautogui as pag 
from PIL import ImageGrab 
import keyboard

print("---사용법---")
print("측정: Alt ")
print("made by Ksh")
print("=")
a=0
while a==0:
    if keyboard.is_pressed('Alt'): #측정
        screen = ImageGrab.grab() # 화면 캡쳐
        print(screen.getpixel(pag.position()))
    if keyboard.is_pressed('F4'): #측정
        print()
        print("----종료 made by Ksh---")
        a=0
        break 
