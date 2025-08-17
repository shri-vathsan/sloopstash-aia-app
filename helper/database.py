##
# -*- coding: utf-8 -*-
##
##
# Database helper.
##

# Import community modules.
import sys
import pysqlite3
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import redis as _redis
import chromadb

# Import custom modules.
from config import redis_conf,chroma_conf


# Redis database helper.
class redis(object):

  # Instances.
  _instances = dict()

  # Constructor.
  def __new__(self):
    if 'instance' in redis._instances:
      return redis._instances['instance']
    else:
      self.conf = redis_conf
      self.engine = _redis.Redis(connection_pool=_redis.ConnectionPool(
        host=self.conf['endpoint'],
        port=self.conf['port'],
        max_connections=10,
        db=0
      ))
      return super(redis,self).__new__(self)

  # Initializer.
  def __init__(self):
    redis._instances['instance'] = self


# Chroma database helper.
class chroma(object):

  # Instances.
  _instances = dict()

  # Constructor.
  def __new__(self):
    if 'instance' in chroma._instances:
      return chroma._instances['instance']
    else:
      self.conf = chroma_conf
      self.engine = chromadb.HttpClient(
        host=self.conf['endpoint'],
        port=self.conf['port']
      )
      return super(chroma,self).__new__(self)

  # Initializer.
  def __init__(self):
    chroma._instances['instance'] = self


# Launch database helpers.
redis = redis()
chroma = chroma()
