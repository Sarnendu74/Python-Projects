#importing modules
import pyautogui as pg
import time

#giving delay to program
print("Program will run after 5 seconds")
time.sleep(5)
print("Running")

#after run the program immiediately open whatsapp web

for i in range(30):
    #printing message
    pg.write("Thank You")
    #giving speed
    time.sleep(0.1)
    #sending message by pressing enter
    pg.press("enter")
