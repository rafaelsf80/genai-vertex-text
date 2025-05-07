# python3.8 breaks with gradio
FROM python:3.11

RUN pip install gradio==5.29.0
RUN pip install google-cloud-aiplatform==1.91.0 google-cloud-logging==3.12.1 google-genai==1.13.0

COPY ./app /app

WORKDIR /app

EXPOSE 7860

CMD ["python", "app.py"]