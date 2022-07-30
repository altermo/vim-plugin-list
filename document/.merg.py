import json
import os
import re
def old_merg(data:dict)->None:
    with open('old-format/old.json') as f:
        old=json.load(f)
    for k,v in old.items():
        out=data.setdefault(k,[])
        for i in v:
            if '´' in i:
                if ':' in i:
                    name,text=re.findall(r'^´(.*?)´ : (.*)$',i)[0]
                else:
                    name,text=re.findall(r'^´(.*?)´()$',i)[0]
                out.append(['https://gitlab.com/'+name,text])
                continue
            if ':' in i:
                out.append(re.findall(r'^{(.*?)} : (.*)$',i)[0])
            else:
                out.append(re.findall(r'^{(.*?)}()$',i)[0])
def merg(data:dict):
    for mainname in os.listdir('new-format'):
        for subname in os.listdir(os.path.join('new-format/',mainname)):
            if subname=='other.txt':
                name=mainname
            else:
                name=subname.removesuffix('.txt')
            data.setdefault(name,[]).extend(extract(subname,os.path.join('new-format/',mainname)))
def extract(file:str,path:str)->list:
    out=[]
    with open(os.path.join(path,file)) as f:
        for i in f.read().splitlines():
            out.append(fmt(i))
    return out
def fmt(text:str)->list[str]:
    if 'https://gitlab.com' in text:
        if ':' in text:
            return re.findall(r'^\s*(https://gitlab\.com/*?/.*?)\s*:\s*(.*?)\s*$',text)[0]
        raise NotImplementedError
    if ':' in text:
        return re.findall(r'^\s*(.*?/.*?)\s*:\s*(.*?)\s*$',text)[0]
    return re.findall(r'^\s*(.*?/.*?)\s*()$',text)[0]
def check(data:dict)->None:
    uniq={}
    for k,v in data.items():
        for j in v:
            name,*_=j
            if name in uniq:
                raise Exception(f'"{name}" found 2 times: both in "{k}" and "{uniq[name]}"')
            uniq[name]=k
            if not name.islower():
                raise Exception(f'"{name}" is not all lowercase, in file "{k}"')
            if not re.findall(r'^(?:https://gitlab\.com/)?[a-z0-9_.-]+/[a-z0-9_.-]+$',name):
                raise Exception(f'"{name}" does not seem to be a valid plugin')
def main():
    data={}
    merg(data)
    old_merg(data)
    check(data)
    with open('../document.json','w') as f:
        json.dump(data,f)
if __name__=='__main__':
    main()
