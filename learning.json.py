import json
data = {'name':'john','age':'30','city':'new york'}
with open('output.json','w') as file:
    json.dump(data,file)

with open('pretty_output.json','w')as file:
    json.dump(data,file,indent=4)

with open('output.json','r')as file:
    data = json.load(file)
    print(data)