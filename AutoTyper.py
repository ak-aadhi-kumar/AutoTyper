import pyautogui
import pyperclip
import time

time.sleep(3) # 3 = Time between executing the AutoTyper command and when it starts typing
pyautogui.typewrite(pyperclip.paste(), 0.025) # 0.025 = delay between each keystroke in seconds, too short and it won't type it out correctly, too long and it'll take forever to finish typing
