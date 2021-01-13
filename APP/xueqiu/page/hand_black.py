def hand_balck(func):
    def wrapper(*args, **kwargs):
        from APP.xueqiu.page.base_page import BasePage
        instance:BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            instance.error_no = 0
            return result
        except Exception as e:
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