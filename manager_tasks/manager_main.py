from manager import Manager
from developer import Developer

dev1 = Developer("rox", 34000, "Java")
dev2 = Developer("bob", 50000, "java")
dev3 = Developer("tim", 7000,  "Python")
dev4 = Developer("nina", 7000,  "java")
dev5 = Developer("hana", 7000,  "Python")

devs = [dev1, dev2, dev3, dev4, dev5]

mgr = Manager("Mo", 70000, devs)

print("Java Developers:")
java_devs = mgr.all_java_devs()
for dev in java_devs:
    print(dev.name)

print()

print("Python Developers:")
python_devs = mgr.all_python_devs()
for dev in python_devs:
    print(dev.name)
