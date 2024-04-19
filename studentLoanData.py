import pandas as pd
input_file_path = 'lynnData.txt'

# split the input on the loan type code delimitter
loans = open(input_file_path, 'r').read().split('Loan Type Code:')

data = []

for loan in loans:
    loan_map = {}

    # split each loan details into individual strings
    loan_details = loan.splitlines() 

    # remove the lingering loan type code
    loan_details.pop(0) 

    for line in loan_details:

        # Create a key value mapping of each loan's details
        key, value = line.split(':', 1)
        value = value.replace('$', '').replace(',', '').replace('%', '')
        loan_map[key] = value

    # add each loan mapping to a list of loan mappings
    data.append(loan_map)

# convert to data frame and export to excel file.
df = pd.DataFrame(data)

def create_excel_from_data(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)
    print(f"Excel file '{excel_file}' has been created.")

excel_file = 'student_loan_data.xlsx'
create_excel_from_data(df, excel_file)

