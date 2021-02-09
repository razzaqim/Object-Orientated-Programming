from employee import Employee
from developer import Developer

class Manager(Employee):
    """ this is the manager class """
    def __init__(self, name, salary, staff):
        super().__init__(name, salary)
        self.staff = staff

    def all_java_devs(self):
        java_devs = []
        for dev in self.staff:
            if isinstance(dev, Developer) and dev.language.lower() == "java":
                 java_devs.append(dev)
        return java_devs

    def all_python_devs(self):
        python_devs = []
        for dev in self.staff:
            if dev.language == "Python":
                python_devs.append(dev)
        return python_devs