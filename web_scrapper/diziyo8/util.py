import json
def json_save(data,path):
    with open('data/'+ path + '.json','w',encoding='utf8') as f:
        json.dump(data, f,indent=4,ensure_ascii=False)
        f.write('\n')