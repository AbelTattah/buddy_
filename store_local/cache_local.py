from collections import defaultdict

class Cache_Local:
    def __init__(self) -> None:
        self.store = defaultdict()
    
    def setCache(self,key,value):
        self.store[key] = value
        return key+"assigned to value: "+ str(value)
    
    def getCache(self,key):
        keys = self.store.keys()
        for searh_key in keys:
            if searh_key==key:
                return self.store[key]
        return "not_set"


