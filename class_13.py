'''
Delegation: you can model can-do relationships,
where an object hands a task over to another object
'''

class Stack:
    def __init__(self, items=None):
        #._items that can take its initial data from the items argument
        if items is None:
            self._items = []
        else:
            self._items = list(items)
            
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        return self._items.pop()
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._items})"
    
