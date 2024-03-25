from flask import Flask, render_template, request, send_file
import excel_operations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get file paths from the form
        input_excel1 = request.files['input_excel1_path']
        input_excel2 = request.files['input_excel2_path']
        
        # Define output file paths
        output_excel_unique_path = "output_unique.xlsx"
        output_excel_comparison_path = "output_comparison.xlsx"
        
        # Save uploaded files
        input_excel1.save(input_excel1.filename)
        input_excel2.save(input_excel2.filename)
        
        # Process Excel files
        excel_operations.extract_unique_rows(input_excel1.filename, output_excel_unique_path)
        excel_operations.compare_id_columns(input_excel1.filename, input_excel2.filename, output_excel_comparison_path)
        
        # Provide download links in response
        return render_template('download.html', output_excel_unique=output_excel_unique_path, output_excel_comparison=output_excel_comparison_path)

    return render_template('index.html')

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
