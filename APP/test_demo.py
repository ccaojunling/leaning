from appium import webdriver
class TestDemo:
  def test_001(self):
    desire_cap = {
      "platformName": "android",
      "deviceName": "127.0.0.1:7555",
      "appPackage": "com.xueqiu.android",
      "appActivity": ".view.WelcomeActivityAlias",
      "noReset": True
    }
    driver = webdriver.Remote("http://10.0.1.207:4444/wd/hub",desire_cap)
    driver.implicitly_wait(5)

    el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    el1.click()
    el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    el2.send_keys("alibaba")
    el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
    el3.click()
