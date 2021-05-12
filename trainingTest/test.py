import os
import sys
import time
import pyautogui
#打开paint
os.popen(r'mspaint')
time.sleep(2)
#获取当前鼠标位置
position = currentMouseX, currentMouseY = pyautogui.position()
print(position)
pyautogui.hotkey('alt','SPACE', 'x')
#鼠标移动到黄色选择黄色
pyautogui.moveTo(x=875, y=55,duration=0.2, tween=pyautogui.linear)
pyautogui.click()
#鼠标移动到size选择8PX
pyautogui.moveTo(x=630, y=65,duration=0.2, tween=pyautogui.linear)
pyautogui.click()
pyautogui.moveTo(x=650, y=250,duration=0.2, tween=pyautogui.linear)
pyautogui.click()
#画图100PX*100PX的正方形
pyautogui.mouseDown(x=500, y=500, button='left')
pyautogui.mouseUp(x=500, y=600, button='left',duration=1)
time.sleep(0)
pyautogui.mouseDown(x=500, y=600, button='left')
pyautogui.mouseUp(x=600, y=600, button='left',duration=1)
time.sleep(0)
pyautogui.mouseDown(x=500, y=500, button='left')
pyautogui.mouseUp(x=600, y=500, button='left',duration=1)
time.sleep(0)
pyautogui.mouseDown(x=600, y=500, button='left')
pyautogui.mouseUp(x=600, y=600, button='left',duration=1)
#鼠标移动选择红色
pyautogui.moveTo(x=827, y=55,duration=0.2, tween=pyautogui.linear)
pyautogui.click()
#鼠标移动选择3PX
pyautogui.moveTo(x=630, y=65,duration=0.2, tween=pyautogui.linear)
pyautogui.click()
pyautogui.moveTo(x=650, y=174,duration=0.2, tween=pyautogui.linear)
time.sleep(0)
pyautogui.click()
#画图100PX*100PX的正方形
pyautogui.mouseDown(x=500, y=500, button='left')
pyautogui.mouseUp(x=500, y=600, button='left',duration=1)
time.sleep(0)
pyautogui.mouseDown(x=500, y=600, button='left')
pyautogui.mouseUp(x=600, y=600, button='left',duration=1)
time.sleep(0)
pyautogui.mouseDown(x=500, y=500, button='left')
pyautogui.mouseUp(x=600, y=500, button='left',duration=1)
time.sleep(0)
pyautogui.mouseDown(x=600, y=500, button='left')
pyautogui.mouseUp(x=600, y=600, button='left',duration=1)

#等待3秒后关闭当前操作
time.sleep(2)
# pyautogui.hotkey('alt','f4')
# pyautogui.moveTo(x=1000, y=520,duration=0.2, tween=pyautogui.linear)
# pyautogui.click()
os.system("taskkill /F /IM mspaint.exe")
# os._exit(0)
#
# sys.exit(0)

