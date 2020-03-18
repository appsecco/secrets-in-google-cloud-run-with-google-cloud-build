FROM python:3.7

# Copying this separately prevents re-running pip install on every code change.
COPY requirements.txt ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

ARG SERV_AUTH_TOKEN
ENV AUTH_TOKEN=${SERV_AUTH_TOKEN}

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 main:app