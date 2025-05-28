# Use uma imagem oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Instala ferramentas e dependências para build de confluent-kafka
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    librdkafka-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir --timeout=1000 -r requirements.txt

# Copia todo o código da aplicação para dentro do container
COPY . .

# Comando padrão para rodar a aplicação
CMD ["python", "pipeline.py"]
