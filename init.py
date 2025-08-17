##
# -*- coding: utf-8 -*-
##
##
# Bootstrap AIA app service.
##

# Import community modules.
import sys

# Append App specific Python paths.
sys.path.append('model')
sys.path.append('controller')
sys.path.append('helper')

# Import community modules.
import argparse
from flask import Flask,request

# Import custom modules.
from controller.user import user_web_controller
from controller.document import document_web_controller
from controller.chat import chat_web_controller


# Health web controller.
def health_web_controller():
  return str('OK')

# View dashboard.
def dashboard():
  if request.method=='GET':
    return user_web_controller(request).get()
  else:
    return None

# Create document.
def create_document():
  if request.method=='GET':
    return document_web_controller(request).get()
  elif request.method=='POST':
    return document_web_controller(request).post()
  else:
    return None

# Update document.
def update_document(arg_0):
  if request.method=='GET':
    return document_web_controller(request).get(str(arg_0))
  elif request.method=='POST':
    return document_web_controller(request).post(str(arg_0))
  else:
    return None

# List documents.
def list_documents():
  if request.method=='GET':
    return document_web_controller(request).get()
  else:
    return None

# Run chat.
def run_chat():
  if request.method=='GET':
    return chat_web_controller(request).get()
  elif request.method=='POST':
    return chat_web_controller(request).post()
  else:
    return None


# Initialize Flask app.
app = Flask('AIA app',template_folder='view')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# App routes.
app.add_url_rule('/health',view_func=health_web_controller)
app.add_url_rule('/dashboard',view_func=dashboard)
app.add_url_rule('/document/create',view_func=create_document,methods=['GET','POST'])
app.add_url_rule('/document/<int:arg_0>/update',view_func=update_document,methods=['GET','POST'])
app.add_url_rule('/documents',view_func=list_documents)
app.add_url_rule('/chat/run',view_func=run_chat,methods=['GET','POST'])


if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--port',type=int,default=2000)
  parser.add_argument('--host',default='0.0.0.0')
  args = parser.parse_args()
  try:
    print('Starting AIA app service...')
    app.run(debug=True,host=args.host,port=args.port)
  except KeyboardInterrupt:
    print('Stopping AIA app service...')
  finally:
    pass
