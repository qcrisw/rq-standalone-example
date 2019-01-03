def consume_func(job):
  if type(job) == bytes:
    job = job.decode('utf-8')
    job = int(job)
  print("Consumed job %d" % job)
