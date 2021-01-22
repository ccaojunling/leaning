import allure


def handle_balck(func):
    def wrapper(*args, **kwargs):
        from APP.xueqiu.page.base_page import BasePage
        # 第一个参数就是 self
        instance:BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_no = 0
            return result
        except Exception as e:
            # 出现异常，进行截图上传到allure 报告
            instance.driver.save_screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)

            if instance.error_no > instance.max_no:
                raise e
            instance.error_no += 1
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper