import Classes.Path as Path
#import bs4
import re

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.
# Please add comments along with your code.
class TrecwebCollection:
    doc_no = -1

    def __init__(self):
        # 1. Open the file in Path.DataWebDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!

      
        f = open(Path.DataWebDir, errors="ignore")
        xml = f.read()
        self.m = re.compile("<DOC>(.*?)</DOC>", re.DOTALL).findall(xml)
        return

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        # 3. the HTML tags should be removed in document content.
        #global doc_no
        self.doc_no=self.doc_no+1
        #global m
        if (self.doc_no >= len(self.m)):
            return None
        docNo = re.compile('<DOCNO>(.*?)</DOCNO>', re.DOTALL).findall(self.m[self.doc_no])
        content = re.compile('<TEXT>(.*?)</TEXT>', re.DOTALL).findall(self.m[self.doc_no])

        return [docNo, content]
    

