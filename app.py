from flask import Flask, render_template, request,send_file
import excel_operations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get file paths from the form
        input_excel1_path = request.files['input_excel1_path']
        input_excel2_path = request.files['input_excel2_path']
        
        # Define output file paths
        output_excel_unique_path = "output_unique.xlsx"
        output_excel_comparison_path = "output_comparison.xlsx"
        
        # Save uploaded files
        input_excel1_path.save(input_excel1_path.filename)
        input_excel2_path.save(input_excel2_path.filename)
        
        # Extract unique rows and compare ID columns
        excel_operations.extract_unique_rows(input_excel1_path.filename, output_excel_unique_path)
        excel_operations.compare_id_columns(input_excel1_path.filename, input_excel2_path.filename, output_excel_comparison_path)
        
        return render_template('index.html', message="Excel files processed successfully!", 
                               output_excel_unique=output_excel_unique_path,
                               output_excel_comparison=output_excel_comparison_path)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
