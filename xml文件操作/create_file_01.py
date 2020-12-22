#from xml.dom.minidom import *
# 创建一个文档对象
#from xml.dom.minidom import Document

from xml.dom import minidom
from xml.dom.minidom import parse

doc= minidom.Document()

#创建一个根节点
root= doc.createElement('Root')

#根节点添加属性
# root.setAttribute('company','中体彩')
# print(root.getAttribute('company'))

#根节点加入到tree
doc.appendChild(root)


#创建二级节点
company=doc.createElement('Header')
version=doc.createElement('Version')
version.appendChild(doc.createTextNode('001')) #添加文本节点

#创建一个带着文本节点的子节点
SenderCode=doc.createElement('SenderCode')
SenderCode.appendChild(doc.createTextNode('131101'))  #<ceo>吴总</ceo>

ReceiverCode = doc.createElement('ReceiverCode')
ReceiverCode.appendChild(doc.createTextNode('000899'))


company.appendChild(version) #name加入到company
company.appendChild(SenderCode)
company.appendChild(ReceiverCode)
root.appendChild(company)#company加入到根节点


print(doc.toxml())

#存成xml文件
fp=open('d:\\workspace\\test.xml','w',encoding='utf-8')
doc.writexml(fp,indent='',addindent='\t',newl='\n',encoding='utf-8')
fp.close()


domtree=parse('d:\\workspace\\test.xml')
datalist=domtree.documentElement
d={}
#获取标签为database的子节点
database=datalist.getElementsByTagName('Header')
print(database)

#database的子节点轮询，过滤掉textNode节点，取出文本值
for i in database[0].childNodes[1::2]:
    tag=i.tagName
    d[tag]=i.childNodes[0].data #childNodes 获取的是一个列表，通过childNodes[0]获取具体对象

print('root:',d)