##
# -*- coding: utf-8 -*-
##
##
# Common helper.
##

# Import community modules.
import re


# Split text into chunks.
def split_text(value,size=1000,overlap=50):
  tokens = re.findall(r'\w+',value)
  items = []
  for item in range(0,len(tokens),size-overlap):
    items.append(' '.join(tokens[item:item+size]))
  return items
