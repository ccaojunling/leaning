from xml文件操作.create_node import createnode


a = createnode()
root = a.create_root("Root")
header = a.create_element("Header")
version = a.create_element_text("Version","001")
SenderCode = a.create_element_text("SenderCode","131101")
a.add_element(header,version)
a.add_element(header,SenderCode)
a.add_element(root,header)
body = a.create_element("Body")
MasterAgrmt = a.create_element("MasterAgrmt")
ExceID = a.create_element_text("ExceID","1311010008992020082500000001")
a.add_element(body,MasterAgrmt)
a.add_element(MasterAgrmt,ExceID)
a.add_element(root,body)




a.write_to_xml('d:\\workspace\\test.xml')


