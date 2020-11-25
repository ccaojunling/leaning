import time
from appium import webdriver

capabilities = {}
# Android平台测试
capabilities['platformName'] = 'Android'
# 测试手机版本为5.0
capabilities['platformVersion'] = '6.0'
capabilities['deviceName'] = '127.0.0.1:7555'
# 系统手机中的联系人app的包名
capabilities['appPackage'] = 'com.xueqiu.android'
# 系统手机中的联系人app的主入口activity
capabilities['appActivity'] = '.common.MainActivity'
# 连接测试机所在服务器服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

time.sleep(2)
#断开连接
driver.quit()


#  com.xueqiu.android/.main.view.MainActivity
# com.xueqiu.android/.common.MainActivity