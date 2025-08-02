# app_empenho.py
import os, shutil, threading, webbrowser
import pdfquery, openpyxl
from flask import Flask, request, render_template, send_file, redirect, url_for

app = Flask(__name__)

def empty_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('pdf_file')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdfs_dir = os.path.join(base_dir, 'pdfs')
        rascunhos_dir = os.path.join(base_dir, 'RascunhosGerados')
        modelo_excel = os.path.join(base_dir, 'Modelo.xlsx')

        coordinates = [  # conforme definido
            {'left': 200.0, 'top': 549.52, 'width': 16.68, 'height': 10.0},
            {'left': 41.0, 'top': 418.52, 'width': 374.62, 'height': 10.0},
            {'left': 421.0, 'top': 642.52, 'width': 50.02, 'height': 10.0},
            {'left': 200.0, 'top': 464.52, 'width': 139.57, 'height': 10.0},
            {'left': 200.0, 'top': 503.52, 'width': 56.7, 'height': 10.0},
            {'left': 43.0, 'top': 627.52, 'width': 387.29, 'height': 10.0},
            {'left': 125.0, 'top': 306.52, 'width': 122.66, 'height': 10.0},
            {'left': 122.0, 'top': 503.52, 'width': 33.36, 'height': 10.0},
            {'left': 296.0, 'top': 503.52, 'width': 33.36, 'height': 10.0},
            {'left': 485.0, 'top': 503.52, 'width': 73.88, 'height': 10.0},
            {'left': 407.0, 'top': 503.52,'width': 33.36, 'height': 10.0},
        ]

        shutil.copy(modelo_excel, os.path.join(pdfs_dir, "Temp_Consolidado.xlsx"))
        workbook = openpyxl.load_workbook(os.path.join(pdfs_dir, "Temp_Consolidado.xlsx"))
        sheet = workbook.active

        for i, pdf_file in enumerate(uploaded_files):
            path = os.path.join(pdfs_dir, pdf_file.filename)
            pdf_file.save(path)
            pdf = pdfquery.PDFQuery(path)
            pdf.load()

            for j, coord in enumerate(coordinates):
                el = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' %
                            (coord['left'], coord['top'], coord['left'] + coord['width'], coord['top'] + coord['height']))
                sheet.cell(row=i+2, column=j+1).value = el.text().strip()

        final_name = f"Rascunho inicial-{sheet.cell(row=2, column=1).value}.xlsx"
        final_path = os.path.join(rascunhos_dir, final_name)
        workbook.save(final_path)
        workbook.close()

        return redirect(url_for('download_excel', filename=final_name))

    return render_template('index.html')

@app.route('/download_excel/<filename>')
def download_excel(filename):
    path = os.path.join('RascunhosGerados', filename)
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    empty_folder('pdfs')
    empty_folder('RascunhosGerados')
    threading.Thread(target=lambda: webbrowser.open('http://localhost:5000')).start()
    print('Servidor iniciado na porta http://localhost:5000 !')

    app.run(host='0.0.0.0', port=5000, debug=False)
