import json
import re
def main():
    with open('../raw') as f:
        raw=f.read().splitlines()
    with open('../document.json') as f:
        data=json.load(f)
    for i in data.values():
        for j in i.values():
            for k in j:
                if k.startswith('´'):
                    k='´https://gitlab.com/'+k[1:]
                plug,=re.findall('^[{´](.*?)[}´]',k)
                raw.remove(plug)
    print('\n'.join(raw))
if __name__=='__main__':
    main()
