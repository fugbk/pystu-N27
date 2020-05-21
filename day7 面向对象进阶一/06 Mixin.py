# encoding = utf-8
__author__ = "Ang Li"


class Document:
    def __init__(self, content):
        self.content = content


class Word(Document): pass
class Pdf(Document): pass


# 作为一个补充方法，添加功能
class PrintableMixin:   # Mixin类，都会以Mixin结尾
    def print(self):
        print('in mixin: <{}>'.format(self.content))    # 执行print时，的self.content 会根据mro向上查找


class PrintableWord(PrintableMixin, Word):      # 先继承Mixin，然后才是 Word。这样mro中Mixin的优先级高于Word
    print('print word')                         # 也就实现了Mixin中的方法，覆盖其他类的。


print(PrintableWord.mro())
pw = PrintableWord('test word')
pw.print()