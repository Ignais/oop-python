'''
Enum: iterable by default
'''

from enum import Enum

class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
if __name__ == "__main__":
    
    print(WeekDay.MONDAY)
    print(list(WeekDay))
    