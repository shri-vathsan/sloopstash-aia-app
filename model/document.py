##
# -*- coding: utf-8 -*-
##
##
# Document model.
##

# Import community modules.
import json

# Import custom modules.
from database import redis,chroma
from llm import ollama
from helper import split_text


# Document main model.
class document(object):

  # Initializer.
  def __init__(self):
    self.redis = redis
    self.chroma = chroma
    self.ollama = ollama

  # Create document.
  def create(self,data):
    try:
      id = self.redis.engine.incr(
        self.redis.conf['key_prefix']['document']['counter']
      )
      chunks = split_text('\n'.join([data['name'],data['description'],data['content']]))
      embeddings = []
      for chunk in chunks:
        embeddings.append(self.ollama.generate_embeddings(chunk)[0])
      self.chroma.engine.get_or_create_collection('documents').add(
        ids=[str(id)+':c'+str(index) for index,item in enumerate(chunks)],
        documents=chunks,
        embeddings=embeddings
      )
      del data['content']
      self.redis.engine.hset(
        self.redis.conf['key_prefix']['document']['main'],id,json.dumps(data)
      )
    except Exception as error:
      return False
    else:
      return True

  # Update document.
  def update(self,data):
    try:
      id = data['document_id']
      chunks = split_text('\n'.join([data['name'],data['description'],data['content']]))
      embeddings = []
      for chunk in chunks:
        embeddings.append(self.ollama.generate_embeddings(chunk)[0])
      self.chroma.engine.get_or_create_collection('documents').update(
        ids=[str(id)+':c'+str(index) for index,item in enumerate(chunks)],
        documents=chunks,
        embeddings=embeddings
      )
      del data['document_id']
      del data['content']
      self.redis.engine.hset(
        self.redis.conf['key_prefix']['document']['main'],id,json.dumps(data)
      )
    except Exception as error:
      return False
    else:
      return True

  # Get document.
  def get(self,id):
    data = self.redis.engine.hget(
      self.redis.conf['key_prefix']['document']['main'],id
    )
    if data:
      item = {
        'id':id
      }
      item.update(json.loads(data))
      return item
    else:
      return

  # Count of documents.
  def count(self):
    count = self.redis.engine.hlen(
      self.redis.conf['key_prefix']['document']['main']
    )
    return count

  # List documents.
  def list(self,**kwargs):
    offset = kwargs['offset'] if 'offset' in kwargs else 0
    limit = kwargs['limit'] if 'limit' in kwargs else 5
    data = self.redis.engine.hgetall(
      self.redis.conf['key_prefix']['document']['main']
    )
    items = []
    for key,value in data.items():
      item = {
        'id':int(key)
      }
      item.update(json.loads(value))
      items.append(item)
    return items
