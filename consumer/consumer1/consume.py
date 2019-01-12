def consume_func(job, raw=False):
  if raw:
    job = job.decode('utf-8')
    job = int(job)
  print("Consumed job %d" % job)
