class Page:
    pages = []
    currentPageNum = 0
    backgroundColor = 0
    
    @classmethod
    def next(cls):
        cls.pages[cls.currentPageNum] = None
        cls.currentPageNum+=1
    
    @classmethod
    def getCurrentPage(cls):
        return cls.pages[cls.currentPageNum]
    
    @classmethod
    def appendPage(cls, page):
        cls.pages.append(page)
    
    @classmethod
    def extendPage(cls, pages):
        cls.pages.extend(pages)
    
    @classmethod
    def getTotalPageNum(cls):
        return len(cls.pages)
