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
python -m virtualenv venv
```

### 3) Instalar as dependências

```shell
pip install -r requirements.txt
```

### 5) Gerar o executável

```shell
cd src
pyinstaller --onefile mesclar_pdfs.py
```
