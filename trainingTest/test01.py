def paint():
    import os
    import time
    #打开paint
    os.popen(r'mspaint')
    time.sleep(2)
    # screen_width,screen_high=pyautogui.size()
    # x,y=screen_width/2,screen_high/2
    x,y=300,400
    paint_circle(x,y)#定位圆心
    return ('Painting works well')

def paint_circle(x,y):
    #x,y=300,400 #圆心
    import pyautogui,math
    pyautogui.moveTo(x-100,y)
    for x in range(-100,105,5):
        y=math.sqrt(10000-x*x)
        a=300+x
        b=400-y
        print(a,b)
        pyautogui.dragTo(a,b)
    for x in range(-100, 105, 5):
        y = math.sqrt(10000 - x * x)
        a = 300 - x
        b = 400 + y
        print(a, b)
        pyautogui.dragTo(a, b)
paint()