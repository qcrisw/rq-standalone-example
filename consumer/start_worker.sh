#!/bin/bash
echo Starting rq worker
rq worker --url $REDIS_URL $IN_QUEUE
