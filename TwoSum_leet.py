import re

class newcls:
    def __init__(self):  # reading file name and target value
        self.file = input('Enter File Name')
        self.t = int(input('Enter target value'))
        self.arr = []

    def get_input(self):  # reading list of integer value from a file into an array

        with open(self.file, 'r') as data:
            string1 = data.read()
            arr = list(map(int, re.split('\W', string1)))

        #        value = list(map(int, filter(None, re.split('\W', string1))))

        print('List =', arr)
        self.arr = arr

    def sum1(self):  # finding indexes from the list whose sum value equals target
        found = 0
        for i in range(len(self.arr)):
            if found != self.t - self.arr[i] or i == 0:
                found = self.arr[i]
            else:
                return i - 1, i
        return 0, 0

    def prt(self):  # printing indexes / output
        index1, index2 = newcls.sum1(self)
        if index1 == 0 and index2 == 0:
            print("No target matching")
        else:
            out = [index1, index2]
            #    out.append(index1) #another way of inserting value in list
            #    out.append(index2)

            print(out)


obj1 = newcls()
obj1.get_input()
obj1.prt()
