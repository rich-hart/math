import yaml
import json
import os
from os.path import basename,splitext,join
def book_to_json(path):
    book = dict([ (splitext(basename(f))[0],join(path,f)) for f in os.listdir(path) ])
    for (k,v) in book.items():
        with open(v,'r') as f:
            if 'bib' in v:
                book[k]= f.read()
            else:
                book[k]=yaml.load(f)
    return json.dumps(book)

def book_to_dict(path):
    pass

def book_to_statment_list(path):
    pass
