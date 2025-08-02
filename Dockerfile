# Usa uma imagem base do Python
FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libgl1 \
    mupdf \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Define o comando para iniciar o app Flask
CMD ["python", "app.py"]
