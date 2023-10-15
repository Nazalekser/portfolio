'''You are given a valid XML document, and you have to print its score. 
The score is calculated by the sum of the score of each element. 
For any element, the score is equal to the number of attributes it has. '''


import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    score = 0
    for child in node.iter():
        score += len(child.attrib)
    return score


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# def get_attr_number(node):
#     return sum([len(child.attrib) for child in node.iter()])

# def get_attr_number(node):
#     counter = 0
#     counter += len(node.attrib)
#     for element in node:
#         counter += get_attr_number(element)
#     return counter


