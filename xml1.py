# import sys
# import xml.etree.ElementTree as etree

# def get_attr_number(node):
#     # your code goes here
#     list = []
#     count = 0
#     for child in root.iter():
#         if child.attrib:
#             list.append(child.attrib)
#     for j in list:
#         if type(j) is dict:
#             count = count + len(j)
#     return(count)


# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))
