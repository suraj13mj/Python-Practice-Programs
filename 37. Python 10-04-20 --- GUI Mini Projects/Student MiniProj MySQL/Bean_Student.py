class Student:
    def __init__(self,name='',rollno=0,address='',college='',branch='',sex='',news=0):
        self.__rollno = rollno
        self.__name = name
        self.__address = address
        self.__college = college
        self.__branch = branch
        self.__sex = sex
        self.__news = news

    @property
    def Rollno(self):
        return self.__rollno
    @Rollno.setter
    def Rollno(self,rollno):
        self.__rollno = rollno

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name):
        self.__name = name

    @property
    def Address(self):
        return self.__address
    @Address.setter
    def Address(self,address):
        self.__address = address

    @property
    def College(self):
        return self.__college
    @College.setter
    def College(self,college):
        self.__college = college

    @property
    def Branch(self):
        return self.__branch
    @Branch.setter
    def Branch(self,branch):
        self.__branch = branch

    @property
    def Sex(self):
        return self.__sex
    @Sex.setter
    def Sex(self,sex):
        self.__sex = sex

    @property
    def News(self):
        return self.__news
    @News.setter
    def News(self,news):
        self.__news = news

    
