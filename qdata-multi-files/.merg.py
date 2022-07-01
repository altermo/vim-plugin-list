def main():
    text=[]
    with open('../raw') as f:
        raw=set(f.read().splitlines())
    def testinraw(name):
        if name not in raw:
            raise Exception(f'{name} is not in raw file: pleas add it to raw file')
    for k,v in {
            'colorscheme.txt':'{%s} : colorscheme',
            'forks.txt':'{%s} : is a fork of {%s}',
            'libs.txt':'{%s} : lib for {%s}',
            'links.txt':'{%s} : link to {%s}',
            'not-plugins.txt':'{%s} : not a plugin',
            'other.txt':'{%s} : %s',
            'telescope-extensions.txt':'{%s} : telescope extensions to %s',
            'use-instead.txt':'{%s} : is not maineind/depreciated, use {%s} isntead',
            'ide.txt':'{%s} : is an ide',
        }.items():
        with open(k) as f:
            file=f.read()
            if ' > ' in file: split=' > '
            elif ' : ' in file: split=' : '
            else: split=None
            for i in file.splitlines():
                if split:
                    beg,end=i.split(split)
                    if '>' in split:
                        testinraw(beg)
                        testinraw(end)
                    text.append(v%(beg,end))
                else:
                    testinraw(i)
                    text.append(v%i)
    with open('../quick-data.txt','w') as f:
        f.write('\n'.join(sorted(text)))
if __name__=='__main__':
    main()
