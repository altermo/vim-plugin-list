import json
import re
class Assembler:
    def __init__(self,rawlist:list[str],data:dict[str,dict[str,dict[str,str]]],pre:str,end:str,qdocs:dict[str,dict[str,list[list[str]]]])->None:
        self.text=pre
        self.data=data
        self.qdocs=qdocs
        self.raw=rawlist
        self.end=end
    def create(self)->str:
        self.check()
        self.create_jumplist()
        self.create_extdocs()
        self.create_qdocs()
        self.create_raw()
        return self.text+self.end
    def check(self):
        for cat in self.qdocs.values():
            for doc in cat:
                name,text=doc
                for i in re.findall(r'\{(.*?)\}',text):
                    if i not in self.raw:
                        raise Exception(f'"{i}" not in raw')
                if name not in self.raw:
                    raise Exception(f'"{name}" not in raw')
        uniq=set(self.raw)
        for i in self.raw:
            if i not in uniq:
                raise Exception(f'raw contains duplicates "{i}"')
            uniq.remove(i)
            if not i.islower():
                raise Exception(f'{i} is not all lowercase')
            if not re.findall(r'^(?:(?:https://gitlab\.com/)|(?:https://git\.sr\.ht/~))?[a-z0-9_.-]+/[a-z0-9_.-]+$',i):
                raise Exception(f'{i} does not seem to be a valid plugin')
    def create_jumplist(self)->None:
        doc='# Jump list\n'
        doc+='  * [extensions/options/readmore/...](#extensionsreadmoreoptions)\n'
        doc+='  * [documented](#documented)\n'
        for i in self.qdocs:
            doc+=f'    * [{i}](#{i})\n'
        doc+='  * [not documented](#not-documented)\n'
        doc+='  * [donate](#donate)\n'
        self.text+=doc
    def create_extdocs(self)->None:
        doc='# Extensions/readmore/options/...\n'
        for k,v in self.data.get('extensions',{}).items():
            doc+=f'  * {self.pluglinkweb(k)} : '+', '.join(f'[{name}]({link})' for name,link in v.items())+'\n'
        self.text+=doc
    def create_qdocs(self)->None:
        self.text+='# Documented\n'
        for k,v in self.qdocs.items():
            self.text+=f'## {k}\n'
            for j in sorted(v):
                name,text=j
                self.raw.remove(name)
                if text:
                    self.text+=f'  * {self.pluglinkweb(name)} : {self.formatplug(text)}\n'
                else:
                    self.text+=f'  * {self.pluglinkweb(name)}\n'
    @staticmethod
    def formatplug(text:str)->str:
        return re.sub(r'\{([a-z0-9A-Z._-]*?/[a-z0-9A-Z._-]*?)\}',r'[\1](https://github.com/\1)',text)
    def pluglinkweb(self,name:str)->str:
        if name.startswith('https://gitlab.com/'):
            linkpre='https://gitlab.com'
            name=name.removeprefix('https://gitlab.com/')
        else:linkpre='https://github.com'
        return f'[{name}]({linkpre}/{name})'
    def create_raw(self)->None:
        self.text+='# Not-documented\n'
        self.text+=''.join(f'  * {self.pluglinkweb(i)}\n' for i in self.raw)
def main():
    with open('raw') as f:
        rawlist=f.read().splitlines()
    with open('data.json') as f:
        data=json.load(f)
    with open('document.json') as f:
        qdocs=json.load(f)
    pre=r'''# vim-plugin-list
This is a list of plugins.

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_NOTE: this list was documented over a span of multiple months and has some weirdness (in othe words, it would not be weird to presume that I was high when writing this (I was not))._

_Other BETER vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [awesome-nvim](https://github.com/rockerBOO/awesome-neovim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins), [vim-galore](https://github.com/mhinz/vim-galore/blob/master/PLUGINS.md), [](https://github.com/astier/vlugins)_

'''
    end=r'''
# Donate
If you want to donate then you need to find the link:
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a](https://www.buymeacoffee.com/altermo) [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()'''
    with open('README.md','w') as f:
        f.write(Assembler(rawlist,data,pre,end,qdocs).create())
if __name__=="__main__":
    main()
