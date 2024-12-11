from flat import Bill, Flatmate
from pdfgenerate import PdfReport

input_amount = int(input('Enter the amount of the bill: '))
input_period = input('Enter the period of the bill: ')
input_name1 = input('Enter the name of the first flatmate: ')
input_days1 = int(input('Enter the number of days the first flatmate stayed in the house: '))
input_name2 = input('Enter the name of the second flatmate: ')
input_days2 = int(input('Enter the number of days the second flatmate stayed in the house: '))

bill1 = Bill(input_amount, input_period)
flatmate1 = Flatmate(input_name1, input_days1)
flatmate2 = Flatmate(input_name2, input_days2)

report_generator = PdfReport(f'{bill1.period}.pdf')
report_generator.generate(flatmate1,flatmate2,bill1)


print(flatmate1.pays(bill1,flatmate2))
print(flatmate2.pays(bill1,flatmate1))