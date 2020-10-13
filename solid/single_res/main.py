from Employee import Employee, EmployeeDAO
from ReportFormatter import ReportType, EmployeeReportFormatter


class Main:
    def __call__(self):
        emp = Employee(1, 'Raj', 'Sales', True)
        self.hireEmployee(emp)
        self.printEmployeeReport(emp, ReportType.CSV)
        self.printEmployeeReport(emp, ReportType.XML)
        self.deleteEmployee(emp)

    def hireEmployee(self, employee):
        EmployeeDAO.save(employee)

    def deleteEmployee(self, employee):
        EmployeeDAO.remove(employee)

    def printEmployeeReport(self, employee, report_type):
        emp_report = EmployeeReportFormatter(employee, report_type)
        print(emp_report.get_formatted_employee())


main = Main()
main()