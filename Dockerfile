FROM ollama/ollama

WORKDIR /app
COPY requirements.txt .
COPY bot_menu.py .
COPY config.py .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

CMD ["sh", "-c", "ollama serve & python3 bot_menu.py"] 