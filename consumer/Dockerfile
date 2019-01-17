FROM python:3.6.5

WORKDIR /home

# upgrade pip itself
RUN pip3 install --upgrade pip

# copy requirements first to cache the deps
COPY rq-standalone-example/consumer/requirements.txt /home
COPY /rq /home/rq/
RUN pip3 install -r requirements.txt

# copy the rest of the crawler source
COPY rq-standalone-example/consumer/ /home

# CMD ["./start_worker.sh"]
CMD ["python3", "-u", "start_worker.py"]
