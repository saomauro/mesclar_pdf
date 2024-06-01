# mesclar_pdf
Combinar arquivos pdf em um único arquivo

## Como usar

1. Baixe a última versão do programa em [Releases](https://github.com/saomauro/mesclar_pdfs/releases)
2. Copie o arquivo "mesclar_pdfs.exe" para uma pasta do computador.
3. Execute o arquivo.
4. Escolha a pasta onde estão os arquivos pdf a serem combinados.
5. Escolha o nome e local do arquivo final.
6. Clique em combinar.

## Como Desenvolver

### 1) Clone o repositório e altere para branch develop
```shell
git clone git@github.com:saomauro/mesclar_pdf.git
cd mesclar_pdf
git switch develop
```

### 2) Monte um ambiente virtual

```shell
python -m venv venv
```

### 3) Ativar o ambiente virtual

#### 3.1) Windows Powershell
```shell
& .\venv\Scripts\activate.ps1
```
#### 3.2) Windows Cmd
```shell
venv\Scripts\activate.bat
```

### 4) Instalar as dependências
```shell
pip install -r requirements.txt
```

### 5) Instalar o PyInstaller
```shell
pip install pyinstaller
```

### 6) Gerar o executável
```shell
pyinstaller --onefile mesclar_pdfs.py
```
