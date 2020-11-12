import json

def json_save(data,path):
    with open("data/"+path+".json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, indent=4)
        write_file.write('\n')

        ###
# def app_download():
#     #url = "http://www.magicnotes.com/steelbytes/HD_Speed_ENG_Win32.zip"
#     url = download.get('onclick')[11:-13]
#     r = requests.get(url, stream=True)
#     if download is not None:
#         with open(baslik_name+".exe", 'wb') as write_file:
#             write_file.write(r.content)
