# Contribution Guidelines
Thanks for taking you time to improve this github repository.
## Applies to any contribution
* do NOT edit the files [README.md](README.md) or [document.json](document.json)
 (if you do, the content will be overwritten by python scripts)
* all PLUGIN NAMES must be lowercase
* do NOT edit any of the files inside [old-format](document/old-format), only remove/move them to [new-format](document/new-format)
## add/rename/delete a plugin from not-documented
1. add/rename/delete the plugin from/to/in [raw](raw)
2. run [.md_creator.py](.md_creator.py)
## add/rename/delete a plugin from documented
3. learn how the script [.merg.py](document/.merg.py) works
4. add/rename/delete the plugin in/from/to the correct category
    1. note that gitlab plugins are the name+repository prefixed by `https://gitlab.com/`
    2. if you wish to link to another plugin: use the syntax `{name/repository}` for github and (NotImplemented) for gitlab
5. run [.merg.py](document/.merg.py)
6. run [.md_creator.py](.md_creator.py)
    1. note that if a documented plugin is not in [raw](raw) then an exception is thrown
## editing other files
* no guideline (TODO: create guideline)
# how the file structure is set up
* Files starting with a dot are document generating scripts
* [data.json](data.json) file contains data which is neither document nor script
* Files that are in directory [other](other) should be ignored.
## documents
* each document has 1-3 parts:
    * name/repository
    * document (optional)
* examples: `name/repo : is awesome`, `name/colorscheme`
* use text like `[no development]` or `[archived]` only at end of line.
