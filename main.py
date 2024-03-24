import excel_operations

# File paths for input and output Excel files
input_excel1_path = "input_excel1.xlsx"
input_excel2_path = "input_excel2.xlsx"
output_excel_unique_path = "output_unique.xlsx"
output_excel_comparison_path = "output_comparison.xlsx"

# Extract unique rows from the first Excel sheet and save to a new Excel file
excel_operations.extract_unique_rows(input_excel1_path, output_excel_unique_path)

# Compare ID columns between two Excel sheets and save the result to a new Excel file
excel_operations.compare_id_columns(input_excel1_path, input_excel2_path, output_excel_comparison_path)
