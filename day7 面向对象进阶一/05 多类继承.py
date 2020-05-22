# encoding = utf-8
__author__ = "Ang Li"


class Document:     # 抽象类
    def __init__(self, content):
        self.content = content

    def print(self):
        print('start...')
        raise NotImplementedError()     # 抽象方法


class Word(Document): pass
class Pdf(Document): pass


class PrintableWord(Word):  # OPC 原则，修改某个类时，不要直接修改，而是继承下来修改
    def print(self):
        print('word print format: <{}>'.format(self.content))


pw = PrintableWord('word')
pw.print()

