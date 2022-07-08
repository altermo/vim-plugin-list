# vim-plugin-list
This is a list of plugins.

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_Other BETER vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [awesome-nvim](https://github.com/rockerBOO/awesome-neovim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins), [vim-galore](https://github.com/mhinz/vim-galore/blob/master/PLUGINS.md), [vlugins](https://github.com/astier/vlugins)_

# Jump list
  * [extensions/options/readmore/...](#extensionsreadmoreoptions)
  * [documented](#documented)
    * [file-movment](#file-movment)
    * [plugin-maneger](#plugin-maneger)
    * [apps](#apps)
    * [ui-creator](#ui-creator)
    * [git](#git)
    * [other](#other)
    * [integration](#integration)
    * [projects-seessions](#projects-seessions)
    * [undotree](#undotree)
    * [finder](#finder)
    * [lsp](#lsp)
    * [treesitter](#treesitter)
    * [keys](#keys)
    * [tags](#tags)
    * [todo-list](#todo-list)
    * [zen](#zen)
    * [repalce](#repalce)
    * [toggle](#toggle)
    * [textobject](#textobject)
    * [color](#color)
    * [filemanager](#filemanager)
    * [buffers](#buffers)
    * [aligner](#aligner)
    * [keymap-creater](#keymap-creater)
    * [language-suport](#language-suport)
    * [from-one-to-more-lines](#from-one-to-more-lines)
    * [tmux](#tmux)
    * [windows](#windows)
    * [abbreviations](#abbreviations)
    * [folds](#folds)
    * [game](#game)
    * [functions-commands](#functions-commands)
    * [speed-up-loadtimes](#speed-up-loadtimes)
    * [quickfix](#quickfix)
    * [pairs](#pairs)
    * [movment](#movment)
    * [remote](#remote)
    * [visual](#visual)
    * [highlight-underline](#highlight-underline)
    * [snippets](#snippets)
    * [marks](#marks)
    * [comment](#comment)
    * [terminal](#terminal)
    * [markdown-org-neorg](#markdown-org-neorg)
    * [syntax](#syntax)
    * [telescope-extensions](#telescope-extensions)
    * [nvim-cmp-extensions](#nvim-cmp-extensions)
    * [use-instead](#use-instead)
    * [libs](#libs)
    * [gui](#gui)
    * [yanklist](#yanklist)
    * [bufferline](#bufferline)
    * [ide](#ide)
    * [tabline](#tabline)
    * [starter-page](#starter-page)
    * [statusline](#statusline)
    * [autocomplete](#autocomplete)
    * [colorscheme](#colorscheme)
  * [not documented](#not-documented)
  * [donate](#donate)
# Extensions/readmore/options/...
  * [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) : [extensions](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Extra-modules-and-plugins), [supported-languages](https://github.com/nvim-treesitter/nvim-treesitter#supported-languages)
  * [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim) : [list-of-coc-apps](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions#implemented-coc-extensions)
  * [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) : [optional](https://github.com/nvim-telescope/telescope.nvim#optional-dependencies), [extensions](https://github.com/nvim-telescope/telescope.nvim/wiki/Extensions#different-plugins-with-telescope-integration)
  * [preservim/nerdtree](https://github.com/preservim/nerdtree) : [optional](https://github.com/preservim/nerdtree#nerdtree-plugins)
  * [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp) : [extensions](https://github.com/hrsh7th/nvim-cmp/wiki/List-of-sources)
# Documented
## file-movment
  * [airblade/vim-rooter](https://github.com/airblade/vim-rooter) : go to projects root
  * [theprimeagen/harpoon](https://github.com/theprimeagen/harpoon) : mark files and more
## plugin-maneger
  * [wbthomason/packer.nvim](https://github.com/wbthomason/packer.nvim) : use-package inspired plugin/package management for Neovim
## apps
  * [bfredl/nvim-luadev](https://github.com/bfredl/nvim-luadev) : REPL-like environment for developing lua plugins in Nvim
  * [mattn/calendar-vim](https://github.com/mattn/calendar-vim) : creates a calendar window
  * [metakirby5/codi.vim](https://github.com/metakirby5/codi.vim) : The interactive scratchpad for hackers
  * [simrat39/symbols-outline.nvim](https://github.com/simrat39/symbols-outline.nvim) : A tree like view for symbols in Neovim using the Language Server Protocol
  * [wfxr/minimap.vim](https://github.com/wfxr/minimap.vim) : Blazing fast minimap
## ui-creator
  * [anuvyklack/hydra.nvim](https://github.com/anuvyklack/hydra.nvim) : Neovim implementation of the famous Emacs Hydra package
  * [muniftanjim/nui.nvim](https://github.com/muniftanjim/nui.nvim) : UI Component Library
  * [skywind3000/vim-quickui](https://github.com/skywind3000/vim-quickui) : basic UI components to enrich vim's interactive experience
  * [stevearc/dressing.nvim](https://github.com/stevearc/dressing.nvim) : improve vim.ui.select and vim.ui.input
## git
  * [airblade/vim-gitgutter](https://github.com/airblade/vim-gitgutter) : git diff
  * [junegunn/gv.vim](https://github.com/junegunn/gv.vim) : A git commit browser
  * [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim) : Super fast git decorations implemented
  * [timuntersberger/neogit](https://github.com/timuntersberger/neogit) : Magit clone for Neovim
  * [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive) : Fugitive is the premier Vim plugin for Git
  * [tpope/vim-rhubarb](https://github.com/tpope/vim-rhubarb) : If fugitive.vim is the Git, rhubarb.vim is the Hub
## other
  * [andrewradev/sideways.vim](https://github.com/andrewradev/sideways.vim) : move the item under the cursor left or right
  * [antoinemadec/fixcursorhold.nvim](https://github.com/antoinemadec/fixcursorhold.nvim) : fix neovim CursorHold and CursorHoldI AND decouple updatetime from CursorHold and CursorHoldI
  * [bfredl/nvim-ipy](https://github.com/bfredl/nvim-ipy) : Jupyter front-end for Neovim
  * [brglng/vim-im-select](https://github.com/brglng/vim-im-select) : Improve Vim/Neovim experience with input methods
  * [cdelledonne/vim-cmake](https://github.com/cdelledonne/vim-cmake) : building CMake projects inside of vim, with a nice visual feedback
  * [chrisbra/unicode.vim](https://github.com/chrisbra/unicode.vim) : handling unicode and digraphs characters
  * [clojure-vim/acid.nvim](https://github.com/clojure-vim/acid.nvim) : clojure development
  * [davidgranstrom/osc.nvim](https://github.com/davidgranstrom/osc.nvim) : Open Sound Control (OSC) library for Neovim
  * [dhruvasagar/vim-table-mode](https://github.com/dhruvasagar/vim-table-mode) : awesome automatic table creator & formatter
  * [echasnovski/mini.nvim](https://github.com/echasnovski/mini.nvim) : Collection of minimal, independent, and fast Lua modules dedicated to improve Neovim experience
  * [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim) : This is an EditorConfig plugin for Vim
  * [ekickx/clipboard-image.nvim](https://github.com/ekickx/clipboard-image.nvim) : copy images and paste url/path
  * [filipdutescu/renamer.nvim](https://github.com/filipdutescu/renamer.nvim) : Visual-Studio-Code-like renaming UI
  * [glacambre/firenvim](https://github.com/glacambre/firenvim) : Turn your browser¹ into a Neovim client
  * [h-hg/fcitx.nvim](https://github.com/h-hg/fcitx.nvim) : switch and restore fcitx state for each buffer
  * [hkupty/iron.nvim](https://github.com/hkupty/iron.nvim) : Interactive Repls Over Neovim
  * [jbyuki/venn.nvim](https://github.com/jbyuki/venn.nvim) : Draw ASCII diagrams in Neovim
  * [jghauser/kitty-runner.nvim](https://github.com/jghauser/kitty-runner.nvim) : easily send lines from the current buffer to another kitty terminal
  * [jghauser/mkdir.nvim](https://github.com/jghauser/mkdir.nvim) : automatically creates missing directories on saving a file
  * [klen/nvim-test](https://github.com/klen/nvim-test) : Test Runner for neovim
  * [luchermitte/vimfold4c](https://github.com/luchermitte/vimfold4c) : Reactive vim fold plugin for C & C++
  * [m-demare/attempt.nvim](https://github.com/m-demare/attempt.nvim) : Manage your temporary buffers
  * [mg979/vim-visual-multi](https://github.com/mg979/vim-visual-multi) : create multiple visual regions and edit them (basically multiple cursor)
  * [nkakouros-original/numbers.nvim](https://github.com/nkakouros-original/numbers.nvim) : Disables relative line numbers when they don't make sense, e.g. when entering insert mode
  * [notomo/cmdbuf.nvim](https://github.com/notomo/cmdbuf.nvim) : provides command-line window functions by normal buffer and window
  * [pixelneo/vim-python-docstring](https://github.com/pixelneo/vim-python-docstring) : easily create python docstring
  * [pocco81/autosave.nvim](https://github.com/pocco81/autosave.nvim) : saving your work before the world collapses or you type :qa!
  * [rgroli/other.nvim](https://github.com/rgroli/other.nvim) : you can open other/related files for the currently active buffer
  * [rktjmp/paperplanes.nvim](https://github.com/rktjmp/paperplanes.nvim) : Post selections or buffers to online paste bins.
  * [romainl/vim-devdocs](https://github.com/romainl/vim-devdocs) : Look up keywords on https://devdocs.io
  * [skywind3000/asyncrun.vim](https://github.com/skywind3000/asyncrun.vim) : async run shell commands in qf window
  * [skywind3000/asynctasks.vim](https://github.com/skywind3000/asynctasks.vim) : modern task system
  * [skywind3000/vim-dict](https://github.com/skywind3000/vim-dict) : Automatically add dictionary files to current buffer according to the filetype
  * [theprimeagen/refactoring.nvim](https://github.com/theprimeagen/refactoring.nvim) : refactor code
  * [tyru/open-browser-github.vim](https://github.com/tyru/open-browser-github.vim) : Opens GitHub URL of current file, etc.
  * [tyru/open-browser-unicode.vim](https://github.com/tyru/open-browser-unicode.vim) : Opens Unicode character information
  * [tyru/open-browser.vim](https://github.com/tyru/open-browser.vim) : Open URI with your favorite browser
  * [udayvir-singh/tangerine.nvim](https://github.com/udayvir-singh/tangerine.nvim) : painless way to add fennel to your config
  * [vim-scripts/cyclecolor](https://github.com/vim-scripts/cyclecolor) : cycle through (almost) all available colorschemes
  * [voldikss/vim-translator](https://github.com/voldikss/vim-translator) : tranlate stuff
## integration
  * [acksld/nvim-gfold.lua](https://github.com/acksld/nvim-gfold.lua) : nvim plugin for gfold
  * [adoy/vim-php-refactoring-toolbox](https://github.com/adoy/vim-php-refactoring-toolbox) : PHP refactoring toolbox
  * [ccchapman/watson.nvim](https://github.com/ccchapman/watson.nvim) : An integration for Watson in Neovim
  * [jalvesaq/nvim-r](https://github.com/jalvesaq/nvim-r) : improves Vim's support to edit R code
  * [madskjeldgaard/reaper-nvim](https://github.com/madskjeldgaard/reaper-nvim) : controlling the Reaper DAW
  * [neovim/go-client](https://github.com/neovim/go-client) : Neovim/go-client is a Neovim client and plugin host for Go
  * [svermeulen/nvim-moonmaker](https://github.com/svermeulen/nvim-moonmaker) : adds support for writing moonscript plugins
## projects-seessions
  * [ahmedkhalf/project.nvim](https://github.com/ahmedkhalf/project.nvim) : provides superior project management
  * [ethanholz/nvim-lastplace](https://github.com/ethanholz/nvim-lastplace) : A Lua rewrite of [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace)
  * [rmagatti/auto-session](https://github.com/rmagatti/auto-session) : provide seamless automatic session management
  * [shatur/neovim-session-manager](https://github.com/shatur/neovim-session-manager) : use built-in mksession to manage sessions like folders in VSCode
## undotree
  * [simnalamburt/vim-mundo](https://github.com/simnalamburt/vim-mundo) : visualizes the Vim undo tree written in python
## finder
  * [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) : is a highly extendable fuzzy finder over list
  * [toppair/reach.nvim](https://github.com/toppair/reach.nvim) : buffer / mark / tabpage / colorscheme switcher
## lsp
  * [alexaandru/nvim-lspupdate](https://github.com/alexaandru/nvim-lspupdate) : Updates installed (or auto installs if missing) LSP servers, that are already configured in your init.vim
  * [artur-shaik/jc.nvim](https://github.com/artur-shaik/jc.nvim) : jc LSP
  * [autozimu/languageclient-neovim](https://github.com/autozimu/languageclient-neovim) : LSP support
  * [folke/lsp-colors.nvim](https://github.com/folke/lsp-colors.nvim) : Automatically creates missing LSP diagnostics highlight groups for color schemes that don't yet support the Neovim 0.5 builtin lsp client
  * [folke/trouble.nvim](https://github.com/folke/trouble.nvim) : A pretty list for showing diagnostics, references, telescope results, quickfix and location lists to help you solve all the trouble your code is causing
  * [jbyuki/one-small-step-for-vimkind](https://github.com/jbyuki/one-small-step-for-vimkind) : an adapter for the Neovim lua language
  * [kkharji/lspsaga.nvim](https://github.com/kkharji/lspsaga.nvim) : light-weight lsp plugin based on neovim built-in lsp with highly a performant UI
  * [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) : Configs for the Nvim LSP client
  * [onsails/lspkind.nvim](https://github.com/onsails/lspkind.nvim) : adds vscode-like pictograms to neovim built-in lsp
  * [ray-x/lsp_signature.nvim](https://github.com/ray-x/lsp_signature.nvim) : Show function signature when you type
  * [ray-x/navigator.lua](https://github.com/ray-x/navigator.lua) : lsp navigation and highlighting and more
  * [tamago324/nlsp-settings.nvim](https://github.com/tamago324/nlsp-settings.nvim) : configure Neovim LSP using json/yaml files like coc-settings.json
  * [williamboman/nvim-lsp-installer](https://github.com/williamboman/nvim-lsp-installer) : allow you to manage LSP servers
## treesitter
  * [joosepalviste/nvim-ts-context-commentstring](https://github.com/joosepalviste/nvim-ts-context-commentstring) : setting the commentstring option based on the cursor location in the file
  * [lewis6991/spellsitter.nvim](https://github.com/lewis6991/spellsitter.nvim) : Enable Neovim's builtin spellchecker for buffers with tree-sitter highlighting
  * [mfussenegger/nvim-treehopper](https://github.com/mfussenegger/nvim-treehopper) : Plugin that provides region selection using hints on the abstract syntax tree of a document
  * [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) : treesitter support for neovim
  * [nvim-treesitter/playground](https://github.com/nvim-treesitter/playground) : View treesitter information directly in Neovim
  * [p00f/nvim-ts-rainbow](https://github.com/p00f/nvim-ts-rainbow) : Rainbow parentheses for neovim using tree-sitter
  * [rrethy/nvim-treesitter-textsubjects](https://github.com/rrethy/nvim-treesitter-textsubjects) : Location and syntax aware text objects which *do what you mean*
  * [thehamsta/nvim-treesitter-pairs](https://github.com/thehamsta/nvim-treesitter-pairs) : Create your own pair objects using tree-sitter queries
  * [windwp/nvim-ts-autotag](https://github.com/windwp/nvim-ts-autotag) : Use treesitter to autoclose and autorename html tag
  * [ziontee113/syntax-tree-surfer](https://github.com/ziontee113/syntax-tree-surfer) : Navigate around your document based on Treesitter's abstract Syntax Tree. Step into, step out, step over, step back
## keys
  * [amix/open_file_under_cursor.vim](https://github.com/amix/open_file_under_cursor.vim) : open file under cursor (what did you expect)
  * [booperlv/nvim-gomove](https://github.com/booperlv/nvim-gomove) : moving and duplicating blocks and lines
  * [folke/which-key.nvim](https://github.com/folke/which-key.nvim) : displays a popup with possible key bindings of the command you started typing
  * [glts/vim-radical](https://github.com/glts/vim-radical) : see and convert number from and to different bases (hex,oct,dec,bin)
  * [jdhao/better-escape.vim](https://github.com/jdhao/better-escape.vim) : is created to help Vim/Nvim users escape insert mode quickly using their customized key combinations, without experiencing the lag
  * [linty-org/readline.nvim](https://github.com/linty-org/readline.nvim) : let you do things like move the cursor or delete text by a word or a line at a time.
  * [liuchengxu/vim-which-key](https://github.com/liuchengxu/vim-which-key) : displays available keybindings in popup
  * [max397574/better-escape.nvim](https://github.com/max397574/better-escape.nvim) : lua version of [jdhao/better-escape.vim](https://github.com/jdhao/better-escape.vim)
  * [mizlan/iswap.nvim](https://github.com/mizlan/iswap.nvim) : Interactively select and swap: function arguments, list elements, function parameters, and more
  * [monaqa/dial.nvim](https://github.com/monaqa/dial.nvim) : Extended increment/decrement plugin for Neovim
  * [s1n7ax/nvim-lazy-inner-block](https://github.com/s1n7ax/nvim-lazy-inner-block) : be lazy and example do not type the `i` in `ci)`
  * [tommcdo/vim-exchange](https://github.com/tommcdo/vim-exchange) : Easy text exchange operator
  * [tpope/vim-characterize](https://github.com/tpope/vim-characterize) : adds more info when pressing `ga`
  * [tpope/vim-repeat](https://github.com/tpope/vim-repeat) : make it so that plugins work with the key `.`
  * [tpope/vim-rsi](https://github.com/tpope/vim-rsi) : adds Readline key bindings to cmdline
  * [tpope/vim-surround](https://github.com/tpope/vim-surround) : all about "surroundings": parentheses, brackets, quotes, XML tags, and more
## tags
  * [c0r73x/neotags.lua](https://github.com/c0r73x/neotags.lua) : generates and highlight ctags similar to easytags
  * [majutsushi/tagbar](https://github.com/majutsushi/tagbar) : easy way to browse the tags of the current file and get an overview of its structure
## todo-list
  * [cathywu/vim-todo](https://github.com/cathywu/vim-todo) : Simple syntax highlighting for todo lists
  * [dkarter/bullets.vim](https://github.com/dkarter/bullets.vim) : automated bullet lists
  * [kabbamine/lazylist.vim](https://github.com/kabbamine/lazylist.vim) : create ordered and non ordered lists very quickly
  * [lervag/lists.vim](https://github.com/lervag/lists.vim) : manage text based lists
  * [lervag/vim-rainbow-lists](https://github.com/lervag/vim-rainbow-lists) : add rainbow highlighting of indented lists
## zen
  * [amix/vim-zenroom2](https://github.com/amix/vim-zenroom2) : emulates iA Writer environment
  * [folke/twilight.nvim](https://github.com/folke/twilight.nvim) : dims inactive portions of the code you're editing
  * [folke/zen-mode.nvim](https://github.com/folke/zen-mode.nvim) : Distraction-free coding for Neovim
  * [sunjon/shade.nvim](https://github.com/sunjon/shade.nvim) : dims your inactive windows
## repalce
  * [brooth/far.vim](https://github.com/brooth/far.vim) : replace text through multiple files
  * [gbprod/substitute.nvim](https://github.com/gbprod/substitute.nvim) : very easy to perform quick substitutions and exchange
  * [svermeulen/vim-subversive](https://github.com/svermeulen/vim-subversive) : make it very easy to perform quick substitutions
## toggle
  * [andrewradev/switch.vim](https://github.com/andrewradev/switch.vim) : swich segments of text with predefined replacements
  * [saifulapm/chartoggle.nvim](https://github.com/saifulapm/chartoggle.nvim) : toggle keys end of line
  * [zef/vim-cycle](https://github.com/zef/vim-cycle) : toggle between pairs or lists of related words
## textobject
  * [adriaanzon/vim-textobj-blade-directive](https://github.com/adriaanzon/vim-textobj-blade-directive) : textobject for blade directive
  * [adriaanzon/vim-textobj-matchit](https://github.com/adriaanzon/vim-textobj-matchit) : creates text objects from matchit pairs (example: `if…end`)
  * [chaoren/vim-wordmotion](https://github.com/chaoren/vim-wordmotion) : treat uppercase/lowercase words next to each other as different words
  * [coderifous/textobj-word-column.vim](https://github.com/coderifous/textobj-word-column.vim) : makes operating on columns of code conceptually simpler and reduces keystrokes
  * [d4ku/vim-pushover](https://github.com/d4ku/vim-pushover) : provides an interface to easily create mappings to push around text-objects
  * [deathlyfrantic/vim-textobj-blanklines](https://github.com/deathlyfrantic/vim-textobj-blanklines) : provides a text object for groups of empty lines
  * [kana/vim-textobj-user](https://github.com/kana/vim-textobj-user) : creat your own text objects
  * [michaeljsmith/vim-indent-object](https://github.com/michaeljsmith/vim-indent-object) : adds indentation based text objects
  * [misanthropicbit/vim-numbers](https://github.com/misanthropicbit/vim-numbers) : adds textobject to numbers
  * [nilsboy/vim-textobj-cindent](https://github.com/nilsboy/vim-textobj-cindent) : provides text objects to select a block of lines that have the same or higher indentation as the current line
  * [rhysd/vim-textobj-anyblock](https://github.com/rhysd/vim-textobj-anyblock) : make `ib` and `ab` match all parentheses and not just brackets
  * [wellle/targets.vim](https://github.com/wellle/targets.vim) : adds more bracket baised text objects.
## color
  * [ap/vim-css-color](https://github.com/ap/vim-css-color) : preview colours in source code while editing
  * [chrisbra/colorizer](https://github.com/chrisbra/colorizer) : color colornames and codes
  * [norcalli/nvim-colorizer.lua](https://github.com/norcalli/nvim-colorizer.lua) : A high-performance color highlighter for Neovim which has no external dependencies
  * [nvim-colortils/colortils.nvim](https://github.com/nvim-colortils/colortils.nvim) : Neovim color utils
  * [ziontee113/color-picker.nvim](https://github.com/ziontee113/color-picker.nvim) : lets Neovim Users choose & modify colors
## filemanager
  * [airodactyl/neovim-ranger](https://github.com/airodactyl/neovim-ranger) : ranger for neovim
  * [camspiers/snap](https://github.com/camspiers/snap) : fast finder system
  * [kyazdani42/nvim-tree.lua](https://github.com/kyazdani42/nvim-tree.lua) : A File Explorer For Neovim Written In Lua
  * [ms-jpq/chadtree](https://github.com/ms-jpq/chadtree) : File Manager for Neovim, Better than NERDTree
  * [xuyuanp/yanil](https://github.com/xuyuanp/yanil) : Yet Another Nerdtree In Lua
  * [zgpio/tree.nvim](https://github.com/zgpio/tree.nvim) : File explorer powered by C++
## buffers
  * [asheq/close-buffers.vim](https://github.com/asheq/close-buffers.vim) : quickly close (bdelete) several buffers at once
  * [codcodog/simplebuffer.vim](https://github.com/codcodog/simplebuffer.vim) : switching and deleting buffers easily
  * [elihunter173/dirbuf.nvim](https://github.com/elihunter173/dirbuf.nvim) : directory buffer
  * [famiu/bufdelete.nvim](https://github.com/famiu/bufdelete.nvim) : allow you to delete a buffer without messing up your window layout
  * [ghillb/cybu.nvim](https://github.com/ghillb/cybu.nvim) : notification window, that shows the buffer in focus and its neighbors or list of buffers is ordered by last used
  * [kazhala/close-buffers.nvim](https://github.com/kazhala/close-buffers.nvim) : Lua port of [asheq/close-buffers](https://github.com/asheq/close-buffers) with several feature extensions
  * [matbme/jabs.nvim](https://github.com/matbme/jabs.nvim) : Just Another Buffer Switcher
  * [nyngwang/neononame.lua](https://github.com/nyngwang/neononame.lua) : Layout preserving buffer deletion in Lua
## aligner
  * [godlygeek/tabular](https://github.com/godlygeek/tabular) : makek aligning text easy while also having complex setups
  * [tommcdo/vim-lion](https://github.com/tommcdo/vim-lion) : a tool for aligning text by some character
## keymap-creater
  * [b0o/mapx.nvim](https://github.com/b0o/mapx.nvim) : make mapping and commands more manageable in lua
  * [iron-e/nvim-cartographer](https://github.com/iron-e/nvim-cartographer) : simplify setting and deleting with keybindings / mappings in Lua
  * [lionc/nest.nvim](https://github.com/lionc/nest.nvim) : lua utility to define keymaps in concise, readable, cascading lists and trees
  * [mrjones2014/legendary.nvim](https://github.com/mrjones2014/legendary.nvim) : Define your keymaps, commands, and autocommands as simple Lua tables
  * [slugbyte/unruly-worker](https://github.com/slugbyte/unruly-worker) : a semantic key map for nvim designed for the workman keyboard layout
  * [svermeulen/vimpeccable](https://github.com/svermeulen/vimpeccable) : adds a simple lua api to map keys directly to lua code
## language-suport
  * [alaviss/nim.nvim](https://github.com/alaviss/nim.nvim) : nim language suport
  * [fatih/vim-go](https://github.com/fatih/vim-go) : go language suport
  * [zchee/nvim-go](https://github.com/zchee/nvim-go) : go language suport
## from-one-to-more-lines
  * [acksld/nvim-trevj.lua](https://github.com/acksld/nvim-trevj.lua) : do the opposite of join-line
  * [allendang/nvim-expand-expr](https://github.com/allendang/nvim-expand-expr) : Expand and repeat expression to multiple lines
  * [andrewradev/splitjoin.vim](https://github.com/andrewradev/splitjoin.vim) : switching between a single-line statement and a multi-line one
## tmux
  * [christoomey/vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator) : navigate seamlessly between vim and tmux splits using a consistent set of hotkeys
  * [hkupty/nvimux](https://github.com/hkupty/nvimux) : Nvimux allows neovim to work as a tmux replacement
## windows
  * [beauwilliams/focus.nvim](https://github.com/beauwilliams/focus.nvim) : Splits/Window Management Enhancements for Neovim
  * [blueyed/vim-diminactive](https://github.com/blueyed/vim-diminactive) : dim inactive windows
  * [luukvbaal/stabilize.nvim](https://github.com/luukvbaal/stabilize.nvim) : stabilize buffer content on window open/close events
  * [sindrets/winshift.nvim](https://github.com/sindrets/winshift.nvim) : Rearrange your windows with ease
  * [t9md/vim-choosewin](https://github.com/t9md/vim-choosewin) : enables you to choose a window interactively
  * [wellle/visual-split.vim](https://github.com/wellle/visual-split.vim) : Vim plugin to control splits with visual selections or text objects
  * [wesq3/vim-windowswap](https://github.com/wesq3/vim-windowswap) : Swap windows without ruining your layout
  * [yorickpeterse/nvim-window](https://gitlab.com/yorickpeterse/nvim-window) : quickly switching between windows
## abbreviations
  * [0styx0/abbreinder.nvim](https://github.com/0styx0/abbreinder.nvim) : shows abbreviations if the whole thing is typed
  * [pocco81/abbrevman.nvim](https://github.com/pocco81/abbrevman.nvim) : that manages abbreviations for various natural and programming languages
  * [tpope/vim-abolish](https://github.com/tpope/vim-abolish) : easily create similar abbreviations
## folds
  * [anuvyklack/pretty-fold.nvim](https://github.com/anuvyklack/pretty-fold.nvim) : Folded region preview and Framework for easy foldtext customization
  * [jghauser/fold-cycle.nvim](https://github.com/jghauser/fold-cycle.nvim) : allows you to cycle folds open or closed
  * [konfekt/fastfold](https://github.com/konfekt/fastfold) : only update folds whene you need to, thous improving speed
## game
  * [alec-gibson/nvim-tetris](https://github.com/alec-gibson/nvim-tetris) : tetris game
  * [amix/vim-2048](https://github.com/amix/vim-2048) : 2048 game
## functions-commands
  * [coachshea/neo-pipe](https://github.com/coachshea/neo-pipe) : send text through an external command and display the output in the output buffer
  * [equalsraf/neovim-gui-shim](https://github.com/equalsraf/neovim-gui-shim) : provides functions and commands for Neovim GUIs
  * [nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim) : All the lua functions I don't want to write twice
  * [sqve/sort.nvim](https://github.com/sqve/sort.nvim) : provides a simple command that mimics :sort and supports both line-wise and delimiter sorting
  * [tjdevries/vlog.nvim](https://github.com/tjdevries/vlog.nvim) : Single file, no dependency, easy copy & paste log file
  * [tpope/vim-eunuch](https://github.com/tpope/vim-eunuch) : Vim sugar for the UNIX shell commands that need it the most
## speed-up-loadtimes
  * [lewis6991/impatient.nvim](https://github.com/lewis6991/impatient.nvim) : Speed up loading Lua modules in Neovim to improve startup time
  * [nathom/filetype.nvim](https://github.com/nathom/filetype.nvim) : speed up neovim startup time by replacing the builtin filetype.vim with a faster alternative
## quickfix
  * [bfrg/vim-qf-preview](https://github.com/bfrg/vim-qf-preview) : For the quickfix and location list window to quickly preview the file with the quickfix item under the cursor in a popup window
  * [romainl/vim-qf](https://github.com/romainl/vim-qf) : is a growing collection of settings, commands and mappings put together to make working with the location list/window and the quickfix list/window smoother
  * [yorickpeterse/nvim-pqf](https://gitlab.com/yorickpeterse/nvim-pqf) : Pretty Quickfix windows for NeoVim
## pairs
  * [alvan/vim-closetag](https://github.com/alvan/vim-closetag) : Auto close (X)HTML tags
  * [andymass/vim-matchup](https://github.com/andymass/vim-matchup) : highlight, navigate, and operate on sets of matching text
  * [max-0406/autoclose.nvim](https://github.com/max-0406/autoclose.nvim) : minimalist autoclose plugin for Neovim
  * [steelsojka/pears.nvim](https://github.com/steelsojka/pears.nvim) : Auto pair plugin for neovim
  * [windwp/nvim-autopairs](https://github.com/windwp/nvim-autopairs) : A super powerful autopair plugin for Neovim that supports multiple characters
  * [zhiyuanlck/smart-pairs](https://github.com/zhiyuanlck/smart-pairs) : provides pairs completion, deletion and jump
## movment
  * [abecodes/tabout.nvim](https://github.com/abecodes/tabout.nvim) : tabbing out from parentheses
  * [arp242/jumpy.vim](https://github.com/arp242/jumpy.vim) : filetype-specific mappings for [[, ]], g[, and g] to jump to the next or previous section
  * [chrisbra/improvedft](https://github.com/chrisbra/improvedft) : makes `f`, `t`, `T`, `F` have the ability to jump multiple lines
  * [dahu/vim-fanfingtastic](https://github.com/dahu/vim-fanfingtastic) : multiline, case insensitive and aliasing for `f`, `t`, `T`, `F`
  * [easymotion/vim-easymotion](https://github.com/easymotion/vim-easymotion) : Jump fast to any place to the screen by preesing only up to three keys
  * [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim) : general-purpose motion plugin for Neovim
  * [ggandor/lightspeed.nvim](https://github.com/ggandor/lightspeed.nvim) : Lightspeed is a motion plugin for Neovim, with a relatively small interface and lots of innovative ideas
  * [goldfeld/vim-seek](https://github.com/goldfeld/vim-seek) : like `f` but for two characters
  * [justinmk/vim-sneak](https://github.com/justinmk/vim-sneak) : Jump to any location specified by two characters
  * [phaazon/hop.nvim](https://github.com/phaazon/hop.nvim) : Hop is an EasyMotion-like plugin allowing you to jump anywhere in a document with as few keystrokes as possible
  * [rhysd/clever-f.vim](https://github.com/rhysd/clever-f.vim) : extends f, F, t and T mappings for more convenience. Instead of `;`, `f` is available to repeat
  * [rlane/pounce.nvim](https://github.com/rlane/pounce.nvim) : It's based on incremental fuzzy search.
  * [svermeulen/vim-extended-ft](https://github.com/svermeulen/vim-extended-ft) : multiline, smart case, highlighting and more for `f`, `t`, `T`, `F`
  * [t9md/vim-smalls](https://github.com/t9md/vim-smalls) : Search and jump with easymotion style
## remote
  * [chipsenkbeil/distant.nvim](https://github.com/chipsenkbeil/distant.nvim) : A wrapper around distant that enables users to edit remote files from the comfort of their local environment
  * [esensar/nvim-dev-containera](https://github.com/esensar/nvim-dev-containera) : provide functionality similar to VSCode's remote container development plugin
  * [jamestthompson3/nvim-remote-containers](https://github.com/jamestthompson3/nvim-remote-containers) : give you the functionality of VSCode's remote container development plugin
## visual
  * [ahmedkhalf/notif.nvim](https://github.com/ahmedkhalf/notif.nvim) : Notification system
  * [bennypowers/nvim-regexplainer](https://github.com/bennypowers/nvim-regexplainer) : Describe the regular expression under the cursor
  * [chrisbra/changesplugin](https://github.com/chrisbra/changesplugin) : visualize which lines have been changed since editing started
  * [chrisbra/dynamicsigns](https://github.com/chrisbra/dynamicsigns) : Using Signs for different things (visualy)
  * [edluffy/specs.nvim](https://github.com/edluffy/specs.nvim) : Show where your cursor moves when jumping large distances
  * [gennaro-tedesco/nvim-peekup](https://github.com/gennaro-tedesco/nvim-peekup) : peek registers befor pasting them
  * [haringsrob/nvim_context_vt](https://github.com/haringsrob/nvim_context_vt) : Shows virtual text of the current context after functions, methods, statements, etc.
  * [karb94/neoscroll.nvim](https://github.com/karb94/neoscroll.nvim) : smooth scrolling neovim plugin written in lua
  * [kevinhwang91/nvim-hlslens](https://github.com/kevinhwang91/nvim-hlslens) : search with more visuals
  * [lukas-reineke/virt-column.nvim](https://github.com/lukas-reineke/virt-column.nvim) : Display a character as the colorcolumn
  * [monkoose/matchparen.nvim](https://github.com/monkoose/matchparen.nvim) : highlight matching parentheses
  * [myusuf3/numbers.vim](https://github.com/myusuf3/numbers.vim) : intelligently toggling line numbers
  * [nacro90/numb.nvim](https://github.com/nacro90/numb.nvim) : Peeking the buffer while entering command :[number]
  * [ntpeters/vim-better-whitespace](https://github.com/ntpeters/vim-better-whitespace) : causes all trailing whitespace characters to be highlighted
  * [rcarriga/nvim-notify](https://github.com/rcarriga/nvim-notify) : fancy, configurable, notification manager
  * [rktjmp/highlight-current-n.nvim](https://github.com/rktjmp/highlight-current-n.nvim) : highlights the current /, ? or * match under your cursor when pressing n or N and gets out of the way afterwards
  * [romainl/vim-cool](https://github.com/romainl/vim-cool) : disables search highlighting when you are done searching and re-enables it when you search again
  * [tjdevries/train.nvim](https://github.com/tjdevries/train.nvim) : Train yourself with vim motions and make your own train tracks
  * [tversteeg/registers.nvim](https://github.com/tversteeg/registers.nvim) : Show register content when you try to access it
  * [winston0410/range-highlight.nvim](https://github.com/winston0410/range-highlight.nvim) : hightlights ranges you have entered in commandline
  * [xiyaowong/virtcolumn.nvim](https://github.com/xiyaowong/virtcolumn.nvim) : Display a character as the colorcolumn
## highlight-underline
  * [azabiong/vim-highlighter](https://github.com/azabiong/vim-highlighter) : highlight words and expressions
  * [itchyny/vim-cursorword](https://github.com/itchyny/vim-cursorword) : Underlines the word under the cursor
  * [pocco81/highstr.nvim](https://github.com/pocco81/highstr.nvim) : highlighting visual selections like in a normal document editor
  * [rrethy/vim-illuminate](https://github.com/rrethy/vim-illuminate) : automatically highlighting other uses of the current word under the cursor
  * [xiyaowong/nvim-cursorword](https://github.com/xiyaowong/nvim-cursorword) : part of [yamatsum/nvim-cursorline](https://github.com/yamatsum/nvim-cursorline)
  * [yamatsum/nvim-cursorline](https://github.com/yamatsum/nvim-cursorline) : Highlight words and lines on the cursor
## snippets
  * [drmingdrmer/xptemplate](https://github.com/drmingdrmer/xptemplate) : Code snippets engine for Vim, And snippets library
  * [garbas/vim-snipmate](https://github.com/garbas/vim-snipmate) : provide support for textual snippets, similar to TextMate or other Vim plugins like UltiSnips
  * [honza/vim-snippets](https://github.com/honza/vim-snippets) : contains snippets librarys for various programming languages
  * [hrsh7th/vim-vsnip](https://github.com/hrsh7th/vim-vsnip) : VSCode(LSP)'s snippet feature in vim
  * [l3mon4d3/luasnip](https://github.com/l3mon4d3/luasnip) : snippet engine written in lua
  * [shougo/neosnippet.vim](https://github.com/shougo/neosnippet.vim) : The Neosnippet plug-In adds snippet support to Vim
  * [sirver/ultisnips](https://github.com/sirver/ultisnips) : is the ultimate solution for snippets
## marks
  * [chentoast/marks.nvim](https://github.com/chentoast/marks.nvim) : A better user experience for interacting with and manipulating Vim marks
  * [crusj/bookmarks.nvim](https://github.com/crusj/bookmarks.nvim) : Remember file locations and sort by time and frequency
  * [kshenoy/vim-signature](https://github.com/kshenoy/vim-signature) : place, toggle and display marks
  * [mattesgroeger/vim-bookmarks](https://github.com/mattesgroeger/vim-bookmarks) : toggling bookmarks per line and more
## comment
  * [tpope/vim-commentary](https://github.com/tpope/vim-commentary) : Comment stuff out
## terminal
  * [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim) : persist and toggle multiple terminals
  * [brettanomyces/nvim-editcommand](https://github.com/brettanomyces/nvim-editcommand) : Edit your current shell command inside a scratch buffer
  * [brettanomyces/nvim-terminus](https://github.com/brettanomyces/nvim-terminus) : Edit your current command in a scratch buffer
  * [bronzehedwick/vim-primary-terminal](https://github.com/bronzehedwick/vim-primary-terminal) : Simple terminal management for Neovim.
  * [kassio/neoterm](https://github.com/kassio/neoterm) : Use the same terminal for everything
## markdown-org-neorg
  * [jubnzv/mdeval.nvim](https://github.com/jubnzv/mdeval.nvim) : allows you evaluate code blocks inside markdown, vimwiki, orgmode.nvim and norg documents
  * [lukas-reineke/headlines.nvim](https://github.com/lukas-reineke/headlines.nvim) : adds highlights for text filetypes, like markdown, orgmode, and neorg
  * [nvim-neorg/neorg](https://github.com/nvim-neorg/neorg) : neorg Integration
  * [nvim-orgmode/orgmode](https://github.com/nvim-orgmode/orgmode) : org Integration
  * [suan/vim-instant-markdown](https://github.com/suan/vim-instant-markdown) : preview markdown files in your browser
## syntax
  * [akz92/vim-ionic2](https://github.com/akz92/vim-ionic2) : ionic2 syntax highlight
  * [cespare/vim-toml](https://github.com/cespare/vim-toml) : toml syntax highlight
  * [jwalton512/vim-blade](https://github.com/jwalton512/vim-blade) : blade template syntax highlight
  * [kovetskiy/sxhkd-vim](https://github.com/kovetskiy/sxhkd-vim) : sxhkd syntax highlight
  * [potatoesmaster/i3-vim-syntax](https://github.com/potatoesmaster/i3-vim-syntax) : i3 config syntax highlight
## telescope-extensions
  * [aloussase/telescope-gradle.nvim](https://github.com/aloussase/telescope-gradle.nvim) : telescope extensions to run gradle tasks
  * [aloussase/telescope-maven-search](https://github.com/aloussase/telescope-maven-search) : telescope extensions to search dependencies in MavenCentral
  * [angkeith/telescope-terraform-doc.nvim](https://github.com/angkeith/telescope-terraform-doc.nvim) : telescope extensions to search and browse terraform providers docs
  * [axkirillov/telescope-changed-files](https://github.com/axkirillov/telescope-changed-files) : telescope extensions to browse files that changed between your branch and develop
  * [benfowler/telescope-luasnip.nvim](https://github.com/benfowler/telescope-luasnip.nvim) : telescope extensions to list luasnip snippets
  * [bi0ha2ard/telescope-ros.nvim](https://github.com/bi0ha2ard/telescope-ros.nvim) : telescope extensions to select ROS(2) package
  * [brandoncc/telescope-harpoon.nvim](https://github.com/brandoncc/telescope-harpoon.nvim) : telescope extensions to harpoon (depreciated)
  * [camgraff/telescope-tmux.nvim](https://github.com/camgraff/telescope-tmux.nvim) : telescope extensions to fuzzy-finding over tmux targets
  * [chip/telescope-code-fence.nvim](https://github.com/chip/telescope-code-fence.nvim) : telescope extensions to fetch and parse text files from Github and provide a list of markdown code fences
  * [chip/telescope-software-licenses.nvim](https://github.com/chip/telescope-software-licenses.nvim) : telescope extensions to view common software licenses
  * [cljoly/telescope-repo.nvim](https://github.com/cljoly/telescope-repo.nvim) : telescope extensions to jump to any repository in filesystem
  * [crispgm/telescope-heading.nvim](https://github.com/crispgm/telescope-heading.nvim) : telescope extensions to switch between document's headings
  * [danielpieper/telescope-tmuxinator.nvim](https://github.com/danielpieper/telescope-tmuxinator.nvim) : telescope extensions to integrate with tmuxinator
  * [dhruvmanila/telescope-bookmarks.nvim](https://github.com/dhruvmanila/telescope-bookmarks.nvim) : telescope extensions to open your browser bookmarks
  * [fannheyward/telescope-coc.nvim](https://github.com/fannheyward/telescope-coc.nvim) : telescope extensions to find/filter/preview/pick results from coc.nvim
  * [fcying/telescope-ctags-outline.nvim](https://github.com/fcying/telescope-ctags-outline.nvim) : telescope extensions to get ctags outline
  * [feiyoug/command_center.nvim](https://github.com/feiyoug/command_center.nvim) : telescope extensions to Create and manage keybindings and commands in a more organized manner, and search them quickly
  * [fhill2/telescope-ultisnips.nvim](https://github.com/fhill2/telescope-ultisnips.nvim) : telescope extensions to Integration with ultisnips.nvim
  * [gbrlsnchs/telescope-lsp-handlers.nvim](https://github.com/gbrlsnchs/telescope-lsp-handlers.nvim) : telescope extensions to handle a bunch of lsp stuff
  * [gustavokatel/telescope-asynctasks.nvim](https://github.com/gustavokatel/telescope-asynctasks.nvim) : telescope extensions to integrate with [skywind3000/asynctasks.vim](https://github.com/skywind3000/asynctasks.vim)
  * [jvgrootveld/telescope-zoxide](https://github.com/jvgrootveld/telescope-zoxide) : telescope extensions to allow you to operate zoxide
  * [kelly-lin/telescope-ag](https://github.com/kelly-lin/telescope-ag) : telescope extensions to provide The Silver Searcher (Ag) functionality
  * [kolja/telescope-opds](https://github.com/kolja/telescope-opds) : telescope extensions to Browse opds catalogs
  * [linarcx/telescope-changes.nvim](https://github.com/linarcx/telescope-changes.nvim) : telescope extensions to wrapper around :changes
  * [linarcx/telescope-command-palette.nvim](https://github.com/linarcx/telescope-command-palette.nvim) : telescope extensions to help you to access your custom commands/function/key-bindings
  * [linarcx/telescope-env.nvim](https://github.com/linarcx/telescope-env.nvim) : telescope extensions to Watch environment variables
  * [linarcx/telescope-ports.nvim](https://github.com/linarcx/telescope-ports.nvim) : telescope extensions to Shows ports that are open on your system and gives you the ability to kill their process
  * [nvim-neorg/neorg-telescope](https://github.com/nvim-neorg/neorg-telescope) : telescope extensions to browse neorg file headings
  * [nvim-telescope/telescope-frecency.nvim](https://github.com/nvim-telescope/telescope-frecency.nvim) : telescope extensions to offers intelligent prioritization when selecting files from your editing history
  * [nvim-telescope/telescope-ghq.nvim](https://github.com/nvim-telescope/telescope-ghq.nvim) : telescope extensions to provide its users with operating x-motemen/ghq
  * [nvim-telescope/telescope-symbols.nvim](https://github.com/nvim-telescope/telescope-symbols.nvim) : telescope extensions to pick symbols
  * [tom-anders/telescope-vim-bookmarks.nvim](https://github.com/tom-anders/telescope-vim-bookmarks.nvim) : telescope extensions to integrate with [mattesgroeger/vim-bookmarks](https://github.com/mattesgroeger/vim-bookmarks)
  * [wesleimp/telescope-windowizer.nvim](https://github.com/wesleimp/telescope-windowizer.nvim) : telescope extensions to Create new tmux window ready for edit your selected file inside vim
  * [xiyaowong/telescope-emoji.nvim](https://github.com/xiyaowong/telescope-emoji.nvim) : telescope extensions to search emoji
## nvim-cmp-extensions
  * [david-kunz/cmp-npm](https://github.com/david-kunz/cmp-npm) : nvim-cmp extension for npm autocomplete
  * [f3fora/cmp-spell](https://github.com/f3fora/cmp-spell) : nvim-cmp extension for spell autocomplete
  * [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer) : nvim-cmp extension for buffer autocomplete
  * [hrsh7th/cmp-calc](https://github.com/hrsh7th/cmp-calc) : nvim-cmp extension for math calculation autocomplete
  * [hrsh7th/cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline) : nvim-cmp extension for cmdline autocomplete
  * [hrsh7th/cmp-nvim-lsp-signature-help](https://github.com/hrsh7th/cmp-nvim-lsp-signature-help) : nvim-cmp extension for showing lsp help in autocomplete
  * [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp) : nvim-cmp extension for lsp autocomplete
  * [hrsh7th/cmp-nvim-lua](https://github.com/hrsh7th/cmp-nvim-lua) : nvim-cmp extension for lua autocomplete
  * [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path) : nvim-cmp extension for path autocomplete
  * [lukas-reineke/cmp-rg](https://github.com/lukas-reineke/cmp-rg) : nvim-cmp extension for rg autocomplete
  * [mtoohey31/cmp-fish](https://github.com/mtoohey31/cmp-fish) : nvim-cmp extension for fish autocomplete
  * [petertriho/cmp-git](https://github.com/petertriho/cmp-git) : nvim-cmp extension for git autocomplete
  * [quangnguyen30192/cmp-nvim-tags](https://github.com/quangnguyen30192/cmp-nvim-tags) : nvim-cmp extension for tag autocomplete
  * [quangnguyen30192/cmp-nvim-ultisnips](https://github.com/quangnguyen30192/cmp-nvim-ultisnips) : nvim-cmp extension for ultisnips autocomplete
  * [ray-x/cmp-treesitter](https://github.com/ray-x/cmp-treesitter) : nvim-cmp extension for treesitter autocomplete
  * [rcarriga/cmp-dap](https://github.com/rcarriga/cmp-dap) : nvim-cmp extension for dap autocomplete
  * [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip) : nvim-cmp extension for luasnip autocomplete
  * [tzachar/cmp-tabnine](https://github.com/tzachar/cmp-tabnine) : nvim-cmp extension for tabline autocomplete
  * [zbirenbaum/copilot-cmp](https://github.com/zbirenbaum/copilot-cmp) : nvim-cmp extension for copilot autocomplete
## use-instead
  * [acksld/nvim-revj.lua](https://github.com/acksld/nvim-revj.lua) : is not maineind/depreciated, use [acksld/nvim-trevj.lua](https://github.com/acksld/nvim-trevj.lua) instead
  * [arakashic/chromatica.nvim](https://github.com/arakashic/chromatica.nvim) : is not maineind/depreciated, use [jackguo380/vim-lsp-cxx-highlight](https://github.com/jackguo380/vim-lsp-cxx-highlight) instead
  * [artur-shaik/vim-javacomplete2](https://github.com/artur-shaik/vim-javacomplete2) : is not maineind/depreciated, use [artur-shaik/jc.nvim](https://github.com/artur-shaik/jc.nvim) instead
  * [c0r73x/neotags.nvim](https://github.com/c0r73x/neotags.nvim) : is not maineind/depreciated, use [c0r73x/neotags.lua](https://github.com/c0r73x/neotags.lua) instead
  * [chriskempson/vim-tomorrow-theme](https://github.com/chriskempson/vim-tomorrow-theme) : is not maineind/depreciated, use [chriskempson/base16-vim](https://github.com/chriskempson/base16-vim) instead
  * [evanquan/vim-textobj-delimiters](https://github.com/evanquan/vim-textobj-delimiters) : is not maineind/depreciated, use [wellle/targets.vim](https://github.com/wellle/targets.vim) instead
  * [gregsexton/gitv](https://github.com/gregsexton/gitv) : is not maineind/depreciated, use [junegunn/gv.vim](https://github.com/junegunn/gv.vim) instead
  * [haya14busa/incsearch.vim](https://github.com/haya14busa/incsearch.vim) : is not maineind/depreciated, use [haya14busa/is.vim](https://github.com/haya14busa/is.vim) instead
  * [huawenyu/neogdb.vim](https://github.com/huawenyu/neogdb.vim) : is not maineind/depreciated, use [huawenyu/vimgdb](https://github.com/huawenyu/vimgdb) instead
  * [msanders/snipmate.vim](https://github.com/msanders/snipmate.vim) : is not maineind/depreciated, use [garbas/vim-snipmate](https://github.com/garbas/vim-snipmate) instead
  * [svermeulen/vim-easyclip](https://github.com/svermeulen/vim-easyclip) : is not maineind/depreciated, use [svermeulen/vim-cutlass](https://github.com/svermeulen/vim-cutlass) and [svermeulen/vim-yoink](https://github.com/svermeulen/vim-yoink) and [svermeulen/vim-subversive](https://github.com/svermeulen/vim-subversive) instead
  * [terryma/vim-multiple-cursors](https://github.com/terryma/vim-multiple-cursors) : is not maineind/depreciated, use [mg979/vim-visual-multi](https://github.com/mg979/vim-visual-multi) instead
## libs
  * [0styx0/abbremand.nvim](https://github.com/0styx0/abbremand.nvim) : is library for [0styx0/abbreinder.nvim](https://github.com/0styx0/abbreinder.nvim)
  * [anuvyklack/keymap-layer.nvim](https://github.com/anuvyklack/keymap-layer.nvim) : is library for [anuvyklack/hydra.nvim](https://github.com/anuvyklack/hydra.nvim)
## gui
  * [equalsraf/neovim-qt](https://github.com/equalsraf/neovim-qt)
## yanklist
  * [acksld/nvim-neoclip.lua](https://github.com/acksld/nvim-neoclip.lua)
  * [bfredl/nvim-miniyank](https://github.com/bfredl/nvim-miniyank)
  * [cyansprite/extract](https://github.com/cyansprite/extract)
  * [gbprod/yanky.nvim](https://github.com/gbprod/yanky.nvim)
  * [maxbrunsfeld/vim-yankstack](https://github.com/maxbrunsfeld/vim-yankstack)
  * [svermeulen/vim-yoink](https://github.com/svermeulen/vim-yoink)
## bufferline
  * [ap/vim-buftabline](https://github.com/ap/vim-buftabline)
  * [bling/vim-bufferline](https://github.com/bling/vim-bufferline)
  * [zefei/vim-wintabs](https://github.com/zefei/vim-wintabs)
## ide
  * [abstract-ide/abstract](https://github.com/abstract-ide/abstract)
  * [artart222/codeart](https://github.com/artart222/codeart)
  * [askfiy/nvim](https://github.com/askfiy/nvim)
  * [astronvim/astronvim](https://github.com/astronvim/astronvim)
  * [cankolay3499/cnvim](https://github.com/cankolay3499/cnvim)
  * [cosmicnvim/cosmicnvim](https://github.com/cosmicnvim/cosmicnvim)
  * [crivotz/nv-ide](https://github.com/crivotz/nv-ide)
  * [cstsunfu/.sea.nvim](https://github.com/cstsunfu/.sea.nvim)
  * [hackorum/vapournvim](https://github.com/hackorum/vapournvim)
  * [imbacraft/dusk.nvim](https://github.com/imbacraft/dusk.nvim)
  * [jrychn/modulevim](https://github.com/jrychn/modulevim)
  * [jueqingsizhe66/windowvimfaster](https://github.com/jueqingsizhe66/windowvimfaster)
  * [lunarvim/lunarvim](https://github.com/lunarvim/lunarvim)
  * [ntbbloodbath/doom-nvim](https://github.com/ntbbloodbath/doom-nvim)
  * [nvoid-lua/nvoid](https://github.com/nvoid-lua/nvoid)
  * [shaeinst/roshnivim](https://github.com/shaeinst/roshnivim)
  * [shaunsingh/nyoom.nvim](https://github.com/shaunsingh/nyoom.nvim)
  * [siduck76/nvchad](https://github.com/siduck76/nvchad)
  * [spacevim/spacevim](https://github.com/spacevim/spacevim)
  * [vi-tality/neovitality](https://github.com/vi-tality/neovitality)
## tabline
  * [akinsho/bufferline.nvim](https://github.com/akinsho/bufferline.nvim)
  * [akinsho/nvim-bufferline.lua](https://github.com/akinsho/nvim-bufferline.lua)
  * [alvarosevilla95/luatab.nvim](https://github.com/alvarosevilla95/luatab.nvim)
  * [chrboesch/vim-tabline](https://github.com/chrboesch/vim-tabline)
  * [crispgm/nvim-tabline](https://github.com/crispgm/nvim-tabline)
  * [johann2357/nvim-smartbufs](https://github.com/johann2357/nvim-smartbufs)
  * [kdheepak/tabline.nvim](https://github.com/kdheepak/tabline.nvim)
  * [nanozuki/tabby.nvim](https://github.com/nanozuki/tabby.nvim)
  * [noib3/cokeline.nvim](https://github.com/noib3/cokeline.nvim)
  * [rafcamlet/tabline-framework.nvim](https://github.com/rafcamlet/tabline-framework.nvim)
  * [romgrk/barbar.nvim](https://github.com/romgrk/barbar.nvim)
## starter-page
  * [glepnir/dashboard-nvim](https://github.com/glepnir/dashboard-nvim)
  * [goolord/alpha-nvim](https://github.com/goolord/alpha-nvim)
## statusline
  * [adelarsq/neoline.vim](https://github.com/adelarsq/neoline.vim)
  * [b0o/incline.nvim](https://github.com/b0o/incline.nvim)
  * [beauwilliams/statusline.lua](https://github.com/beauwilliams/statusline.lua)
  * [datwaft/bubbly.nvim](https://github.com/datwaft/bubbly.nvim)
  * [feline-nvim/feline.nvim](https://github.com/feline-nvim/feline.nvim)
  * [itchyny/lightline.vim](https://github.com/itchyny/lightline.vim)
  * [konapun/vacuumline.nvim](https://github.com/konapun/vacuumline.nvim)
  * [ntbbloodbath/galaxyline.nvim](https://github.com/ntbbloodbath/galaxyline.nvim)
  * [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)
  * [ojroques/nvim-hardline](https://github.com/ojroques/nvim-hardline)
  * [powerline/powerline](https://github.com/powerline/powerline)
  * [rebelot/heirline.nvim](https://github.com/rebelot/heirline.nvim)
  * [tamton-aquib/staline.nvim](https://github.com/tamton-aquib/staline.nvim)
  * [tjdevries/express_line.nvim](https://github.com/tjdevries/express_line.nvim)
  * [tpope/vim-flagship](https://github.com/tpope/vim-flagship)
  * [vim-airline/vim-airline](https://github.com/vim-airline/vim-airline)
  * [windwp/windline.nvim](https://github.com/windwp/windline.nvim)
## autocomplete
  * [ajh17/vimcompletesme](https://github.com/ajh17/vimcompletesme)
  * [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp)
  * [maralla/completor.vim](https://github.com/maralla/completor.vim)
  * [ms-jpq/coq_nvim](https://github.com/ms-jpq/coq_nvim)
  * [noib3/nvim-compleet](https://github.com/noib3/nvim-compleet)
  * [vigoux/complementree.nvim](https://github.com/vigoux/complementree.nvim)
  * [ycm-core/youcompleteme](https://github.com/ycm-core/youcompleteme)
## colorscheme
  * [adisen99/apprentice.nvim](https://github.com/adisen99/apprentice.nvim)
  * [adisen99/codeschool.nvim](https://github.com/adisen99/codeschool.nvim)
  * [alessandroyorba/despacio](https://github.com/alessandroyorba/despacio)
  * [altercation/vim-colors-solarized](https://github.com/altercation/vim-colors-solarized)
  * [andersevenrud/nordic.nvim](https://github.com/andersevenrud/nordic.nvim)
  * [arcticicestudio/nord-vim](https://github.com/arcticicestudio/nord-vim)
  * [arthurealike/vim-j](https://github.com/arthurealike/vim-j)
  * [arzg/vim-substrata](https://github.com/arzg/vim-substrata)
  * [axvr/photon.vim](https://github.com/axvr/photon.vim)
  * [axvr/raider.vim](https://github.com/axvr/raider.vim)
  * [base16-project/base16-vim](https://github.com/base16-project/base16-vim)
  * [benwr/tuftish](https://github.com/benwr/tuftish)
  * [bkegley/gloombuddy](https://github.com/bkegley/gloombuddy)
  * [blueshirts/darcula](https://github.com/blueshirts/darcula)
  * [bluz71/vim-moonfly-colors](https://github.com/bluz71/vim-moonfly-colors)
  * [bluz71/vim-nightfly-guicolors](https://github.com/bluz71/vim-nightfly-guicolors)
  * [catppuccin/nvim](https://github.com/catppuccin/nvim)
  * [challenger-deep-theme/vim](https://github.com/challenger-deep-theme/vim)
  * [chriskempson/base16-vim](https://github.com/chriskempson/base16-vim)
  * [christianchiarulli/nvcode-color-schemes.vim](https://github.com/christianchiarulli/nvcode-color-schemes.vim)
  * [chrsm/paramount-ng.nvim](https://github.com/chrsm/paramount-ng.nvim)
  * [cpea2506/one_monokai.nvim](https://github.com/cpea2506/one_monokai.nvim)
  * [dracula/vim](https://github.com/dracula/vim)
  * [edeneast/nightfox.nvim](https://github.com/edeneast/nightfox.nvim)
  * [ellisonleao/gruvbox.nvim](https://github.com/ellisonleao/gruvbox.nvim)
  * [elvessousa/sobrio](https://github.com/elvessousa/sobrio)
  * [fenetikm/falcon](https://github.com/fenetikm/falcon)
  * [flazz/vim-colorschemes](https://github.com/flazz/vim-colorschemes)
  * [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim)
  * [frenzyexists/aquarium-vim](https://github.com/frenzyexists/aquarium-vim)
  * [ghifarit53/tokyonight-vim](https://github.com/ghifarit53/tokyonight-vim)
  * [glepnir/zephyr-nvim](https://github.com/glepnir/zephyr-nvim)
  * [hardselius/warlock](https://github.com/hardselius/warlock)
  * [heraldofsolace/nisha-vim](https://github.com/heraldofsolace/nisha-vim)
  * [icymind/neosolarized](https://github.com/icymind/neosolarized)
  * [ishan9299/modus-theme-vim](https://github.com/ishan9299/modus-theme-vim)
  * [ishan9299/nvim-solarized-lua](https://github.com/ishan9299/nvim-solarized-lua)
  * [jayhowie/crystal-cove](https://github.com/jayhowie/crystal-cove)
  * [jnurmine/zenburn](https://github.com/jnurmine/zenburn)
  * [jonathanfilip/vim-lucius](https://github.com/jonathanfilip/vim-lucius)
  * [joshdick/onedark.vim](https://github.com/joshdick/onedark.vim)
  * [jpo/vim-railscasts-theme](https://github.com/jpo/vim-railscasts-theme)
  * [jsit/toast.vim](https://github.com/jsit/toast.vim)
  * [junegunn/seoul256.vim](https://github.com/junegunn/seoul256.vim)
  * [kabbamine/yowish.vim](https://github.com/kabbamine/yowish.vim)
  * [kaiuri/nvim-mariana](https://github.com/kaiuri/nvim-mariana)
  * [kdheepak/monochrome.nvim](https://github.com/kdheepak/monochrome.nvim)
  * [kvrohit/rasmus.nvim](https://github.com/kvrohit/rasmus.nvim)
  * [kvrohit/substrata.nvim](https://github.com/kvrohit/substrata.nvim)
  * [kyazdani42/blue-moon](https://github.com/kyazdani42/blue-moon)
  * [ladge/antarctic-vim](https://github.com/ladge/antarctic-vim)
  * [lalitmee/cobalt2.nvim](https://github.com/lalitmee/cobalt2.nvim)
  * [ldelossa/vimdark](https://github.com/ldelossa/vimdark)
  * [lifepillar/vim-solarized8](https://github.com/lifepillar/vim-solarized8)
  * [lmburns/kimbox](https://github.com/lmburns/kimbox)
  * [lourenci/github-colors](https://github.com/lourenci/github-colors)
  * [luisiacc/gruvbox-baby](https://github.com/luisiacc/gruvbox-baby)
  * [lunarvim/onedarker.nvim](https://github.com/lunarvim/onedarker.nvim)
  * [mangeshrex/uwu.vim](https://github.com/mangeshrex/uwu.vim)
  * [markeganfuller/vim-journeyman](https://github.com/markeganfuller/vim-journeyman)
  * [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim)
  * [maxst/flatcolor](https://github.com/maxst/flatcolor)
  * [mcchrish/zenbones.nvim](https://github.com/mcchrish/zenbones.nvim)
  * [metalelf0/jellybeans-nvim](https://github.com/metalelf0/jellybeans-nvim)
  * [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next)
  * [mhinz/vim-janah](https://github.com/mhinz/vim-janah)
  * [mjlbach/onedark.nvim](https://github.com/mjlbach/onedark.nvim)
  * [mofiqul/dracula.nvim](https://github.com/mofiqul/dracula.nvim)
  * [mofiqul/vscode.nvim](https://github.com/mofiqul/vscode.nvim)
  * [morhetz/gruvbox](https://github.com/morhetz/gruvbox)
  * [nanotech/jellybeans.vim](https://github.com/nanotech/jellybeans.vim)
  * [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim)
  * [nightsense/cosmic_latte](https://github.com/nightsense/cosmic_latte)
  * [ntbbloodbath/doom-one.nvim](https://github.com/ntbbloodbath/doom-one.nvim)
  * [nxvu699134/vn-night.nvim](https://github.com/nxvu699134/vn-night.nvim)
  * [olimorris/onedarkpro.nvim](https://github.com/olimorris/onedarkpro.nvim)
  * [overcache/neosolarized](https://github.com/overcache/neosolarized)
  * [owickstrom/vim-colors-paramount](https://github.com/owickstrom/vim-colors-paramount)
  * [phha/zenburn.nvim](https://github.com/phha/zenburn.nvim)
  * [phsix/nvim-hybrid](https://github.com/phsix/nvim-hybrid)
  * [plan9-for-vimspace/acme-colors](https://github.com/plan9-for-vimspace/acme-colors)
  * [projekt0n/github-nvim-theme](https://github.com/projekt0n/github-nvim-theme)
  * [rafamadriz/neon](https://github.com/rafamadriz/neon)
  * [rafi/awesome-vim-colorschemes](https://github.com/rafi/awesome-vim-colorschemes)
  * [ray-x/aurora](https://github.com/ray-x/aurora)
  * [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim)
  * [rishabhrd/gruvy](https://github.com/rishabhrd/gruvy)
  * [rishabhrd/nvim-rdark](https://github.com/rishabhrd/nvim-rdark)
  * [rmehri01/onenord.nvim](https://github.com/rmehri01/onenord.nvim)
  * [robertmeta/nofrils](https://github.com/robertmeta/nofrils)
  * [roboron3042/cyberpunk-neon](https://github.com/roboron3042/cyberpunk-neon)
  * [rockerboo/boo-colorscheme-nvim](https://github.com/rockerboo/boo-colorscheme-nvim)
  * [romainl/apprentice](https://github.com/romainl/apprentice)
  * [romainl/flattened](https://github.com/romainl/flattened)
  * [romainl/vim-bruin](https://github.com/romainl/vim-bruin)
  * [romainl/vim-dichromatic](https://github.com/romainl/vim-dichromatic)
  * [romainl/vim-malotru](https://github.com/romainl/vim-malotru)
  * [romainl/vim-sweet16](https://github.com/romainl/vim-sweet16)
  * [rose-pine/neovim](https://github.com/rose-pine/neovim)
  * [rrethy/nvim-base16](https://github.com/rrethy/nvim-base16)
  * [rsms/sublime-theme](https://github.com/rsms/sublime-theme)
  * [sainnhe/edge](https://github.com/sainnhe/edge)
  * [sainnhe/everforest](https://github.com/sainnhe/everforest)
  * [sainnhe/gruvbox-material](https://github.com/sainnhe/gruvbox-material)
  * [sainnhe/sonokai](https://github.com/sainnhe/sonokai)
  * [saurabhdaware/vscode-calvera-dark](https://github.com/saurabhdaware/vscode-calvera-dark)
  * [savq/melange](https://github.com/savq/melange)
  * [shaeinst/roshnivim-cs](https://github.com/shaeinst/roshnivim-cs)
  * [shaunsingh/moonlight.nvim](https://github.com/shaunsingh/moonlight.nvim)
  * [shaunsingh/nord.nvim](https://github.com/shaunsingh/nord.nvim)
  * [shrimpram/vim-stella](https://github.com/shrimpram/vim-stella)
  * [sickill/vim-monokai](https://github.com/sickill/vim-monokai)
  * [softmotions/vim-dark-frost-theme](https://github.com/softmotions/vim-dark-frost-theme)
  * [swalladge/paper.vim](https://github.com/swalladge/paper.vim)
  * [tanvirtin/monokai.nvim](https://github.com/tanvirtin/monokai.nvim)
  * [tek256/simple-dark](https://github.com/tek256/simple-dark)
  * [th3whit3wolf/one-nvim](https://github.com/th3whit3wolf/one-nvim)
  * [th3whit3wolf/onebuddy](https://github.com/th3whit3wolf/onebuddy)
  * [th3whit3wolf/space-nvim](https://github.com/th3whit3wolf/space-nvim)
  * [theniceboy/nvim-deus](https://github.com/theniceboy/nvim-deus)
  * [therubymug/vim-pyte](https://github.com/therubymug/vim-pyte)
  * [tiagovla/tokyodark.nvim](https://github.com/tiagovla/tokyodark.nvim)
  * [titanzero/zephyrium](https://github.com/titanzero/zephyrium)
  * [tjdevries/gruvbuddy.nvim](https://github.com/tjdevries/gruvbuddy.nvim)
  * [tomasiser/vim-code-dark](https://github.com/tomasiser/vim-code-dark)
  * [tomasr/molokai](https://github.com/tomasr/molokai)
  * [tpope/vim-vividchalk](https://github.com/tpope/vim-vividchalk)
  * [u03c1/outrun-vim](https://github.com/u03c1/outrun-vim)
  * [vim-conf-live/vimconflive2021-colorscheme](https://github.com/vim-conf-live/vimconflive2021-colorscheme)
  * [vim-scripts/mayansmoke](https://github.com/vim-scripts/mayansmoke)
  * [vim-scripts/peaksea](https://github.com/vim-scripts/peaksea)
  * [wgibbs/vim-irblack](https://github.com/wgibbs/vim-irblack)
  * [whatyouhide/vim-gotham](https://github.com/whatyouhide/vim-gotham)
  * [wittyjudge/gruvbox-material.nvim](https://github.com/wittyjudge/gruvbox-material.nvim)
  * [yashguptaz/calvera-dark.nvim](https://github.com/yashguptaz/calvera-dark.nvim)
  * [yong1le/darkplus.nvim](https://github.com/yong1le/darkplus.nvim)
  * [yonlu/omni.vim](https://github.com/yonlu/omni.vim)
  * [yuttie/hydrangea-vim](https://github.com/yuttie/hydrangea-vim)
  * [yorickpeterse/nvim-grey](https://gitlab.com/yorickpeterse/nvim-grey)
  * [yorickpeterse/vim-paper](https://gitlab.com/yorickpeterse/vim-paper)
# Not-documented
  * [907th/vim-auto-save](https://github.com/907th/vim-auto-save)
  * [acksld/nvim-anywise-reg.lua](https://github.com/acksld/nvim-anywise-reg.lua)
  * [acksld/nvim-pytrize.lua](https://github.com/acksld/nvim-pytrize.lua)
  * [ackyshake/vimcompletesme](https://github.com/ackyshake/vimcompletesme)
  * [ahmedkhalf/jupyter-nvim](https://github.com/ahmedkhalf/jupyter-nvim)
  * [ahmedkhalf/lsp-rooter.nvim](https://github.com/ahmedkhalf/lsp-rooter.nvim)
  * [akinsho/flutter-tools.nvim](https://github.com/akinsho/flutter-tools.nvim)
  * [akinsho/nvim-toggleterm.lua](https://github.com/akinsho/nvim-toggleterm.lua)
  * [akiyosi/goneovim](https://github.com/akiyosi/goneovim)
  * [amadeus/vim-convert-color-to](https://github.com/amadeus/vim-convert-color-to)
  * [ameertaweel/todo.nvim](https://github.com/ameertaweel/todo.nvim)
  * [amirrezaask/actions.nvim](https://github.com/amirrezaask/actions.nvim)
  * [amirrezaask/fuzzy.nvim](https://github.com/amirrezaask/fuzzy.nvim)
  * [amopel/vim-log-print](https://github.com/amopel/vim-log-print)
  * [amrbashir/nvim-docs-view](https://github.com/amrbashir/nvim-docs-view)
  * [andersevenrud/compe-tmux](https://github.com/andersevenrud/compe-tmux)
  * [andrewradev/linediff.vim](https://github.com/andrewradev/linediff.vim)
  * [andweeb/presence.nvim](https://github.com/andweeb/presence.nvim)
  * [andythigpen/nvim-coverage](https://github.com/andythigpen/nvim-coverage)
  * [anihm136/importmagic.nvim](https://github.com/anihm136/importmagic.nvim)
  * [anott03/nvim-lspinstall](https://github.com/anott03/nvim-lspinstall)
  * [anuvyklack/help-vsplit.nvim](https://github.com/anuvyklack/help-vsplit.nvim)
  * [anuvyklack/nvim-keymap-amend](https://github.com/anuvyklack/nvim-keymap-amend)
  * [aonemd/fmt.vim](https://github.com/aonemd/fmt.vim)
  * [ap/vim-readdir](https://github.com/ap/vim-readdir)
  * [ap/vim-templates](https://github.com/ap/vim-templates)
  * [ap/vim-you-keep-using-that-word](https://github.com/ap/vim-you-keep-using-that-word)
  * [apzelos/blamer.nvim](https://github.com/apzelos/blamer.nvim)
  * [arnarg/todotxt.nvim](https://github.com/arnarg/todotxt.nvim)
  * [arnaud-lb/vim-php-namespace](https://github.com/arnaud-lb/vim-php-namespace)
  * [arp242/batchy.vim](https://github.com/arp242/batchy.vim)
  * [arp242/runbuf.vim](https://github.com/arp242/runbuf.vim)
  * [arthurxavierx/vim-caser](https://github.com/arthurxavierx/vim-caser)
  * [aserebryakov/vim-todo-lists](https://github.com/aserebryakov/vim-todo-lists)
  * [aserowy/tmux.nvim](https://github.com/aserowy/tmux.nvim)
  * [asheq/close-buffers](https://github.com/asheq/close-buffers)
  * [askfiy/nvim-picgo](https://github.com/askfiy/nvim-picgo)
  * [asvetliakov/vscode-neovim](https://github.com/asvetliakov/vscode-neovim)
  * [axieax/urlview.nvim](https://github.com/axieax/urlview.nvim)
  * [axlebedev/footprints](https://github.com/axlebedev/footprints)
  * [ayosec/hltermpaste.vim](https://github.com/ayosec/hltermpaste.vim)
  * [b0o/schemastore.nvim](https://github.com/b0o/schemastore.nvim)
  * [b3nj5m1n/kommentary](https://github.com/b3nj5m1n/kommentary)
  * [bagrat/vim-buffet](https://github.com/bagrat/vim-buffet)
  * [beeender/comrade](https://github.com/beeender/comrade)
  * [beeender/glrnvim](https://github.com/beeender/glrnvim)
  * [beloglazov/vim-online-thesaurus](https://github.com/beloglazov/vim-online-thesaurus)
  * [bkad/camelcasemotion](https://github.com/bkad/camelcasemotion)
  * [blackcauldron7/surround.nvim](https://github.com/blackcauldron7/surround.nvim)
  * [bluz71/vim-mistfly-statusline](https://github.com/bluz71/vim-mistfly-statusline)
  * [bobrown101/git_blame.nvim](https://github.com/bobrown101/git_blame.nvim)
  * [booperlv/cyclecolo.lua](https://github.com/booperlv/cyclecolo.lua)
  * [boson-joe/yanp](https://github.com/boson-joe/yanp)
  * [braxtons12/blame_line.nvim](https://github.com/braxtons12/blame_line.nvim)
  * [brenopacheco/vim-hydra](https://github.com/brenopacheco/vim-hydra)
  * [bronson/vim-trailing-whitespace](https://github.com/bronson/vim-trailing-whitespace)
  * [bronson/vim-visual-star-search](https://github.com/bronson/vim-visual-star-search)
  * [caenrique/nvim-toggle-terminal](https://github.com/caenrique/nvim-toggle-terminal)
  * [caenrique/swap-buffers.nvim](https://github.com/caenrique/swap-buffers.nvim)
  * [camspiers/lens.vim](https://github.com/camspiers/lens.vim)
  * [cappyzawa/trim.nvim](https://github.com/cappyzawa/trim.nvim)
  * [cdn.rawgit.com/sindresorhus](https://github.com/cdn.rawgit.com/sindresorhus)
  * [chaitanyabsprip/present.nvim](https://github.com/chaitanyabsprip/present.nvim)
  * [chengzeyi/multiterm.vim](https://github.com/chengzeyi/multiterm.vim)
  * [chentau/marks.nvim](https://github.com/chentau/marks.nvim)
  * [chiel92/vim-autoformat](https://github.com/chiel92/vim-autoformat)
  * [chimay/wheel](https://github.com/chimay/wheel)
  * [chrisbra/nrrwrgn](https://github.com/chrisbra/nrrwrgn)
  * [chrisbra/vim-diff-enhanced](https://github.com/chrisbra/vim-diff-enhanced)
  * [christoomey/vim-conflicted](https://github.com/christoomey/vim-conflicted)
  * [christoomey/vim-sort-motion](https://github.com/christoomey/vim-sort-motion)
  * [christoomey/vim-system-copy](https://github.com/christoomey/vim-system-copy)
  * [christoomey/vim-tmux-runner](https://github.com/christoomey/vim-tmux-runner)
  * [chrsm/impulse.nvim](https://github.com/chrsm/impulse.nvim)
  * [ciaranm/detectindent](https://github.com/ciaranm/detectindent)
  * [clojure-vim/jazz.nvim](https://github.com/clojure-vim/jazz.nvim)
  * [code-biscuits/nvim-biscuits](https://github.com/code-biscuits/nvim-biscuits)
  * [cohama/agit.vim](https://github.com/cohama/agit.vim)
  * [cohama/lexima.vim](https://github.com/cohama/lexima.vim)
  * [cometsong/commentframe.vim](https://github.com/cometsong/commentframe.vim)
  * [conormcd/matchindent.vim](https://github.com/conormcd/matchindent.vim)
  * [conradirwin/vim-bracketed-paste](https://github.com/conradirwin/vim-bracketed-paste)
  * [cosmicnvim/cosmic-ui](https://github.com/cosmicnvim/cosmic-ui)
  * [crag666/code_runner.nvim](https://github.com/crag666/code_runner.nvim)
  * [crispgm/nvim-go](https://github.com/crispgm/nvim-go)
  * [crusj/hierarchy-tree-go.nvim](https://github.com/crusj/hierarchy-tree-go.nvim)
  * [crusj/structrue-go.nvim](https://github.com/crusj/structrue-go.nvim)
  * [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim)
  * [cuducos/yaml.nvim](https://github.com/cuducos/yaml.nvim)
  * [dag/vim-fish](https://github.com/dag/vim-fish)
  * [danymat/neogen](https://github.com/danymat/neogen)
  * [darazaki/indent-o-matic](https://github.com/darazaki/indent-o-matic)
  * [david-kunz/jester](https://github.com/david-kunz/jester)
  * [davidgranstrom/nvim-markdown-preview](https://github.com/davidgranstrom/nvim-markdown-preview)
  * [davidgranstrom/scnvim](https://github.com/davidgranstrom/scnvim)
  * [davidhalter/jedi-vim](https://github.com/davidhalter/jedi-vim)
  * [dbgx/lldb.nvim](https://github.com/dbgx/lldb.nvim)
  * [dbmrq/vim-ditto](https://github.com/dbmrq/vim-ditto)
  * [dcampos/nvim-snippy](https://github.com/dcampos/nvim-snippy)
  * [dccsillag/magma-nvim](https://github.com/dccsillag/magma-nvim)
  * [declancm/cinnamon.nvim](https://github.com/declancm/cinnamon.nvim)
  * [declancm/windex.nvim](https://github.com/declancm/windex.nvim)
  * [delphinus/vim-auto-cursorline](https://github.com/delphinus/vim-auto-cursorline)
  * [dense-analysis/ale](https://github.com/dense-analysis/ale)
  * [derekwyatt/vim-scala](https://github.com/derekwyatt/vim-scala)
  * [devjoe/vim-codequery](https://github.com/devjoe/vim-codequery)
  * [dhruvasagar/vim-dotoo](https://github.com/dhruvasagar/vim-dotoo)
  * [dhruvasagar/vim-prosession](https://github.com/dhruvasagar/vim-prosession)
  * [dinhhuy258/git.nvim](https://github.com/dinhhuy258/git.nvim)
  * [dkprice/vim-easygrep](https://github.com/dkprice/vim-easygrep)
  * [dm1try/git_fastfix](https://github.com/dm1try/git_fastfix)
  * [dm1try/golden_size](https://github.com/dm1try/golden_size)
  * [dobrovolsky/kb-notes.nvim](https://github.com/dobrovolsky/kb-notes.nvim)
  * [dokwork/vim-hp](https://github.com/dokwork/vim-hp)
  * [donraphaco/neotex](https://github.com/donraphaco/neotex)
  * [dosimple/workspace.vim](https://github.com/dosimple/workspace.vim)
  * [doums/barow](https://github.com/doums/barow)
  * [dpelle/vim-languagetool](https://github.com/dpelle/vim-languagetool)
  * [dpzmick/neovim-hackernews](https://github.com/dpzmick/neovim-hackernews)
  * [dradtke/vim-dap](https://github.com/dradtke/vim-dap)
  * [drmikehenry/vim-fixkey](https://github.com/drmikehenry/vim-fixkey)
  * [drybalka/tree-climber.nvim](https://github.com/drybalka/tree-climber.nvim)
  * [drzel/vim-repo-edit](https://github.com/drzel/vim-repo-edit)
  * [drzel/vim-split-line](https://github.com/drzel/vim-split-line)
  * [dstein64/nvim-scrollview](https://github.com/dstein64/nvim-scrollview)
  * [dstein64/vim-startuptime](https://github.com/dstein64/vim-startuptime)
  * [duane9/nvim-rg](https://github.com/duane9/nvim-rg)
  * [duggiefresh/vim-easydir](https://github.com/duggiefresh/vim-easydir)
  * [dyng/ctrlsf.vim](https://github.com/dyng/ctrlsf.vim)
  * [dzhou121/gonvim](https://github.com/dzhou121/gonvim)
  * [echuraev/translate-shell.vim](https://github.com/echuraev/translate-shell.vim)
  * [edluffy/hologram.nvim](https://github.com/edluffy/hologram.nvim)
  * [edolphin-ydf/goimpl.nvim](https://github.com/edolphin-ydf/goimpl.nvim)
  * [egalpin/apt-vim](https://github.com/egalpin/apt-vim)
  * [egzvor/vimproviser](https://github.com/egzvor/vimproviser)
  * [el-iot/buffer-tree](https://github.com/el-iot/buffer-tree)
  * [el-iot/buffer-tree-explorer](https://github.com/el-iot/buffer-tree-explorer)
  * [elixir-editors/vim-elixir](https://github.com/elixir-editors/vim-elixir)
  * [ellisonleao/carbon-now.nvim](https://github.com/ellisonleao/carbon-now.nvim)
  * [ellisonleao/glow.nvim](https://github.com/ellisonleao/glow.nvim)
  * [ellisonleao/nvim-plugin-template](https://github.com/ellisonleao/nvim-plugin-template)
  * [eluum/vim-autopair](https://github.com/eluum/vim-autopair)
  * [erietz/vim-terminator](https://github.com/erietz/vim-terminator)
  * [ervandew/supertab](https://github.com/ervandew/supertab)
  * [esensar/nvim-dev-container](https://github.com/esensar/nvim-dev-container)
  * [ethanjwright/toolwindow.nvim](https://github.com/ethanjwright/toolwindow.nvim)
  * [ethanjwright/vs-tasks.nvim](https://github.com/ethanjwright/vs-tasks.nvim)
  * [euclidianace/betterlua.vim](https://github.com/euclidianace/betterlua.vim)
  * [euclio/vim-markdown-composer](https://github.com/euclio/vim-markdown-composer)
  * [eugen0329/vim-esearch](https://github.com/eugen0329/vim-esearch)
  * [everduin94/nvim-quick-switcher](https://github.com/everduin94/nvim-quick-switcher)
  * [f-person/git-blame.nvim](https://github.com/f-person/git-blame.nvim)
  * [faerryn/user.nvim](https://github.com/faerryn/user.nvim)
  * [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace)
  * [fedepujol/move.nvim](https://github.com/fedepujol/move.nvim)
  * [felipec/notmuch-vim](https://github.com/felipec/notmuch-vim)
  * [ferrine/md-img-paste.vim](https://github.com/ferrine/md-img-paste.vim)
  * [fhill2/floating.nvim](https://github.com/fhill2/floating.nvim)
  * [fholgado/minibufexpl.vim](https://github.com/fholgado/minibufexpl.vim)
  * [fiatjaf/neuron.vim](https://github.com/fiatjaf/neuron.vim)
  * [floobits/floobits-neovim](https://github.com/floobits/floobits-neovim)
  * [flowtype/vim-flow](https://github.com/flowtype/vim-flow)
  * [fmoralesc/nlanguagetool.nvim](https://github.com/fmoralesc/nlanguagetool.nvim)
  * [fmoralesc/vim-pad](https://github.com/fmoralesc/vim-pad)
  * [fmoralesc/worldslice](https://github.com/fmoralesc/worldslice)
  * [folke/lua-dev.nvim](https://github.com/folke/lua-dev.nvim)
  * [folke/todo-comments.nvim](https://github.com/folke/todo-comments.nvim)
  * [foosoft/vim-argwrap](https://github.com/foosoft/vim-argwrap)
  * [frabjous/knap](https://github.com/frabjous/knap)
  * [francoiscabrol/ranger.vim](https://github.com/francoiscabrol/ranger.vim)
  * [frazrepo/vim-rainbow](https://github.com/frazrepo/vim-rainbow)
  * [fredkschott/covim](https://github.com/fredkschott/covim)
  * [fszymanski/fzf-gitignore](https://github.com/fszymanski/fzf-gitignore)
  * [furkanzmc/firvish.nvim](https://github.com/furkanzmc/firvish.nvim)
  * [furkanzmc/options.nvim](https://github.com/furkanzmc/options.nvim)
  * [furkanzmc/sekme.nvim](https://github.com/furkanzmc/sekme.nvim)
  * [furkanzmc/zettelkasten.nvim](https://github.com/furkanzmc/zettelkasten.nvim)
  * [gaborvecsei/cryptoprice.nvim](https://github.com/gaborvecsei/cryptoprice.nvim)
  * [gaborvecsei/memento.nvim](https://github.com/gaborvecsei/memento.nvim)
  * [gabrielelana/vim-markdown](https://github.com/gabrielelana/vim-markdown)
  * [gabrielpoca/replacer.nvim](https://github.com/gabrielpoca/replacer.nvim)
  * [galicarnax/vim-regex-syntax](https://github.com/galicarnax/vim-regex-syntax)
  * [gbprod/cutlass.nvim](https://github.com/gbprod/cutlass.nvim)
  * [gbprod/phpactor.nvim](https://github.com/gbprod/phpactor.nvim)
  * [gelguy/wilder.nvim](https://github.com/gelguy/wilder.nvim)
  * [gennaro-tedesco/boilit](https://github.com/gennaro-tedesco/boilit)
  * [gennaro-tedesco/nvim-commaround](https://github.com/gennaro-tedesco/nvim-commaround)
  * [gennaro-tedesco/nvim-jqx](https://github.com/gennaro-tedesco/nvim-jqx)
  * [gfanto/fzf-lsp.nvim](https://github.com/gfanto/fzf-lsp.nvim)
  * [github.com/wbthomason](https://github.com/github.com/wbthomason)
  * [github/copilot.vim](https://github.com/github/copilot.vim)
  * [glench/vim-jinja2-syntax](https://github.com/glench/vim-jinja2-syntax)
  * [glepnir/galaxyline.nvim](https://github.com/glepnir/galaxyline.nvim)
  * [glepnir/indent-guides.nvim](https://github.com/glepnir/indent-guides.nvim)
  * [glepnir/lspsaga.nvim](https://github.com/glepnir/lspsaga.nvim)
  * [glepnir/prodoc.nvim](https://github.com/glepnir/prodoc.nvim)
  * [glepnir/spaceline.vim](https://github.com/glepnir/spaceline.vim)
  * [gmarik/vundle.vim](https://github.com/gmarik/vundle.vim)
  * [goerz/jupytext.vim](https://github.com/goerz/jupytext.vim)
  * [gpanders/editorconfig.nvim](https://github.com/gpanders/editorconfig.nvim)
  * [groctel/jobsplit.nvim](https://github.com/groctel/jobsplit.nvim)
  * [groenewege/vim-less](https://github.com/groenewege/vim-less)
  * [gruvbox-community/gruvbox](https://github.com/gruvbox-community/gruvbox)
  * [gu-fan/riv.vim](https://github.com/gu-fan/riv.vim)
  * [gukz/ftft.nvim](https://github.com/gukz/ftft.nvim)
  * [guns/vim-clojure-highlight](https://github.com/guns/vim-clojure-highlight)
  * [guns/vim-clojure-static](https://github.com/guns/vim-clojure-static)
  * [guns/vim-sexp](https://github.com/guns/vim-sexp)
  * [guns/vim-slamhound](https://github.com/guns/vim-slamhound)
  * [gustavokatel/sidebar.nvim](https://github.com/gustavokatel/sidebar.nvim)
  * [gwatcha/reaper-keys](https://github.com/gwatcha/reaper-keys)
  * [h2ero/vim-markdown-wiki](https://github.com/h2ero/vim-markdown-wiki)
  * [haifengkao/insertleftbracket.nvim](https://github.com/haifengkao/insertleftbracket.nvim)
  * [hanschen/vim-ipython-cell](https://github.com/hanschen/vim-ipython-cell)
  * [haorenw1025/completion-nvim](https://github.com/haorenw1025/completion-nvim)
  * [hardenedapple/vsh](https://github.com/hardenedapple/vsh)
  * [harrisoncramer/jump-tag](https://github.com/harrisoncramer/jump-tag)
  * [hauleth/usnip.vim](https://github.com/hauleth/usnip.vim)
  * [haya14busa/is.vim](https://github.com/haya14busa/is.vim)
  * [haya14busa/vim-asterisk](https://github.com/haya14busa/vim-asterisk)
  * [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming)
  * [haya14busa/vim-easyoperator-line](https://github.com/haya14busa/vim-easyoperator-line)
  * [haya14busa/vim-easyoperator-phrase](https://github.com/haya14busa/vim-easyoperator-phrase)
  * [henriquehbr/ataraxis.lua](https://github.com/henriquehbr/ataraxis.lua)
  * [henriquehbr/nvim-startup.lua](https://github.com/henriquehbr/nvim-startup.lua)
  * [herringtondarkholme/yats.vim](https://github.com/herringtondarkholme/yats.vim)
  * [hkupty/runes.nvim](https://github.com/hkupty/runes.nvim)
  * [honza/dockerfile.vim](https://github.com/honza/dockerfile.vim)
  * [hoob3rt/lualine.nvim](https://github.com/hoob3rt/lualine.nvim)
  * [hood/popui.nvim](https://github.com/hood/popui.nvim)
  * [hoschi/yode-nvim](https://github.com/hoschi/yode-nvim)
  * [hrsh7th/cmp-nvim-lsp-document-symbol](https://github.com/hrsh7th/cmp-nvim-lsp-document-symbol)
  * [hrsh7th/nvim-compe](https://github.com/hrsh7th/nvim-compe)
  * [hrsh7th/vim-eft](https://github.com/hrsh7th/vim-eft)
  * [hrsh7th/vim-lamp](https://github.com/hrsh7th/vim-lamp)
  * [hrsh7th/vim-searchx](https://github.com/hrsh7th/vim-searchx)
  * [https://gitlab.com/yorickpeterse/nvim-wind](/https://gitlab.com/yorickpeterse/nvim-wind)
  * [huawenyu/vimgdb](https://github.com/huawenyu/vimgdb)
  * [hupfdule/refactorvim](https://github.com/hupfdule/refactorvim)
  * [hyiltiz/vim-plugins-profile](https://github.com/hyiltiz/vim-plugins-profile)
  * [iamcco/coc-spell-checker](https://github.com/iamcco/coc-spell-checker)
  * [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim)
  * [iberianpig/tig-explorer.vim](https://github.com/iberianpig/tig-explorer.vim)
  * [ibhagwan/fzf-lua](https://github.com/ibhagwan/fzf-lua)
  * [idanarye/vim-merginal](https://github.com/idanarye/vim-merginal)
  * [inkarkat/vim-advancedsorters](https://github.com/inkarkat/vim-advancedsorters)
  * [inkarkat/vim-mark](https://github.com/inkarkat/vim-mark)
  * [inkarkat/vim-patterncomplete](https://github.com/inkarkat/vim-patterncomplete)
  * [inkarkat/vim-spellcheck](https://github.com/inkarkat/vim-spellcheck)
  * [instant-markdown/vim-instant-markdown](https://github.com/instant-markdown/vim-instant-markdown)
  * [int3/vim-extradite](https://github.com/int3/vim-extradite)
  * [ipod825/igit.nvim](https://github.com/ipod825/igit.nvim)
  * [ipod825/vim-netranger](https://github.com/ipod825/vim-netranger)
  * [iqxd/vim-mine-sweeping](https://github.com/iqxd/vim-mine-sweeping)
  * [iron-e/nvim-highlite](https://github.com/iron-e/nvim-highlite)
  * [iron-e/nvim-libmodal](https://github.com/iron-e/nvim-libmodal)
  * [ironhouzi/starlite-nvim](https://github.com/ironhouzi/starlite-nvim)
  * [ironhouzi/vim-stim](https://github.com/ironhouzi/vim-stim)
  * [is0n/fm-nvim](https://github.com/is0n/fm-nvim)
  * [is0n/jaq-nvim](https://github.com/is0n/jaq-nvim)
  * [itchyny/calendar.vim](https://github.com/itchyny/calendar.vim)
  * [itmecho/bufterm.nvim](https://github.com/itmecho/bufterm.nvim)
  * [itmecho/neoterm.nvim](https://github.com/itmecho/neoterm.nvim)
  * [ivyl/vim-bling](https://github.com/ivyl/vim-bling)
  * [ixru/nvim-markdown](https://github.com/ixru/nvim-markdown)
  * [j-hui/fidget.nvim](https://github.com/j-hui/fidget.nvim)
  * [jaawerth/fennel-nvim](https://github.com/jaawerth/fennel-nvim)
  * [jackguo380/vim-lsp-cxx-highlight](https://github.com/jackguo380/vim-lsp-cxx-highlight)
  * [jakemason/ouroboros](https://github.com/jakemason/ouroboros)
  * [jakergrossman/tagurl.vim](https://github.com/jakergrossman/tagurl.vim)
  * [jakewvincent/mkdnflow.nvim](https://github.com/jakewvincent/mkdnflow.nvim)
  * [jakewvincent/texmagic.nvim](https://github.com/jakewvincent/texmagic.nvim)
  * [jalvesaq/vimcmdline](https://github.com/jalvesaq/vimcmdline)
  * [jameshiew/nvim-magic](https://github.com/jameshiew/nvim-magic)
  * [jamessan/vim-gnupg](https://github.com/jamessan/vim-gnupg)
  * [janko-m/vim-test](https://github.com/janko-m/vim-test)
  * [jaxbot/github-issues.vim](https://github.com/jaxbot/github-issues.vim)
  * [jbyuki/carrot.nvim](https://github.com/jbyuki/carrot.nvim)
  * [jbyuki/instant.nvim](https://github.com/jbyuki/instant.nvim)
  * [jbyuki/nabla.nvim](https://github.com/jbyuki/nabla.nvim)
  * [jceb/vim-orgmode](https://github.com/jceb/vim-orgmode)
  * [jeaye/color_coded](https://github.com/jeaye/color_coded)
  * [jedi2610/nvim-rooter.lua](https://github.com/jedi2610/nvim-rooter.lua)
  * [jedrzejboczar/possession.nvim](https://github.com/jedrzejboczar/possession.nvim)
  * [jedrzejboczar/toggletasks.nvim](https://github.com/jedrzejboczar/toggletasks.nvim)
  * [jeetsukumaran/vim-indentwise](https://github.com/jeetsukumaran/vim-indentwise)
  * [jeetsukumaran/vim-pythonsense](https://github.com/jeetsukumaran/vim-pythonsense)
  * [jelera/vim-javascript-syntax](https://github.com/jelera/vim-javascript-syntax)
  * [jenterkin/vim-autosource](https://github.com/jenterkin/vim-autosource)
  * [jghauser/auto-pandoc.nvim](https://github.com/jghauser/auto-pandoc.nvim)
  * [jghauser/follow-md-links.nvim](https://github.com/jghauser/follow-md-links.nvim)
  * [jiangmiao/auto-pairs](https://github.com/jiangmiao/auto-pairs)
  * [jimmyhuang454/easycompleteyou](https://github.com/jimmyhuang454/easycompleteyou)
  * [jlanzarotta/bufexplorer](https://github.com/jlanzarotta/bufexplorer)
  * [jlesquembre/nterm.nvim](https://github.com/jlesquembre/nterm.nvim)
  * [jmcomets/vim-pony](https://github.com/jmcomets/vim-pony)
  * [jodosha/vim-godebug](https://github.com/jodosha/vim-godebug)
  * [johmsalas/text-case.nvim](https://github.com/johmsalas/text-case.nvim)
  * [jorengarenar/minisnip](https://github.com/jorengarenar/minisnip)
  * [jorengarenar/minplug](https://github.com/jorengarenar/minplug)
  * [jorengarenar/vim-mvvis](https://github.com/jorengarenar/vim-mvvis)
  * [jorengarenar/vim-sbnr](https://github.com/jorengarenar/vim-sbnr)
  * [jorengarenar/vim-sql-upper](https://github.com/jorengarenar/vim-sql-upper)
  * [jose-elias-alvarez/buftabline.nvim](https://github.com/jose-elias-alvarez/buftabline.nvim)
  * [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim)
  * [jose-elias-alvarez/nvim-lsp-ts-utils](https://github.com/jose-elias-alvarez/nvim-lsp-ts-utils)
  * [joshmcguigan/estream](https://github.com/joshmcguigan/estream)
  * [jpalardy/vim-slime](https://github.com/jpalardy/vim-slime)
  * [jrasmusbm/vim-peculiar](https://github.com/jrasmusbm/vim-peculiar)
  * [jreybert/vimagit](https://github.com/jreybert/vimagit)
  * [jsborjesson/vim-uppercase-sql](https://github.com/jsborjesson/vim-uppercase-sql)
  * [jsfaint/gen_tags.vim](https://github.com/jsfaint/gen_tags.vim)
  * [jubnzv/virtual-types.nvim](https://github.com/jubnzv/virtual-types.nvim)
  * [julian/vim-textobj-variable-segment](https://github.com/julian/vim-textobj-variable-segment)
  * [julienr/vim-cellmode](https://github.com/julienr/vim-cellmode)
  * [junegunn/fzf](https://github.com/junegunn/fzf)
  * [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)
  * [junegunn/goyo.vim](https://github.com/junegunn/goyo.vim)
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
  * [junegunn/vim-peekaboo](https://github.com/junegunn/vim-peekaboo)
  * [junegunn/vim-plug](https://github.com/junegunn/vim-plug)
  * [junegunn/vim-pseudocl](https://github.com/junegunn/vim-pseudocl)
  * [junegunn/vim-slash](https://github.com/junegunn/vim-slash)
  * [junegunn/vim-xmark](https://github.com/junegunn/vim-xmark)
  * [junkblocker/git-time-lapse](https://github.com/junkblocker/git-time-lapse)
  * [junnplus/nvim-lsp-setup](https://github.com/junnplus/nvim-lsp-setup)
  * [jupyter-vim/jupyter-vim](https://github.com/jupyter-vim/jupyter-vim)
  * [justinmk/vim-dirvish](https://github.com/justinmk/vim-dirvish)
  * [justinmk/vim-gtfo](https://github.com/justinmk/vim-gtfo)
  * [justinmk/vim-ipmotion](https://github.com/justinmk/vim-ipmotion)
  * [k-takata/minpac](https://github.com/k-takata/minpac)
  * [kaile256/vim-foldpeek](https://github.com/kaile256/vim-foldpeek)
  * [kaiuri/nvim-juliana](https://github.com/kaiuri/nvim-juliana)
  * [kalekundert/vim-coiled-snake](https://github.com/kalekundert/vim-coiled-snake)
  * [kamykn/spelunker.vim](https://github.com/kamykn/spelunker.vim)
  * [kana/vim-smartinput](https://github.com/kana/vim-smartinput)
  * [kana/vim-textobj-indent](https://github.com/kana/vim-textobj-indent)
  * [kchmck/vim-coffee-script](https://github.com/kchmck/vim-coffee-script)
  * [kdav5758/truezen.nvim](https://github.com/kdav5758/truezen.nvim)
  * [kdheepak/lazygit.nvim](https://github.com/kdheepak/lazygit.nvim)
  * [kdheepak/panvimdoc](https://github.com/kdheepak/panvimdoc)
  * [kethku/neovide](https://github.com/kethku/neovide)
  * [kevinhwang91/nvim-bqf](https://github.com/kevinhwang91/nvim-bqf)
  * [kevinhwang91/nvim-ufo](https://github.com/kevinhwang91/nvim-ufo)
  * [kevinhwang91/rnvimr](https://github.com/kevinhwang91/rnvimr)
  * [kezhenxu94/vim-mysql-plugin](https://github.com/kezhenxu94/vim-mysql-plugin)
  * [kien/ctrlp.vim](https://github.com/kien/ctrlp.vim)
  * [killthemule/nvimpam](https://github.com/killthemule/nvimpam)
  * [kkharji/sqlite.lua](https://github.com/kkharji/sqlite.lua)
  * [kkoomen/vim-doge](https://github.com/kkoomen/vim-doge)
  * [klen/nvim-config-local](https://github.com/klen/nvim-config-local)
  * [klen/python-mode](https://github.com/klen/python-mode)
  * [koenverburg/peepsight.nvim](https://github.com/koenverburg/peepsight.nvim)
  * [konfekt/foldtext](https://github.com/konfekt/foldtext)
  * [kosayoda/nvim-lightbulb](https://github.com/kosayoda/nvim-lightbulb)
  * [kovetskiy/neovim-move](https://github.com/kovetskiy/neovim-move)
  * [kovisoft/paredit](https://github.com/kovisoft/paredit)
  * [kristijanhusak/orgmode.nvim](https://github.com/kristijanhusak/orgmode.nvim)
  * [kristijanhusak/vim-packager](https://github.com/kristijanhusak/vim-packager)
  * [kwkarlwang/bufjump.nvim](https://github.com/kwkarlwang/bufjump.nvim)
  * [kwkarlwang/bufresize.nvim](https://github.com/kwkarlwang/bufresize.nvim)
  * [kyazdani42/nvim-web-devicons](https://github.com/kyazdani42/nvim-web-devicons)
  * [kylechui/nvim-surround](https://github.com/kylechui/nvim-surround)
  * [lambdalisue/battery.vim](https://github.com/lambdalisue/battery.vim)
  * [lambdalisue/fern.vim](https://github.com/lambdalisue/fern.vim)
  * [lambdalisue/gina.vim](https://github.com/lambdalisue/gina.vim)
  * [lambdalisue/readablefold.vim](https://github.com/lambdalisue/readablefold.vim)
  * [lambdalisue/suda.vim](https://github.com/lambdalisue/suda.vim)
  * [ldelossa/calltree.nvim](https://github.com/ldelossa/calltree.nvim)
  * [ldelossa/gh.nvim](https://github.com/ldelossa/gh.nvim)
  * [ldelossa/litee.nvim](https://github.com/ldelossa/litee.nvim)
  * [ledesmablt/vim-run](https://github.com/ledesmablt/vim-run)
  * [ledger/vim-ledger](https://github.com/ledger/vim-ledger)
  * [lenovsky/nuake](https://github.com/lenovsky/nuake)
  * [lervag/vimtex](https://github.com/lervag/vimtex)
  * [lervag/wiki.vim](https://github.com/lervag/wiki.vim)
  * [lewis6991/nvim-treesitter-context](https://github.com/lewis6991/nvim-treesitter-context)
  * [lewis6991/satellite.nvim](https://github.com/lewis6991/satellite.nvim)
  * [lfilho/cosco.vim](https://github.com/lfilho/cosco.vim)
  * [lfv89/vim-interestingwords](https://github.com/lfv89/vim-interestingwords)
  * [lhkipp/nvim-locationist](https://github.com/lhkipp/nvim-locationist)
  * [lifepillar/pgsql.vim](https://github.com/lifepillar/pgsql.vim)
  * [lifepillar/vim-colortemplate](https://github.com/lifepillar/vim-colortemplate)
  * [lifepillar/vim-mucomplete](https://github.com/lifepillar/vim-mucomplete)
  * [linarcx/telescope-scriptnames.nvim](https://github.com/linarcx/telescope-scriptnames.nvim)
  * [linden-project/linny.vim](https://github.com/linden-project/linny.vim)
  * [linty-org/key-menu.nvim](https://github.com/linty-org/key-menu.nvim)
  * [liuchengxu/eleline.vim](https://github.com/liuchengxu/eleline.vim)
  * [liuchengxu/vim-clap](https://github.com/liuchengxu/vim-clap)
  * [liuchengxu/vista.vim](https://github.com/liuchengxu/vista.vim)
  * [loricandre/oneterm](https://github.com/loricandre/oneterm)
  * [loricandre/oneterm.nvim](https://github.com/loricandre/oneterm.nvim)
  * [lotabout/skim.vim](https://github.com/lotabout/skim.vim)
  * [lpinilla/vim-codepainter](https://github.com/lpinilla/vim-codepainter)
  * [luc-tielen/telescope_hoogle](https://github.com/luc-tielen/telescope_hoogle)
  * [luchermitte/lh-brackets](https://github.com/luchermitte/lh-brackets)
  * [luchermitte/lh-cpp](https://github.com/luchermitte/lh-cpp)
  * [ludopinelli/comment-box.nvim](https://github.com/ludopinelli/comment-box.nvim)
  * [ludovicchabant/vim-gutentags](https://github.com/ludovicchabant/vim-gutentags)
  * [luk400/vim-jukit](https://github.com/luk400/vim-jukit)
  * [lukas-reineke/cmp-under-comparator](https://github.com/lukas-reineke/cmp-under-comparator)
  * [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim)
  * [lukas-reineke/lsp-format.nvim](https://github.com/lukas-reineke/lsp-format.nvim)
  * [lukelbd/vim-tabline](https://github.com/lukelbd/vim-tabline)
  * [lunarvim/colorschemes](https://github.com/lunarvim/colorschemes)
  * [lunarvim/darkplus.nvim](https://github.com/lunarvim/darkplus.nvim)
  * [lunarvim/lualine.nvim](https://github.com/lunarvim/lualine.nvim)
  * [lunixbochs/actualvim](https://github.com/lunixbochs/actualvim)
  * [luochen1990/rainbow](https://github.com/luochen1990/rainbow)
  * [luukvbaal/nnn.nvim](https://github.com/luukvbaal/nnn.nvim)
  * [lyude/neovim-gtk](https://github.com/lyude/neovim-gtk)
  * [lyuts/vim-rtags](https://github.com/lyuts/vim-rtags)
  * [m-demare/hlargs.nvim](https://github.com/m-demare/hlargs.nvim)
  * [m00qek/baleia.nvim](https://github.com/m00qek/baleia.nvim)
  * [m00qek/plugin-template.nvim](https://github.com/m00qek/plugin-template.nvim)
  * [machakann/vim-highlightedyank](https://github.com/machakann/vim-highlightedyank)
  * [machakann/vim-sandwich](https://github.com/machakann/vim-sandwich)
  * [macthecadillac/vimdo](https://github.com/macthecadillac/vimdo)
  * [macurovc/insert-docstring](https://github.com/macurovc/insert-docstring)
  * [marcweber/vim-addon-manager](https://github.com/marcweber/vim-addon-manager)
  * [marcweber/vim-addon-mw-utils](https://github.com/marcweber/vim-addon-mw-utils)
  * [marklcrns/vim-smartq](https://github.com/marklcrns/vim-smartq)
  * [markonm/traces.vim](https://github.com/markonm/traces.vim)
  * [mattboehm/vim-accordion](https://github.com/mattboehm/vim-accordion)
  * [mattn/emmet-vim](https://github.com/mattn/emmet-vim)
  * [mattn/gist-vim](https://github.com/mattn/gist-vim)
  * [mattn/vim-gist](https://github.com/mattn/vim-gist)
  * [mattn/vim-molder](https://github.com/mattn/vim-molder)
  * [matze/vim-move](https://github.com/matze/vim-move)
  * [max397574/lua-dev.nvim](https://github.com/max397574/lua-dev.nvim)
  * [max397574/which-key.nvim](https://github.com/max397574/which-key.nvim)
  * [maxmellon/vim-jsx-pretty](https://github.com/maxmellon/vim-jsx-pretty)
  * [mbbill/undotree](https://github.com/mbbill/undotree)
  * [mcauley-penney/tidy.nvim](https://github.com/mcauley-penney/tidy.nvim)
  * [mcchrish/nnn.vim](https://github.com/mcchrish/nnn.vim)
  * [meznaric/conmenu](https://github.com/meznaric/conmenu)
  * [mfussenegger/nvim-dap](https://github.com/mfussenegger/nvim-dap)
  * [mfussenegger/nvim-lint](https://github.com/mfussenegger/nvim-lint)
  * [mfussenegger/nvim-lsp-compl](https://github.com/mfussenegger/nvim-lsp-compl)
  * [mfussenegger/nvim-ts-hint-textobject](https://github.com/mfussenegger/nvim-ts-hint-textobject)
  * [mg979/tasks.vim](https://github.com/mg979/tasks.vim)
  * [mhartington/formatter.nvim](https://github.com/mhartington/formatter.nvim)
  * [mhartington/nvim-typescript](https://github.com/mhartington/nvim-typescript)
  * [mhinz/vim-crates](https://github.com/mhinz/vim-crates)
  * [mhinz/vim-grepper](https://github.com/mhinz/vim-grepper)
  * [mhinz/vim-lookup](https://github.com/mhinz/vim-lookup)
  * [mhinz/vim-mix-format](https://github.com/mhinz/vim-mix-format)
  * [mhinz/vim-rfc](https://github.com/mhinz/vim-rfc)
  * [mhinz/vim-signify](https://github.com/mhinz/vim-signify)
  * [mhinz/vim-startify](https://github.com/mhinz/vim-startify)
  * [michaelb/sniprun](https://github.com/michaelb/sniprun)
  * [mickael-menu/zk-nvim](https://github.com/mickael-menu/zk-nvim)
  * [micmine/jumpwire.nvim](https://github.com/micmine/jumpwire.nvim)
  * [microsoft.github.io/language-server-protocol](https://github.com/microsoft.github.io/language-server-protocol)
  * [mileszs/ack.vim](https://github.com/mileszs/ack.vim)
  * [milisims/nvim-luaref](https://github.com/milisims/nvim-luaref)
  * [milisims/tree-sitter-org](https://github.com/milisims/tree-sitter-org)
  * [millermedeiros/vim-esformatter](https://github.com/millermedeiros/vim-esformatter)
  * [miversen33/import.nvim](https://github.com/miversen33/import.nvim)
  * [miversen33/netman.nvim](https://github.com/miversen33/netman.nvim)
  * [mizlan/termbufm](https://github.com/mizlan/termbufm)
  * [mjbrownie/vim-htmldjango_omnicomplete](https://github.com/mjbrownie/vim-htmldjango_omnicomplete)
  * [mjlbach/try.nvim](https://github.com/mjlbach/try.nvim)
  * [mjswensen/themer](https://github.com/mjswensen/themer)
  * [moll/vim-bbye](https://github.com/moll/vim-bbye)
  * [moll/vim-node](https://github.com/moll/vim-node)
  * [mordechaihadad/bob](https://github.com/mordechaihadad/bob)
  * [mrjones2014/dash.nvim](https://github.com/mrjones2014/dash.nvim)
  * [mrjones2014/smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim)
  * [mtth/scratch.vim](https://github.com/mtth/scratch.vim)
  * [mxw/vim-jsx](https://github.com/mxw/vim-jsx)
  * [my/supercoolplugin](https://github.com/my/supercoolplugin)
  * [mzlogin/vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc)
  * [nanotee/luv-vimdocs](https://github.com/nanotee/luv-vimdocs)
  * [nanotee/nvim-lsp-basics](https://github.com/nanotee/nvim-lsp-basics)
  * [nanotee/nvim-lua-guide](https://github.com/nanotee/nvim-lua-guide)
  * [nanotee/sqls.nvim](https://github.com/nanotee/sqls.nvim)
  * [nanotee/zoxide.vim](https://github.com/nanotee/zoxide.vim)
  * [narajaon/onestatus](https://github.com/narajaon/onestatus)
  * [narutoxy/dim.lua](https://github.com/narutoxy/dim.lua)
  * [natdm/bswap](https://github.com/natdm/bswap)
  * [natebosch/vim-lsc](https://github.com/natebosch/vim-lsc)
  * [natecraddock/sessions.nvim](https://github.com/natecraddock/sessions.nvim)
  * [natecraddock/telescope-zf-native.nvim](https://github.com/natecraddock/telescope-zf-native.nvim)
  * [natecraddock/workspaces.nvim](https://github.com/natecraddock/workspaces.nvim)
  * [nathanaelkane/vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides)
  * [nathom/tmux.nvim](https://github.com/nathom/tmux.nvim)
  * [ncm2/float-preview.nvim](https://github.com/ncm2/float-preview.nvim)
  * [ncm2/ncm2](https://github.com/ncm2/ncm2)
  * [neoclide/coc-git](https://github.com/neoclide/coc-git)
  * [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim)
  * [neomake/neomake](https://github.com/neomake/neomake)
  * [neovim.io/logos](https://github.com/neovim.io/logos)
  * [neovimhaskell/haskell-vim](https://github.com/neovimhaskell/haskell-vim)
  * [nfischer/vim-rainbows](https://github.com/nfischer/vim-rainbows)
  * [nfrid/due.nvim](https://github.com/nfrid/due.nvim)
  * [nikvdp/neomux](https://github.com/nikvdp/neomux)
  * [nmac427/guess-indent.nvim](https://github.com/nmac427/guess-indent.nvim)
  * [noahfrederick/vim-composer](https://github.com/noahfrederick/vim-composer)
  * [noib3/nvim-oxi](https://github.com/noib3/nvim-oxi)
  * [norcalli/nvim-base16.lua](https://github.com/norcalli/nvim-base16.lua)
  * [norcalli/nvim-terminal.lua](https://github.com/norcalli/nvim-terminal.lua)
  * [norcalli/nvim_utils](https://github.com/norcalli/nvim_utils)
  * [norcalli/snippets.nvim](https://github.com/norcalli/snippets.nvim)
  * [noscript/taberian.vim](https://github.com/noscript/taberian.vim)
  * [notomo/gesture.nvim](https://github.com/notomo/gesture.nvim)
  * [ntbbloodbath/cheovim](https://github.com/ntbbloodbath/cheovim)
  * [ntbbloodbath/color-converter.nvim](https://github.com/ntbbloodbath/color-converter.nvim)
  * [ntbbloodbath/nvenv](https://github.com/ntbbloodbath/nvenv)
  * [ntbbloodbath/rest.nvim](https://github.com/ntbbloodbath/rest.nvim)
  * [numirias/semshi](https://github.com/numirias/semshi)
  * [numtostr/bufonly.nvim](https://github.com/numtostr/bufonly.nvim)
  * [numtostr/comment.nvim](https://github.com/numtostr/comment.nvim)
  * [numtostr/fterm.nvim](https://github.com/numtostr/fterm.nvim)
  * [numtostr/navigator.nvim](https://github.com/numtostr/navigator.nvim)
  * [nvie/vim-flake8](https://github.com/nvie/vim-flake8)
  * [nvim-lua/completion-nvim](https://github.com/nvim-lua/completion-nvim)
  * [nvim-lua/lsp-status.nvim](https://github.com/nvim-lua/lsp-status.nvim)
  * [nvim-lua/lsp_extensions.nvim](https://github.com/nvim-lua/lsp_extensions.nvim)
  * [nvim-lua/popup.nvim](https://github.com/nvim-lua/popup.nvim)
  * [nvim-neo-tree/neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim)
  * [nvim-neotest/neotest](https://github.com/nvim-neotest/neotest)
  * [nvim-telescope/telescope-arecibo.nvim](https://github.com/nvim-telescope/telescope-arecibo.nvim)
  * [nvim-telescope/telescope-bibtex.nvim](https://github.com/nvim-telescope/telescope-bibtex.nvim)
  * [nvim-telescope/telescope-cheat.nvim](https://github.com/nvim-telescope/telescope-cheat.nvim)
  * [nvim-telescope/telescope-dap.nvim](https://github.com/nvim-telescope/telescope-dap.nvim)
  * [nvim-telescope/telescope-file-browser.nvim](https://github.com/nvim-telescope/telescope-file-browser.nvim)
  * [nvim-telescope/telescope-fzf-native.nvim](https://github.com/nvim-telescope/telescope-fzf-native.nvim)
  * [nvim-telescope/telescope-fzf-writer.nvim](https://github.com/nvim-telescope/telescope-fzf-writer.nvim)
  * [nvim-telescope/telescope-fzy-native.nvim](https://github.com/nvim-telescope/telescope-fzy-native.nvim)
  * [nvim-telescope/telescope-github.nvim](https://github.com/nvim-telescope/telescope-github.nvim)
  * [nvim-telescope/telescope-hop.nvim](https://github.com/nvim-telescope/telescope-hop.nvim)
  * [nvim-telescope/telescope-live-grep-args.nvim](https://github.com/nvim-telescope/telescope-live-grep-args.nvim)
  * [nvim-telescope/telescope-media-files.nvim](https://github.com/nvim-telescope/telescope-media-files.nvim)
  * [nvim-telescope/telescope-node-modules.nvim](https://github.com/nvim-telescope/telescope-node-modules.nvim)
  * [nvim-telescope/telescope-packer.nvim](https://github.com/nvim-telescope/telescope-packer.nvim)
  * [nvim-telescope/telescope-project.nvim](https://github.com/nvim-telescope/telescope-project.nvim)
  * [nvim-telescope/telescope-rs.nvim](https://github.com/nvim-telescope/telescope-rs.nvim)
  * [nvim-telescope/telescope-smart-history.nvim](https://github.com/nvim-telescope/telescope-smart-history.nvim)
  * [nvim-telescope/telescope-snippets.nvim](https://github.com/nvim-telescope/telescope-snippets.nvim)
  * [nvim-telescope/telescope-ui-select.nvim](https://github.com/nvim-telescope/telescope-ui-select.nvim)
  * [nvim-telescope/telescope-vimspector.nvim](https://github.com/nvim-telescope/telescope-vimspector.nvim)
  * [nvim-telescope/telescope-z.nvim](https://github.com/nvim-telescope/telescope-z.nvim)
  * [nvim-treesitter/module-template](https://github.com/nvim-treesitter/module-template)
  * [nvim-treesitter/nvim-tree-docs](https://github.com/nvim-treesitter/nvim-tree-docs)
  * [nvim-treesitter/nvim-treesitter-context](https://github.com/nvim-treesitter/nvim-treesitter-context)
  * [nvim-treesitter/nvim-treesitter-refactor](https://github.com/nvim-treesitter/nvim-treesitter-refactor)
  * [nvim-treesitter/nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects)
  * [nyngwang/neoroot.lua](https://github.com/nyngwang/neoroot.lua)
  * [nyngwang/neozoom.lua](https://github.com/nyngwang/neozoom.lua)
  * [oberblastmeister/neuron.nvim](https://github.com/oberblastmeister/neuron.nvim)
  * [oberblastmeister/termwrapper.nvim](https://github.com/oberblastmeister/termwrapper.nvim)
  * [octol/vim-cpp-enhanced-highlight](https://github.com/octol/vim-cpp-enhanced-highlight)
  * [odie/gitabra](https://github.com/odie/gitabra)
  * [ojroques/nvim-bufbar](https://github.com/ojroques/nvim-bufbar)
  * [ojroques/nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy)
  * [ojroques/vim-oscyank](https://github.com/ojroques/vim-oscyank)
  * [ojroques/vim-scrollstatus](https://github.com/ojroques/vim-scrollstatus)
  * [olacin/telescope-cc.nvim](https://github.com/olacin/telescope-cc.nvim)
  * [olacin/telescope-gitmoji.nvim](https://github.com/olacin/telescope-gitmoji.nvim)
  * [olexsmir/gopher.nvim](https://github.com/olexsmir/gopher.nvim)
  * [olical/aniseed](https://github.com/olical/aniseed)
  * [olical/conjure](https://github.com/olical/conjure)
  * [olical/vim-enmasse](https://github.com/olical/vim-enmasse)
  * [olimorris/persisted.nvim](https://github.com/olimorris/persisted.nvim)
  * [onsails/diaglist.nvim](https://github.com/onsails/diaglist.nvim)
  * [onsails/lspkind-nvim](https://github.com/onsails/lspkind-nvim)
  * [orlp/vim-bunlink](https://github.com/orlp/vim-bunlink)
  * [othree/es.next.syntax.vim](https://github.com/othree/es.next.syntax.vim)
  * [othree/html5.vim](https://github.com/othree/html5.vim)
  * [othree/javascript-libraries-syntax.vim](https://github.com/othree/javascript-libraries-syntax.vim)
  * [othree/yajs.vim](https://github.com/othree/yajs.vim)
  * [p00f/cphelper.nvim](https://github.com/p00f/cphelper.nvim)
  * [pacha/vem-tabline](https://github.com/pacha/vem-tabline)
  * [pangloss/vim-javascript](https://github.com/pangloss/vim-javascript)
  * [pappasam/vim-filetype-formatter](https://github.com/pappasam/vim-filetype-formatter)
  * [paulocesar/neovim-db](https://github.com/paulocesar/neovim-db)
  * [pechorin/any-jump.vim](https://github.com/pechorin/any-jump.vim)
  * [peterrincker/vim-argumentative](https://github.com/peterrincker/vim-argumentative)
  * [petertriho/nvim-scrollbar](https://github.com/petertriho/nvim-scrollbar)
  * [pgdouyon/vim-accio](https://github.com/pgdouyon/vim-accio)
  * [pgdouyon/vim-evanesco](https://github.com/pgdouyon/vim-evanesco)
  * [philrunninger/nerdtree-buffer-ops](https://github.com/philrunninger/nerdtree-buffer-ops)
  * [philrunninger/nerdtree-visual-selection](https://github.com/philrunninger/nerdtree-visual-selection)
  * [pianocomposer321/consolation.nvim](https://github.com/pianocomposer321/consolation.nvim)
  * [pianocomposer321/project-templates.nvim](https://github.com/pianocomposer321/project-templates.nvim)
  * [pianocomposer321/yabs.nvim](https://github.com/pianocomposer321/yabs.nvim)
  * [plasticboy/vim-markdown](https://github.com/plasticboy/vim-markdown)
  * [pocco81/dap-buddy.nvim](https://github.com/pocco81/dap-buddy.nvim)
  * [pocco81/dapinstall.nvim](https://github.com/pocco81/dapinstall.nvim)
  * [pocco81/noclc.nvim](https://github.com/pocco81/noclc.nvim)
  * [pocco81/truezen.nvim](https://github.com/pocco81/truezen.nvim)
  * [post-install/update](https://github.com/post-install/update)
  * [powerman/vim-plugin-ansiesc](https://github.com/powerman/vim-plugin-ansiesc)
  * [prabirshrestha/asyncomplete.vim](https://github.com/prabirshrestha/asyncomplete.vim)
  * [prabirshrestha/quickpick.vim](https://github.com/prabirshrestha/quickpick.vim)
  * [prabirshrestha/vim-lsp](https://github.com/prabirshrestha/vim-lsp)
  * [preservim/nerdcommenter](https://github.com/preservim/nerdcommenter)
  * [preservim/nerdtree](https://github.com/preservim/nerdtree)
  * [preservim/tagbar](https://github.com/preservim/tagbar)
  * [preservim/vim-markdown](https://github.com/preservim/vim-markdown)
  * [preservim/vim-pencil](https://github.com/preservim/vim-pencil)
  * [preservim/vimux](https://github.com/preservim/vimux)
  * [prettier/vim-prettier](https://github.com/prettier/vim-prettier)
  * [pseewald/vim-anyfold](https://github.com/pseewald/vim-anyfold)
  * [psliwka/vim-smoothie](https://github.com/psliwka/vim-smoothie)
  * [ptzz/lf.vim](https://github.com/ptzz/lf.vim)
  * [puremourning/vimspector](https://github.com/puremourning/vimspector)
  * [pwntester/codeql.nvim](https://github.com/pwntester/codeql.nvim)
  * [pwntester/octo.nvim](https://github.com/pwntester/octo.nvim)
  * [qpkorr/vim-bufkill](https://github.com/qpkorr/vim-bufkill)
  * [qpkorr/vim-renamer](https://github.com/qpkorr/vim-renamer)
  * [quintik/snip](https://github.com/quintik/snip)
  * [qvacua/vimr](https://github.com/qvacua/vimr)
  * [qxxxb/vim-searchhi](https://github.com/qxxxb/vim-searchhi)
  * [r1ri/suffer](https://github.com/r1ri/suffer)
  * [racer-rust/vim-racer](https://github.com/racer-rust/vim-racer)
  * [rafaelsq/nvim-goc.lua](https://github.com/rafaelsq/nvim-goc.lua)
  * [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets)
  * [rafcamlet/nvim-luapad](https://github.com/rafcamlet/nvim-luapad)
  * [raghur/vim-ghost](https://github.com/raghur/vim-ghost)
  * [raimondi/delimitmate](https://github.com/raimondi/delimitmate)
  * [raimondi/yaifa](https://github.com/raimondi/yaifa)
  * [ranjithshegde/orgwiki.nvim](https://github.com/ranjithshegde/orgwiki.nvim)
  * [rasukarusan/nvim-select-multi-line](https://github.com/rasukarusan/nvim-select-multi-line)
  * [ray-x/go.nvim](https://github.com/ray-x/go.nvim)
  * [rbgrouleff/bclose.vim](https://github.com/rbgrouleff/bclose.vim)
  * [rbong/vim-buffest](https://github.com/rbong/vim-buffest)
  * [rbong/vim-crystalline](https://github.com/rbong/vim-crystalline)
  * [rbong/vim-flog](https://github.com/rbong/vim-flog)
  * [rbtnn/vim-mario](https://github.com/rbtnn/vim-mario)
  * [rcarriga/nvim-dap-ui](https://github.com/rcarriga/nvim-dap-ui)
  * [rcarriga/vim-ultest](https://github.com/rcarriga/vim-ultest)
  * [reedes/vim-lexical](https://github.com/reedes/vim-lexical)
  * [reedes/vim-textobj-quote](https://github.com/reedes/vim-textobj-quote)
  * [reedes/vim-wordy](https://github.com/reedes/vim-wordy)
  * [renerocksai/telekasten.nvim](https://github.com/renerocksai/telekasten.nvim)
  * [rexagod/samwise.nvim](https://github.com/rexagod/samwise.nvim)
  * [rhysd/committia.vim](https://github.com/rhysd/committia.vim)
  * [rhysd/conflict-marker.vim](https://github.com/rhysd/conflict-marker.vim)
  * [rhysd/git-messenger.vim](https://github.com/rhysd/git-messenger.vim)
  * [rhysd/vim-grammarous](https://github.com/rhysd/vim-grammarous)
  * [rhysd/vim-operator-surround](https://github.com/rhysd/vim-operator-surround)
  * [rickhowe/diffchar.vim](https://github.com/rickhowe/diffchar.vim)
  * [rip-rip/clang_complete](https://github.com/rip-rip/clang_complete)
  * [ripxorip/aerojump.nvim](https://github.com/ripxorip/aerojump.nvim)
  * [ripxorip/bolt.nvim](https://github.com/ripxorip/bolt.nvim)
  * [rishabhrd/nvim-lsputils](https://github.com/rishabhrd/nvim-lsputils)
  * [rktjmp/fwatch.nvim](https://github.com/rktjmp/fwatch.nvim)
  * [rktjmp/hotpot.nvim](https://github.com/rktjmp/hotpot.nvim)
  * [rktjmp/lush.nvim](https://github.com/rktjmp/lush.nvim)
  * [rliang/termedit.nvim](https://github.com/rliang/termedit.nvim)
  * [rmagatti/alternate-toggler](https://github.com/rmagatti/alternate-toggler)
  * [rmagatti/goto-preview](https://github.com/rmagatti/goto-preview)
  * [rmagatti/session-lens](https://github.com/rmagatti/session-lens)
  * [rmichelsen/nvy](https://github.com/rmichelsen/nvy)
  * [rockerboo/awesome-neovim](https://github.com/rockerboo/awesome-neovim)
  * [rohit-px2/nvui](https://github.com/rohit-px2/nvui)
  * [romainl/vim-qlist](https://github.com/romainl/vim-qlist)
  * [romainl/vim-quicklist](https://github.com/romainl/vim-quicklist)
  * [romgrk/nvim-treesitter-context](https://github.com/romgrk/nvim-treesitter-context)
  * [romgrk/searchreplace.vim](https://github.com/romgrk/searchreplace.vim)
  * [ron89/thesaurus_query.vim](https://github.com/ron89/thesaurus_query.vim)
  * [roosta/fzf-folds.vim](https://github.com/roosta/fzf-folds.vim)
  * [roxma/nvim-completion-manager](https://github.com/roxma/nvim-completion-manager)
  * [roxma/vim-tmux-clipboard](https://github.com/roxma/vim-tmux-clipboard)
  * [rraks/pyro](https://github.com/rraks/pyro)
  * [rrethy/nvim-treesitter-endwise](https://github.com/rrethy/nvim-treesitter-endwise)
  * [rstacruz/vim-closer](https://github.com/rstacruz/vim-closer)
  * [ruifm/gitlinker.nvim](https://github.com/ruifm/gitlinker.nvim)
  * [rust-lang/rust.vim](https://github.com/rust-lang/rust.vim)
  * [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons)
  * [ryanss/vim-hackernews](https://github.com/ryanss/vim-hackernews)
  * [ryvnf/readline.vim](https://github.com/ryvnf/readline.vim)
  * [s1n7ax/nvim-comment-frame](https://github.com/s1n7ax/nvim-comment-frame)
  * [s1n7ax/nvim-search-and-replace](https://github.com/s1n7ax/nvim-search-and-replace)
  * [s1n7ax/nvim-terminal](https://github.com/s1n7ax/nvim-terminal)
  * [s1n7ax/nvim-window-picker](https://github.com/s1n7ax/nvim-window-picker)
  * [saecki/crates.nvim](https://github.com/saecki/crates.nvim)
  * [sakhnik/nvim-gdb](https://github.com/sakhnik/nvim-gdb)
  * [samjwill/nvim-unception](https://github.com/samjwill/nvim-unception)
  * [samoshkin/vim-find-files](https://github.com/samoshkin/vim-find-files)
  * [samoshkin/vim-mergetool](https://github.com/samoshkin/vim-mergetool)
  * [sanhajio/synonyms.vim](https://github.com/sanhajio/synonyms.vim)
  * [savq/paq-nvim](https://github.com/savq/paq-nvim)
  * [sbdchd/neoformat](https://github.com/sbdchd/neoformat)
  * [scalameta/nvim-metals](https://github.com/scalameta/nvim-metals)
  * [scjangra/files-nvim](https://github.com/scjangra/files-nvim)
  * [scrooloose/nerdcommenter](https://github.com/scrooloose/nerdcommenter)
  * [scrooloose/nerdtree](https://github.com/scrooloose/nerdtree)
  * [scrooloose/nerdtree-project-plugin](https://github.com/scrooloose/nerdtree-project-plugin)
  * [scrooloose/syntastic](https://github.com/scrooloose/syntastic)
  * [seandewar/killersheep.nvim](https://github.com/seandewar/killersheep.nvim)
  * [seandewar/nvimesweeper](https://github.com/seandewar/nvimesweeper)
  * [severin-lemaignan/vim-minimap](https://github.com/severin-lemaignan/vim-minimap)
  * [sgur/vim-editorconfig](https://github.com/sgur/vim-editorconfig)
  * [shadmansaleh/irc.nvim](https://github.com/shadmansaleh/irc.nvim)
  * [shaeinst/penvim](https://github.com/shaeinst/penvim)
  * [sharkdp/fd](https://github.com/sharkdp/fd)
  * [sheerun/vim-polyglot](https://github.com/sheerun/vim-polyglot)
  * [sheodox/projectlaunch.nvim](https://github.com/sheodox/projectlaunch.nvim)
  * [shinglyu/vim-codespell](https://github.com/shinglyu/vim-codespell)
  * [shivamashtikar/tmuxjump.vim](https://github.com/shivamashtikar/tmuxjump.vim)
  * [shohi/neva](https://github.com/shohi/neva)
  * [shougo/ddc.vim](https://github.com/shougo/ddc.vim)
  * [shougo/defx.nvim](https://github.com/shougo/defx.nvim)
  * [shougo/dein.vim](https://github.com/shougo/dein.vim)
  * [shougo/denite.nvim](https://github.com/shougo/denite.nvim)
  * [shougo/deol.nvim](https://github.com/shougo/deol.nvim)
  * [shougo/deoplete.nvim](https://github.com/shougo/deoplete.nvim)
  * [shougo/neobundle.vim](https://github.com/shougo/neobundle.vim)
  * [shougo/neocomplcache.vim](https://github.com/shougo/neocomplcache.vim)
  * [shougo/neocomplete.vim](https://github.com/shougo/neocomplete.vim)
  * [shougo/neosnippet-snippets](https://github.com/shougo/neosnippet-snippets)
  * [shougo/unite.vim](https://github.com/shougo/unite.vim)
  * [shougo/vimfiler.vim](https://github.com/shougo/vimfiler.vim)
  * [sickill/vim-pasta](https://github.com/sickill/vim-pasta)
  * [sidofc/mkdx](https://github.com/sidofc/mkdx)
  * [sidorares/node-vim-debugger](https://github.com/sidorares/node-vim-debugger)
  * [simonefranza/nvim-conv](https://github.com/simonefranza/nvim-conv)
  * [simrat39/rust-tools.nvim](https://github.com/simrat39/rust-tools.nvim)
  * [sindrets/diffview.nvim](https://github.com/sindrets/diffview.nvim)
  * [sitiom/nvim-numbertoggle](https://github.com/sitiom/nvim-numbertoggle)
  * [sjl/clam.vim](https://github.com/sjl/clam.vim)
  * [sjl/gundo.vim](https://github.com/sjl/gundo.vim)
  * [sjl/vitality.vim](https://github.com/sjl/vitality.vim)
  * [skywind3000/gutentags_plus](https://github.com/skywind3000/gutentags_plus)
  * [skywind3000/quickmenu.vim](https://github.com/skywind3000/quickmenu.vim)
  * [skywind3000/vim-auto-popmenu](https://github.com/skywind3000/vim-auto-popmenu)
  * [skywind3000/vim-rt-format](https://github.com/skywind3000/vim-rt-format)
  * [slarwise/telescope-args.nvim](https://github.com/slarwise/telescope-args.nvim)
  * [slashmili/alchemist.vim](https://github.com/slashmili/alchemist.vim)
  * [slim-template/vim-slim](https://github.com/slim-template/vim-slim)
  * [smiteshp/nvim-gps](https://github.com/smiteshp/nvim-gps)
  * [smiteshp/nvim-navic](https://github.com/smiteshp/nvim-navic)
  * [smithbm2316/centerpad.nvim](https://github.com/smithbm2316/centerpad.nvim)
  * [smjonas/inc-rename.nvim](https://github.com/smjonas/inc-rename.nvim)
  * [smjonas/snippet-converter.nvim](https://github.com/smjonas/snippet-converter.nvim)
  * [smolck/uivonim](https://github.com/smolck/uivonim)
  * [sodapopcan/vim-twiggy](https://github.com/sodapopcan/vim-twiggy)
  * [softinio/scaladex.nvim](https://github.com/softinio/scaladex.nvim)
  * [solarnz/thrift.vim](https://github.com/solarnz/thrift.vim)
  * [someone-stole-my-name/yaml-companion.nvim](https://github.com/someone-stole-my-name/yaml-companion.nvim)
  * [sslivkoff/vim-scroll-barnacle](https://github.com/sslivkoff/vim-scroll-barnacle)
  * [stanangeloff/php.vim](https://github.com/stanangeloff/php.vim)
  * [startup-nvim/startup.nvim](https://github.com/startup-nvim/startup.nvim)
  * [stefandtw/quickfix-reflector.vim](https://github.com/stefandtw/quickfix-reflector.vim)
  * [stephpy/vim-php-cs-fixer](https://github.com/stephpy/vim-php-cs-fixer)
  * [stevearc/aerial.nvim](https://github.com/stevearc/aerial.nvim)
  * [stevearc/gkeep.nvim](https://github.com/stevearc/gkeep.nvim)
  * [stevearc/qf_helper.nvim](https://github.com/stevearc/qf_helper.nvim)
  * [stevearc/stickybuf.nvim](https://github.com/stevearc/stickybuf.nvim)
  * [strboul/urlview.vim](https://github.com/strboul/urlview.vim)
  * [stsewd/fzf-checkout.vim](https://github.com/stsewd/fzf-checkout.vim)
  * [stsewd/gx-extended.vim](https://github.com/stsewd/gx-extended.vim)
  * [stsewd/sphinx.nvim](https://github.com/stsewd/sphinx.nvim)
  * [sudormrfbin/cheatsheet.nvim](https://github.com/sudormrfbin/cheatsheet.nvim)
  * [sukima/xmledit](https://github.com/sukima/xmledit)
  * [sunjon/stylish.nvim](https://github.com/sunjon/stylish.nvim)
  * [suy/vim-context-commentstring](https://github.com/suy/vim-context-commentstring)
  * [svermeulen/nvim-marksman](https://github.com/svermeulen/nvim-marksman)
  * [svermeulen/vim-cutlass](https://github.com/svermeulen/vim-cutlass)
  * [szw/vim-maximizer](https://github.com/szw/vim-maximizer)
  * [szymonmaszke/vimpyter](https://github.com/szymonmaszke/vimpyter)
  * [tadaa/vimade](https://github.com/tadaa/vimade)
  * [takac/vim-hardtime](https://github.com/takac/vim-hardtime)
  * [tamago324/lir.nvim](https://github.com/tamago324/lir.nvim)
  * [tamago324/telescope-openbrowser.nvim](https://github.com/tamago324/telescope-openbrowser.nvim)
  * [tami5/sqlite.lua](https://github.com/tami5/sqlite.lua)
  * [tanvirtin/vgit.nvim](https://github.com/tanvirtin/vgit.nvim)
  * [tastyep/structlog.nvim](https://github.com/tastyep/structlog.nvim)
  * [tc72/telescope-tele-tabby.nvim](https://github.com/tc72/telescope-tele-tabby.nvim)
  * [tek/proteome.nvim](https://github.com/tek/proteome.nvim)
  * [tenfyzhong/completeparameter.vim](https://github.com/tenfyzhong/completeparameter.vim)
  * [ternjs/tern_for_vim](https://github.com/ternjs/tern_for_vim)
  * [terrortylor/nvim-comment](https://github.com/terrortylor/nvim-comment)
  * [terryma/vim-expand-region](https://github.com/terryma/vim-expand-region)
  * [thaerkh/vim-workspace](https://github.com/thaerkh/vim-workspace)
  * [theblob42/drex.nvim](https://github.com/theblob42/drex.nvim)
  * [thehamsta/module-template](https://github.com/thehamsta/module-template)
  * [thehamsta/nvim-dap-virtual-text](https://github.com/thehamsta/nvim-dap-virtual-text)
  * [thehamsta/nvim-treesitter-commonlisp](https://github.com/thehamsta/nvim-treesitter-commonlisp)
  * [themercorp/themer.lua](https://github.com/themercorp/themer.lua)
  * [theprimeagen/git-worktree.nvim](https://github.com/theprimeagen/git-worktree.nvim)
  * [theprimeagen/vim-apm](https://github.com/theprimeagen/vim-apm)
  * [theprimeagen/vim-be-good](https://github.com/theprimeagen/vim-be-good)
  * [thezeroalpha/vim-visualrun](https://github.com/thezeroalpha/vim-visualrun)
  * [thibthib18/mongo-nvim](https://github.com/thibthib18/mongo-nvim)
  * [thibthib18/ros-nvim](https://github.com/thibthib18/ros-nvim)
  * [thinca/vim-themis](https://github.com/thinca/vim-themis)
  * [thirtythreeforty/lessspace.vim](https://github.com/thirtythreeforty/lessspace.vim)
  * [thyrum/vim-stabs](https://github.com/thyrum/vim-stabs)
  * [tiagofumo/vim-nerdtree-syntax-highlight](https://github.com/tiagofumo/vim-nerdtree-syntax-highlight)
  * [timakro/vim-yadi](https://github.com/timakro/vim-yadi)
  * [timeyyy/orchestra.nvim](https://github.com/timeyyy/orchestra.nvim)
  * [timuntersberger/neofs](https://github.com/timuntersberger/neofs)
  * [tjdevries/colorbuddy.nvim](https://github.com/tjdevries/colorbuddy.nvim)
  * [tjdevries/colorbuddy.vim](https://github.com/tjdevries/colorbuddy.vim)
  * [tjdevries/nlua.nvim](https://github.com/tjdevries/nlua.nvim)
  * [tjdevries/overlength.vim](https://github.com/tjdevries/overlength.vim)
  * [tklepzig/vim-buffer-navigator](https://github.com/tklepzig/vim-buffer-navigator)
  * [tmhedberg/simpylfold](https://github.com/tmhedberg/simpylfold)
  * [tmsvg/pear-tree](https://github.com/tmsvg/pear-tree)
  * [tobys/pdv](https://github.com/tobys/pdv)
  * [tomlion/vim-solidity](https://github.com/tomlion/vim-solidity)
  * [tommcdo/vim-express](https://github.com/tommcdo/vim-express)
  * [tommcdo/vim-fugitive-blame-ext](https://github.com/tommcdo/vim-fugitive-blame-ext)
  * [tomtom/tcomment_vim](https://github.com/tomtom/tcomment_vim)
  * [tomtom/tlib_vim](https://github.com/tomtom/tlib_vim)
  * [toniz4/vim-stt](https://github.com/toniz4/vim-stt)
  * [townk/vim-autoclose](https://github.com/townk/vim-autoclose)
  * [tpope/vim-apathy](https://github.com/tpope/vim-apathy)
  * [tpope/vim-bundler](https://github.com/tpope/vim-bundler)
  * [tpope/vim-dadbod](https://github.com/tpope/vim-dadbod)
  * [tpope/vim-dispatch](https://github.com/tpope/vim-dispatch)
  * [tpope/vim-endwise](https://github.com/tpope/vim-endwise)
  * [tpope/vim-fireplace](https://github.com/tpope/vim-fireplace)
  * [tpope/vim-obsession](https://github.com/tpope/vim-obsession)
  * [tpope/vim-pathogen](https://github.com/tpope/vim-pathogen)
  * [tpope/vim-projectionist](https://github.com/tpope/vim-projectionist)
  * [tpope/vim-rails](https://github.com/tpope/vim-rails)
  * [tpope/vim-salve](https://github.com/tpope/vim-salve)
  * [tpope/vim-scriptease](https://github.com/tpope/vim-scriptease)
  * [tpope/vim-sexp-mappings-for-regular-people](https://github.com/tpope/vim-sexp-mappings-for-regular-people)
  * [tpope/vim-sleuth](https://github.com/tpope/vim-sleuth)
  * [tpope/vim-speeddating](https://github.com/tpope/vim-speeddating)
  * [tpope/vim-tbone](https://github.com/tpope/vim-tbone)
  * [tpope/vim-unimpaired](https://github.com/tpope/vim-unimpaired)
  * [tpope/vim-vinegar](https://github.com/tpope/vim-vinegar)
  * [tracyone/neomake-multiprocess](https://github.com/tracyone/neomake-multiprocess)
  * [triglav/vim-visual-increment](https://github.com/triglav/vim-visual-increment)
  * [troydm/easytree.vim](https://github.com/troydm/easytree.vim)
  * [tveskag/nvim-blame-line](https://github.com/tveskag/nvim-blame-line)
  * [tweekmonster/braceless.vim](https://github.com/tweekmonster/braceless.vim)
  * [tweekmonster/exception.vim](https://github.com/tweekmonster/exception.vim)
  * [tweekmonster/gofmt.vim](https://github.com/tweekmonster/gofmt.vim)
  * [tweekmonster/helpful.vim](https://github.com/tweekmonster/helpful.vim)
  * [tweekmonster/hl-goimport.vim](https://github.com/tweekmonster/hl-goimport.vim)
  * [tweekmonster/impsort.vim](https://github.com/tweekmonster/impsort.vim)
  * [tweekmonster/startuptime.vim](https://github.com/tweekmonster/startuptime.vim)
  * [tyru/capture.vim](https://github.com/tyru/capture.vim)
  * [tyru/caw.vim](https://github.com/tyru/caw.vim)
  * [tzachar/cmp-fuzzy-buffer](https://github.com/tzachar/cmp-fuzzy-buffer)
  * [tzachar/cmp-fuzzy-path](https://github.com/tzachar/cmp-fuzzy-path)
  * [udayvir-singh/hibiscus.nvim](https://github.com/udayvir-singh/hibiscus.nvim)
  * [uga-rosa/translate.nvim](https://github.com/uga-rosa/translate.nvim)
  * [unblevable/quick-scope](https://github.com/unblevable/quick-scope)
  * [untitled-ai/jupyter_ascending](https://github.com/untitled-ai/jupyter_ascending)
  * [valloric/matchtagalways](https://github.com/valloric/matchtagalways)
  * [valloric/youcompleteme](https://github.com/valloric/youcompleteme)
  * [vhakulinen/gnvim](https://github.com/vhakulinen/gnvim)
  * [vhyrro/neorg](https://github.com/vhyrro/neorg)
  * [vifm/neovim-vifm](https://github.com/vifm/neovim-vifm)
  * [vifm/vifm.vim](https://github.com/vifm/vifm.vim)
  * [vijaymarupudi/nvim-fzf](https://github.com/vijaymarupudi/nvim-fzf)
  * [vim-airline/vim-airline-themes](https://github.com/vim-airline/vim-airline-themes)
  * [vim-chat/vim-chat](https://github.com/vim-chat/vim-chat)
  * [vim-ctrlspace/vim-ctrlspace](https://github.com/vim-ctrlspace/vim-ctrlspace)
  * [vim-jp/vital.vim](https://github.com/vim-jp/vital.vim)
  * [vim-pandoc/vim-pandoc](https://github.com/vim-pandoc/vim-pandoc)
  * [vim-python/python-syntax](https://github.com/vim-python/python-syntax)
  * [vim-scripts/a.vim](https://github.com/vim-scripts/a.vim)
  * [vim-scripts/align](https://github.com/vim-scripts/align)
  * [vim-scripts/autocomplpop](https://github.com/vim-scripts/autocomplpop)
  * [vim-scripts/bufexplorer.zip](https://github.com/vim-scripts/bufexplorer.zip)
  * [vim-scripts/csapprox](https://github.com/vim-scripts/csapprox)
  * [vim-scripts/grep.vim](https://github.com/vim-scripts/grep.vim)
  * [vim-scripts/replacewithregister](https://github.com/vim-scripts/replacewithregister)
  * [vim-scripts/sessionman.vim](https://github.com/vim-scripts/sessionman.vim)
  * [vim-scripts/taglist.vim](https://github.com/vim-scripts/taglist.vim)
  * [vim-scripts/tetris.vim](https://github.com/vim-scripts/tetris.vim)
  * [vim-syntastic/syntastic](https://github.com/vim-syntastic/syntastic)
  * [vim-test/vim-test](https://github.com/vim-test/vim-test)
  * [vim-utils/vim-man](https://github.com/vim-utils/vim-man)
  * [vim-vdebug/vdebug](https://github.com/vim-vdebug/vdebug)
  * [vim-volt/volt](https://github.com/vim-volt/volt)
  * [vim/killersheep](https://github.com/vim/killersheep)
  * [vimpostor/vim-tpipeline](https://github.com/vimpostor/vim-tpipeline)
  * [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki)
  * [voldikss/vim-browser-search](https://github.com/voldikss/vim-browser-search)
  * [voldikss/vim-floaterm](https://github.com/voldikss/vim-floaterm)
  * [vonheikemen/searchbox.nvim](https://github.com/vonheikemen/searchbox.nvim)
  * [vonr/align.nvim](https://github.com/vonr/align.nvim)
  * [vuki656/package-info.nvim](https://github.com/vuki656/package-info.nvim)
  * [vundlevim/vundle.vim](https://github.com/vundlevim/vundle.vim)
  * [vv-vim/vv](https://github.com/vv-vim/vv)
  * [w0rp/ale](https://github.com/w0rp/ale)
  * [wakatime/vim-wakatime](https://github.com/wakatime/vim-wakatime)
  * [waylonwalker/telegraph.nvim](https://github.com/waylonwalker/telegraph.nvim)
  * [wbthomason/buildit.nvim](https://github.com/wbthomason/buildit.nvim)
  * [wbthomason/lsp-status.nvim](https://github.com/wbthomason/lsp-status.nvim)
  * [webdevel/tabulous](https://github.com/webdevel/tabulous)
  * [weilbith/nvim-code-action-menu](https://github.com/weilbith/nvim-code-action-menu)
  * [weilbith/nvim-floating-tag-preview](https://github.com/weilbith/nvim-floating-tag-preview)
  * [weilbith/nvim-lsp-bacomp](https://github.com/weilbith/nvim-lsp-bacomp)
  * [weilbith/nvim-lsp-smag](https://github.com/weilbith/nvim-lsp-smag)
  * [weirongxu/coc-explorer](https://github.com/weirongxu/coc-explorer)
  * [wellle/context.vim](https://github.com/wellle/context.vim)
  * [wellle/tmux-complete.vim](https://github.com/wellle/tmux-complete.vim)
  * [whynothugo/lsp_lines.nvim](https://github.com/whynothugo/lsp_lines.nvim)
  * [will133/vim-dirdiff](https://github.com/will133/vim-dirdiff)
  * [willthbill/opener.nvim](https://github.com/willthbill/opener.nvim)
  * [wincent/command-t](https://github.com/wincent/command-t)
  * [wincent/ferret](https://github.com/wincent/ferret)
  * [wincent/pinnacle](https://github.com/wincent/pinnacle)
  * [windwp/nvim-projectconfig](https://github.com/windwp/nvim-projectconfig)
  * [windwp/nvim-spectre](https://github.com/windwp/nvim-spectre)
  * [windwp/nvim-ts-closetag](https://github.com/windwp/nvim-ts-closetag)
  * [winston0410/cmd-parser.nvim](https://github.com/winston0410/cmd-parser.nvim)
  * [winston0410/commented.nvim](https://github.com/winston0410/commented.nvim)
  * [wsdjeg/flygrep.vim](https://github.com/wsdjeg/flygrep.vim)
  * [wsdjeg/vim-cheat](https://github.com/wsdjeg/vim-cheat)
  * [wsdjeg/vim-fetch](https://github.com/wsdjeg/vim-fetch)
  * [wyattjsmith1/weather.nvim](https://github.com/wyattjsmith1/weather.nvim)
  * [xeluxee/competitest.nvim](https://github.com/xeluxee/competitest.nvim)
  * [xiyaowong/link-visitor.nvim](https://github.com/xiyaowong/link-visitor.nvim)
  * [xiyaowong/nvim-transparent](https://github.com/xiyaowong/nvim-transparent)
  * [xolox/vim-lua-ftplugin](https://github.com/xolox/vim-lua-ftplugin)
  * [xolox/vim-lua-inspect](https://github.com/xolox/vim-lua-inspect)
  * [xolox/vim-misc](https://github.com/xolox/vim-misc)
  * [xolox/vim-notes](https://github.com/xolox/vim-notes)
  * [xolox/vim-session](https://github.com/xolox/vim-session)
  * [xuyuanp/nerdtree-git-plugin](https://github.com/xuyuanp/nerdtree-git-plugin)
  * [xuyuanp/scrollbar.nvim](https://github.com/xuyuanp/scrollbar.nvim)
  * [yamatsum/nvim-nonicons](https://github.com/yamatsum/nvim-nonicons)
  * [yatli/fvim](https://github.com/yatli/fvim)
  * [yazgoo/yank-history](https://github.com/yazgoo/yank-history)
  * [yegappan/mru](https://github.com/yegappan/mru)
  * [yehuohan/popc](https://github.com/yehuohan/popc)
  * [yggdroot/indentline](https://github.com/yggdroot/indentline)
  * [yggdroot/leaderf](https://github.com/yggdroot/leaderf)
  * [ygm2/rooter.nvim](https://github.com/ygm2/rooter.nvim)
  * [yorickpeterse/nvim-dd](https://github.com/yorickpeterse/nvim-dd)
  * [yorickpeterse/nvim-pqf](https://github.com/yorickpeterse/nvim-pqf)
  * [yorickpeterse/nvim-window](https://github.com/yorickpeterse/nvim-window)
  * [yqlbu/neovim-server](https://github.com/yqlbu/neovim-server)
  * [yssl/qfenter](https://github.com/yssl/qfenter)
  * [yuki-yano/zero.nvim](https://github.com/yuki-yano/zero.nvim)
  * [yuratomo/w3m.vim](https://github.com/yuratomo/w3m.vim)
  * [yuttie/comfortable-motion.vim](https://github.com/yuttie/comfortable-motion.vim)
  * [zane-/cder.nvim](https://github.com/zane-/cder.nvim)
  * [zane-/howdoi.nvim](https://github.com/zane-/howdoi.nvim)
  * [zegervdv/nrpattern.nvim](https://github.com/zegervdv/nrpattern.nvim)
  * [zenbro/mirror.vim](https://github.com/zenbro/mirror.vim)
  * [zgpio/brew.nvim](https://github.com/zgpio/brew.nvim)
  * [zhimsel/vim-stay](https://github.com/zhimsel/vim-stay)
  * [ziontee113/icon-picker.nvim](https://github.com/ziontee113/icon-picker.nvim)
  * [zirrostig/vim-schlepp](https://github.com/zirrostig/vim-schlepp)
  * [zsugabubus/crazy8.nvim](https://github.com/zsugabubus/crazy8.nvim)

# Donate
If you want to donate then you need to find the link:
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a](https://www.buymeacoffee.com/altermo) [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()
* [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]() [a]()