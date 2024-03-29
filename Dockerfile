# set base image (host OS)
FROM python:3.8

# set working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local source to working directory
COPY . .

# command to run on container start
CMD ["python","./server.py"]
