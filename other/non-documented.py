import json
import re
def main():
    out=''
    with open('../raw') as f:
        raw=f.read().splitlines()
    with open('../document.json') as f:
        data=json.load(f)
    for i in data.values():
        for j in i:
            if j.startswith('´'):
                j='´https://gitlab.com/'+j[1:]
            plug,=re.findall('^[{´](.*?)[}´]',j)
            raw.remove(plug)
    print('\n'.join(raw))
if __name__=='__main__':
    main()
