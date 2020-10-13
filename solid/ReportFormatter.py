from enum import Enum


class ReportType(Enum):
    CSV = 1
    XML = 2


class ReportFormatter:
    def __init__(self, report_obj, report_type: ReportType):

        self.report_obj = report_obj
        self.report_type = report_type
        if self.report_type == ReportType.CSV:
            self.__formatted_out = self.__convertToCsv()
        elif self.report_type == ReportType.XML:
            self.__formatted_out = self.__convertToXml()
        else:
            self.__formatted_out = None

    def __convertToXml(self):
        return "XML : <title> " + str(self.report_obj) + "</title>"

    def __convertToCsv(self):
        return "CSV : ,,, " + str(self.report_obj) + ",,,"

    def get_output(self):
        return self.__formatted_out


class EmployeeReportFormatter(ReportFormatter):
    def __init__(self, employee, report_type: ReportType):
        super(EmployeeReportFormatter, self).__init__(employee, report_type)

    def get_formatted_employee(self):
        return self.get_output()