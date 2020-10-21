import yaml
def get_data():
    with open("./data/calc.yml",encoding='utf-8') as f:
        datas_yml = yaml.safe_load(f)
    add_date = datas_yml['add']['datas']
    add_ids = datas_yml['add']['ids']
    print(add_ids)
    print(add_date)
    return [add_date, add_ids]
class TestDemo:

    def setup_class(self):
        print("TestDemo set up class")

    def teardown_class(self):
        print("Testdemo tear down class")

    def setup(self):
        print("TestDemo set up")

    def teardown(self):
        print("TestDemo tear down")

    def test_demo2(self):
        print("demo2")

    def test_demo3(self):
        print("demo3")
    def test_data(self):
        shuju = get_data()
        print(shuju[0],shuju[1])