# from flask import Flask, render_template, request, make_response, g
from redis import Redis
import os
import socket
import random
import json

redis = Redis(host="redis", db=0, socket_timeout=5)

while True:

    voter_id = hex(random.getrandbits(64))[2:-1]
    vote = 'b'
    data = json.dumps({'voter_id': voter_id, 'vote': vote})
    redis.rpush('votes', data)

