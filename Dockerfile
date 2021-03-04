FROM django
ADD . /penpirate
WORKDIR /penpirate
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]