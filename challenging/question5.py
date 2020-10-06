class InputOutString(object):
    def __init__(self):
        self.s=""


    def getString(self):
        self.s=input()


    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()


#that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# items=[x for x in input().split(',')]
# items.sort()
# print(','.join(items))