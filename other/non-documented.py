import json
def main():
    with open('../raw') as f:
        raw=f.read().splitlines()
    with open('../document.json') as f:
        data=json.load(f)
    for i in data.values():
            for plug in i:
                name,*_=plug
                raw.remove(name)
    print('\n'.join(raw))
if __name__=='__main__':
    main()
