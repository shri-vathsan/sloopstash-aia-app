##
# -*- coding: utf-8 -*-
##
##
# Chat controller.
##

# Import community modules.
from flask import render_template

# Import custom modules.
from controller import root_web_controller
from model.chat import chat


# Chat web controller.
class chat_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    if self.request.path=='/chat/run':
      self.var['chat'] = {}
      return render_template('chat/run.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)

  # HTTP POST method processor.
  def post(self,*args,**kwargs):
    if self.request.path=='/chat/run':
      data = {
        'question':self.request.form.get('question')
      }
      self.var['chat'] = {}
      self.var['chat']['answer'] = chat().run(data)
      return render_template('chat/run.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)
