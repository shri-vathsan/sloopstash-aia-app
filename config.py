##
# -*- coding: utf-8 -*-
##
##
# Config module.
##

# Import community modules.
import os
import json


# Load main.conf configuration file.
def main_conf():
  file = open('conf/main.conf','r')
  conf = file.read()
  conf = json.loads(conf)
  file.close()
  return conf

# Load static.conf configuration file.
def static_conf():
  file = open('conf/static.conf','r')
  conf = file.read()
  conf = json.loads(conf)
  file.close()
  if 'STATIC_ENDPOINT' in os.environ:
    conf['endpoint'] = os.environ['STATIC_ENDPOINT']
  return conf

# Load redis.conf configuration file.
def redis_conf():
  file = open('conf/redis.conf','r')
  conf = file.read()
  conf = json.loads(conf)
  file.close()
  return conf

# Load chroma.conf configuration file.
def chroma_conf():
  file = open('conf/chroma.conf','r')
  conf = file.read()
  conf = json.loads(conf)
  file.close()
  return conf

# Load ollama.conf configuration file.
def ollama_conf():
  file = open('conf/ollama.conf','r')
  conf = file.read()
  conf = json.loads(conf)
  file.close()
  return conf


# Invoke functions.
main_conf = main_conf()
static_conf = static_conf()
redis_conf = redis_conf()
chroma_conf = chroma_conf()
ollama_conf = ollama_conf()
