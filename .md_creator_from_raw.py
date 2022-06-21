def main():
    with open('raw') as f:
        text=f.read()
    pre=r'''# vim-plugin-list
This is a list of plugins.
_TODO: categorize and document_

_NOTE: this list may contain  mirrors._

_Other vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins)_
'''
    out=pre+'\n'+'\n'.join(f'* [{i}](https://github.com/{i})' for i in text.split('\n'))
    with open('README.md','w') as f:
        f.write(out)
if __name__ == "__main__":
    main()
