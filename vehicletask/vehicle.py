class Vehicle:

    def __init__(self, id):
        self.id = id
        self.hire_date = "None"
        self.return_date = "None"

    def __str__(self):
          return f" Vehicle Id: {self.id} Hire Date: {self.hire_date} Return Date: {self.return_date}"
