FROM python:3
RUN apt-get -y update
# for dlib
RUN apt-get install -y build-essential cmake
# for opencv
RUN apt-get install -y libopencv-dev

# pip install
RUN pip install --upgrade pip
RUN pip install numpy==1.20.1
RUN pip install opencv-python
RUN pip install dlib==19.17.0
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/