from os import environ as env
from urllib.parse import uses_netloc, urlparse
from redis import StrictRedis
from rq import Queue

queue_name = env['OUT_QUEUE']
url = env['REDIS_URL']

uses_netloc.append('redis')
url = urlparse(url)
# use StrictRedis to support ssl later on
conn = StrictRedis(host=url.hostname, port=url.port,
                   db=0, password=url.password)

q = Queue(queue_name, connection=conn)

for i in range(1, 2):
  print("Producing job %d" % i)
  q.enqueue('consumer1.consume.consume_func', i)
  print("Producing job %d" % (i+1))
  q.enqueue('consumer1.consume.consume_func', f"{i+1}".encode('utf-8'), raw=True)
