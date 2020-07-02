from abc import ABC, abstractmethod

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee(ABC):
    @abstractmethod
    def __init__(self, code, name, salary, departament):
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.__departament = departament
        self.__work_hours = 8
    
    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.__work_hours

    def get_department(self):
        return self.__departament.name

    def set_department(self, name, code):
        self.__departament = Department(name, code)

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self._Employee__salary * 0.15

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale