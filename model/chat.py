##
# -*- coding: utf-8 -*-
##
##
# Chat model.
##

# Import custom modules.
from database import chroma
from llm import ollama


# Chat main model.
class chat(object):

  # Initializer.
  def __init__(self):
    self.chroma = chroma
    self.ollama = ollama

  # Run chat.
  def run(self,data):
    try:
      items = self.chroma.engine.get_or_create_collection('documents').query(
        query_embeddings=self.ollama.generate_embeddings(data['question']),
        n_results=5
      )
      context = '\n\n'.join(items.get('documents',[[]])[0])
      prompt = f"""
        Only use the below context to answer the question. Do not make up information.
        Context: {context}
        Question: {data['question']}
        Answer:
      """
      answer = self.ollama.generate_answer(prompt)
    except Exception as error:
      return False
    else:
      return answer
