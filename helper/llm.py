##
# -*- coding: utf-8 -*-
##
##
# LLM helper.
##

# Import community modules.
import ollama as _ollama

# Import custom modules.
from config import ollama_conf


# Ollama LLM helper.
class ollama(object):

  # Instances.
  _instances = dict()

  # Constructor.
  def __new__(self):
    if 'instance' in ollama._instances:
      return ollama._instances['instance']
    else:
      self.conf = ollama_conf
      self.engine = _ollama.Client(
        host='http://' \
          +self.conf['endpoint']+':' \
          +str(self.conf['port'])
      )
      return super(ollama,self).__new__(self)

  # Initializer.
  def __init__(self):
    ollama._instances['instance'] = self

  # Generate Ollama embeddings.
  def generate_embeddings(self,input):
    return self.engine.embed(
      model=self.conf['embedding']['model']['name']+':'+self.conf['embedding']['model']['size'],
      input=input
    ).embeddings

  # Generate Ollama answer.
  def generate_answer(self,prompt):
    return self.engine.generate(
      model=self.conf['language']['model']['name']+':'+self.conf['language']['model']['size'],
      prompt=prompt,
      stream=False
    ).response


# Launch LLM helpers.
ollama = ollama()
