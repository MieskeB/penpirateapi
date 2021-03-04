FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN [ "python", "manage.py runserver 0.0.0.0:8000" ]