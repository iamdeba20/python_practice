class Chapter:
    def __init__(self,title,pagecount):
        self.titile=title
        self.pagecount=pagecount

class book:
    def __init__(self,title):
        self.title=title
        self.chapter=[]
    def addchapter(self,chapter):
        self.chapter.append(chapter)
    def pagecounts(self):
        sum=0
        for ch in self.chapter:
            sum=sum+ch.pagecount
        return sum

b = book("Python Basics")

c1 = Chapter("Intro", 10)
c2 = Chapter("Loops", 20)

b.addchapter(c1)
b.addchapter(c2)

print(b.pagecounts())   # Output: 30
