import yaml

with open('data.yaml') as f:
    
    docs = yaml.load_all(f, Loader=yaml.UnsafeLoader)

    for doc in docs:
        
        for k, v in doc.items():
            print(k, "->", v)