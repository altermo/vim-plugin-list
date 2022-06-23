# vim-plugin-list
This is a list of plugins.
_TODO: categorize, document and remove not plugins_

_Pleas tell me if non main links should take you to its place in list or to its website_

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_Other vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins)_

# Lists
<details><summary>I recommend for vim</summary>

* file manager : [preservim/nerdtree](#preservimnerdtree)
* highlighting : [sheerun/vim-polyglot](#sheerunvim-polyglot)
* syntax : [vim-syntastic/syntastic](#vim-syntasticsyntastic)
* undotree : [mbbill/undotree](#mbbillundotree)
* FZF : [junegunn/fzf.vim](#junegunnfzfvim)
* statusline : [vim-airline/vim-airline](#vim-airlinevim-airline)
* statusline+tabline : [itchyny/lightline.vim](#itchynylightlinevim)
* colorscheme1 : [mjlbach/onedark.nvim](#mjlbachonedarknvim)
* colorscheme2 : [NTBBloodbath/doom-one.nvim](#NTBBloodbathdoom-onenvim)
* colorscheme3 : [rafamadriz/neon](#rafamadrizneon)
* autocomplete : [neoclide/coc.nvim](#neoclidecocnvim)
</details>
<details><summary>other interesting</summary>

* autocomplete : [skywind3000/vim-auto-popmenu](#skywind3000vim-auto-popmenu)
* minimap : [severin-lemaignan/vim-minimap](#severin-lemaignanvim-minimap)
* neorg : [nvim-neorg/neorg](#nvim-neorgneorg)
* firefox integration : [glacambre/firenvim](#glacambrefirenvim)
* cursor word : [itchyny/vim-cursorword](#itchynyvim-cursorword)
* align text : [tommcdo/vim-lion](#tommcdovim-lion)
* yankstack : [bfredl/nvim-miniyank](#bfredlnvim-miniyank)
* sh commands in vimscript : [tpope/vim-eunuch](#tpopevim-eunuch)
* translator : [voldikss/vim-translator](#voldikssvim-translator)
* dirbuf : [elihunter173/dirbuf.nvim](#elihunter173dirbufnvim)
* fastfold : [Konfekt/FastFold](#KonfektFastFold)
</details>

# Documented-list
## Code
### highlighting
  * ###### [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim)
    * Tags: highlighting, syntax, integration, LSP, NodeJS
    * Requirements: neovim>=4.0 or vim>=8.0.1453, node>=12.12
    * Adds ways to install LSP from vim via NodeJS and a few other things
    * Readmore: [list-of-coc-apps](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions#implemented-coc-extensions)
  * ###### [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter)
    * Tags: [treesitter](#treesitter), highlighting, [neovim](#neovim), integration
    * Requirements: neovim>=7.0
    * Adds treesitter support and treesitter highlighting to neovim
    * Readmore: [extensions](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Extra-modules-and-plugins), [supported-languages](https://github.com/nvim-treesitter/nvim-treesitter#supported-languages)
  * ###### [sheerun/vim-polyglot](https://github.com/sheerun/vim-polyglot)
    * Tags: highlighting
    * A highlighting plugin collection which supports 99% of file types
## Command
### Explorer
  * ###### [preservim/nerdtree](https://github.com/preservim/nerdtree)
    * Tags: tree, explorer
    * A popular sidebar explorer
    * Readmore: [optional](https://github.com/preservim/nerdtree#nerdtree-plugins)
  * [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim)
    * Tags: [lua](#lua), FZF, [neovim](#neovim), explorer
    * Requiers: [nvim-lua/plenary.nvim](#nvim-luaplenarynvim)
    * Requirements: neovim>=7.0
    * Lua based fuzzy finder
    * Readmore: [optional](https://github.com/nvim-telescope/telescope.nvim#optional-dependencies), [extensions](https://github.com/nvim-telescope/telescope.nvim/wiki/Extensions#different-plugins-with-telescope-integration)
# Quick-documented-list
* 0styx0/abbreinder.nvim : remember abbreviations
* 0styx0/abbremand.nvim : lib for {0styx0/abbreinder.nvim}
* acksld/nvim-neoclip.lua : see yank history
* adelarsq/neoline.vim : statusline and tabline
* airblade/vim-gitgutter : git diff
* airblade/vim-rooter : go to projects root
* airodactyl/neovim-ranger : ranger for neovim
* akinsho/nvim-toggleterm.lua : link to {akinsho/toggleterm}
* akinsho/toggleterm.nvim : persist and toggle multiple terminals
* akz92/vim-ionic2 : ionic2 syntax highlighting
* alaviss/nim.nvim : nim language plugin
* alessandroyorba/despacio : colorscheme
* aloussase/telescope-gradle.nvim : telescope extension to run gradle tasks
* aloussase/telescope-maven-search : telescope extension to search dependencies in MavenCentral
* altercation/vim-colors-solarized : colorscheme
* alvan/vim-closetag : Auto close (X)HTML tags
* amix/open_file_under_cursor.vim : open file under cursor (what did you expect)
* amix/vim-2048 : 2048 game
* amix/vim-commentary : fork from {tpope/vim-commentary}
* amix/vim-zenroom2 : emulates iA Writer environment
* andrewradev/splitjoin.vim : switching between a single-line statement and a multi-line one
* andrewradev/switch.vim : swich segments of text with predefined replacements 
* angkeith/telescope-terraform-doc.nvim : telescope extension to search and browse terraform providers docs
* antoinemadec/fixcursorhold.nvim : fix neovim CursorHold and CursorHoldI AND decouple updatetime from CursorHold and CursorHoldI
* ap/vim-css-color : preview colours in source code while editing
* arakashic/chromatica.nvim : Clang based syntax highlighting for Neovim [depreciated]
* arp242/jumpy.vim : filetype-specific mappings for [[, ]], g[, and g] to jump to the next or previous section
* artur-shaik/vim-javacomplete2 : depreciated, use {artur-shaik/jc.nvim} instead
* asheq/close-buffers.vim : quickly close (bdelete) several buffers at once
* autozimu/languageclient-neovim : LSP support
* azabiong/vim-highlighter : highlight words and expressions
# Non-documented-list
  * [beauwilliams/focus.nvim](https://github.com/beauwilliams/focus.nvim)

  * [benfowler/telescope-luasnip.nvim](https://github.com/benfowler/telescope-luasnip.nvim)

  * [bfredl/nvim-ipy](https://github.com/bfredl/nvim-ipy)

  * [bfredl/nvim-luadev](https://github.com/bfredl/nvim-luadev)

  * ###### [bfredl/nvim-miniyank](https://github.com/bfredl/nvim-miniyank)

  * [bfrg/vim-qf-preview](https://github.com/bfrg/vim-qf-preview)

  * [bi0ha2ard/telescope-ros.nvim](https://github.com/bi0ha2ard/telescope-ros.nvim)

  * [bling/vim-airline](https://github.com/bling/vim-airline)

  * [blueshirts/darcula](https://github.com/blueshirts/darcula)

  * [blueyed/vim-diminactive](https://github.com/blueyed/vim-diminactive)

  * [brandoncc/telescope-harpoon.nvim](https://github.com/brandoncc/telescope-harpoon.nvim)

  * [brettanomyces/nvim-editcommand](https://github.com/brettanomyces/nvim-editcommand)

  * [brettanomyces/nvim-terminus](https://github.com/brettanomyces/nvim-terminus)

  * [brglng/vim-im-select](https://github.com/brglng/vim-im-select)

  * [bronzehedwick/vim-primary-terminal](https://github.com/bronzehedwick/vim-primary-terminal)

  * [brooth/far.vim](https://github.com/brooth/far.vim)

  * [bruno-/vim-man](https://github.com/bruno-/vim-man)

  * [burntsushi/ripgrep](https://github.com/burntsushi/ripgrep)

  * [c0r73x/neotags.lua](https://github.com/c0r73x/neotags.lua)

  * [c0r73x/neotags.nvim](https://github.com/c0r73x/neotags.nvim)

  * [camgraff/telescope-tmux.nvim](https://github.com/camgraff/telescope-tmux.nvim)

  * [camspiers/snap](https://github.com/camspiers/snap)

  * [catppuccin/nvim](https://github.com/catppuccin/nvim)

  * [ccchapman/watson.nvim](https://github.com/ccchapman/watson.nvim)

  * [cdelledonne/vim-cmake](https://github.com/cdelledonne/vim-cmake)

  * [cespare/vim-toml](https://github.com/cespare/vim-toml)

  * [challenger-deep-theme/vim](https://github.com/challenger-deep-theme/vim)

  * [chip/telescope-code-fence.nvim](https://github.com/chip/telescope-code-fence.nvim)

  * [chip/telescope-software-licenses.nvim](https://github.com/chip/telescope-software-licenses.nvim)

  * [chrboesch/vim-tabline](https://github.com/chrboesch/vim-tabline)

  * [chrisbra/changesplugin](https://github.com/chrisbra/changesplugin)

  * [chrisbra/colorizer](https://github.com/chrisbra/colorizer)

  * [chrisbra/dynamicsigns](https://github.com/chrisbra/dynamicsigns)

  * [chrisbra/unicode.vim](https://github.com/chrisbra/unicode.vim)

  * [chriskempson/base16-vim/](https://github.com/chriskempson/base16-vim/)

  * [chriskempson/vim-tomorrow-theme](https://github.com/chriskempson/vim-tomorrow-theme)

  * [christoomey/vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator)

  * [cljoly/telescope-repo.nvim](https://github.com/cljoly/telescope-repo.nvim)

  * [clojure-vim/acid.nvim](https://github.com/clojure-vim/acid.nvim)

  * [coachshea/neo-pipe](https://github.com/coachshea/neo-pipe)

  * [codcodog/simplebuffer.vim](https://github.com/codcodog/simplebuffer.vim)

  * [coderifous/textobj-word-column.vim](https://github.com/coderifous/textobj-word-column.vim)

  * [crispgm/telescope-heading.nvim](https://github.com/crispgm/telescope-heading.nvim)

  * [critiqjo/lldb.nvim](https://github.com/critiqjo/lldb.nvim)

  * [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim)

  * [cyansprite/extract](https://github.com/cyansprite/extract)

  * [dag/vim-fish](https://github.com/dag/vim-fish)

  * [danielpieper/telescope-tmuxinator.nvim](https://github.com/danielpieper/telescope-tmuxinator.nvim)

  * [dense-analysis/ale](https://github.com/dense-analysis/ale)

  * [derekwyatt/vim-scala](https://github.com/derekwyatt/vim-scala)

  * [devjoe/vim-codequery](https://github.com/devjoe/vim-codequery)

  * [dhruvasagar/vim-table-mode](https://github.com/dhruvasagar/vim-table-mode)

  * [dhruvmanila/telescope-bookmarks.nvim](https://github.com/dhruvmanila/telescope-bookmarks.nvim)

  * [dm1try/git_fastfix](https://github.com/dm1try/git_fastfix)

  * [dm1try/golden_size](https://github.com/dm1try/golden_size)

  * [doc/user/lsp.html](https://github.com/doc/user/lsp.html)

  * [donraphaco/neotex](https://github.com/donraphaco/neotex)

  * [dpzmick/neovim-hackernews](https://github.com/dpzmick/neovim-hackernews)

  * [dracula/vim](https://github.com/dracula/vim)

  * [dstein64/nvim-scrollview](https://github.com/dstein64/nvim-scrollview)

  * [dstein64/vim-startuptime](https://github.com/dstein64/vim-startuptime)

  * [duane9/nvim-rg](https://github.com/duane9/nvim-rg)

  * [dyng/ctrlsf.vim](https://github.com/dyng/ctrlsf.vim)

  * [easymotion/vim-easymotion](https://github.com/easymotion/vim-easymotion)

  * [edeneast/nightfox.nvim](https://github.com/edeneast/nightfox.nvim)

  * [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim)

  * [edolphin-ydf/goimpl.nvim](https://github.com/edolphin-ydf/goimpl.nvim)

  * ###### [elihunter173/dirbuf.nvim](https://github.com/elihunter173/dirbuf.nvim)

  * [ellisonleao/gruvbox.nvim](https://github.com/ellisonleao/gruvbox.nvim)

  * [elvessousa/sobrio](https://github.com/elvessousa/sobrio)

  * [equalsraf/neovim-gui-shim](https://github.com/equalsraf/neovim-gui-shim)

  * [ervandew/supertab](https://github.com/ervandew/supertab)

  * [euclidianace/betterlua.vim](https://github.com/euclidianace/betterlua.vim)

  * [euclio/vim-markdown-composer](https://github.com/euclio/vim-markdown-composer)

  * [eugen0329/vim-esearch](https://github.com/eugen0329/vim-esearch)

  * [f3fora/cmp-spell](https://github.com/f3fora/cmp-spell)

  * [fannheyward/telescope-coc.nvim](https://github.com/fannheyward/telescope-coc.nvim)

  * [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace)

  * [fatih/vim-go](https://github.com/fatih/vim-go)

  * [fcying/telescope-ctags-outline.nvim](https://github.com/fcying/telescope-ctags-outline.nvim)

  * [feiyoug/command_center.nvim](https://github.com/feiyoug/command_center.nvim)

  * [fenetikm/falcon](https://github.com/fenetikm/falcon)

  * [ferrine/md-img-paste.vim](https://github.com/ferrine/md-img-paste.vim)

  * [fhill2/telescope-ultisnips.nvim](https://github.com/fhill2/telescope-ultisnips.nvim)

  * [fholgado/minibufexpl.vim](https://github.com/fholgado/minibufexpl.vim)

  * [flazz/vim-colorschemes](https://github.com/flazz/vim-colorschemes)

  * [floobits/floobits-neovim](https://github.com/floobits/floobits-neovim)

  * [fmoralesc/nlanguagetool.nvim](https://github.com/fmoralesc/nlanguagetool.nvim)

  * [fmoralesc/worldslice](https://github.com/fmoralesc/worldslice)

  * [folke/lsp-colors.nvim](https://github.com/folke/lsp-colors.nvim)

  * [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim)

  * [folke/trouble.nvim](https://github.com/folke/trouble.nvim)

  * [folke/which-key.nvim](https://github.com/folke/which-key.nvim)

  * [folke/zen-mode.nvim](https://github.com/folke/zen-mode.nvim)

  * [francoiscabrol/ranger.vim](https://github.com/francoiscabrol/ranger.vim)

  * [frazrepo/vim-rainbow](https://github.com/frazrepo/vim-rainbow)

  * [fszymanski/fzf-gitignore](https://github.com/fszymanski/fzf-gitignore)

  * [galicarnax/vim-regex-syntax](https://github.com/galicarnax/vim-regex-syntax)

  * [garbas/vim-snipmate](https://github.com/garbas/vim-snipmate)

  * [gbprod/yanky.nvim](https://github.com/gbprod/yanky.nvim)

  * [gbrlsnchs/telescope-lsp-handlers.nvim](https://github.com/gbrlsnchs/telescope-lsp-handlers.nvim)

  * [gfanto/fzf-lsp.nvim](https://github.com/gfanto/fzf-lsp.nvim)

  * [ghifarit53/tokyonight-vim](https://github.com/ghifarit53/tokyonight-vim)

  * ###### [glacambre/firenvim](https://github.com/glacambre/firenvim)

  * [glench/vim-jinja2-syntax](https://github.com/glench/vim-jinja2-syntax)

  * [glepnir/dashboard-nvim](https://github.com/glepnir/dashboard-nvim)

  * [glepnir/galaxyline.nvim](https://github.com/glepnir/galaxyline.nvim)

  * [glepnir/indent-guides.nvim](https://github.com/glepnir/indent-guides.nvim)

  * [glepnir/lspsaga.nvim](https://github.com/glepnir/lspsaga.nvim)

  * [glepnir/zephyr-nvim](https://github.com/glepnir/zephyr-nvim)

  * [gmarik/vundle.vim](https://github.com/gmarik/vundle.vim)

  * [godlygeek/tabular](https://github.com/godlygeek/tabular)

  * [goolord/alpha-nvim](https://github.com/goolord/alpha-nvim)

  * [groenewege/vim-less](https://github.com/groenewege/vim-less)

  * [guns/vim-clojure-highlight](https://github.com/guns/vim-clojure-highlight)

  * [guns/vim-clojure-static](https://github.com/guns/vim-clojure-static)

  * [guns/vim-slamhound](https://github.com/guns/vim-slamhound)

  * [gustavokatel/telescope-asynctasks.nvim](https://github.com/gustavokatel/telescope-asynctasks.nvim)

  * [haifengkao/insertleftbracket.nvim](https://github.com/haifengkao/insertleftbracket.nvim)

  * [hardenedapple/vsh/](https://github.com/hardenedapple/vsh/)

  * [haya14busa/incsearch.vim](https://github.com/haya14busa/incsearch.vim)

  * [haya14busa/vim-easyoperator-line](https://github.com/haya14busa/vim-easyoperator-line)

  * [henriquehbr/ataraxis.lua](https://github.com/henriquehbr/ataraxis.lua)

  * [henriquehbr/nvim-startup.lua](https://github.com/henriquehbr/nvim-startup.lua)

  * [hkupty/iron.nvim](https://github.com/hkupty/iron.nvim)

  * [hkupty/nvimux](https://github.com/hkupty/nvimux)

  * [honza/dockerfile.vim](https://github.com/honza/dockerfile.vim)

  * [honza/vim-snippets](https://github.com/honza/vim-snippets)

  * [hoschi/yode-nvim](https://github.com/hoschi/yode-nvim)

  * [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer)

  * [hrsh7th/cmp-calc](https://github.com/hrsh7th/cmp-calc)

  * [hrsh7th/cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline)

  * [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp)

  * [hrsh7th/cmp-nvim-lsp-document-symbol](https://github.com/hrsh7th/cmp-nvim-lsp-document-symbol)

  * [hrsh7th/cmp-nvim-lsp-signature-help](https://github.com/hrsh7th/cmp-nvim-lsp-signature-help)

  * [hrsh7th/cmp-nvim-lua](https://github.com/hrsh7th/cmp-nvim-lua)

  * [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path)

  * [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp)

  * [huawenyu/neogdb.vim](https://github.com/huawenyu/neogdb.vim)

  * [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim)

  * [icymind/neosolarized](https://github.com/icymind/neosolarized)

  * [inkarkat/vim-patterncomplete](https://github.com/inkarkat/vim-patterncomplete)

  * [ipod825/vim-netranger](https://github.com/ipod825/vim-netranger)

  * [iron-e/nvim-highlite](https://github.com/iron-e/nvim-highlite)

  * [iron-e/nvim-libmodal](https://github.com/iron-e/nvim-libmodal)

  * ###### [itchyny/lightline.vim](https://github.com/itchyny/lightline.vim)

  * ###### [itchyny/vim-cursorword](https://github.com/itchyny/vim-cursorword)

  * [jalvesaq/nvim-r](https://github.com/jalvesaq/nvim-r)

  * [jalvesaq/vimcmdline](https://github.com/jalvesaq/vimcmdline)

  * [janko-m/vim-test](https://github.com/janko-m/vim-test)

  * [jbyuki/instant.nvim](https://github.com/jbyuki/instant.nvim)

  * [jbyuki/venn.nvim](https://github.com/jbyuki/venn.nvim)

  * [jceb/vim-orgmode](https://github.com/jceb/vim-orgmode)

  * [jgvw/telescope-arglist.nvim](https://github.com/jgvw/telescope-arglist.nvim)

  * [jiangmiao/auto-pairs](https://github.com/jiangmiao/auto-pairs)

  * [jmcomets/vim-pony/](https://github.com/jmcomets/vim-pony/)

  * [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim)

  * [joshdick/onedark.vim](https://github.com/joshdick/onedark.vim)

  * [jreybert/vimagit](https://github.com/jreybert/vimagit)

  * [jsfaint/gen_tags.vim](https://github.com/jsfaint/gen_tags.vim)

  * [jsit/toast.vim](https://github.com/jsit/toast.vim)

  * [junegunn/fzf](https://github.com/junegunn/fzf)

  * ###### [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)

  * [junegunn/goyo.vim](https://github.com/junegunn/goyo.vim)

  * [junegunn/gv.vim](https://github.com/junegunn/gv.vim)

  * [junegunn/heytmux](https://github.com/junegunn/heytmux)

  * [junegunn/limelight.vim](https://github.com/junegunn/limelight.vim)

  * [junegunn/rainbow_parentheses.vim](https://github.com/junegunn/rainbow_parentheses.vim)

  * [junegunn/vader.vim](https://github.com/junegunn/vader.vim)

  * [junegunn/vim-after-object](https://github.com/junegunn/vim-after-object)

  * [junegunn/vim-carbon-now-sh](https://github.com/junegunn/vim-carbon-now-sh)

  * [junegunn/vim-cfr](https://github.com/junegunn/vim-cfr)

  * [junegunn/vim-easy-align](https://github.com/junegunn/vim-easy-align)

  * [junegunn/vim-emoji](https://github.com/junegunn/vim-emoji)

  * [junegunn/vim-fnr](https://github.com/junegunn/vim-fnr)

  * [junegunn/vim-github-dashboard](https://github.com/junegunn/vim-github-dashboard)

  * [junegunn/vim-journal](https://github.com/junegunn/vim-journal)

  * [junegunn/vim-plug](https://github.com/junegunn/vim-plug)

  * [junegunn/vim-pseudocl](https://github.com/junegunn/vim-pseudocl)

  * [junegunn/vim-slash](https://github.com/junegunn/vim-slash)

  * [junegunn/vim-xmark](https://github.com/junegunn/vim-xmark)

  * [justinmk/vim-dirvish](https://github.com/justinmk/vim-dirvish)

  * [justinmk/vim-gtfo](https://github.com/justinmk/vim-gtfo)

  * [justinmk/vim-sneak](https://github.com/justinmk/vim-sneak)

  * [jvgrootveld/telescope-zoxide](https://github.com/jvgrootveld/telescope-zoxide)

  * [kana/vim-textobj-indent](https://github.com/kana/vim-textobj-indent)

  * [kana/vim-textobj-user](https://github.com/kana/vim-textobj-user)

  * [karb94/neoscroll.nvim](https://github.com/karb94/neoscroll.nvim)

  * [kassio/neoterm](https://github.com/kassio/neoterm)

  * [kchmck/vim-coffee-script](https://github.com/kchmck/vim-coffee-script)

  * [kelly-lin/telescope-ag](https://github.com/kelly-lin/telescope-ag)

  * [kevinhwang91/nvim-bqf](https://github.com/kevinhwang91/nvim-bqf)

  * [kevinhwang91/nvim-hlslens](https://github.com/kevinhwang91/nvim-hlslens)

  * [kevinhwang91/rnvimr](https://github.com/kevinhwang91/rnvimr)

  * [kezhenxu94/vim-mysql-plugin](https://github.com/kezhenxu94/vim-mysql-plugin)

  * [killthemule/nvimpam](https://github.com/killthemule/nvimpam)

  * [kkoomen/vim-doge](https://github.com/kkoomen/vim-doge)

  * [klen/python-mode](https://github.com/klen/python-mode)

  * [kolja/telescope-opds](https://github.com/kolja/telescope-opds)

  * [konfekt/fastfold](https://github.com/konfekt/fastfold)

  * [kosayoda/nvim-lightbulb](https://github.com/kosayoda/nvim-lightbulb)

  * [kovetskiy/sxhkd-vim](https://github.com/kovetskiy/sxhkd-vim)

  * [kovisoft/paredit](https://github.com/kovisoft/paredit)

  * [kyazdani42/nvim-tree.lua](https://github.com/kyazdani42/nvim-tree.lua)

  * [kyazdani42/nvim-web-devicons](https://github.com/kyazdani42/nvim-web-devicons)

  * [l3mon4d3/luasnip](https://github.com/l3mon4d3/luasnip)

  * [lambdalisue/fern.vim](https://github.com/lambdalisue/fern.vim)

  * [lenovsky/nuake](https://github.com/lenovsky/nuake)

  * [lervag/vimtex](https://github.com/lervag/vimtex)

  * [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim)

  * [lewis6991/impatient.nvim](https://github.com/lewis6991/impatient.nvim)

  * [linarcx/telescope-changes.nvim](https://github.com/linarcx/telescope-changes.nvim)

  * [linarcx/telescope-command-palette.nvim](https://github.com/linarcx/telescope-command-palette.nvim)

  * [linarcx/telescope-env.nvim](https://github.com/linarcx/telescope-env.nvim)

  * [linarcx/telescope-ports.nvim](https://github.com/linarcx/telescope-ports.nvim)

  * [linarcx/telescope-scriptnames.nvim](https://github.com/linarcx/telescope-scriptnames.nvim)

  * [liuchengxu/vim-clap](https://github.com/liuchengxu/vim-clap)

  * [liuchengxu/vim-which-key](https://github.com/liuchengxu/vim-which-key)

  * [luc-tielen/telescope_hoogle](https://github.com/luc-tielen/telescope_hoogle)

  * [ludovicchabant/vim-gutentags](https://github.com/ludovicchabant/vim-gutentags)

  * [luisiacc/gruvbox-baby](https://github.com/luisiacc/gruvbox-baby)

  * [lukas-reineke/cmp-rg](https://github.com/lukas-reineke/cmp-rg)

  * [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim)

  * [luochen1990/rainbow](https://github.com/luochen1990/rainbow)

  * [machakann/vim-highlightedyank](https://github.com/machakann/vim-highlightedyank)

  * [macthecadillac/vimdo](https://github.com/macthecadillac/vimdo)

  * [majutsushi/tagbar](https://github.com/majutsushi/tagbar)

  * [marcweber/vim-addon-manager](https://github.com/marcweber/vim-addon-manager)

  * [marcweber/vim-addon-mw-utils](https://github.com/marcweber/vim-addon-mw-utils)

  * [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim)

  * [mattesgroeger/vim-bookmarks](https://github.com/mattesgroeger/vim-bookmarks)

  * [mattn/calendar-vim](https://github.com/mattn/calendar-vim)

  * [mattn/gist-vim](https://github.com/mattn/gist-vim)

  * [maxbrunsfeld/vim-yankstack](https://github.com/maxbrunsfeld/vim-yankstack)

  * [maxmellon/vim-jsx-pretty](https://github.com/maxmellon/vim-jsx-pretty)

  * [maxst/flatcolor](https://github.com/maxst/flatcolor)

  * ###### [mbbill/undotree](https://github.com/mbbill/undotree)

  * [mcchrish/nnn.vim](https://github.com/mcchrish/nnn.vim)

  * [metakirby5/codi.vim](https://github.com/metakirby5/codi.vim)

  * [mfussenegger/nvim-dap](https://github.com/mfussenegger/nvim-dap)

  * [mg979/vim-visual-multi](https://github.com/mg979/vim-visual-multi)

  * [mhartington/nvim-typescript](https://github.com/mhartington/nvim-typescript)

  * [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next)

  * [mhinz/vim-grepper](https://github.com/mhinz/vim-grepper)

  * [mhinz/vim-janah](https://github.com/mhinz/vim-janah)

  * [mhinz/vim-rfc](https://github.com/mhinz/vim-rfc)

  * [mhinz/vim-signify](https://github.com/mhinz/vim-signify)

  * [mhinz/vim-startify](https://github.com/mhinz/vim-startify)

  * [michaelb/sniprun](https://github.com/michaelb/sniprun)

  * [michaeljsmith/vim-indent-object](https://github.com/michaeljsmith/vim-indent-object)

  * [mileszs/ack.vim](https://github.com/mileszs/ack.vim)

  * [mjbrownie/vim-htmldjango_omnicomplete](https://github.com/mjbrownie/vim-htmldjango_omnicomplete)

  * ###### [mjlbach/onedark.nvim](https://github.com/mjlbach/onedark.nvim)

  * [monkoose/matchparen.nvim](https://github.com/monkoose/matchparen.nvim)

  * [morhetz/gruvbox](https://github.com/morhetz/gruvbox)

  * [ms-jpq/chadtree](https://github.com/ms-jpq/chadtree)

  * [ms-jpq/coq_nvim](https://github.com/ms-jpq/coq_nvim)

  * [mtoohey31/cmp-fish](https://github.com/mtoohey31/cmp-fish)

  * [mzlogin/vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc)

  * [nanotech/jellybeans.vim](https://github.com/nanotech/jellybeans.vim)

  * [nanotee/zoxide.vim](https://github.com/nanotee/zoxide.vim)

  * [natecraddock/telescope-zf-native.nvim](https://github.com/natecraddock/telescope-zf-native.nvim)

  * [nathanaelkane/vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides)

  * [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim)

  * [ncm2/ncm2](https://github.com/ncm2/ncm2)

  * [neomake/neomake](https://github.com/neomake/neomake)

  * [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig)

  * [neovimhaskell/haskell-vim](https://github.com/neovimhaskell/haskell-vim)

  * [nfischer/vim-rainbows](https://github.com/nfischer/vim-rainbows)

  * [nightsense/cosmic_latte](https://github.com/nightsense/cosmic_latte)

  * [nikvdp/neomux](https://github.com/nikvdp/neomux)

  * [noahfrederick/vim-composer](https://github.com/noahfrederick/vim-composer)

  * [norcalli/nvim-colorizer.lua](https://github.com/norcalli/nvim-colorizer.lua)

  * [norcalli/nvim_utils](https://github.com/norcalli/nvim_utils)

  * [ntbbloodbath/doom-one.nvim](https://github.com/ntbbloodbath/doom-one.nvim)

  * [ntpeters/vim-better-whitespace](https://github.com/ntpeters/vim-better-whitespace)

  * [numirias/semshi](https://github.com/numirias/semshi)

  * [numtostr/comment.nvim](https://github.com/numtostr/comment.nvim)

  * [nvim-lua/lsp_extensions.nvim](https://github.com/nvim-lua/lsp_extensions.nvim)

  * ###### [nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim)

  * [nvim-lua/popup.nvim](https://github.com/nvim-lua/popup.nvim)

  * [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)

  * [nvim-neo-tree/neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim)

  * ###### [nvim-neorg/neorg](https://github.com/nvim-neorg/neorg)

  * [nvim-neorg/neorg-telescope](https://github.com/nvim-neorg/neorg-telescope)

  * [nvim-orgmode/orgmode](https://github.com/nvim-orgmode/orgmode)

  * [nvim-telescope/telescope-dap.nvim](https://github.com/nvim-telescope/telescope-dap.nvim)

  * [nvim-telescope/telescope-file-browser.nvim](https://github.com/nvim-telescope/telescope-file-browser.nvim)

  * [nvim-telescope/telescope-frecency.nvim](https://github.com/nvim-telescope/telescope-frecency.nvim)

  * [nvim-telescope/telescope-fzf-native.nvim](https://github.com/nvim-telescope/telescope-fzf-native.nvim)

  * [nvim-telescope/telescope-fzf-writer.nvim](https://github.com/nvim-telescope/telescope-fzf-writer.nvim)

  * [nvim-telescope/telescope-fzy-native.nvim](https://github.com/nvim-telescope/telescope-fzy-native.nvim)

  * [nvim-telescope/telescope-ghq.nvim](https://github.com/nvim-telescope/telescope-ghq.nvim)

  * [nvim-telescope/telescope-github.nvim](https://github.com/nvim-telescope/telescope-github.nvim)

  * [nvim-telescope/telescope-hop.nvim](https://github.com/nvim-telescope/telescope-hop.nvim)

  * [nvim-telescope/telescope-media-files.nvim](https://github.com/nvim-telescope/telescope-media-files.nvim)

  * [nvim-telescope/telescope-node-modules.nvim](https://github.com/nvim-telescope/telescope-node-modules.nvim)

  * [nvim-telescope/telescope-packer.nvim](https://github.com/nvim-telescope/telescope-packer.nvim)

  * [nvim-telescope/telescope-project.nvim](https://github.com/nvim-telescope/telescope-project.nvim)

  * [nvim-telescope/telescope-symbols.nvim](https://github.com/nvim-telescope/telescope-symbols.nvim)

  * [nvim-telescope/telescope-vimspector.nvim](https://github.com/nvim-telescope/telescope-vimspector.nvim)

  * [nvim-telescope/telescope-z.nvim](https://github.com/nvim-telescope/telescope-z.nvim)

  * [nvim-treesitter/nvim-treesitter-refactor](https://github.com/nvim-treesitter/nvim-treesitter-refactor)

  * [nvim-treesitter/nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects)

  * [nvim-treesitter/playground](https://github.com/nvim-treesitter/playground)

  * [octol/vim-cpp-enhanced-highlight](https://github.com/octol/vim-cpp-enhanced-highlight)

  * [olacin/telescope-cc.nvim](https://github.com/olacin/telescope-cc.nvim)

  * [olacin/telescope-gitmoji.nvim](https://github.com/olacin/telescope-gitmoji.nvim)

  * [olical/aniseed](https://github.com/olical/aniseed)

  * [olical/conjure](https://github.com/olical/conjure)

  * [onsails/lspkind-nvim](https://github.com/onsails/lspkind-nvim)

  * [onsails/lspkind-nvim/](https://github.com/onsails/lspkind-nvim/)

  * [onsails/lspkind.nvim](https://github.com/onsails/lspkind.nvim)

  * [othree/javascript-libraries-syntax.vim](https://github.com/othree/javascript-libraries-syntax.vim)

  * [overcache/neosolarized](https://github.com/overcache/neosolarized)

  * [p00f/nvim-ts-rainbow](https://github.com/p00f/nvim-ts-rainbow)

  * [pangloss/vim-javascript](https://github.com/pangloss/vim-javascript)

  * [paulocesar/neovim-db](https://github.com/paulocesar/neovim-db)

  * [pechorin/any-jump.vim](https://github.com/pechorin/any-jump.vim)

  * [pgdouyon/vim-accio](https://github.com/pgdouyon/vim-accio)

  * [phaazon/hop.nvim](https://github.com/phaazon/hop.nvim)

  * [philrunninger/nerdtree-buffer-ops](https://github.com/philrunninger/nerdtree-buffer-ops)

  * [philrunninger/nerdtree-visual-selection](https://github.com/philrunninger/nerdtree-visual-selection)

  * [pianocomposer321/project-templates.nvim](https://github.com/pianocomposer321/project-templates.nvim)

  * [potatoesmaster/i3-vim-syntax](https://github.com/potatoesmaster/i3-vim-syntax)

  * [powerman/vim-plugin-ansiesc](https://github.com/powerman/vim-plugin-ansiesc)

  * [preservim/nerdcommenter](https://github.com/preservim/nerdcommenter)

  * [preservim/tagbar](https://github.com/preservim/tagbar)

  * [psliwka/vim-smoothie](https://github.com/psliwka/vim-smoothie)

  * [pwntester/octo.nvim](https://github.com/pwntester/octo.nvim)

  * [qpkorr/vim-renamer](https://github.com/qpkorr/vim-renamer)

  * [quangnguyen30192/cmp-nvim-tags](https://github.com/quangnguyen30192/cmp-nvim-tags)

  * [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets)

  * ###### [rafamadriz/neon](https://github.com/rafamadriz/neon)

  * [rafcamlet/nvim-luapad](https://github.com/rafcamlet/nvim-luapad)

  * [rafi/awesome-vim-colorschemes](https://github.com/rafi/awesome-vim-colorschemes)

  * [raghur/vim-ghost](https://github.com/raghur/vim-ghost)

  * [raimondi/delimitmate](https://github.com/raimondi/delimitmate)

  * [ray-x/cmp-treesitter](https://github.com/ray-x/cmp-treesitter)

  * [ray-x/lsp_signature.nvim](https://github.com/ray-x/lsp_signature.nvim)

  * [rbgrouleff/bclose.vim](https://github.com/rbgrouleff/bclose.vim)

  * [rcarriga/nvim-notify](https://github.com/rcarriga/nvim-notify)

  * [rhysd/clever-f.vim](https://github.com/rhysd/clever-f.vim)

  * [rhysd/git-messenger.vim](https://github.com/rhysd/git-messenger.vim)

  * [ripxorip/aerojump.nvim](https://github.com/ripxorip/aerojump.nvim)

  * [ripxorip/bolt.nvim](https://github.com/ripxorip/bolt.nvim)

  * [rliang/termedit.nvim](https://github.com/rliang/termedit.nvim)

  * [rmagatti/session-lens](https://github.com/rmagatti/session-lens)

  * [rmehri01/onenord.nvim](https://github.com/rmehri01/onenord.nvim)

  * [romainl/apprentice](https://github.com/romainl/apprentice)

  * [romainl/vim-qf](https://github.com/romainl/vim-qf)

  * [romgrk/barbar.nvim](https://github.com/romgrk/barbar.nvim)

  * [romgrk/nvim-treesitter-context](https://github.com/romgrk/nvim-treesitter-context)

  * [rose-pine/neovim](https://github.com/rose-pine/neovim)

  * [roxma/nvim-completion-manager](https://github.com/roxma/nvim-completion-manager)

  * [roxma/vim-tmux-clipboard](https://github.com/roxma/vim-tmux-clipboard)

  * [rraks/pyro](https://github.com/rraks/pyro)

  * [rrethy/vim-illuminate](https://github.com/rrethy/vim-illuminate)

  * [ruifm/gitlinker.nvim](https://github.com/ruifm/gitlinker.nvim)

  * [rust-lang/rust.vim](https://github.com/rust-lang/rust.vim)

  * [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons)

  * [s1n7ax/nvim-comment-frame](https://github.com/s1n7ax/nvim-comment-frame)

  * [s1n7ax/nvim-lazy-inner-block](https://github.com/s1n7ax/nvim-lazy-inner-block)

  * [s1n7ax/nvim-search-and-replace](https://github.com/s1n7ax/nvim-search-and-replace)

  * [s1n7ax/nvim-terminal](https://github.com/s1n7ax/nvim-terminal)

  * [s1n7ax/nvim-window-picker](https://github.com/s1n7ax/nvim-window-picker)

  * [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip)

  * [sainnhe/gruvbox-material](https://github.com/sainnhe/gruvbox-material)

  * [sakhnik/nvim-gdb](https://github.com/sakhnik/nvim-gdb)

  * [savq/paq-nvim](https://github.com/savq/paq-nvim)

  * [sbdchd/neoformat](https://github.com/sbdchd/neoformat)

  * [scrooloose/nerdcommenter](https://github.com/scrooloose/nerdcommenter)

  * [scrooloose/nerdtree](https://github.com/scrooloose/nerdtree)

  * [scrooloose/nerdtree-project-plugin](https://github.com/scrooloose/nerdtree-project-plugin)

  * [scrooloose/syntastic](https://github.com/scrooloose/syntastic)

  * ###### [severin-lemaignan/vim-minimap](https://github.com/severin-lemaignan/vim-minimap)

  * [sgur/vim-editorconfig](https://github.com/sgur/vim-editorconfig)

  * [sharkdp/fd](https://github.com/sharkdp/fd)

  * [shaunsingh/nord.nvim](https://github.com/shaunsingh/nord.nvim)

  * [shougo/defx.nvim](https://github.com/shougo/defx.nvim)

  * [shougo/dein.vim](https://github.com/shougo/dein.vim)

  * [shougo/denite.nvim](https://github.com/shougo/denite.nvim)

  * [shougo/deoplete.nvim](https://github.com/shougo/deoplete.nvim)

  * [shougo/neobundle.vim](https://github.com/shougo/neobundle.vim)

  * [shougo/neocomplcache.vim](https://github.com/shougo/neocomplcache.vim)

  * [shougo/neocomplete.vim](https://github.com/shougo/neocomplete.vim)

  * [shougo/neosnippet-snippets](https://github.com/shougo/neosnippet-snippets)

  * [shougo/neosnippet.vim](https://github.com/shougo/neosnippet.vim)

  * [shougo/unite.vim](https://github.com/shougo/unite.vim)

  * [shougo/vimfiler.vim](https://github.com/shougo/vimfiler.vim)

  * [sickill/vim-monokai](https://github.com/sickill/vim-monokai)

  * [sidofc/mkdx](https://github.com/sidofc/mkdx)

  * [simnalamburt/vim-mundo](https://github.com/simnalamburt/vim-mundo)

  * [simrat39/symbols-outline.nvim](https://github.com/simrat39/symbols-outline.nvim)

  * [sindrets/diffview.nvim](https://github.com/sindrets/diffview.nvim)

  * [sindrets/winshift.nvim](https://github.com/sindrets/winshift.nvim)

  * [sirver/ultisnips](https://github.com/sirver/ultisnips)

  * [sjl/gundo.vim](https://github.com/sjl/gundo.vim)

  * [skywind3000/asyncrun.vim](https://github.com/skywind3000/asyncrun.vim)

  * [skywind3000/asynctasks.vim](https://github.com/skywind3000/asynctasks.vim)

  * ###### [skywind3000/vim-auto-popmenu](https://github.com/skywind3000/vim-auto-popmenu)

  * [skywind3000/vim-dict](https://github.com/skywind3000/vim-dict)

  * [skywind3000/vim-quickui](https://github.com/skywind3000/vim-quickui)

  * [slashmili/alchemist.vim](https://github.com/slashmili/alchemist.vim)

  * [slim-template/vim-slim](https://github.com/slim-template/vim-slim)

  * [softinio/scaladex.nvim](https://github.com/softinio/scaladex.nvim)

  * [solarnz/thrift.vim](https://github.com/solarnz/thrift.vim)

  * [stevearc/dressing.nvim](https://github.com/stevearc/dressing.nvim)

  * [suan/vim-instant-markdown](https://github.com/suan/vim-instant-markdown)

  * [sudormrfbin/cheatsheet.nvim](https://github.com/sudormrfbin/cheatsheet.nvim)

  * [sukima/xmledit/](https://github.com/sukima/xmledit/)

  * [svermeulen/nvim-marksman](https://github.com/svermeulen/nvim-marksman)

  * [svermeulen/nvim-moonmaker](https://github.com/svermeulen/nvim-moonmaker)

  * [svermeulen/vim-extended-ft](https://github.com/svermeulen/vim-extended-ft)

  * [svermeulen/vimpeccable](https://github.com/svermeulen/vimpeccable)

  * [szw/vim-maximizer](https://github.com/szw/vim-maximizer)

  * [tamago324/telescope-openbrowser.nvim](https://github.com/tamago324/telescope-openbrowser.nvim)

  * [tc72/telescope-tele-tabby.nvim](https://github.com/tc72/telescope-tele-tabby.nvim)

  * [tek/proteome.nvim](https://github.com/tek/proteome.nvim)

  * [tek256/simple-dark](https://github.com/tek256/simple-dark)

  * [tenfyzhong/completeparameter.vim](https://github.com/tenfyzhong/completeparameter.vim)

  * [ternjs/tern_for_vim](https://github.com/ternjs/tern_for_vim)

  * [terrortylor/nvim-comment](https://github.com/terrortylor/nvim-comment)

  * [terryma/vim-expand-region](https://github.com/terryma/vim-expand-region)

  * [terryma/vim-multiple-cursors](https://github.com/terryma/vim-multiple-cursors)

  * [theprimeagen/harpoon](https://github.com/theprimeagen/harpoon)

  * [theprimeagen/refactoring.nvim](https://github.com/theprimeagen/refactoring.nvim)

  * [theprimeagen/vim-apm](https://github.com/theprimeagen/vim-apm)

  * [theprimeagen/vim-be-good](https://github.com/theprimeagen/vim-be-good)

  * [therubymug/vim-pyte](https://github.com/therubymug/vim-pyte)

  * [tiagofumo/vim-nerdtree-syntax-highlight](https://github.com/tiagofumo/vim-nerdtree-syntax-highlight)

  * [timeyyy/orchestra.nvim](https://github.com/timeyyy/orchestra.nvim)

  * [tjdevries/nlua.nvim](https://github.com/tjdevries/nlua.nvim)

  * [tobys/pdv](https://github.com/tobys/pdv)

  * [tom-anders/telescope-vim-bookmarks.nvim](https://github.com/tom-anders/telescope-vim-bookmarks.nvim)

  * [tomasiser/vim-code-dark](https://github.com/tomasiser/vim-code-dark)

  * [tomasr/molokai](https://github.com/tomasr/molokai)

  * [tomlion/vim-solidity](https://github.com/tomlion/vim-solidity)

  * ###### [tommcdo/vim-lion](https://github.com/tommcdo/vim-lion)

  * [tomtom/tcomment_vim](https://github.com/tomtom/tcomment_vim)

  * [tomtom/tlib_vim](https://github.com/tomtom/tlib_vim)

  * [townk/vim-autoclose](https://github.com/townk/vim-autoclose)

  * [tpope/vim-abolish](https://github.com/tpope/vim-abolish)

  * [tpope/vim-bundler](https://github.com/tpope/vim-bundler)

  * [tpope/vim-commentary](https://github.com/tpope/vim-commentary)

  * [tpope/vim-dispatch](https://github.com/tpope/vim-dispatch)

  * [tpope/vim-endwise](https://github.com/tpope/vim-endwise)

  * ###### [tpope/vim-eunuch](https://github.com/tpope/vim-eunuch)

  * [tpope/vim-fireplace](https://github.com/tpope/vim-fireplace)

  * [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive)

  * [tpope/vim-pathogen](https://github.com/tpope/vim-pathogen)

  * [tpope/vim-projectionist](https://github.com/tpope/vim-projectionist)

  * [tpope/vim-rails](https://github.com/tpope/vim-rails)

  * [tpope/vim-repeat](https://github.com/tpope/vim-repeat)

  * [tpope/vim-rhubarb](https://github.com/tpope/vim-rhubarb)

  * [tpope/vim-scriptease](https://github.com/tpope/vim-scriptease)

  * [tpope/vim-speeddating](https://github.com/tpope/vim-speeddating)

  * [tpope/vim-surround](https://github.com/tpope/vim-surround)

  * [tpope/vim-unimpaired](https://github.com/tpope/vim-unimpaired)

  * [tpope/vim-vinegar](https://github.com/tpope/vim-vinegar)

  * [tracyone/neomake-multiprocess](https://github.com/tracyone/neomake-multiprocess)

  * [tversteeg/registers.nvim](https://github.com/tversteeg/registers.nvim)

  * [tversteeg/registers.đvim](https://github.com/tversteeg/registers.đvim)

  * [tyru/open-browser.vim](https://github.com/tyru/open-browser.vim)

  * [tzachar/cmp-tabnine](https://github.com/tzachar/cmp-tabnine)

  * [unblevable/quick-scope](https://github.com/unblevable/quick-scope)

  * [valloric/matchtagalways](https://github.com/valloric/matchtagalways)

  * [valloric/youcompleteme](https://github.com/valloric/youcompleteme)

  * [vifm/neovim-vifm](https://github.com/vifm/neovim-vifm)

  * [vifm/vifm.vim](https://github.com/vifm/vifm.vim)

  * ###### [vim-airline/vim-airline](https://github.com/vim-airline/vim-airline)

  * [vim-airline/vim-airline-themes](https://github.com/vim-airline/vim-airline-themes)

  * [vim-chat/vim-chat](https://github.com/vim-chat/vim-chat)

  * [vim-conf-live/vimconflive2021-colorscheme](https://github.com/vim-conf-live/vimconflive2021-colorscheme)

  * [vim-pandoc/vim-pandoc](https://github.com/vim-pandoc/vim-pandoc)

  * [vim-python/python-syntax](https://github.com/vim-python/python-syntax)

  * [vim-scripts/align](https://github.com/vim-scripts/align)

  * [vim-scripts/bufexplorer.zip](https://github.com/vim-scripts/bufexplorer.zip)

  * [vim-scripts/csapprox](https://github.com/vim-scripts/csapprox)

  * [vim-scripts/cyclecolor](https://github.com/vim-scripts/cyclecolor)

  * [vim-scripts/grep.vim](https://github.com/vim-scripts/grep.vim)

  * [vim-scripts/mayansmoke](https://github.com/vim-scripts/mayansmoke)

  * [vim-scripts/peaksea](https://github.com/vim-scripts/peaksea)

  * [vim-scripts/replacewithregister](https://github.com/vim-scripts/replacewithregister)

  * [vim-scripts/sessionman.vim](https://github.com/vim-scripts/sessionman.vim)

  * ###### [vim-syntastic/syntastic](https://github.com/vim-syntastic/syntastic)

  * [vim-test/vim-test](https://github.com/vim-test/vim-test)

  * [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki)

  * [voldikss/vim-browser-search](https://github.com/voldikss/vim-browser-search)

  * [voldikss/vim-floaterm](https://github.com/voldikss/vim-floaterm)

  * ###### [voldikss/vim-translator](https://github.com/voldikss/vim-translator)

  * [w0rp/ale](https://github.com/w0rp/ale)

  * [wbthomason/buildit.nvim](https://github.com/wbthomason/buildit.nvim)

  * [wbthomason/lsp-status.nvim](https://github.com/wbthomason/lsp-status.nvim)

  * [wbthomason/packer.nvim](https://github.com/wbthomason/packer.nvim)

  * [wellle/context.vim](https://github.com/wellle/context.vim)

  * [wellle/targets.vim](https://github.com/wellle/targets.vim)

  * [wellle/tmux-complete.vim](https://github.com/wellle/tmux-complete.vim)

  * [wellle/visual-split.vim](https://github.com/wellle/visual-split.vim)

  * [wesleimp/telescope-windowizer.nvim](https://github.com/wesleimp/telescope-windowizer.nvim)

  * [wesq3/vim-windowswap](https://github.com/wesq3/vim-windowswap)

  * [wfxr/minimap.vim](https://github.com/wfxr/minimap.vim)

  * [wgibbs/vim-irblack](https://github.com/wgibbs/vim-irblack)

  * [williamboman/nvim-lsp-installer](https://github.com/williamboman/nvim-lsp-installer)

  * [windwp/nvim-autopairs](https://github.com/windwp/nvim-autopairs)

  * [windwp/nvim-ts-autotag](https://github.com/windwp/nvim-ts-autotag)

  * [winston0410/commented.nvim](https://github.com/winston0410/commented.nvim)

  * [wittyjudge/gruvbox-material.nvim](https://github.com/wittyjudge/gruvbox-material.nvim)

  * [wsdjeg/flygrep.vim](https://github.com/wsdjeg/flygrep.vim)

  * [wsdjeg/vim-cheat](https://github.com/wsdjeg/vim-cheat)

  * [xiyaowong/telescope-emoji.nvim](https://github.com/xiyaowong/telescope-emoji.nvim)

  * [xolox/vim-misc](https://github.com/xolox/vim-misc)

  * [xolox/vim-session](https://github.com/xolox/vim-session)

  * [xuyuanp/nerdtree-git-plugin](https://github.com/xuyuanp/nerdtree-git-plugin)

  * [ycm-core/youcompleteme](https://github.com/ycm-core/youcompleteme)

  * [yegappan/mru](https://github.com/yegappan/mru)

  * [yehuohan/popc](https://github.com/yehuohan/popc)

  * [yggdroot/indentline](https://github.com/yggdroot/indentline)

  * [yggdroot/leaderf](https://github.com/yggdroot/leaderf)

  * [yong1le/darkplus.nvim](https://github.com/yong1le/darkplus.nvim)

  * [yqlbu/neovim-server](https://github.com/yqlbu/neovim-server)

  * [yuratomo/w3m.vim](https://github.com/yuratomo/w3m.vim)

  * [yuttie/hydrangea-vim](https://github.com/yuttie/hydrangea-vim)

  * [zchee/nvim-go](https://github.com/zchee/nvim-go)

  * [zenbro/mirror.vim](https://github.com/zenbro/mirror.vim)

  * [zgpio/brew.nvim](https://github.com/zgpio/brew.nvim)

  * [zgpio/tree.nvim](https://github.com/zgpio/tree.nvim)

  * [zsugabubus/crazy8.nvim](https://github.com/zsugabubus/crazy8.nvim)

# Tags
* ###### treesitter
related to [nvim-treesitter](#nvim-treesitternvim-treesitter)
* ###### lua
is writen primarily in lua insted of vim-script
* ###### neovim
only works with neovim and not vim