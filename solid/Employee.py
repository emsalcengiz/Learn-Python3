from DatabaseConnection import DatabaseConnectionManager


class Employee:
    def __init__(self,id:int, name:str, dept:str, working:bool):
        self.id = id
        self.name = name
        self.dept = dept
        self.working = working

    def __str__(self):
        return f"Employee(id={self.id}, name={self.name},dept={self.dept},working={self.working})"


class EmployeeDAO:
    connectionManager = DatabaseConnectionManager()

    @classmethod
    def save(cls, employee):
        print(f"employee {employee} saved to db")
        pass

    @classmethod
    def remove(cls, employee):
        print(f"employee {employee} removed to db")
        pass