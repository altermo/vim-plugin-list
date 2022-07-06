def main():
    with open('../raw') as f:
        raw=f.read().splitlines()
    with open('in.txt') as f:
        inp=f.read().splitlines()
    out=(i for i in map(str.lower,inp) if i not in raw)
    with open('out.txt','w') as f:
        f.write('\n'.join(out))
if __name__=='__main__':
    main()
