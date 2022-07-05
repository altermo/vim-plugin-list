import os
import json
def remake(x:list[list[str]],pat:str,mid:str=' : ')->list[str]:
    prepat1='{%s}'+mid
    prepat2='%s´'+mid
    return [(prepat1+pat if i[0][0]!='´' else prepat2+pat)%tuple(i) for i in x]
def categorys(data:dict)->None:
    for i in os.listdir('categorys/'):
        cat,_=os.path.splitext(i)
        with open(f'categorys/{i}') as f:
            data[cat]=remake([i.split(' : ') for i in f.read().splitlines()],'%s')
def docs(data:dict)->None:
    for i in os.listdir('docs/'):
        cat,_=os.path.splitext(i)
        with open(f'docs/{i}') as f:
            pat,*text=f.read().splitlines()
            data[cat]=remake([i.split(' : ') for i in text],pat)
def linked(data:dict)->None:
    for i in os.listdir('linked/'):
        cat,_=os.path.splitext(i)
        with open(f'linked/{i}') as f:
            pat,*text=f.read().splitlines()
            data[cat]=remake([i.split(' > ') for i in text],pat)
def types(data:dict)->None:
    for i in os.listdir('types/'):
        cat,_=os.path.splitext(i)
        with open(f'types/{i}') as f:
            data[cat]=remake([i.split(' : ') for i in f.read().splitlines()],'','')
def main()->None:
    data={}
    categorys(data)
    docs(data)
    linked(data)
    types(data)
    with open('../document.json','w') as f:
        json.dump(data,f)
if __name__=='__main__':
    main()
