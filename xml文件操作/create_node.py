from xml.dom.minidom import Document


class createnode:

    def __init__(self):
        self.doc = Document()

    def create_root(self,name):
        root = self.doc.createElement(name)
        self.doc.appendChild(root)
        return root

    def create_element(self,name):
        company = self.doc.createElement(name)
        return company

    def create_element_text(self,name,text):
        company = self.doc.createElement(name)
        company.appendChild(self.doc.createTextNode(text))
        return company

    def add_element(self,node,child):
        node.appendChild(child)

    def write_to_xml(self,path):
        fp = open(path, 'w', encoding='utf-8')
        self.doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
        fp.close()

class parse_xml:
    pass


if __name__ == '__main__':
    a = createnode()
    root = a.create_root("Root")
    header = a.create_element("Header")
    version = a.create_element_text("Version", "001")
    SenderCode = a.create_element_text("SenderCode", "131101")
    a.add_element(header, version)
    a.add_element(header, SenderCode)
    a.add_element(root, header)
    a.write_to_xml('d:\\workspace\\test.xml')



