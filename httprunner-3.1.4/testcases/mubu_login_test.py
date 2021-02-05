from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class Testlogin(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/")
            .get("https://mubu.com/")
            .with_headers(
                **{
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "use-redesign": "1",
                    "csrf_token": "800ffb3f-2b24-4089-b71d-419cc16c4fae",
                    "language": "en-US",
                    "country": "US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1612253972,1612344469,1612431127",
                    "SESSION": "8105c8cb-19f6-4f72-bcdf-64efa80fd6f5",
                    "reg_prepareId": "1776c69a96c-1776c69a914-4d76-a30b-29d265d2c4cb",
                    "reg_focusId": "44b4507d-ceb0-4d76-a30b-1776c69bb78",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1612431622",
                    "SLARDAR_WEB_ID": "a2e71275-5ec2-4822-a475-80a3a87b1c2a",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
            .get("https://mubu.com/login")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "use-redesign": "1",
                    "csrf_token": "800ffb3f-2b24-4089-b71d-419cc16c4fae",
                    "language": "en-US",
                    "country": "US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1612253972,1612344469,1612431127",
                    "SESSION": "8105c8cb-19f6-4f72-bcdf-64efa80fd6f5",
                    "reg_prepareId": "1776c69a96c-1776c69a914-4d76-a30b-29d265d2c4cb",
                    "reg_focusId": "44b4507d-ceb0-4d76-a30b-1776c69bb78",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1612431630",
                    "SLARDAR_WEB_ID": "972f06e5-ab46-4bad-8667-96b4e7f83a05",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
            .get("https://mubu.com/login/password")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/login",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "use-redesign": "1",
                    "csrf_token": "800ffb3f-2b24-4089-b71d-419cc16c4fae",
                    "language": "en-US",
                    "country": "US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1612253972,1612344469,1612431127",
                    "SESSION": "8105c8cb-19f6-4f72-bcdf-64efa80fd6f5",
                    "reg_prepareId": "1776c6a268f-1776c6a2668-4449-b840-e77dab22130b",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1612431632",
                    "SLARDAR_WEB_ID": "b9e0a38a-77fa-4c63-b854-4e9e949b692c",
                    "reg_focusId": "e9ef39b1-b965-4449-b840-1776c6a29e5",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
            .post("https://mubu.com/api/login/submit")
            .with_headers(
                **{
                    "content-length": "47",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/login/password",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "use-redesign": "1",
                    "csrf_token": "800ffb3f-2b24-4089-b71d-419cc16c4fae",
                    "language": "en-US",
                    "country": "US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1612253972,1612344469,1612431127",
                    "SESSION": "8105c8cb-19f6-4f72-bcdf-64efa80fd6f5",
                    "reg_prepareId": "1776c6a268f-1776c6a2668-4449-b840-e77dab22130b",
                    "reg_focusId": "e9ef39b1-b965-4449-b840-1776c6a29e5",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1612431633",
                    "SLARDAR_WEB_ID": "d6e2c935-bfcc-4021-a0c8-0bb5ca474d27",
                }
            )
            .with_data(
                {"phone": "18633046286", "password": "123456", "remember": "true"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/app")
            .get("https://mubu.com/app")
            .with_headers(
                **{
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "referer": "https://mubu.com/login/password",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "data_unique_id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "use-redesign": "1",
                    "csrf_token": "800ffb3f-2b24-4089-b71d-419cc16c4fae",
                    "language": "en-US",
                    "country": "US",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1612253972,1612344469,1612431127",
                    "SESSION": "8105c8cb-19f6-4f72-bcdf-64efa80fd6f5",
                    "reg_prepareId": "1776c6a268f-1776c6a2668-4449-b840-e77dab22130b",
                    "reg_focusId": "e9ef39b1-b965-4449-b840-1776c6a29e5",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1612431633",
                    "SLARDAR_WEB_ID": "d6e2c935-bfcc-4021-a0c8-0bb5ca474d27",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "user_persistence": "02679bc6-142e-4b7b-8a7b-695200733f33",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
            .post("https://api2.mubu.com/v3/api/message/get_message_unread")
            .with_headers(
                **{
                    "content-length": "10",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "Content-Type": "application/json;charset=UTF-8;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "data-unique-id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "x-request-id": "75da4d3f-2b98-47a8-8bf1-8fbe9042fe4d",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"page": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/")
            .get("https://api2.mubu.com/v3/")
            .with_headers(
                **{
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "no-cors",
                    "sec-fetch-dest": "image",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_cookies(
                **{
                    "use-redesign": "1",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1612253972,1612344469,1612431127",
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1612431633",
                    "SLARDAR_WEB_ID": "bf800fac-196c-4f9f-91cc-d22e2438e07d",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 17)
            .assert_equal("body.msg", "illegal request")
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
            .get("https://api2.mubu.com/v3/api/list/star_relation/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "data-unique-id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "x-request-id": "0cc6f425-2a6e-4fcf-9eee-4afde5140cf8",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
            .post("https://api2.mubu.com/v3/api/list/get_all_documents_page")
            .with_headers(
                **{
                    "content-length": "12",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "Content-Type": "application/json;charset=UTF-8;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "data-unique-id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "x-request-id": "1086418d-8301-43ab-a04f-ea6514602e63",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"start": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
            .post("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "content-length": "0",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "data-unique-id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "x-request-id": "2408abe0-8cf3-48bb-a70a-3dcb33521cf1",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
            .post("https://api2.mubu.com/v3/api/advertisement/get")
            .with_headers(
                **{
                    "content-length": "10",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "Content-Type": "application/json;charset=UTF-8;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "data-unique-id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "x-request-id": "141fb45e-7dfb-4bac-88dd-167055977ab5",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "content-length": "30",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTA4OTU1MzYiLCJleHAiOjE2MTUwMjM2NDEsImlhdCI6MTYxMjQzMTY0MX0.KnPbUCPymXPAisYoxKTy7A2YsySJbMm2w6HowJEeUZjFz1EBm5WIzkGk2K1wEM4yZJ5fpDJU4XlcsyPb-sYieg",
                    "Content-Type": "application/json;charset=UTF-8;charset=UTF-8",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "data-unique-id": "944e79f5-b0a0-4ac8-8fd3-3d45b810d3b3",
                    "x-request-id": "9511165b-cb6f-45a6-ac79-aa422a82cf78",
                    "version": "3.0.0",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal(
                'headers."Content-Type"', "application/json;charset=UTF-8;charset=UTF-8"
            )
            .assert_equal("body.code", 0)
        )
    ]

if __name__ == "__main__":
    Testlogin().test_start()