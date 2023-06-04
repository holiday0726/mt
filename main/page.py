class Page:
    pages = []
    current = 0
    
    @classmethod
    def next(cls):
        cls.pages[cls.current] = None
        cls.current+=1
        
    
