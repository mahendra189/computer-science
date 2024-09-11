from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# Function to create a table in an Excel file
def create_excel_table(output_excel_path):
    # Create a workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active

    # Sample data for the table
    # data = [
    #     ["ID", "Name", "Age", "City"],
    #     [1, "Alice", 30, "New York"],
    #     [2, "Bob", 24, "Los Angeles"],
    #     [3, "Charlie", 29, "Chicago"],
    #     [4, "David", 35, "Houston"]
    # ]
    data = [
        ["Name", "Standard", "Father's Name", "Percentage", "Documents"],
        ["John Doe", "10th", "Mr. Doe", 85.5, "Passport, Report Card"],
        ["Jane Smith", "9th", "Mr. Smith", 92.3, "Birth Certificate, Report Card"],
        ["Mike Brown", "11th", "Mr. Brown", 78.0, "ID Card, Report Card"],
        ["Emily Davis", "12th", "Mr. Davis", 88.7, "Passport, Report Card"]
    ]


    # Write the data to the worksheet
    for row in data:
        ws.append(row)

    # Define the range for the table
    table_range = f"A1:D{len(data)}"

    # Create a table
    table = Table(displayName="SampleTable", ref=table_range)

    # Add a default style with striped rows and banded columns
    style = TableStyleInfo(
        name="TableStyleMedium9",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=True
    )
    table.tableStyleInfo = style

    # Add the table to the worksheet
    ws.add_table(table)

    # Save the workbook to the specified file
    wb.save(output_excel_path)
    print(f"Table created and saved to {output_excel_path}")

# Define the path to the output Excel file
output_excel_path = 'path_to_your_excel_file.xlsx'

# Create the table in the Excel file
create_excel_table(output_excel_path)
