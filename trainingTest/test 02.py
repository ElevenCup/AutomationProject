# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 实例化浏览器
driver = webdriver.Chrome()
driver.get("https://www.demoqa.com/automation-practice-form")
# 浏览器最大化
driver.maximize_window()
# 在名字输入‘Aa123'
driver.find_element_by_id('firstName').send_keys('Aa123')
# 等待2秒
time.sleep(0)
# 在lastname输入：123！@#￥
driver.find_element_by_id('lastName').send_keys('123!@#$')
# 等待2秒
time.sleep(0)
# 填入邮箱
driver.find_element_by_id('userEmail').send_keys('test@gmail.com')
# 等待2秒
time.sleep(0)
# 选择male
driver.find_element_by_class_name('custom-control').click()
# 输入用户号码
driver.find_element_by_id('userNumber').send_keys('1234567890')
# 等待3秒
time.sleep(0)
# 选择日期(模拟键盘事件)
setDate = driver.find_element_by_id('dateOfBirthInput')
setDate.click()
setDate.send_keys(Keys.CONTROL, 'a')
setDate.send_keys("1994-3-25")
setDate.send_keys(Keys.ENTER)
# 等待2秒
time.sleep(2)
#选择科目
subjects = driver.find_element_by_css_selector('input#subjectsInput')
#subjects.click()
subjects.send_keys("english")
time.sleep(2)
subjects.send_keys(Keys.ENTER)
time.sleep(3)
# xpath定位：选择运动，音乐，阅读
driver.find_element_by_xpath("//*[@id='hobbies-checkbox-1']/../label").click()
driver.find_element_by_xpath("//*[@id='hobbies-checkbox-2']/../label").click()
driver.find_element_by_xpath("//*[@id='hobbies-checkbox-3']/../label").click()

#上传照片
driver.find_element_by_id('uploadPicture').send_keys('C:/Users/Public/Pictures/Sample Pictures/Hydrangeas.jpg')

#随便写点
driver.find_element_by_id('currentAddress').send_keys('你好帅啊！！！')
#选择国家和城市
driver.find_element_by_id('react-select-3-input').click()
# 等待3秒
time.sleep(3)
# 退出
# driver.close()
