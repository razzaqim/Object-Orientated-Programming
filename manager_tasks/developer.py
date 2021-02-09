from employee import Employee

class Developer(Employee):
    """ This is the developer class """

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language 