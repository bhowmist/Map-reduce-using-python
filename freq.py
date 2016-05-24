#!/usr/bin/env python2.7
import mincemeat
import sys

# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

#Taking the filename from command line
enter=sys.argv
file = open(enter[1],'r')
data = list(file)
file.close()


# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    #considering the key count to keep track of taotal count of the numbers
    count='count'
    for char in v:
      #removing the new line characters
      if char !='\n':                
           char=char.lower()
           yield char, 1
           yield count,1

def reducefn(k, vs):
       if k=='count':
       		count=sum(vs)
       		return count
       result=sum(vs)
       return result
    

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
resultlist = []


for k in results.keys():
  #not appending the 'count' key value pair in ouput list
  if k !='count':
  	resultlist.append((k,results[k]))

#sorting the list  
resultlist = sorted(resultlist, key=lambda a: a[1])

     
#final output
for i in resultlist:
   q=float (i[1])/float (results['count'])
   print str(i[0]), str(round(q*100,2))+'%',str(i[1])

      
