# Business Management

Este projeto é um sistema de gerenciamento de usuários e empresas, desenvolvido em Python 3.9 utilizando o framework Django. Ele inclui agendamento de tarefas com Django-Q e Redis como message broker. O objetivo principal é fornecer uma plataforma web para registrar e gerenciar informações de usuários e empresas, além de oferecer integração com a Receita Federal para atualização automática de dados das empresas.

## Funcionalidades Principais

- **Cadastro de Usuário:** Os usuários podem se registrar fornecendo informações básicas como nome, sobrenome, e-mail e senha.
- **Cadastro de Empresa:** As empresas podem ser registradas com detalhes como CNPJ, Razão Social e Nome Fantasia. Os usuários podem estar associados a múltiplas empresas.
- **Login de Usuário:** Autenticação de usuários através do e-mail e senha registrados.
- **Cadastro de Membros na Empresa:** Permite aos usuários adicionar membros a uma empresa específica.
- **Listagem de Empresas do Usuário:** Retorna todas as empresas associadas ao usuário logado.
- **Listagem de Membros de uma Empresa:** Retorna todos os membros associados a uma empresa específica.

### Atualização Automática de Dados

O sistema realiza atualizações automáticas dos dados das empresas utilizando a API da Receita Federal. Após 30 dias da criação de uma empresa, o sistema acessa a API para atualizar informações como Razão Social, Nome Fantasia e Status/Situação.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.9
- pip (Gerenciador de pacotes do Python)

## Configuração do Ambiente

1. **Clone o repositório do projeto:**
git clone https://github.com/andrey-f-cassio/business_management.git
cd business_management

2. **Crie um ambiente virtual:**
python3 -m venv .venv

3. **Ative o ambiente virtual:**
- No Windows:
  ```
  .\.venv\Scripts\activate
  ```
- No Linux:
  ```
  source .venv/bin/activate
  ```

4. **Instale as dependências do projeto:**
- pip install pip-tools
- pip-compile requirements/requirements.in
- pip-sync requirements/requirements.txt

## Configuração do Django

Execute estes comandos para configurar o Django:

1. **Migrações do banco de dados:**
python manage.py migrate

2. **Crie um superusuário (opcional):**
python manage.py createsuperuser

3. **Execute o servidor de desenvolvimento:**
python manage.py runserver

Agora, você pode acessar o projeto em `http://127.0.0.1:8000/` no seu navegador.

### Usando Docker Compose
1. Instale o Docker.
2. dentro da pasta raiz do projeto execute ```docker-compose up --build```
3. Agora, você pode acessar o projeto em http://127.0.0.1:8000/ no seu navegador.
