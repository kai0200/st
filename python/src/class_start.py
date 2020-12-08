# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

'''
Class Test
基类要继承object，否则super(sonclass, self) 会无法生效
python3 使用super() python2 使用super(sonclass, self).function
'''

# 最简单类
class Test:
    pass

# 类的实例
class Person(object):
    def __init__(self, name, gender=0, weight=0, age=0):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.age = age

    def put(self):
        return({'name': self.name, 
                'gender': self.gender, 
                'weight': self.weight, 
                'age': self.age}
              )


# 继承
class Student(Person):
    def __init__(self, name, classroom = 503):
        Person.__init__(self, name)
        self.classroom = classroom

    def put(self):
        return({
                'name': self.name, 
                'gender': self.gender, 
                'weight': self.weight, 
                'age': self.age,
                'classroom': self.classroom
                })


class Computer(object):
    def __init__(self, pcname, cpusize=4, memsize=16, disksize=512):
        self.pcname = pcname
        self.cpusize = cpusize
        self.memsize = memsize
        self.disksize = disksize

    def put_pc(self):
        return(self.pcname, self.cpusize, self.memsize, self.disksize)


# 多重继承
class UniversityST(Student, Computer):
    def __init__(self, name, pcname="PC", universityName=""):
        Student.__init__(self, name)
        Computer.__init__(self, pcname)
        self.universityName = universityName

    def put_super(self):
        #Student.put(self) # 注意调取父类方法要加self
        #super().put(self) # 注意调取父类方法要加self
        super(UniversityST, self).put()

    def put_super_pc(self):
        Computer.put_pc(self)


if __name__ == '__main__':
    #person = Person('Bat Man')
    #person.gender = 1
    #person.weight = 150
    #person.age = 21
    #print(person.put())

    #student = Student('Supper Man')
    #print(student.put())

    uS = UniversityST('Jobs', pcname = 'Macbook pro')
    print(uS.put_super())  # 错误的定义方式
    print(uS.put_super_pc()) # 错误的定义方式

    #print(uS.put())
    #print(uS.put_pc())


