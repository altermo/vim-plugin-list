# Contribution Guidelines
Thanks for taking you time to improve this github repository.
## Applies to any contribution
* do NOT edit the files [README.md](README.md) or [document.json](document.json)
 (if you do, the content will be overwritten by python scripts)
* all PLUGIN NAMES must be lowercase
## add/rename/delete a plugin from not-documented
1. add/rename/delete the plugin from/to/in [raw](raw)
2. run [.md_creator.py](.md_creator.py)
## add/rename/delete a plugin from documented
0. learn how the script [.merg.py](document/.merg.py) works
1. add/rename/delete the plugin in/from/to the correct category
    1. note that gitlab plugins are the name+repository prefixed by a `´` (example: `´name/repository`)
2. run [.merg.py](document/.merg.py)
3. run [.md_creator.py](.md_creator.py)
    1. note that if a documented plugin is not in [raw](raw) then an exception is thrown
## editing other files
* no guideline (TODO: create guideline)
# how the file structure is set up
* Files starting with a dot are document generating scripts
* [data.json](data.json) file contains data which is neither document nor script
* Files that are in directory [other](other) should be ignored.
## documents
* The [categorys](document/categorys) directory contains full on descriptions
* The [docs](document/docs) directory has 2 parts:
    * the first line sets the format
    * all other lines are documents
    * the formatting works like `for i in all_other: format % i`
* The [linked](document/linked) directory has 2 parts:
    * the first line sets the format
    * all other lines are links with the structure `%s > %s`
    * the formatting works like `for i in all_other: beg, end = i.split(' > '); beg + ( format % end )`
* The [types](document/types) directory has only plugins (no documentations)
