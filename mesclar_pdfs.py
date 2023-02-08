import PyPDF2
import PySimpleGUI as sg
import os

sg.theme('Dark Blue 3')
layout = [
    [sg.Text('Pasta: '), sg.InputText(key='entrada', disabled=True),
     sg.FolderBrowse('...')],
    [sg.Text('Saída: '), sg.InputText(key='saida', disabled=True),
     sg.FileSaveAs('...', file_types=(('PDF', '.pdf'),))],
    [sg.Button('Combinar'), sg.Button('Sair')]
]

window = sg.Window('Combinar arquivos PDF', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Combinar':
        pasta = values['entrada']

        if pasta.endswith('\\') or pasta.endswith('/'):
            pasta = pasta[:-1]

        arquivos = os.listdir(pasta)
        arquivos.sort()
        with PyPDF2.PdfMerger() as merger:
            for arquivo in arquivos:
                if os.path.isfile(f'{pasta}/{arquivo}') and arquivo.lower().endswith('.pdf'):
                    merger.append(f'{pasta}/{arquivo}')
            merger.write(values['saida'])

window.close()
