import re
import typing


class newcls:
    def __init__(self):  # defining list  of integer and target value
        string1 = input()
        self.arr = list(map(int, filter(None, re.split('\W', string1))))
        self.t = int(input())

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
            out.append(index1)
            out.append(index2)

            print(out)


obj1 = newcls()
obj1.prt()
