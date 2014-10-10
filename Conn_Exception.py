'''
Created on Aug 1, 2014

@author: naruto
'''
from __future__ import print_function
import re
class MyException(Exception):
    '''
    classdocs
    '''
    pass
class NameNotFound(MyException):
    """It creates a cycle to get teh string of the delimiter
    """
    def __mannually(self):
        while True:
            name_delimiter=raw_input('Delimiter: ')
            if re.search('[,/?&~!@#$%^*]', name_delimiter):
                print('Please use only alphanumeric or periods')
            else:
                print("Using delimiter: ", name_delimiter)
                break
        return name_delimiter
print('is', )