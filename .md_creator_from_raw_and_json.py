import json
def list2str(title:str,x:list)->str:
    if len(x):return title+': '+', '.join(x)+'\n'
    else:return ''
def list_link(x:list)->list:
    return [f'[{i}](#{i})' for i in x]
def doc_from_plug(plugdata:dict,plug:str,level=1)->str:
    ind1='  '*level+'*'
    ind2='  '+'  '*level+'*'
    doc=''
    if plugdata.get('islinked',False): #TODO: auto is linked detector
        doc+=f'{ind1} ###### [{plug}](https://github.com/{plug})\n'
    else:
        doc+=f'{ind1} [{plug}](https://github.com/{plug})\n'
    linktags=plugdata.get('linktags',[])
    tags=plugdata.get('tags',[])
    if tags or linktags:
        doc+=f'{ind2} Tags: '
        doc+=', '.join(tags)
        if tags and linktags:doc+=', '
        doc+=', '.join(f'[{i}](#{i})' for i in linktags)
        doc+='\n'
    doc+=list2str(f'{ind2} Requiers',list_link(plugdata.get('requiers',[])))
    doc+=list2str(f'{ind2} Requirements',plugdata.get('requirements',[]))
    if plugdata.get('docs',''):doc+=f'{ind2} '+plugdata.get('docs','')+'\n'
    doc+=list2str(f'{ind2} Optional/extensions',list_link(plugdata.get('optional',[])))
     #TODO: add small doc of what they extends
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
    #TODO: add jump list
    out+=f'# Documented-list\n'
    for i,subplugdict in data.get('plugins',{}).items():
        out+=f'## {i}\n'
        for j,plugs in subplugdict.items():
            out+=f'### {j}\n'
            for k,plugdata in plugs.items():
                rawlist.remove(k)
                out+=doc_from_plug(plugdata,k)
        out+='\n'
    out+=f'# Other\n'
    out+='\n'.join(f'* [{i}](https://github.com/{i})' for i in rawlist)

    out+='\n\n# Tags\n'
    for name,tagdata in data.get('tags').items():
        out+=(f'* ###### {name}\n{tagdata}\n')
    with open('README.md','w') as f:
        f.write(out)
if __name__ == "__main__":
    main()
