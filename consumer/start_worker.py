from os import environ as env
from urllib.parse import uses_netloc, urlparse
from redis import StrictRedis
from rq import Queue, Connection
from rq.worker import HerokuWorker as Worker

queue_name = env['IN_QUEUE']
url = env['REDIS_URL']

uses_netloc.append('redis')
url = urlparse(url)
# use StrictRedis to support ssl later on
conn = StrictRedis(host=url.hostname, port=url.port,
                   db=0, password=url.password)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, [queue_name]))
        worker.work()
