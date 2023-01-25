class  Chairman:
    cname = "Name"
    NoOfHods = 8
class Hod(Chairman):
    name = input("enter name:")
    deptno = 2
class Faculty(Hod):
    NoOfFaculty =    100
obj = Faculty()
print(obj.deptno