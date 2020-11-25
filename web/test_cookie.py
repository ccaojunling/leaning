import shelve
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCookieDemo():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
          'value': '1688850084032993'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
          'value': 'rFvaFPDNNpTX3p-1eUZihon9KX7aGVs7av5n5HZO2mjaaORMM8aX4ql7A7K1q7HlCI2Q7VEXQdTpu9KhtiDVMqSQpWVe04F5GNfLoust8rvMndqPKYh7C7-S1jT1Zdb-8Bm80kRyVCCrE9IxCMd6yaNf4nH7pZ_TswuO9syd7SFFFV_qc_B-twx7bZuDaoufvvVSExc6ouy6SnSHSSqj-PDDb8nsPbWL45b1JSDGtrPTA_kIgs569Bjk48xLrs0pDG5ZEp8JJmvrS7pbP2q-vA'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
          'value': '1688850084032993'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
          'value': '1970325114175152'},
         {'domain': '.qq.com', 'expiry': 1603675611, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
          'value': 'GA1.2.358851082.1603543704'},
         {'domain': 'work.weixin.qq.com', 'expiry': 1603620587, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
          'secure': False, 'value': '81equf4'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
          'value': '23641096901450318'},
         {'domain': '.qq.com', 'expiry': 1666661211, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
          'value': 'GA1.2.962439968.1603543704'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1635079700, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
          'secure': False, 'value': '0'},
         {'domain': '.work.weixin.qq.com', 'expiry': 1606181213, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
          'path': '/', 'secure': False, 'value': 'zh'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
          'value': 'a7169180'},
         {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
          'value': 'f42ba63fbd96a09ae476eba9d07d9f96a7b04791d4338cc39205b6e0efac7734'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
          'value': 'yYULSmPfc2bSgeCSB5poBYmOd3bbM0NCXjsXCTfImpS8XcSx0UTZpK1_Wea4kvmt'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
          'value': '1'},
         {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
          'value': 'direct'},
         {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
          'value': 'mGB0yEJXG0'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys("D:\\通讯录批量导入.xlsx")
        file_name = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert file_name == "通讯录批量导入.xlsx"
        sleep(3)




    def test_shelve(self):
        # 这shelve是python内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 通过key,value格式来把数据保存到shelve中
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850084032993'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'rFvaFPDNNpTX3p-1eUZihon9KX7aGVs7av5n5HZO2mjaaORMM8aX4ql7A7K1q7HlCI2Q7VEXQdTpu9KhtiDVMqSQpWVe04F5GNfLoust8rvMndqPKYh7C7-S1jT1Zdb-8Bm80kRyVCCrE9IxCMd6yaNf4nH7pZ_TswuO9syd7SFFFV_qc_B-twx7bZuDaoufvvVSExc6ouy6SnSHSSqj-PDDb8nsPbWL45b1JSDGtrPTA_kIgs569Bjk48xLrs0pDG5ZEp8JJmvrS7pbP2q-vA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850084032993'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325114175152'},
            {'domain': '.qq.com', 'expiry': 1603675611, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.358851082.1603543704'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603620587, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '81equf4'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '23641096901450318'},
            {'domain': '.qq.com', 'expiry': 1666661211, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.962439968.1603543704'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635079700, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/',
             'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606181213, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7169180'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'f42ba63fbd96a09ae476eba9d07d9f96a7b04791d4338cc39205b6e0efac7734'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'yYULSmPfc2bSgeCSB5poBYmOd3bbM0NCXjsXCTfImpS8XcSx0UTZpK1_Wea4kvmt'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'mGB0yEJXG0'}]
        # 第一步 存储数据
        db =shelve.open("cookies")
        db["cookie"] = cookies
        db.close()
        # 执行完成会生成三个数据库文件
        # 第二步 调用数据库
        # db = shelve.open("cookies")
        # cookies = db['cookie']
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")







