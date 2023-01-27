FROM python:3.9.16

WORKDIR /app

# Install Flask and other required packages
COPY ./app/requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy the flask app files
COPY ./app /app

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
