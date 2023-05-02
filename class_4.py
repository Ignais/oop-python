'''
Getter and Setter
'''

class PersonNonCorrect:
    '''
        This way isn't popular in Python community.
    '''
    
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
        
class PersonCorrect:
    '''
    This is the most popular way.
    '''
    
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.upper()
        
if __name__ == "__main__":
    
    juan = PersonNonCorrect("Juan")
    
    pedro = PersonCorrect("Pedro")
    
    print(juan.get_name())
    
    print(pedro.name)