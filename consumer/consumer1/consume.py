from json import loads

def consume_func(job, raw=False):
  # import logging; logging.basicConfig(level=logging.DEBUG)
  # logging.info(raw)
  if raw:
    job = loads(job.decode('utf-8'))
  print(f"consumed job {job['a']}")
