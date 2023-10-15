'''You are given an HTML code snippet of n lines.
Your task is to print the single-line comments, multi-line comments and the data.

Print the result in the following format:

>>> Single-line Comment  
Comment
>>> Data                 
My Data
>>> Multi-line Comment  
Comment_multiline[0]
Comment_multiline[1]
>>> Data
My Data
>>> Single-line Comment:  
'''

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment", data, sep='\n')
        else:
            print(">>> Single-line Comment", data, sep='\n')

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data", data, sep='\n')


parser = MyHTMLParser()

html = ''
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser.feed(html)

'''
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str):
        print(f">>> Multi-line Comment\n{data}") if "\n" in data else print(
            f">>> Single-line Comment\n{data}")

    def handle_data(self, data: str):
        if data != "\n":
            print(f">>> Data\n{data}")


N = int(input())
parser = MyHTMLParser()

parser.feed("\n".join([input() for _ in range(N)]))
'''
