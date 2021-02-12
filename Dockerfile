FROM python:3
RUN apt-get -y update
# for dlib
RUN apt-get install -y build-essential cmake
# for opencv
RUN apt-get install -y libopencv-dev

# pip install
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/