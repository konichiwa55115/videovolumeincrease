FROM python:3.9-buster
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN apt-get install -y libavfilter-dev
RUN apt install dos2unix
RUN apt-get install yasm libvpx. libx264. -y
RUN pip3 install -U pip
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
RUN git clone https://github.com/konichiwa55115/vidmk /LazyDeveloper && cd /LazyDeveloper && git clone https://github.com/GregorR/rnnoise-models&& cd /
WORKDIR /LazyDeveloper
RUN cd /LazyDeveloper &&  python bot.py
