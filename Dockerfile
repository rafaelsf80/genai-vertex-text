FROM python:3.8

RUN pip install gradio>=3.36.1
RUN pip install google-cloud-aiplatform==1.25.0 google-cloud-logging

COPY ./app /app

WORKDIR /app

EXPOSE 7860

CMD ["python", "app.py"]
