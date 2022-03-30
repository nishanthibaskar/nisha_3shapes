#Start by pulling the python image
FROM python:latest

RUN apt-get -y update

RUN apt-get -y install nginx
RUN apt-get -y install python3-dev
RUN apt-get -y install build-essential

#Create a new directory app
RUN mkdir /app
#Make the workdir
WORKDIR /app
# Copy the requirements file into the image
COPY requirements.txt .
# install the requirements.txt
RUN pip install -r requirements.txt

# copy the code to appropriate locations
COPY trdl.py /app/trdl.py
COPY startup.sh /app/startup.sh
COPY uwsgi.ini /app/uwsgi.ini

COPY nginx.conf /etc/nginx

#Make the startup executable, expose port 80 and run startup file for nginx.
RUN chmod +x ./startup.sh

EXPOSE 8080

CMD [ "./startup.sh" ]