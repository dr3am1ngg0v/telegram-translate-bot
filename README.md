# *Telegram Translate Bot*
Митрофанов Иван Олегович Фт-320007

# **Описание**
Данный Телеграм-бот переводит отправленное сообщение на Английский язык, при этом отправленное сообщение может быть на любом другом языке.
Для установки бота необходимо:

### **1. Запуск через Python**

Клонируем репозиторий:
```bash
git clone git@github.com:dr3am1ngg0v/telegram-translate-bot
```

Создаем файл *.env* и записываем в него токен Телеграм-бота:
```env
TG_TOKEN="<tg-token-here>"
```

Затем активируем виртуальную среду Venv:

**Linux**

```bash
cd ./telegram-translate-bot
source venv/bin/activate
```

**Windows**
```
cd ./telegram-translate-bot
venv\bin\Activate
```

Если нет желания активировать *venv*, то просто устанавливаем библиотеки:
```bash
pip install -r requirements.txt
```

И запускаем бота:
```bash
python main.py
```

> ### **2. Запуск через Docker**

Клонируем репозиторий:
```bash
git clone git@github.com:dr3am1ngg0v/telegram-translate-bot
```

Создаем файл *.env* и записываем в него токен Телеграм-бота:
```env
TG_TOKEN="<tg-token-here>"
```

Содержимое Dockerfile:
```
FROM python:3.10-slim
WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

Создаем изображение в Docker и запускаем контейнер:
```bash
docker build -t tg-bot .
docker run -it tg-bot
```
