# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements/requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie todos os arquivos do diretório atual para o diretório /app no contêiner
COPY . .

# Exponha a porta 8000 para permitir conexões com o servidor Django
EXPOSE 8000
