FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-dev python3-pip python3-venv 
 
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -U -r requirements.txt
COPY fsubbot.py fsubbot.py
EXPOSE 5000
CMD python3 fsubbot.py
