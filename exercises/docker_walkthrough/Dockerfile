FROM python:3.9
LABEL maintainer="CodigoMatriz"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]
