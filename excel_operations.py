import pandas as pd

def extract_unique_rows(input_excel_path, output_excel_path):
    """
    Extract unique rows from the input Excel sheet and save to a new Excel file.
    """
    # Read the input Excel file
    df = pd.read_excel(input_excel_path)
    
    # Remove duplicate rows based on ID and global code columns
    df_unique = df.drop_duplicates(subset=["Id", "Global Code"])
    
    # Save the unique rows to a new Excel file
    df_unique.to_excel(output_excel_path, index=False)


def compare_id_columns(input_excel1_path, input_excel2_path, output_excel_path):
    """
    Compare ID columns between two Excel sheets and save the result to a new Excel file.
    Extract only the data where the ID has different codes.
    """
    # Read the input Excel files
    df1 = pd.read_excel(input_excel1_path)
    df2 = pd.read_excel(input_excel2_path)
    
    # Merge the two dataframes on the ID column
    merged_df = pd.merge(df1, df2, on="Id", suffixes=("_1", "_2"), how="inner")
    
    # Filter the merged dataframe to include only rows where the codes are different
    different_code_df = merged_df[merged_df['Global Code_1'] != merged_df['Global Code_2']]
    
    # Save the comparison result to a new Excel file
    different_code_df.to_excel(output_excel_path, index=False)
