##
# -*- coding: utf-8 -*-
##
##
# Document controller.
##

# Import community modules.
import math
from decimal import Decimal
from flask import render_template,jsonify,redirect

# Import custom modules.
from controller import root_web_controller
from model.document import document


# Document web controller.
class document_web_controller(root_web_controller):

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    if self.request.path=='/documents':
      if self.request.args.get('count'):
        documents = document().count()
        if documents>0:
          limit = Decimal(5.0)
          pages = math.ceil(documents/limit)
          return jsonify({'status':'success','result':{'count':documents,'pages':int(pages)}})
        else:
          return jsonify({'status':'failure','message':'Not available.'})
      else:
        limit = 5
        offset = (int(self.request.args.get('page'))*limit)-limit if self.request.args.get('page') else 0
        documents = document().list(offset=offset,limit=limit)
        return jsonify({'status':'success','result':{'items':documents}})
    elif self.request.path=='/document/create':
      return render_template('document/create.html',var=self.var)
    elif self.request.path=='/document/'+args[0]+'/update':
      document_id = args[0]
      self.var['document'] = document().get(document_id)
      return render_template('document/update.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)

  # HTTP POST method processor.
  def post(self,*args,**kwargs):
    if self.request.path=='/document/create':
      data = {
        'name':self.request.form.get('name'),
        'description':self.request.form.get('description'),
        'content':self.request.form.get('content')
      }
      if document().create(data) is True:
        return redirect('/dashboard')
      else:
        return render_template('error.html',var=self.var)
    elif self.request.path=='/document/'+args[0]+'/update':
      data = {
        'name':self.request.form.get('name'),
        'description':self.request.form.get('description'),
        'content':self.request.form.get('content')
      }
      data['document_id'] = args[0]
      if document().update(data) is True:
        return redirect('/dashboard')
      else:
        return render_template('error.html',var=self.var)
    else:
      return render_template('error.html',var=self.var)
