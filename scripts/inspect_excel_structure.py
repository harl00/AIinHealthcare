import pandas as pd

# Path to the Excel file
excel_path = 'data/aihw_injcat213_suppdatatables_bystate_v2_25112025.xlsx'

# Load the Excel file
excel_file = pd.ExcelFile(excel_path)

# Print all sheet names
print('Sheet names:')
print(excel_file.sheet_names)

# For each sheet, print the first 3 rows and column headers
for sheet in excel_file.sheet_names:
    print(f'\nSheet: {sheet}')
    df = pd.read_excel(excel_file, sheet_name=sheet)
    print('Columns:', df.columns.tolist())
    print(df.head(3))
