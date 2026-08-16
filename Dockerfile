FROM python:3.12
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install pydantic['email']
COPY alembic.ini /alembic.ini
COPY alembic /alembic
COPY main.py /main.py
COPY app /app
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]

EXPOSE 8000

