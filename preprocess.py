import xlrd
import numpy

#       Initial Data
# Open the workbook and define the worksheet
book = xlrd.open_workbook("input/StudentList2.xlsx")
sheet = book.sheet_by_name("Initial Interviews by Firm")

firmNames = sheet.row_values(0)
studentSet = set()

for rx in range(1, sheet.nrows):
    for cell in sheet.row_values(rx):
        if cell:
            studentSet.add(cell)

# firmMap = { firm: index for index, firm in enumerate(firm) }
studentNames = list(studentSet)
studentMap = { student: index for index, student in enumerate(studentNames) }

meetings = numpy.zeros((len(firmNames), len(studentNames)), dtype=numpy.dtype(int))

for rx in range(1, sheet.nrows):
    for i, cell in enumerate(sheet.row_values(rx)):
        if cell:
            meetings[i, studentMap[cell]] = 1

print(meetings)
