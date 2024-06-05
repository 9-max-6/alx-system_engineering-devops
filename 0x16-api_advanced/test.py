                         
#!/usr/bin/python3

max = {
  "name": "Random Item",
  "price": 12.99,
  "inStock": True,
  "category": "Electronics",
  "details": {
    "brand": "Acme",
    "color": "Blue",
    "weight": 2.5
  }
}

def flatten_dict(dicts,result={}):
    for key, value in dicts.items():
        if isinstance(value, dict):
            flatten_dict(value, result)
        else:
            result[key] = value
    return result