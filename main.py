import os
import time
import pandas as pd

# Set the folder path where the CSV files are located

folder_path ='/Users/samihabdeljabbar/TM/example_folder'

while True:
    # Get the list of CSV files in the folder

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

 Check if there is at least one CSV file in the folder
    if len(csv_files) > 0:
        # Get the first CSV file in the list (assuming there is only one CSV file in the folder)
        csv_file = csv_files[0]

    # Read the CSV file into a DataFrame 
        df = pd.read_csv(os.path.join(folder_path, csv_file))

        # Create separate DataFrames for withdrawals, deposits, and checks
        withdrawals = df[df['Transaction Type'] == 'Withdrawal']
        deposits = df[df['Transaction Type'] == 'Deposit']
        checks = df[df['Transaction Type'] == 'Check']

        # Create a Pandas Excel writer using xlsxwriter as the engine
        writer = pd.ExcelWriter('transactions.xlsx', engine='xlsxwriter')

        # Write each DataFrame to a different worksheet in the same workbook
        withdrawals.to_excel(writer, sheet_name='Withdrawals', index=False)
        deposits.to_excel(writer, sheet_name='Deposits', index=False)
        checks.to_excel(writer, sheet_name='Checks', index=False)

        # Save the workbook
        writer.save()

        # Wait for 5 seconds before checking the folder again
        time.sleep(5)
    else:
        # Wait for 5 seconds before checking the folder again
        time.sleep(5)
