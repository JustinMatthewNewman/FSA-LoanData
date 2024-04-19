import pandas as pd

delimiter = 'Loan Type Code:'
loans = open('lynnData.txt', 'r').read().split(delimiter)

data = []
for loan in loans:
    
    loan_map = {}
    
    lines = loan.splitlines()
    lines.pop(0)

    for line in lines:
    
        key, value = line.split(':', 1)
        value = value.replace('$', '').replace(',', '').replace('%', '')
        loan_map[key] = value

    data.append(loan_map)


df = pd.DataFrame(data)
print(df)


def create_excel_from_data(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)
    print(f"Excel file '{excel_file}' has been created.")

excel_file = 'student_loan_data.xlsx'
create_excel_from_data(df, excel_file)

