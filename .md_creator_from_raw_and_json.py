import json
def main():
    with open('raw') as f:
        raw=f.read()
    with open('data.json') as f:
        data=json.load(f.read())

    pre=r'''# vim-plugin-list
This is a list of plugins.
_TODO: categorize, document and remove not plugins_

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_Other vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins)_
'''
    out=pre+'\n'+'\n'.join(f'* [{i}](https://github.com/{i})' for i in raw.split('\n'))
    with open('README.md','w') as f:
        f.write(out)
if __name__ == "__main__":
    main()
