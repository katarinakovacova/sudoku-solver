FROM python:3.12.3-slim-bookworm

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY backend ./backend
COPY sudoku ./sudoku
COPY manage.py .

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
