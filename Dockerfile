FROM ubuntu:18.04

# Install system dependencies
RUN apt-get -y update && apt-get install -y --fix-missing \
    build-essential \
    pkg-config \
    software-properties-common \
    python3.6 python3-dev python3-virtualenv \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

# Set working directory
RUN mkdir -p /home/microservice
WORKDIR /home/microservice

# Setup virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

# Install project dependencies
COPY requirements.txt requirements.txt
RUN pip install gunicorn
RUN pip install uWSGI
RUN pip install -r requirements.txt

# Copy project
COPY ./ ./

# Run service
CMD ["python3", "aadhaar_verifier.py"]
