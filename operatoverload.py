class Student:
    def __init__(self,m1,m2):
        """

        :rtype: object
        """
        self.m1=m1
        self.m2 = m2
    def __add__(self, other):
        m1=self.m1 + other.m1
        m2 = self.m2 + other.m2
        S3 = Student(m1,m2)
        print(S3.m2)
        return S3
    def sum(self,a=None,b=None,c=None):
        if a!= None and b!=None and c!= None:
            s=a+b+c
        elif a!= None and b!=None:
            s=a+b
        else:
            s=a
        return s

S1 = Student(33,44)
S2 =Student(11,11)
S3 = S1 + S2
print(S3.m1)
print(S1.sum(5,4,6))