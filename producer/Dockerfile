FROM python:3.6.5

WORKDIR /home

# upgrade pip itself
RUN pip3 install --upgrade pip

# copy requirements first to cache the deps
COPY rq-standalone-example/producer/requirements.txt /home
RUN pip3 install -r requirements.txt
COPY /rq /home/rq
RUN pip3 install -e ./rq
# copy the rest of the crawler source
COPY rq-standalone-example/producer/ /home

CMD ["python3", "produce.py"]
