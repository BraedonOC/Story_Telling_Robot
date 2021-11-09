from ubuntu:18.04

WORKDIR /story_telling_robot

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # Essentials
    sudo git vim lsb-release unzip\
    cmake automake build-essential checkinstall \
    autoconf libtool \
    curl wget gnupg2 \
    ca-certificates openssl  \
    python2 \
    # Things I like
    htop tmux
 
RUN apt -y install python-tk 

RUN python get-pip.py && \
    rm get-pip.py &&\
    python -m pip install pip &&\

# Copy the naoqi SDK into the /story_telling_robot directory
COPY pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/ ./pynaoqi-python2.7-2.8.6.23-linux64-20191127_152327/



