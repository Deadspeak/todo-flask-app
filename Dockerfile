#Python image
FROM python:3.12-slim

#Set up working directory
WORKDIR /app

#Copy files
COPY requirements.txt
RUN pip install -r requirements.txt

#Port expose
EXPOSE 8000

#Startup command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
