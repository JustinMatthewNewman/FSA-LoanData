import pandas as pd

delimiter = 'Loan Type Code:'
loans = open('lynnData.txt', 'r').read().split(delimiter)
loans.pop(0)
list_loans = []
for loan in loans:
    list_loans.append((delimiter + loan).split('\n'))

cols = [
    'Loan Type Code:', 'Loan Type Description:', 'Loan Award ID:', 'Loan Attending School Name:',
    'Loan Date:', 'Loan Repayment Begin Date:', 'Loan Period Begin Date:', 'Loan Period End Date:',
    'Loan Amount:', 'Loan Disbursed Amount:', 'Loan Canceled Amount:', 'Loan Canceled Date:',
    'Loan Outstanding Principal Balance:', 'Loan Outstanding Interest Balance:',
    'Loan Most Recent Payment Effective Date:', 'Loan Next Payment Due Date:',
    'Loan Cumulative Payment Amount:', 'Loan PSLF Cumulative Matched Months:', 'Academic Level:',
    'Award Year:', 'Capitalized Interest:', 'Net Loan Amount:', 'UpdtDt:',
    'Current Loan Status Description:', 'Current Standard-Standard Schedule Payment Amount:',
    'Permanent Standard-Standard Schedule Payment Amount:', 'Loan Status Effective Date:',
    'Loan Interest Rate Type Description:', 'Loan Interest Rate:', 'Loan Actual Interest Rate:', 'Loan Statutory Interest Rate:'
]

data = []
stop_len = len(cols)
for loan in list_loans:
    temp_loan = []
    for c in cols:
        for line in loan:
            if line.startswith(c):
                temp_loan.append(line.split(':')[1].replace('$', '').replace(',', '').replace('%', ''))
    if len(temp_loan) > stop_len:
        for n in range(len(temp_loan) - stop_len):
            temp_loan.pop()
    data.append(temp_loan)

df = pd.DataFrame.from_records(data, columns=list(map(lambda c: c.replace(':', ''), cols)), coerce_float=True)

def create_excel_from_data(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)
    print(f"Excel file '{excel_file}' has been created.")

excel_file = 'student_loan_data.xlsx'
create_excel_from_data(df, excel_file)

