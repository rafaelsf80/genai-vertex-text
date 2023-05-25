# gcloud auth configure-docker europe-west4-docker.pkg.dev
# gcloud builds submit --tag europe-west4-docker.pkg.dev/argolis-rafaelsanchez-ml-dev/ml-pipelines-repo/genai-text-demo
# gcloud run deploy genai-text-demo --port 7860 --image europe-west4-docker.pkg.dev/argolis-rafaelsanchez-ml-dev/ml-pipelines-repo/genai-text-demo --allow-unauthenticated --region=europe-west4 --platform=managed  --project=argolis-rafaelsanchez-ml-dev

# python3.8 breaks with gradio
FROM python:3.7

RUN pip install gradio 
RUN pip install google-cloud-aiplatform==1.25.0 google-cloud-logging

COPY ./app /app

WORKDIR /app

EXPOSE 7860

CMD ["python", "app.py"]