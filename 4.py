##Implement the function sort_by_price_ascending, which:
##Accepts a string a json format, as in the example below
##Orders items by price in ascending order.
##if two products have the same price, it orders them by their name in alphabetical order
## returns a string in Json format that is equivalent to the one in the input format
##for example the call 
##sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee", "price":9.99},{"name":"rice","price":4.04}]');
##should return
##[{"name":"eggs","price":1},"{"name":"rice","price":4.04},{"name":"coffee", "price":9.99}]'


import json
from pandas.io.json import json_normalize 

def sort_by_price_ascending(json_string):
   if json_string=="": return "Empty String"
   s=json.loads(json_string)
   df = json_normalize(s)
   df.sort_values(['price', 'name'], ascending=[True, True],inplace=True)
   out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
   return(out)
  
    
print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))