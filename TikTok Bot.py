# Import
import time
import pyautogui
import webbrowser
import pyperclip
import tkinter as tk

#Input for the bot
hashtag_raw0 = "learn knowledge business success finance entrepreneur startup career history science tech politics economics math physics chemistry goals leader inspiration happiness productivity education growth love know invest study productive"
hashtag = hashtag_raw0.split(' ') #split the string of a sentence into a list of individual hashtags
times = 400
time_watch = 15

# Load files and click on first video
# webbrowser.open('https://docs.google.com/spreadsheets/d/1en85AFmK-PrpGB3kGtuw0l6GI_lIP4WVS5syTYBtnx0/edit#gid=0')
# webbrowser.open('https://www.tiktok.com/en?lang=mr-IN')

#Introduction print out text over screen
time.sleep(5)
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
text("TikTok Simulation Bot!")
text("by Digital Kings")
tk.mainloop()


pyautogui.FAILSAFE = True #Failsafe mechanism
pyautogui.moveTo(1029,585) #moving to the first video when tiktok is open
pyautogui.click()
time.sleep(2) #waiting for the first video to load

#Start the scraping hashtag process

for i in range(times):

    #Go to position to copy hashtag
    pyautogui.moveTo(1256, 232)
    pyautogui.click() #remove previous selection
    time.sleep(0.1)
    pyautogui.click()  # remove previous selection
    time.sleep(0.1)
    pyautogui.dragTo(1890, 320, 0.2, button="left")
    pyautogui.hotkey('ctrl', 'c')
    x = pyperclip.paste()

    for word in hashtag:
        if word in x:
            time.sleep(time_watch)
            pyautogui.moveTo(650, 539)
            pyautogui.doubleClick()
            pyautogui.moveTo(1798, 180) #click to follow
            pyautogui.click()
            time.sleep(1)
            break

    # Go to sheet to patse data

    pyautogui.hotkey('ctrl','tab')
    time.sleep(1)
    pyautogui.moveTo(433,343)
    time.sleep(0.1)
    pyautogui.doubleClick()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.25)

    # Go back to TikTok for next video

    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.1)
    pyautogui.moveTo(1189, 620)
    pyautogui.click()
    time.sleep(0.25)

    # Copy next video data but for comparison with the previous

    pyautogui.moveTo(1256, 232)
    pyautogui.click()  # remove previous selection
    time.sleep(0.1)
    pyautogui.click()  # remove previous selection
    time.sleep(0.1)
    pyautogui.dragTo(1890, 320, 0.2, button="left")
    pyautogui.hotkey('ctrl', 'c')
    y = pyperclip.paste()

    for word in hashtag:
        if word in y:
            time.sleep(time_watch)
            pyautogui.moveTo(650, 539)
            pyautogui.doubleClick()
            pyautogui.moveTo(1798, 180)  # click to follow
            pyautogui.click()
            time.sleep(1)
            break

    #Condition for stopping when reaching the end of a period of videos
    if x == y:
        pyautogui.moveTo(46, 137) #Click to exit current video
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.scroll(-10000000)
        time.sleep(4)
        pyautogui.moveTo(1018, 643)
        pyautogui.click()
        time.sleep(2)
        continue
    else:
        #Go to sheet to patse data
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(1)
        pyautogui.moveTo(433, 343)
        time.sleep(0.1)
        pyautogui.doubleClick()
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.25)

        #Go back to TikTok for next video
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.1)
        pyautogui.moveTo(1189, 620)
        pyautogui.click()
        time.sleep(0.5)
        continue







