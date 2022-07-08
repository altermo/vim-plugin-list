import json
BLOCSK=' ▏▎▍▌▋▊▉'
def first_letter(x:list)->None:
    first_letters=[i[0] for i in x]
    for i in set(first_letters):
        count=first_letters.count(i)
        present=count*1000//len(x)/10
        print(f'{i}|{present}%'.ljust(6)+'|'+count//8*'█'+BLOCSK[count%8])
def main()->None:
    with open('../raw') as f:
        raw=f.read().splitlines()
    with open('../document.json') as f:
        data=json.load(f)
        doc=sum((sum(i.values(),[]) for i in data.values()),[])
    print('Frequency of first letters:')
    first_letter(raw)
    print(f'Documented: {len(doc)}/{len(raw)}={len(doc)*1000//len(raw)/10}%')
if __name__=='__main__':
    main()
