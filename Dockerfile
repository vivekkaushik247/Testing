# This file executes the mqtt connection python script
FROM python:3
#ENV PATH /usr/local/bin:$PATH
#ENV PYTHON_VERSION 3.6.9
WORKDIR /home/vivek/Downloads/
#ADD /home/vivek/Downloads/mqttPublisher.py 
COPY "mqttPublisher.py" .
RUN pip3 install paho-mqtt
RUN pip3 install uuid
#ARG Conn_name
ENTRYPOINT ["python", "mqttPublisher.py"]
CMD ["VIVEK", "VIVEK01"]
