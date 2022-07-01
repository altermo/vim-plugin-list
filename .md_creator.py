import json
import re
class Assembler:
    def __init__(self,rawlist:list,data:dict,pre:str,qdocs:list)->None:
        self.text=pre
        self.data=data
        self.qdocs=qdocs
        self.raw=rawlist
    def create(self)->str:
        self.create_jumplist()
        self.create_extdocs()
        self.create_qdocs()
        self.create_raw()
        return self.text
    def create_jumplist(self)->None:
        pass #TODO
    def create_extdocs(self)->None:
        doc='# Extensions/readmore/options/...\n'
        for k,v in self.data.get('extensions',{}).items():
            doc+=f'  * {self.pluglinkweb(k)} : '+', '.join(f'[{name}]({link})' for name,link in v.items())+'\n'
        self.text+=doc
    def create_qdocs(self)->None:
        self.text+='# Quick-documented-list\n'
        for i in self.qdocs:
            name=i.split(':')[0].removesuffix('} ').removeprefix('{')
            self.raw.remove(name)
            self.text+=f'  * {self.formatplug(i)}\n'
    def formatplug(self,text:str)->str:
        return re.sub(r'\{(.*?)\}',r'[\1](https://github.com/\1)',text)
    def pluglinkweb(self,name:str)->str:
        if name.startswith('https://gitlab.com'):linkpre=''
        else:linkpre='https://github.com'
        return f'[{name}]({linkpre}/{name})'
    def create_raw(self)->None:
        self.text+='# Non-documented-list\n'
        self.text+=''.join(f'  * {self.pluglinkweb(i)}\n' for i in self.raw)
def main():
    with open('raw') as f:
        rawlist=f.read().splitlines()
    with open('data.json') as f:
        data=json.load(f)
    with open('quick-data.txt') as f:
        qdocs=f.read().splitlines()
    pre=r'''# vim-plugin-list
This is a list of plugins.
_TODO: categorize, document and remove not plugins_

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_Other vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [awesome-nvim](https://github.com/rockerBOO/awesome-neovim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins), [vim-galore](https://github.com/mhinz/vim-galore/blob/master/PLUGINS.md)_

'''
    with open('README.md','w') as f:
        f.write(Assembler(rawlist,data,pre,qdocs).create())
if __name__=="__main__":
    main()
