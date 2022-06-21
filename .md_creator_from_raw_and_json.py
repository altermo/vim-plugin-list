import json
def doc_from_plug(plugdata:dict,plug:str)->str:
    doc=''
    if plugdata.get('islinked',False):
        doc+=f'* ###### [{plug}](https://github.com/{plug})\n'
    else:
        doc+=f'* [{plug}](https://github.com/{plug})\n'
    linktags=plugdata.get('linktags',[])
    tags=plugdata.get('tags',[])
    if tags or linktags:
        doc+='  * Tags: '
        doc+=', '.join(tags)
        if tags and linktags:doc+=', '
        doc+=', '.join(f'[{i}]({i})' for i in linktags)
        doc+='\n'
    if plugdata.get('requiers',[]):
        doc+='  * Requiers: '
        doc+=', '.join(plugdata.get('requiers',[]))
        doc+='\n'
    if plugdata.get('requirements',[]):
        doc+='  * Requirements: '
        doc+=', '.join(plugdata.get('requirements',[]))
        doc+='\n'
    if plugdata.get('docs',''):
        doc+='  * '+plugdata.get('docs','')+'\n'
    return doc
def main():
    with open('raw') as f:
        rawlist=f.read().split('\n')
    with open('data.json') as f:
        data=json.load(f)
    out=r'''# vim-plugin-list
This is a list of plugins.
_TODO: categorize, document and remove not plugins_

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_Other vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins)_

'''
    for i in (plugins:=data.get('plugins',{})):
        out+=f'# {i}\n'
        for j in plugins.get(i,{}):
            rawlist.remove(j)
            out+=doc_from_plug(plugins.get(i,{}).get(j,{}),j)
        out+='\n'
    out+='\n'.join(f'* [{i}](https://github.com/{i})' for i in rawlist)
    with open('README.md','w') as f:
        f.write(out)
if __name__ == "__main__":
    main()
