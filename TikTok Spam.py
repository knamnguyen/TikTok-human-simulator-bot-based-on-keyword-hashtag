# Import
import time
import pyautogui
import webbrowser
import pyperclip
import tkinter as tk

#Load files and click on first video
# webbrowser.open('https://www.tiktok.com/en')

time.sleep(5)
keyword_raw = "growth"
keyword = keyword_raw.split(' ')
hashtag_raw = "learn knowledge business success finance entrepreneur startup career history science tech politics economics math physics chemistry goals leader inspiration happiness productivity education growth love know invest study productive"
hashtag = hashtag_raw.split(' ') #split the string of a sentence into a list of individual hashtags
times = 10
time_watch = 15

#Process hashtag
pyautogui.FAILSAFE = True

#Introduction
def text(n):
    label = tk.Label(text=(str(n)), font = "Calibri 100" ,fg='yellow',bg = "black")
    label.master.overrideredirect(True)
    label.master.geometry("+150+312")
    label.master.lift()
    label.master.wm_attributes("-topmost",True)
    label.master.wm_attributes("-disabled",True)
    label.master.wm_attributes("-transparentcolor","white")
    label.after(2500,label.master.destroy)
    label.pack()
text("TikTok Spamming Bot!")
text("by Digital Kings")
tk.mainloop()

for i in keyword:
    hashtag_1 = [word for word in hashtag if word not in i]
    pyautogui.moveTo(738,117)
    pyautogui.doubleClick()
    pyautogui.hotkey("ctrl","a")
    pyautogui.write(i)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.moveTo(853,888)
    pyautogui.doubleClick()
    time.sleep(4)

#start spamming process - only like videos that have more than 2 favourite hashtags:
    for y in range(times):
        for z in range(12):
            pyautogui.moveTo(1256, 232)
            pyautogui.click()  # remove previous selection
            time.sleep(0.1)
            pyautogui.click()  # remove previous selection
            time.sleep(0.1)
            pyautogui.dragTo(1890, 320, 0.2, button="left")
            pyautogui.moveTo(1893, 60)
            pyautogui.click()
            pyautogui.moveTo(1797, 484)
            pyautogui.click()
            x = pyperclip.paste()

            for word2 in hashtag_1:
                if word2 in x:
                    time.sleep(time_watch)
                    pyautogui.moveTo(1798, 180)  # click to follow
                    pyautogui.click()
                    time.sleep(1)
                    break
            pyautogui.moveTo(650, 539)
            pyautogui.doubleClick()
            time.sleep(0.1)
            pyautogui.moveTo(1191, 583)
            pyautogui.click()

        time.sleep(0.1)
        pyautogui.moveTo(49,139,1)
        pyautogui.click()

        if y == times-1:
            break
        else:
            pyautogui.moveTo(1919, 1052)
            pyautogui.mouseDown(button='left')
            time.sleep(3)
            pyautogui.mouseUp(button='left')
            pyautogui.scroll(-25000)
            time.sleep(1)
            pyautogui.moveTo(1157,960)
            pyautogui.click()
            time.sleep(2)
            pyautogui.scroll(-20)
            pyautogui.moveTo(849,991,1)
            time.sleep(2)
            pyautogui.click()


