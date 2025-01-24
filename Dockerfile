# 1) Escolha da imagem-base
#    Aqui estamos usando Python 3.10 "slim", que é uma versão menor (menos pacotes pré-instalados).
FROM python:3.11-slim

# 2) Cria um diretório de trabalho no container
WORKDIR /app

# 3) Copia o arquivo de dependências (requirements.txt) para o container
COPY requirements.txt /app/

# 4) Atualiza o pip e instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5) Copia todo o restante do código para dentro de /app
COPY . /app/

# 6) Expõe a porta 8000 para acessar o servidor do Django
EXPOSE 8000

# 7) Comando default para iniciar a aplicação
#    Aqui vamos rodar o runserver, mas lembre que em produção,
#    normalmente você usaria gunicorn + nginx. Para fins de teste/desafio, ok.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
