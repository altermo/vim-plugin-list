import json
class Assembler:
    def __init__(self,rawlist:list,data:dict,pre:str,qdocs:list)->None:
        self.text=pre
        self.data=data
        self.qdocs=qdocs
        self.raw=rawlist
    def create(self)->str:
        self.create_jumplist()
        self.create_recommend()
        self.create_extdocs()
        self.create_qdocs()
        self.create_raw()
        return self.text
    def create_jumplist(self)->None:
        pass #TODO
    def create_extdocs(self)->None:
        doc='# Extensions/readmore/options/...\n'
        for k,v in self.data.get('extensions',{}).items():
            doc+=self.plugtolink(k)+' : '+', '.join(f'[{name}]({link})' for name,link in v.items())+'\n'
        self.text+=doc
    def create_recommend(self)->None:
        doc='# Lists\n'
        for name,recommend in self.data.get('lists',{}).items():
            doc+=f'<details><summary>{name}</summary>\n\n'
            doc+=''.join(f'* {typ} : {self.plugtolink(name)}\n' for typ,name in recommend.items())
            doc+=f'</details>\n'
        doc+='\n'
        self.text+=doc
    def create_qdocs(self)->None:
        self.text+='# Quick-documented-list\n'
        for i in self.qdocs:
            name=i.split(':')[0].removesuffix(' ')
            self.raw.remove(name)
            self.text+=self.pluglinkweb(name).removesuffix('\n')+' :'+i.split(':',1)[1]+'\n'
    def pluglinkweb(self,name:str)->str:
        if name.startswith('https://gitlab.com'):linkpre=''
        else:linkpre='https://github.com'
        pre='  *'
        return f'{pre} [{name}]({linkpre}/{name})\n'
    def plugtolink(self,x:str)->str:
        return self.pluglinkweb(x)
    def create_raw(self)->None:
        self.text+='# Non-documented-list\n'
        self.text+='\n'.join(self.pluglinkweb(i) for i in self.raw)+'\n'
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

_Pleas tell me if non main links should take you to its place in list or to its website_

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_Other vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins)_

'''
    with open('README.md','w') as f:
        f.write(Assembler(rawlist,data,pre,qdocs).create())
if __name__=="__main__":
    main()
