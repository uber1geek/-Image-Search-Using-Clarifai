import os
import sys
from clarifai.client import ClarifaiApi
from clarifai.rest import ClarifaiApp
import sqlite3
import pprint


def create_table():
  conn = sqlite3.connect('search.db')
  conn.execute('CREATE TABLE IF NOT EXISTS imgTags(url text, tags text)')
  conn.close()

def data_entry(imgUrl, imgTags):
  conn = sqlite3.connect('search.db')
  conn.execute('INSERT INTO imgTags (URL, TAGS) VALUES ("'+imgUrl+'", "'+imgTags+'")')
  conn.commit()
  conn.close()


global_path = ""



# In[6]:

def main(argv):
  if len(argv) > 1:
    imageurl = argv[1]
  else:
    imageurl = 'https://samples.clarifai.com/metro-north.jpg'
    print(" -- Using the default since no local directory was provided")
    print(" -- Must input url, directory path, or file path")

  api = ClarifaiApp()
  create_table()

  #for attr in dir(api):
    #print "obj.%s = %s" % (attr, getattr(api, attr))

  if imageurl.startswith('http'):
    model = api.models.get('general-v1.3')
    #print model.predict_by_url(imageurl)
    response = model.predict_by_url(imageurl)
    iterableArray = response['outputs'][0]['data']['concepts']
    #pprint.pprint(iterableArray[0]['name'])
    #pprint.pprint(response['outputs'][0]['data']['concepts'])
    tags = "";
    for key in iterableArray:
      tags+= key['name']+","
      
    data_entry(imageurl, tags)



  elif os.path.isdir(imageurl):
    model = api.models.get('general-v1.3')
    response = model.predict_by_url(imageurl)
    iterableArray = response['outputs'][0]['data']['concepts']
    tags = "";
    for key in iterableArray:
      tags+= key['name']+","
      
    data_entry(imageurl, tags)
    


  elif os.path.isfile(imageurl):
    with open(imageurl,'rb') as image_file:
      response = model.predict_by_url(imageurl)
      iterableArray = response['outputs'][0]['data']['concepts']
      tags = "";
      for key in iterableArray:
        tags+= key['name']+","
      
    data_entry(imageurl, tags)

  else:
    raise Exception("Must input url, directory path, or file path")



if __name__ == '__main__':
  main(sys.argv)
  



