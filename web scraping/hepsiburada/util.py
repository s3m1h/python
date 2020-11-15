import json
def json_save(data,path):
    with open(path + '.json','w',encoding='utf8') as f:
        json.dump(liste, f, indent=4)
        f.write("\n")