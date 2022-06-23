import json
class Assembler:
    def __init__(self,rawlist:list,data:dict,pre:str,qdocs:list)->None:
        self.text=pre
        self.data=data
        self.qdocs=qdocs
        self.raw=rawlist
        self.tags=self.data.get('tags',{})
        self.plugs=self.data.get('plugins',{})
        self.level=1
        self.ind1='  '*self.level+'*'
        self.ind2='  '*(self.level+1)+'*'
    def create(self)->str:
        self.init_tags()
        self.init_plugs()
        self.create_jumplist()
        self.create_recommend()
        self.create_docs()
        self.create_qdocs()
        self.create_raw()
        self.create_tags()
        return self.text
    def init_tags(self)->None:
        self.linktags=set(self.tags)
    def init_plugs(self)->None:
        self.linkplugs=set(self.data.get('forcelink',[]))
        for maincategory in self.plugs.values():
            for subcategory in maincategory.values():
                for plugdata in subcategory.values():
                    self.linkplugs|=set(i for i in plugdata.get('requiers',[]))
                    self.linkplugs|=set(i for i in plugdata.get('optional',[]))
        for recommend in self.data.get('lists',{}).values():
            self.linkplugs|=set(recommend.values())
    def create_jumplist(self)->None:
        pass #TODO
    def create_recommend(self)->None:
        doc='# Lists\n'
        for name,recommend in self.data.get('lists',{}).items():
            doc+=f'<details><summary>{name}</summary>\n\n'
            doc+=''.join(f'* {typ} : {self.plugtolink(name)}\n' for typ,name in recommend.items())
            doc+=f'</details>\n'
        doc+='\n'
        self.text+=doc
    def create_docs(self)->None:
        self.text+='# Documented-list\n'
        for name,maincategory in self.plugs.items():
            self.text+=f'## {name}\n'
            for name,subcategory in maincategory.items():
                self.text+=f'### {name}\n'
                for name,plugdata in sorted(subcategory.items(),key=lambda x:x[0].split('/')[1]):
                    self.raw.remove(name)
                    self.chech_plug(name,plugdata)
                    self.doc_from_plug(name,plugdata)
    def create_qdocs(self)->None:
        self.text+='# Quick-documented-list\n'
        for i in self.qdocs:
            name=i.split(':')[0].removesuffix(' ')
            self.raw.remove(name)
            self.text+='* '+self.pluglinkweb(name)+' '+i.split(':',1)[1]+'\n'
    def chech_plug(self,name:str,plugdata:dict)->None:
        if 'last-update' not in plugdata:
            raise Exception(f'{name} has no last-update')
        if 'tags' not in plugdata:
            raise Warning(f'{name} has no tags')
        if 'docs' not in plugdata:
            raise Warning(f'{name} has no docs')
    def pluglinkweb(self,name:str)->str:
        if name in self.linkplugs:
            return f'{self.ind1} ###### [{name}](https://github.com/{name})\n'
        else:
            return f'{self.ind1} [{name}](https://github.com/{name})\n'
    def doc_from_plug(self,name:str,plugdata:dict)->None:
        doc=self.pluglinkweb(name)
        if (tags:=plugdata.get('tags',[])):
            doc+=f'{self.ind2} Tags: '+', '.join(self.tolink(i) if i in self.linktags else i for i in tags)+'\n'
        doc+=self.list2str(f'{self.ind2} Requiers: ',[self.plugtolink(i) for i in plugdata.get('requiers',[])])
        doc+=self.list2str(f'{self.ind2} Requirements: ',plugdata.get('requirements',[]))
        if (docs:=plugdata.get('docs','')):
            doc+=f'{self.ind2} '+docs+'\n'
        if (readmore:=plugdata.get('readmore',{})):
            doc+=f'{self.ind2} Readmore: '
            doc+=', '.join(f'[{k}]({v})' for k,v in readmore.items())
            doc+='\n'
        self.text+=doc
    @staticmethod
    def tolink(x:str)->str:
        return f'[{x}](#{x})'
    @staticmethod
    def plugtolink(x:str)->str:
        return f'[{x}](#{x.replace("/","").replace(".","")})'
    @staticmethod
    def list2str(title:str,x:list)->str:
        if len(x):return title+', '.join(x)+'\n'
        else:return ''
    def create_raw(self)->None:
        self.text+='# Non-documented-list\n'
        self.text+='\n'.join(self.pluglinkweb(i) for i in self.raw)+'\n'
    def create_tags(self)->None:
        self.text+='# Tags\n'
        self.text+='\n'.join(f'* ###### {name}\n{tagdata}' for name,tagdata in self.tags.items())
def main():
    with open('raw') as f:
        rawlist=f.read().split('\n')
    with open('data.json') as f:
        data=json.load(f)
    with open('quick-data.txt') as f:
        qdocs=f.read().split('\n')
        if '' in qdocs:qdocs.remove('')
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
