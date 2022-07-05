import json
import re
def main():
    with open('../raw') as f:
        raw=f.read().splitlines()
    with open('../document.json') as f:
        qdata=json.load(f)
    for i in qdata.values():
        for j in i:
            if j[0]=='´':
                raw.remove('https://gitlab.com/'+re.findall(r'^´(.*?)´',j)[0])
                continue
            raw.remove(re.findall(r'^{(.*?)}',j)[0])
    with open('not-documented.txt','w') as f:
        f.write('\n'.join(raw))
if __name__=='__main__':
    main()
