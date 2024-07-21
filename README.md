# vim-plugin-list
This is a list of plugins.

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_NOTE: this list was documented over a span of multiple months and has some weirdness (in othe words, it would not be weird to presume that I was high when writing this (I was not))._

_Other BETER vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [awesome-nvim](https://github.com/rockerBOO/awesome-neovim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins), [vim-galore](https://github.com/mhinz/vim-galore/blob/master/PLUGINS.md), [](https://github.com/astier/vlugins)_

# Jump list
  * [extensions/options/readmore/...](#extensionsreadmoreoptions)
  * [documented](#documented)
    * [deoplete-extensions](#deoplete-extensions)
    * [telescope-extensions](#telescope-extensions)
    * [extension](#extension)
    * [tmux](#tmux)
    * [nvim-cmp-extensions](#nvim-cmp-extensions)
    * [buffers](#buffers)
    * [aligner](#aligner)
    * [toggle](#toggle)
    * [key](#key)
    * [auto-pairs](#auto-pairs)
    * [other](#other)
    * [comment](#comment)
    * [library](#library)
    * [remote-colab](#remote-colab)
    * [chat](#chat)
    * [mouse](#mouse)
    * [windows](#windows)
    * [detectindent](#detectindent)
    * [indent](#indent)
    * [folds](#folds)
    * [quickfix](#quickfix)
    * [gui](#gui)
    * [ide](#ide)
    * [sidebar](#sidebar)
    * [tag](#tag)
    * [file](#file)
    * [spell](#spell)
    * [note](#note)
    * [preview](#preview)
    * [file-movment](#file-movment)
    * [todo](#todo)
    * [markdown-langueges](#markdown-langueges)
    * [snippets](#snippets)
    * [language](#language)
    * [lsp](#lsp)
    * [lint](#lint)
    * [autocomplete](#autocomplete)
    * [syntax](#syntax)
    * [integration](#integration)
    * [fennel](#fennel)
    * [test](#test)
    * [debug](#debug)
    * [repl](#repl)
    * [color](#color)
    * [tabline](#tabline)
    * [visual](#visual)
    * [scrollbar](#scrollbar)
    * [statusline](#statusline)
    * [highlight](#highlight)
    * [zen](#zen)
    * [colorscheme](#colorscheme)
    * [bufferline](#bufferline)
    * [yanklist](#yanklist)
    * [hop](#hop)
    * [movment](#movment)
    * [textobject](#textobject)
    * [game](#game)
    * [startscreen](#startscreen)
    * [projects-seessions](#projects-seessions)
    * [undotree](#undotree)
    * [command](#command)
    * [replace](#replace)
    * [terminal](#terminal)
    * [file-explorer](#file-explorer)
    * [plugin-maneger](#plugin-maneger)
    * [git](#git)
    * [finder](#finder)
    * [apps](#apps)
    * [ui-creator](#ui-creator)
    * [treesitter](#treesitter)
    * [keys](#keys)
    * [tags](#tags)
    * [todo-list](#todo-list)
    * [repalce](#repalce)
    * [filemanager](#filemanager)
    * [keymap-creater](#keymap-creater)
    * [language-suport](#language-suport)
    * [from-one-to-more-lines](#from-one-to-more-lines)
    * [abbreviations](#abbreviations)
    * [functions-commands](#functions-commands)
    * [speed-up-loadtimes](#speed-up-loadtimes)
    * [pairs](#pairs)
    * [remote](#remote)
    * [highlight-underline](#highlight-underline)
    * [marks](#marks)
    * [markdown-org-neorg](#markdown-org-neorg)
    * [use-instead](#use-instead)
    * [libs](#libs)
    * [starter-page](#starter-page)
  * [not documented](#not-documented)
  * [donate](#donate)
# Extensions/readmore/options/...
  * [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) : [extensions](https://github.com/nvim-treesitter/nvim-treesitter/wiki/Extra-modules-and-plugins), [supported-languages](https://github.com/nvim-treesitter/nvim-treesitter#supported-languages)
  * [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim) : [list-of-coc-apps](https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions#implemented-coc-extensions)
  * [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) : [optional](https://github.com/nvim-telescope/telescope.nvim#optional-dependencies), [extensions](https://github.com/nvim-telescope/telescope.nvim/wiki/Extensions#different-plugins-with-telescope-integration)
  * [preservim/nerdtree](https://github.com/preservim/nerdtree) : [optional](https://github.com/preservim/nerdtree#nerdtree-plugins)
  * [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp) : [extensions](https://github.com/hrsh7th/nvim-cmp/wiki/List-of-sources)
# Documented
## deoplete-extensions
  * [callmekohei/deoplete-fsharp](https://github.com/callmekohei/deoplete-fsharp) : deoplete.nvim source for F#
  * [carlitux/deoplete-ternjs](https://github.com/carlitux/deoplete-ternjs) : deoplete.nvim source for javascript
  * [deoplete-plugins/deoplete-clang](https://github.com/deoplete-plugins/deoplete-clang) : C/C++/Objective-C/Objective-C++ source for deoplete.nvim
  * [deoplete-plugins/deoplete-dictionary](https://github.com/deoplete-plugins/deoplete-dictionary) : deoplete source for dictionary
  * [deoplete-plugins/deoplete-jedi](https://github.com/deoplete-plugins/deoplete-jedi) : deoplete.nvim source for jedi
  * [deoplete-plugins/deoplete-lsp](https://github.com/deoplete-plugins/deoplete-lsp) : LSP Completion source for deoplete
  * [deoplete-plugins/deoplete-terminal](https://github.com/deoplete-plugins/deoplete-terminal) : Terminal completion for deoplete.nvim
  * [juliaeditorsupport/deoplete-julia](https://github.com/juliaeditorsupport/deoplete-julia) : This package supplements julia-vim by providing syntax completions, through Deoplete [archived]
  * [kristijanhusak/deoplete-phpactor](https://github.com/kristijanhusak/deoplete-phpactor) : Phpactor integration for deoplete.nvim
  * [lighttiger2505/deoplete-vim-lsp](https://github.com/lighttiger2505/deoplete-vim-lsp) : deoplete source for vim-lsp
  * [ponko2/deoplete-fish](https://github.com/ponko2/deoplete-fish) : deoplete.nvim source for fish
  * [uplus/deoplete-solargraph](https://github.com/uplus/deoplete-solargraph) : deoplete.nvim source for Ruby with solargraph
## telescope-extensions
  * [aloussase/telescope-gradle.nvim](https://github.com/aloussase/telescope-gradle.nvim) : telescope extensions to run gradle tasks
  * [aloussase/telescope-maven-search](https://github.com/aloussase/telescope-maven-search) : telescope extensions to search dependencies in MavenCentral
  * [angkeith/telescope-terraform-doc.nvim](https://github.com/angkeith/telescope-terraform-doc.nvim) : telescope extensions to search and browse terraform providers docs
  * [axkirillov/easypick.nvim](https://github.com/axkirillov/easypick.nvim) : easily create Telescope pickers
  * [axkirillov/telescope-changed-files](https://github.com/axkirillov/telescope-changed-files) : telescope extensions to browse files that changed between your branch and develop
  * [benfowler/telescope-luasnip.nvim](https://github.com/benfowler/telescope-luasnip.nvim) : telescope extensions to list luasnip snippets
  * [bi0ha2ard/telescope-ros.nvim](https://github.com/bi0ha2ard/telescope-ros.nvim) : telescope extensions to select ROS(2) package
  * [brandoncc/telescope-harpoon.nvim](https://github.com/brandoncc/telescope-harpoon.nvim) : telescope extensions to harpoon (depreciated)
  * [camgraff/telescope-tmux.nvim](https://github.com/camgraff/telescope-tmux.nvim) : telescope extensions to fuzzy-finding over tmux targets
  * [chip/telescope-code-fence.nvim](https://github.com/chip/telescope-code-fence.nvim) : telescope extensions to fetch and parse text files from Github and provide a list of markdown code fences
  * [chip/telescope-software-licenses.nvim](https://github.com/chip/telescope-software-licenses.nvim) : telescope extensions to view common software licenses
  * [cljoly/telescope-repo.nvim](https://github.com/cljoly/telescope-repo.nvim) : telescope extensions to jump to any repository in filesystem
  * [crispgm/telescope-heading.nvim](https://github.com/crispgm/telescope-heading.nvim) : telescope extensions to switch between document's headings
  * [danielfalk/smart-open.nvim](https://github.com/danielfalk/smart-open.nvim) : provide the best possible suggestions for quickly opening files
  * [danielpieper/telescope-tmuxinator.nvim](https://github.com/danielpieper/telescope-tmuxinator.nvim) : telescope extensions to integrate with tmuxinator
  * [debugloop/telescope-undo.nvim](https://github.com/debugloop/telescope-undo.nvim) : Visualize your undo tree in telescope
  * [desdic/agrolens.nvim](https://github.com/desdic/agrolens.nvim) : runs custom tree-sitter queries
  * [desdic/telescope-rooter.nvim](https://github.com/desdic/telescope-rooter.nvim) : changes the working directory to the to the project/root path
  * [dhruvmanila/telescope-bookmarks.nvim](https://github.com/dhruvmanila/telescope-bookmarks.nvim) : telescope extensions to open your browser bookmarks
  * [edolphin-ydf/goimpl.nvim](https://github.com/edolphin-ydf/goimpl.nvim) : telescope extension for goimlp
  * [elpiloto/telescope-vimwiki.nvim](https://github.com/elpiloto/telescope-vimwiki.nvim) : Look for your vimwiki pages using telescope
  * [ethanjwright/vs-tasks.nvim](https://github.com/ethanjwright/vs-tasks.nvim) : Telescope plugin to load and run tasks in a project that conform to VS Code's Editor Tasks
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
  * [linarcx/telescope-scriptnames.nvim](https://github.com/linarcx/telescope-scriptnames.nvim) : telescope extension wrapper around `:scriptnames`
  * [luc-tielen/telescope_hoogle](https://github.com/luc-tielen/telescope_hoogle) : telescope plugin for Hoogle
  * [lukaspietzschmann/telescope-tabs](https://github.com/lukaspietzschmann/telescope-tabs) : list and select tabs in telescope
  * [natecraddock/telescope-zf-native.nvim](https://github.com/natecraddock/telescope-zf-native.nvim) : native telescope bindings to zf for sorting results
  * [nvim-neorg/neorg-telescope](https://github.com/nvim-neorg/neorg-telescope) : telescope extensions to browse neorg file headings
  * [nvim-telescope/telescope-arecibo.nvim](https://github.com/nvim-telescope/telescope-arecibo.nvim) : Neovim Telescope extension for searching the web
  * [nvim-telescope/telescope-bibtex.nvim](https://github.com/nvim-telescope/telescope-bibtex.nvim) : Search and paste entries from `*.bib` files with telescope.nvim
  * [nvim-telescope/telescope-cheat.nvim](https://github.com/nvim-telescope/telescope-cheat.nvim) : An attempt to recreate cheat.sh with lua, neovim, sqlite.lua, and telescope.nvim
  * [nvim-telescope/telescope-dap.nvim](https://github.com/nvim-telescope/telescope-dap.nvim) : Integration for nvim-dap with telescope.nvim
  * [nvim-telescope/telescope-file-browser.nvim](https://github.com/nvim-telescope/telescope-file-browser.nvim) : file browser extension for telescope.nvim
  * [nvim-telescope/telescope-frecency.nvim](https://github.com/nvim-telescope/telescope-frecency.nvim) : telescope extensions to offers intelligent prioritization when selecting files from your editing history
  * [nvim-telescope/telescope-fzf-native.nvim](https://github.com/nvim-telescope/telescope-fzf-native.nvim) : FZF-native (`c` port of fzf) style sorter for telescope
  * [nvim-telescope/telescope-fzf-writer.nvim](https://github.com/nvim-telescope/telescope-fzf-writer.nvim) : Incorporating fzf into telescope
  * [nvim-telescope/telescope-fzy-native.nvim](https://github.com/nvim-telescope/telescope-fzy-native.nvim) : FZY style sorter that is compiled
  * [nvim-telescope/telescope-ghq.nvim](https://github.com/nvim-telescope/telescope-ghq.nvim) : telescope extensions to provide its users with operating x-motemen/ghq
  * [nvim-telescope/telescope-github.nvim](https://github.com/nvim-telescope/telescope-github.nvim) : telescope integration with github cli
  * [nvim-telescope/telescope-hop.nvim](https://github.com/nvim-telescope/telescope-hop.nvim) : an extension for telescope.nvim for hopping to the moon
  * [nvim-telescope/telescope-live-grep-args.nvim](https://github.com/nvim-telescope/telescope-live-grep-args.nvim) : Live grep args picker for telescope.nvim
  * [nvim-telescope/telescope-media-files.nvim](https://github.com/nvim-telescope/telescope-media-files.nvim) : Preview images, pdf, epub, video, and fonts from Neovim using Telescope
  * [nvim-telescope/telescope-node-modules.nvim](https://github.com/nvim-telescope/telescope-node-modules.nvim) : telescope extension that provides its users with node packages under `node_modules/` dir
  * [nvim-telescope/telescope-packer.nvim](https://github.com/nvim-telescope/telescope-packer.nvim) : Integration for packer.nvim with telescope.nvim
  * [nvim-telescope/telescope-project.nvim](https://github.com/nvim-telescope/telescope-project.nvim) : extension for telescope.nvim that allows you to switch between projects
  * [nvim-telescope/telescope-rs.nvim](https://github.com/nvim-telescope/telescope-rs.nvim) : Experimental features for telescope in RUST
  * [nvim-telescope/telescope-smart-history.nvim](https://github.com/nvim-telescope/telescope-smart-history.nvim) : history implementation that memorizes prompt input for a specific context as a telescope extension
  * [nvim-telescope/telescope-snippets.nvim](https://github.com/nvim-telescope/telescope-snippets.nvim) : Integration for snippets.nvim with telescope.nvim [archived]
  * [nvim-telescope/telescope-symbols.nvim](https://github.com/nvim-telescope/telescope-symbols.nvim) : telescope extensions to pick symbols
  * [nvim-telescope/telescope-ui-select.nvim](https://github.com/nvim-telescope/telescope-ui-select.nvim) : It sets `vim.ui.select` to telescope
  * [nvim-telescope/telescope-vimspector.nvim](https://github.com/nvim-telescope/telescope-vimspector.nvim) : Integration for vimspector with telescope.nvim
  * [nvim-telescope/telescope-z.nvim](https://github.com/nvim-telescope/telescope-z.nvim) : an extension for telescope.nvim that provides its users with operating rupa/z or its compatibles
  * [olacin/telescope-cc.nvim](https://github.com/olacin/telescope-cc.nvim) : telescope integration of Conventional Commits
  * [olacin/telescope-gitmoji.nvim](https://github.com/olacin/telescope-gitmoji.nvim) : telescope integration of gitmoji
  * [otavioschwanck/telescope-alternate.nvim](https://github.com/otavioschwanck/telescope-alternate.nvim) : Alternate between common files using pre-defined regexp
  * [prochri/telescope-all-recent.nvim](https://github.com/prochri/telescope-all-recent.nvim) : Frecency algorthim for sorting telescope pickers
  * [runiq/telescope-trouble.nvim](https://github.com/runiq/telescope-trouble.nvim) : see trouble info from telescope
  * [slarwise/telescope-args.nvim](https://github.com/slarwise/telescope-args.nvim) : telescopeextension for navigating the argument list
  * [tamago324/telescope-openbrowser.nvim](https://github.com/tamago324/telescope-openbrowser.nvim) : Integration for open-browser.vim with telescope.nvim
  * [tc72/telescope-tele-tabby.nvim](https://github.com/tc72/telescope-tele-tabby.nvim) : A tab switcher extension for Telescope
  * [tom-anders/telescope-vim-bookmarks.nvim](https://github.com/tom-anders/telescope-vim-bookmarks.nvim) : telescope extensions to integrate with [mattesgroeger/vim-bookmarks](https://github.com/mattesgroeger/vim-bookmarks)
  * [tsakirist/telescope-lazy.nvim](https://github.com/tsakirist/telescope-lazy.nvim) : browse plugins installed with lazy.nvim
  * [wesleimp/telescope-windowizer.nvim](https://github.com/wesleimp/telescope-windowizer.nvim) : telescope extensions to Create new tmux window ready for edit your selected file inside vim
  * [xiyaowong/telescope-emoji.nvim](https://github.com/xiyaowong/telescope-emoji.nvim) : telescope extensions to search emoji
  * [zane-/cder.nvim](https://github.com/zane-/cder.nvim) : A telescope.nvimextension for quickly changing your working directory
  * [zane-/howdoi.nvim](https://github.com/zane-/howdoi.nvim) : telescope extension for previewing howdoi results
## extension
  * [abeldekat/lazyflex.nvim](https://github.com/abeldekat/lazyflex.nvim) : add-on for lazy.nvim that makes it easy to troubleshoot the config
  * [antoinemadec/coc-fzf](https://github.com/antoinemadec/coc-fzf) : fzf with coc.nvim
  * [arkav/lualine-lsp-progress](https://github.com/arkav/lualine-lsp-progress) : Information provided by active lsp clients from the $/progress endpoint as a statusline component for lualine.nvim
  * [ggandor/leap-ast.nvim](https://github.com/ggandor/leap-ast.nvim) : jump, select, operate on ast node via [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim)
  * [ggandor/leap-spooky.nvim](https://github.com/ggandor/leap-spooky.nvim) : remote operations via [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim)
  * [haya14busa/incsearch-easymotion.vim](https://github.com/haya14busa/incsearch-easymotion.vim) : Integration between [haya14busa/incsearch.vim](https://github.com/haya14busa/incsearch.vim) and [easymotion/vim-easymotion](https://github.com/easymotion/vim-easymotion)
  * [haya14busa/incsearch-fuzzy.vim](https://github.com/haya14busa/incsearch-fuzzy.vim) : incremantal fuzzy search extension for incsearch.vim
  * [jistr/vim-nerdtree-tabs](https://github.com/jistr/vim-nerdtree-tabs) : make NERDTree a true panel, independent of tabs [no maintain]
  * [kristijanhusak/defx-git](https://github.com/kristijanhusak/defx-git) : Git status implementation for defx.nvim
  * [kristijanhusak/defx-icons](https://github.com/kristijanhusak/defx-icons) : Custom implementation of vim-devicons for defx.nvim
  * [kristijanhusak/vim-dirvish-git](https://github.com/kristijanhusak/vim-dirvish-git) : Plugin for dirvish.vim that shows git status flags
  * [lambdalisue/battery.vim](https://github.com/lambdalisue/battery.vim) : a statusline or tablinecomponent for vim
  * [matsui54/defx-sftp](https://github.com/matsui54/defx-sftp) : a defx source for sftp
  * [mengelbrecht/lightline-bufferline](https://github.com/mengelbrecht/lightline-bufferline) : add bufferline functionality for lightline
  * [neoclide/coc-pairs](https://github.com/neoclide/coc-pairs) : auto pairs for coc
  * [ofirgall/goto-breakpoints.nvim](https://github.com/ofirgall/goto-breakpoints.nvim) : cycle between nvim-dap's breakpoints
  * [philrunninger/nerdtree-buffer-ops](https://github.com/philrunninger/nerdtree-buffer-ops) : a NERDTree plugin that highlights all visible nodes that are open in Vim
  * [philrunninger/nerdtree-visual-selection](https://github.com/philrunninger/nerdtree-visual-selection) : defines key mappings that will work on nodes contained in a Visual selection in NERDTree
  * [roginfarrer/vim-dirvish-dovish](https://github.com/roginfarrer/vim-dirvish-dovish) : The file manipulation commands for vim-dirvish that you've always wanted
  * [roobert/surround-ui.nvim](https://github.com/roobert/surround-ui.nvim) : change the key combos for [kylechui/nvim-surround](https://github.com/kylechui/nvim-surround)
  * [scrooloose/nerdtree-project-plugin](https://github.com/scrooloose/nerdtree-project-plugin) : nerd extension which preserves Tree state (open/closed dirs) between sessions
  * [shougo/ddu-ui-filer](https://github.com/shougo/ddu-ui-filer) : File list plugin for ddu.vim
  * [thehamsta/nvim-treesitter-commonlisp](https://github.com/thehamsta/nvim-treesitter-commonlisp) : extends the standard highlighting of nvim-treesitter for Common Lisp
  * [thomasfaingnaert/vim-lsp-neosnippet](https://github.com/thomasfaingnaert/vim-lsp-neosnippet) : integrates neosnippet.vim in vim-lsp
  * [tiagofumo/vim-nerdtree-syntax-highlight](https://github.com/tiagofumo/vim-nerdtree-syntax-highlight) : adds syntax for nerdtree on most common file extensions
  * [tjdevries/tree-sitter-lua](https://github.com/tjdevries/tree-sitter-lua) : Tree sitter grammar for Lua built to be used inside of Neovim
  * [tommcdo/vim-fugitive-blame-ext](https://github.com/tommcdo/vim-fugitive-blame-ext) : extends the functionality of tpope's fugitive plugin by showing first line of the commit message
  * [tpope/vim-vinegar](https://github.com/tpope/vim-vinegar) : enhances netrw, partially in an attempt to mitigate the need for more disruptive "project drawer" style plugins
  * [vim-airline/vim-airline-themes](https://github.com/vim-airline/vim-airline-themes) : official theme repository for vim-airline
  * [weirongxu/coc-explorer](https://github.com/weirongxu/coc-explorer) : Explorer extension for coc.nvim
  * [wellle/tmux-complete.vim](https://github.com/wellle/tmux-complete.vim) : insert mode completion of words in adjacent tmux panes
  * [wsdjeg/dein-ui.vim](https://github.com/wsdjeg/dein-ui.vim) : UI for Shougo's dein.vim
  * [xuyuanp/nerdtree-git-plugin](https://github.com/xuyuanp/nerdtree-git-plugin) : A plugin of NERDTree showing git status flags
  * [yamatsum/nvim-nonicons](https://github.com/yamatsum/nvim-nonicons) : Collection of configurations for nvim-web-devicons
## tmux
  * [aserowy/tmux.nvim](https://github.com/aserowy/tmux.nvim) : a few features making vim and tmux work beautifully together
  * [christoomey/vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator) : navigate seamlessly between vim and tmux splits using a consistent set of hotkeys
  * [christoomey/vim-tmux-runner](https://github.com/christoomey/vim-tmux-runner) : A simple, vimscript only, command runner for sending commands from vim to tmux
  * [hkupty/nvimux](https://github.com/hkupty/nvimux) : Nvimux allows neovim to work as a tmux replacement
  * [junegunn/heytmux](https://github.com/junegunn/heytmux) : Tmux scripting made easy
  * [narajaon/onestatus](https://github.com/narajaon/onestatus) : helps you interact with your tmux
  * [nathom/tmux.nvim](https://github.com/nathom/tmux.nvim) : lets you seamlessly navigate between tmux panes and vim splits
  * [numtostr/navigator.nvim](https://github.com/numtostr/navigator.nvim) : Smoothly navigate between splits and panes
  * [otavioschwanck/tmux-awesome-manager.nvim](https://github.com/otavioschwanck/tmux-awesome-manager.nvim) : provides a pack of functionalities to work with TMUX
  * [preservim/vimux](https://github.com/preservim/vimux) : easily interact with tmux from vim
  * [roxma/vim-tmux-clipboard](https://github.com/roxma/vim-tmux-clipboard) : provides seamless integration for vim and tmux's clipboard
  * [shivamashtikar/tmuxjump.vim](https://github.com/shivamashtikar/tmuxjump.vim) : A plugin to open file from file paths printed in sibling tmux pane
  * [sourproton/tunnell.nvim](https://github.com/sourproton/tunnell.nvim) : send tunnel text to tmux pane
  * [tpope/vim-tbone](https://github.com/tpope/vim-tbone) : Basic tmux support for Vim
  * [vimpostor/vim-tpipeline](https://github.com/vimpostor/vim-tpipeline) : Embed your vim statusline in the tmux statusline
## nvim-cmp-extensions
  * [amarakon/nvim-cmp-buffer-lines](https://github.com/amarakon/nvim-cmp-buffer-lines) : provides a source for all the lines in the current buffer
  * [andersevenrud/cmp-tmux](https://github.com/andersevenrud/cmp-tmux) : Tmux completion source for nvim-cmp
  * [david-kunz/cmp-npm](https://github.com/david-kunz/cmp-npm) : nvim-cmp extension for npm autocomplete
  * [dcampos/cmp-snippy](https://github.com/dcampos/cmp-snippy) : nvim-snippy source for nvim-cmp
  * [dmitmel/cmp-cmdline-history](https://github.com/dmitmel/cmp-cmdline-history) : nvim-cmp source for getting completions from command-line or search histories.
  * [dmitmel/cmp-digraphs](https://github.com/dmitmel/cmp-digraphs) : nvim-cmp source for completing digraphs
  * [f3fora/cmp-spell](https://github.com/f3fora/cmp-spell) : nvim-cmp extension for spell autocomplete
  * [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer) : nvim-cmp extension for buffer autocomplete
  * [hrsh7th/cmp-calc](https://github.com/hrsh7th/cmp-calc) : nvim-cmp extension for math calculation autocomplete
  * [hrsh7th/cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline) : nvim-cmp extension for cmdline autocomplete
  * [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp) : nvim-cmp extension for lsp autocomplete
  * [hrsh7th/cmp-nvim-lsp-document-symbol](https://github.com/hrsh7th/cmp-nvim-lsp-document-symbol) : nvim-cmp source for textDocument/documentSymbol via nvim-lsp
  * [hrsh7th/cmp-nvim-lsp-signature-help](https://github.com/hrsh7th/cmp-nvim-lsp-signature-help) : nvim-cmp extension for showing lsp help in autocomplete
  * [hrsh7th/cmp-nvim-lua](https://github.com/hrsh7th/cmp-nvim-lua) : nvim-cmp extension for lua autocomplete
  * [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path) : nvim-cmp extension for path autocomplete
  * [hrsh7th/cmp-vsnip](https://github.com/hrsh7th/cmp-vsnip) : nvim-cmp source for vim-vsnip
  * [jcdickinson/codeium.nvim](https://github.com/jcdickinson/codeium.nvim) : native Codeium autocompletion for nvim-cmp
  * [lukas-reineke/cmp-rg](https://github.com/lukas-reineke/cmp-rg) : nvim-cmp extension for rg autocomplete
  * [lukas-reineke/cmp-under-comparator](https://github.com/lukas-reineke/cmp-under-comparator) : A tiny function for nvim-cmpto better sort completion items that start with one or more underlines
  * [max397574/cmp-greek](https://github.com/max397574/cmp-greek) : nvim-cmp source for greek letters
  * [mtoohey31/cmp-fish](https://github.com/mtoohey31/cmp-fish) : nvim-cmp extension for fish autocomplete
  * [notomo/cmp-neosnippet](https://github.com/notomo/cmp-neosnippet) : nvim-cmp source for neosnippet
  * [paterjason/cmp-conjure](https://github.com/paterjason/cmp-conjure) : nvim-cmp source for conjure
  * [petertriho/cmp-git](https://github.com/petertriho/cmp-git) : nvim-cmp extension for git autocomplete
  * [quangnguyen30192/cmp-nvim-tags](https://github.com/quangnguyen30192/cmp-nvim-tags) : nvim-cmp extension for tag autocomplete
  * [quangnguyen30192/cmp-nvim-ultisnips](https://github.com/quangnguyen30192/cmp-nvim-ultisnips) : nvim-cmp extension for ultisnips autocomplete
  * [ray-x/cmp-treesitter](https://github.com/ray-x/cmp-treesitter) : nvim-cmp extension for treesitter autocomplete
  * [rcarriga/cmp-dap](https://github.com/rcarriga/cmp-dap) : nvim-cmp extension for dap autocomplete
  * [roobert/tailwindcss-colorizer-cmp.nvim](https://github.com/roobert/tailwindcss-colorizer-cmp.nvim) : Add vs-code-stile TailwindCss color hints to nvim-cmp
  * [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip) : nvim-cmp extension for luasnip autocomplete
  * [tzachar/cmp-fuzzy-buffer](https://github.com/tzachar/cmp-fuzzy-buffer) : nvim-cmp source for fuzzy matched items from using the current buffer
  * [tzachar/cmp-fuzzy-path](https://github.com/tzachar/cmp-fuzzy-path) : nvim-cmp source for filesystem paths, employing `fd` and regular expressions to find files
  * [tzachar/cmp-tabnine](https://github.com/tzachar/cmp-tabnine) : nvim-cmp extension for tabline autocomplete
  * [uga-rosa/cmp-dictionary](https://github.com/uga-rosa/cmp-dictionary) : Dictionary completion source for nvim-cmp
  * [zbirenbaum/copilot-cmp](https://github.com/zbirenbaum/copilot-cmp) : nvim-cmp extension for copilot autocomplete
## buffers
  * [0x7a7a/bufpin.nvim](https://github.com/0x7a7a/bufpin.nvim) : pin buffers, or let them be sorted by most recently used
  * [axkirillov/hbac.nvim](https://github.com/axkirillov/hbac.nvim) : close unneeded buffers if to many
  * [caenrique/swap-buffers.nvim](https://github.com/caenrique/swap-buffers.nvim) : swap buffers easily between split windows without changing the window layout
  * [chrisgrieser/nvim-early-retirement](https://github.com/chrisgrieser/nvim-early-retirement) : close unneeded buffers after some time
  * [codcodog/simplebuffer.vim](https://github.com/codcodog/simplebuffer.vim) : switching and deleting buffers easily
  * [el-iot/buffer-tree](https://github.com/el-iot/buffer-tree) : rendering your buffer-list as an ascii-tree
  * [el-iot/buffer-tree-explorer](https://github.com/el-iot/buffer-tree-explorer) : exploring vim-buffers, rendered as an ascii-tree
  * [elihunter173/dirbuf.nvim](https://github.com/elihunter173/dirbuf.nvim) : directory buffer
  * [famiu/bufdelete.nvim](https://github.com/famiu/bufdelete.nvim) : allow you to delete a buffer without messing up your window layout
  * [ghillb/cybu.nvim](https://github.com/ghillb/cybu.nvim) : notification window, that shows the buffer in focus and its neighbors or list of buffers is ordered by last used
  * [j-morano/buffer_manager.nvim](https://github.com/j-morano/buffer_manager.nvim) : easily manage Neovim buffers
  * [kazhala/close-buffers.nvim](https://github.com/kazhala/close-buffers.nvim) : Lua port of asheq/close-buffers with several feature extensions
  * [kwkarlwang/bufjump.nvim](https://github.com/kwkarlwang/bufjump.nvim) : jump to previous buffer in jump list
  * [kwkarlwang/bufresize.nvim](https://github.com/kwkarlwang/bufresize.nvim) : keep your buffers width and height in proportion when the terminal window is resized
  * [matbme/jabs.nvim](https://github.com/matbme/jabs.nvim) : Just Another Buffer Switcher
  * [natdm/bswap](https://github.com/natdm/bswap) : easily rearrange or navigate buffers in split windows
  * [numtostr/bufonly.nvim](https://github.com/numtostr/bufonly.nvim) : Delete all the buffers except the current
  * [nyngwang/neononame.lua](https://github.com/nyngwang/neononame.lua) : Layout preserving buffer deletion in Lua
  * [sqve/bufignore.nvim](https://github.com/sqve/bufignore.nvim) : auto unlist specific buffers
  * [tklepzig/vim-buffer-navigator](https://github.com/tklepzig/vim-buffer-navigator) : Display buffers as tree in a separate window
## aligner
  * [godlygeek/tabular](https://github.com/godlygeek/tabular) : makek aligning text easy while also having complex setups
  * [junegunn/vim-easy-align](https://github.com/junegunn/vim-easy-align) : A simple, easy-to-use Vim alignment plugin
  * [rrethy/nvim-align](https://github.com/rrethy/nvim-align) : align text with a command using neovim
  * [tommcdo/vim-lion](https://github.com/tommcdo/vim-lion) : a tool for aligning text by some character
  * [vim-scripts/align](https://github.com/vim-scripts/align) : align statements on their equal signs, make comment boxes, align comments, align declarations, etc.
  * [vonr/align.nvim](https://github.com/vonr/align.nvim) : is a minimal plugin for NeoVim for aligning lines
## toggle
  * [andrewradev/switch.vim](https://github.com/andrewradev/switch.vim) : swich segments of text with predefined replacements
  * [ecthelionvi/neoswap.nvim](https://github.com/ecthelionvi/neoswap.nvim) : easily swap words
  * [nfrid/markdown-togglecheck](https://github.com/nfrid/markdown-togglecheck) : toggles task list check boxes in markdown
  * [nguyenvukhang/nvim-toggler](https://github.com/nguyenvukhang/nvim-toggler) : Invert text in vim, purely with lua
  * [rmagatti/alternate-toggler](https://github.com/rmagatti/alternate-toggler) : a very small plugin for toggling alternate "boolean" values
  * [saifulapm/chartoggle.nvim](https://github.com/saifulapm/chartoggle.nvim) : toggle keys end of line
  * [tpope/vim-speeddating](https://github.com/tpope/vim-speeddating) : make it possible to use `<C-a>` to increase dates
  * [wansmer/binary-swap.nvim](https://github.com/wansmer/binary-swap.nvim) : swap operands in binary expressions
  * [wansmer/sibling-swap.nvim](https://github.com/wansmer/sibling-swap.nvim) : swaps closest siblings with Tree-Sitter
  * [zef/vim-cycle](https://github.com/zef/vim-cycle) : toggle between pairs or lists of related words
## key
  * [aarondiel/spread.nvim](https://github.com/aarondiel/spread.nvim) : spread objects to multiple lines
  * [antonk52/markdowny.nvim](https://github.com/antonk52/markdowny.nvim) : markdown like keybindings
  * [anuvyklack/keymap-amend.nvim](https://github.com/anuvyklack/keymap-amend.nvim) : allows to amend the exisintg keybinding in Neovim
  * [anuvyklack/nvim-keymap-amend](https://github.com/anuvyklack/nvim-keymap-amend) : amend the exisintg keybinding in Neovim
  * [ap/vim-you-keep-using-that-word](https://github.com/ap/vim-you-keep-using-that-word) : When using word motion with the ccommand, it does not mean what Vim normally thinks it means and this solves that
  * [bennypowers/splitjoin.nvim](https://github.com/bennypowers/splitjoin.nvim) : Split-joint list like syntax constructs
  * [bkad/camelcasemotion](https://github.com/bkad/camelcasemotion) : make word motions respect camel case
  * [bronson/vim-visual-star-search](https://github.com/bronson/vim-visual-star-search) : allows you to select some text using Vim's visual mode, then hit * and # to search for it elsewhere in the file
  * [cassin01/wf.nvim](https://github.com/cassin01/wf.nvim) : a which-key like plugin
  * [chrisgrieser/nvim-recorder](https://github.com/chrisgrieser/nvim-recorder) : Simplifying and improving how you interact with macros
  * [chrisgrieser/nvim-spider](https://github.com/chrisgrieser/nvim-spider) : move by sub-word and ignore useless punctuation
  * [christoomey/vim-sort-motion](https://github.com/christoomey/vim-sort-motion) : provides the ability to sort in Vim using text objects and motions
  * [christoomey/vim-system-copy](https://github.com/christoomey/vim-system-copy) : copying / pasting text to the os specific clipboard
  * [conradirwin/vim-bracketed-paste](https://github.com/conradirwin/vim-bracketed-paste) : enables transparent pasting (i.e. no more `:set paste!`)
  * [declancm/cinnamon.nvim](https://github.com/declancm/cinnamon.nvim) : Smooth scrolling for ANY movement command
  * [drmikehenry/vim-fixkey](https://github.com/drmikehenry/vim-fixkey) : fixes key codes for console (terminal) Vim
  * [drzel/vim-split-line](https://github.com/drzel/vim-split-line) : easily split lines
  * [ecthelionvi/neocomposer.nvim](https://github.com/ecthelionvi/neocomposer.nvim) : makes macros easier
  * [egzvor/vimproviser](https://github.com/egzvor/vimproviser) : quick remapping of two of your most convenient keys to actions that are most important for you right now
  * [ervandew/supertab](https://github.com/ervandew/supertab) : allows you to use <Tab> for all your insert completion needs
  * [foosoft/vim-argwrap](https://github.com/foosoft/vim-argwrap) : an industrial strength argument wrapping and unwrapping extension
  * [gbprod/cutlass.nvim](https://github.com/gbprod/cutlass.nvim) : overrides the delete operations to actually just delete and not affect the current yank
  * [gbprod/stay-in-place.nvim](https://github.com/gbprod/stay-in-place.nvim) : Neovim plugin that prevent the cursor from moving when using shift and filter actions
  * [gukz/ftft.nvim](https://github.com/gukz/ftft.nvim) : same with as native f|t|F|T but with useful highlights
  * [guns/vim-sexp](https://github.com/guns/vim-sexp) : brings the Vim philosophy of precision editing to S-expressions
  * [gwatcha/reaper-keys](https://github.com/gwatcha/reaper-keys) : an extension for the REAPER DAW, that provides a new action mapping system based on key sequences instead of key chords
  * [hrsh7th/vim-eft](https://github.com/hrsh7th/vim-eft) : provides f/t/F/T mappings that can be customized by your setting
  * [hrsh7th/vim-seak](https://github.com/hrsh7th/vim-seak) : enhances the `/` and `?`
  * [hrsh7th/vim-searchx](https://github.com/hrsh7th/vim-searchx) : extend search motions
  * [inkarkat/vim-enhancedjumps](https://github.com/inkarkat/vim-enhancedjumps) : This plugin enhances the built-in `CTRL-I`/`CTRL-O` jump commands
  * [inkarkat/vim-mark](https://github.com/inkarkat/vim-mark) : adds mappings and a :Mark command to highlight several words in different colors simultaneously
  * [ironhouzi/starlite-nvim](https://github.com/ironhouzi/starlite-nvim) : Expedient and simple text highlighting using built in Neovim commands: `*`, `g*`, `#`, `g#`
  * [ironhouzi/vim-stim](https://github.com/ironhouzi/vim-stim) : aims to improve the built in star-command
  * [junegunn/vim-oblique](https://github.com/junegunn/vim-oblique) : Improved `/`-search for Vim
  * [junegunn/vim-peekaboo](https://github.com/junegunn/vim-peekaboo) : extends `"` and `@` in normal mode and `<CTRL-R>` in insert mode so you can see the contents of the registers
  * [junegunn/vim-slash](https://github.com/junegunn/vim-slash) : provides a set of mappings for enhancing in-buffer search experience
  * [kana/vim-repeat](https://github.com/kana/vim-repeat) : Enable to repeat last change by non built-in commands
  * [kylechui/nvim-surround](https://github.com/kylechui/nvim-surround) : Surround selections, stylishly
  * [lambdalisue/pinkyless.vim](https://github.com/lambdalisue/pinkyless.vim) : Rest your pinkies by using this plugin
  * [linty-org/key-menu.nvim](https://github.com/linty-org/key-menu.nvim) : which-key like plugin with a different style menu
  * [luchermitte/lh-brackets](https://github.com/luchermitte/lh-brackets) : provides various commands and functions to help design smart and advanced mappings dedicated to text insertion
  * [lyuts/vim-rtags](https://github.com/lyuts/vim-rtags) : Vim bindings for rtags
  * [marklcrns/vim-smartq](https://github.com/marklcrns/vim-smartq) : Master key for quitting vim buffers
  * [matze/vim-move](https://github.com/matze/vim-move) : Vim plugin that moves lines and selections in a more visual manner
  * [michamos/vim-bepo](https://github.com/michamos/vim-bepo) : une prise en charge de la disposition de clavier bépo (translate: integration bépo keyboard layout)
  * [nelstrom/vim-cutlass](https://github.com/nelstrom/vim-cutlass) : remove text without overwriting the default register
  * [nexmean/caskey.nvim](https://github.com/nexmean/caskey.nvim) : Declarative cascade key mappings configuration
  * [nvimdev/dyninput.nvim](https://github.com/nvimdev/dyninput.nvim) : auto change input depending on context
  * [ojroques/vim-oscyank](https://github.com/ojroques/vim-oscyank) : A plugin to copy text to the system clipboard from anywhere using the ANSI OSC52 sequence
  * [osyo-manga/vim-jplus](https://github.com/osyo-manga/vim-jplus) : Join lines inserting characters in between
  * [peterrincker/vim-argumentative](https://github.com/peterrincker/vim-argumentative) : aids with manipulating and moving between function arguments
  * [preservim/vim-wordchipper](https://github.com/preservim/vim-wordchipper) : improve text shredding in insert mode
  * [rhysd/accelerated-jk](https://github.com/rhysd/accelerated-jk) : accelerates j/k mappings' steps while j or k key is repeating
  * [rhysd/vim-operator-surround](https://github.com/rhysd/vim-operator-surround) : provides Vim operator mappings to deal with surrounds
  * [rrethy/vim-lacklustertab](https://github.com/rrethy/vim-lacklustertab) : Like supertab but not as super
  * [rutatang/compter.nvim](https://github.com/rutatang/compter.nvim) : customize ctrl-a and ctrl-x
  * [ryvnf/readline.vim](https://github.com/ryvnf/readline.vim) : a library used for implementing line editing across many command-line tools
  * [sickill/vim-pasta](https://github.com/sickill/vim-pasta) : improve indentation of pasting
  * [stsewd/gx-extended.vim](https://github.com/stsewd/gx-extended.vim) : Extend `gx` to use it beyond just URLs
  * [svermeulen/vim-cutlass](https://github.com/svermeulen/vim-cutlass) : overrides the delete operations to actually just delete and not affect the current yank
  * [svermeulen/vim-easyclip](https://github.com/svermeulen/vim-easyclip) : a plugin for Vim which contains a collection of clipboard related functionality [no development]
  * [takac/vim-hardtime](https://github.com/takac/vim-hardtime) : helps you break that annoying habit vimmers have of scrolling up and down the page using `jjjjj` and `kkkkk`
  * [terryma/vim-expand-region](https://github.com/terryma/vim-expand-region) : allows you to visually select increasingly larger regions of text using the same key combination
  * [thyrum/vim-stabs](https://github.com/thyrum/vim-stabs) : This script allows you to use your normal tab settings for the beginning of the line, and have tabs expanded as spaces anywhere else
  * [tommcdo/vim-express](https://github.com/tommcdo/vim-express) : Define your own operators that apply either a VimL expression or a substitution to any motion or text object
  * [tpope/vim-capslock](https://github.com/tpope/vim-capslock) : toggle temporary caps lock
  * [tpope/vim-sexp-mappings-for-regular-people](https://github.com/tpope/vim-sexp-mappings-for-regular-people) : adds better default mappings to [guns/vim-sexp](https://github.com/guns/vim-sexp)
  * [tpope/vim-unimpaired](https://github.com/tpope/vim-unimpaired) : adds complementary pairs of mappings (like `:bnext`/`bprevious`)
  * [triglav/vim-visual-increment](https://github.com/triglav/vim-visual-increment) : adds the ability to do increasing and decreasing  ofnumber or letter sequences on multiple lines via visual mode
  * [ur4ltz/surround.nvim](https://github.com/ur4ltz/surround.nvim) : surround text using sandwich or surround style
  * [vim-scripts/improved-paragraph-motion](https://github.com/vim-scripts/improved-paragraph-motion) : A simple utility improve the "}" and "{" motion in normal and visual mode
  * [vim-scripts/replacewithregister](https://github.com/vim-scripts/replacewithregister) : replace wanted wth registers content
  * [wansmer/langmapper.nvim](https://github.com/wansmer/langmapper.nvim) : make better for non English input methods
  * [wansmer/treesj](https://github.com/wansmer/treesj) : for splitting/joining blocks of code like arrays, hashes, statements, objects, dictionaries, etc
  * [waylonwalker/telegraph.nvim](https://github.com/waylonwalker/telegraph.nvim) : provides a way to send command conveniently and bind them to hotkeys
  * [weissle/easy-action](https://github.com/weissle/easy-action) : execute an action, such as yank and delete, but keeps your cursor position
  * [wsdjeg/vim-fetch](https://github.com/wsdjeg/vim-fetch) : process line and column jump specifications in file paths as found in stack traces and similar output
  * [xiyaowong/accelerated-jk.nvim](https://github.com/xiyaowong/accelerated-jk.nvim) : lua rewrite of [rhysd/accelerated-jk](https://github.com/rhysd/accelerated-jk)
  * [yuki-yano/zero.nvim](https://github.com/yuki-yano/zero.nvim) : toggles between ^ and 0 in normal mode
  * [yuttie/comfortable-motion.vim](https://github.com/yuttie/comfortable-motion.vim) : physics-based smooth scrolling
  * [zdcthomas/yop.nvim](https://github.com/zdcthomas/yop.nvim) : easily make operators
  * [zegervdv/nrpattern.nvim](https://github.com/zegervdv/nrpattern.nvim) : Neovim plugin to expand the number formats supported to increment or decrement
## auto-pairs
  * [altermo/ultimate-autopair.nvim](https://github.com/altermo/ultimate-autopair.nvim) : Aims to have all the auto-pairing fetures
  * [andrewradev/tagalong.vim](https://github.com/andrewradev/tagalong.vim) : automatically rename closing html/xml tags
  * [cohama/lexima.vim](https://github.com/cohama/lexima.vim) : Auto close parentheses and repeat by dot dot dot
  * [eluum/vim-autopair](https://github.com/eluum/vim-autopair) : very simple vim plugin for autocompleting the paired characters
  * [eraserhd/parinfer-rust](https://github.com/eraserhd/parinfer-rust) : lisp auto-pairs written in rust
  * [hrsh7th/nvim-insx](https://github.com/hrsh7th/nvim-insx) : Flexible insert-mode key mapping manager
  * [jiangmiao/auto-pairs](https://github.com/jiangmiao/auto-pairs) : Insert or delete brackets, parens, quotes in pair
  * [kana/vim-smartinput](https://github.com/kana/vim-smartinput) : Provide smart input assistant
  * [lunarwatcher/auto-pairs](https://github.com/lunarwatcher/auto-pairs) : a simple auto-pairing plugin
  * [m4xshen/autoclose.nvim](https://github.com/m4xshen/autoclose.nvim) : minimalist autoclose plugin
  * [raimondi/delimitmate](https://github.com/raimondi/delimitmate) : automatic closing of quotes, parenthesis, brackets, etc
  * [rrethy/nvim-treesitter-endwise](https://github.com/rrethy/nvim-treesitter-endwise) : wisely add "end" in ruby, Lua, Vimscript, etc
  * [rrethy/vim-impiared](https://github.com/rrethy/vim-impiared) : a pair plugin
  * [rstacruz/vim-closer](https://github.com/rstacruz/vim-closer) : Closes brackets
  * [shougo/neopairs.vim](https://github.com/shougo/neopairs.vim) : Auto insert pairs when complete done
  * [tenfyzhong/completeparameter.vim](https://github.com/tenfyzhong/completeparameter.vim) : complete function's parameters after complete a function
  * [tmsvg/pear-tree](https://github.com/tmsvg/pear-tree) : A painless, powerful Vim auto-pair plugin
  * [townk/vim-autoclose](https://github.com/townk/vim-autoclose) : auto complete parentheses [archived]
  * [vim-scripts/delimitmate.vim](https://github.com/vim-scripts/delimitmate.vim) : automatic closing of quotes, parenthesis, brackets
  * [windwp/nvim-ts-closetag](https://github.com/windwp/nvim-ts-closetag) : Use treesitter to autoclose and autorename html tag
  * [zsaberlv0/completeparameter_generic.vim](https://github.com/zsaberlv0/completeparameter_generic.vim) : generic verion of CompleteParameter.vim
## other
  * [00sapo/visual.nvim](https://github.com/00sapo/visual.nvim) : kak like keymaps
  * [0oastro/silicon.lua](https://github.com/0oastro/silicon.lua) : generate beautiful images of code using silicon
  * [0x5a4/oogway.nvim](https://github.com/0x5a4/oogway.nvim) : get wisdom from Oogway
  * [907th/vim-auto-save](https://github.com/907th/vim-auto-save) : automatically saves changes to disk without having to use `:w` [no maintain]
  * [9seconds/repolink.nvim](https://github.com/9seconds/repolink.nvim) : quickly share repo files/line ranges
  * [aasim-a/scrolleof.nvim](https://github.com/aasim-a/scrolleof.nvim) : make scrollof go past end of line
  * [abstract-ide/penvim](https://github.com/abstract-ide/penvim) : project's root directory and documents indentation detector
  * [acksld/nvim-pytrize.lua](https://github.com/acksld/nvim-pytrize.lua) : Helps navigating `pytest.mark.parametrizeentries`
  * [acksld/swenv.nvim](https://github.com/acksld/swenv.nvim) : quickly switch python virtual environments from within neovim
  * [alfredodeza/coveragepy.vim](https://github.com/alfredodeza/coveragepy.vim) : help integrate Ned Batchelder's excellent coverage.py tool
  * [amopel/vim-log-print](https://github.com/amopel/vim-log-print) : Like a commenter plugin, but for log/print statements
  * [andrewradev/linediff.vim](https://github.com/andrewradev/linediff.vim) : provides a simple command, `:Linediff`,which is used to diff two separate blocks of text
  * [andrewradev/sideways.vim](https://github.com/andrewradev/sideways.vim) : move the item under the cursor left or right
  * [andweeb/presence.nvim](https://github.com/andweeb/presence.nvim) : Discord Rich Presence plugin for Neovim
  * [andythigpen/nvim-coverage](https://github.com/andythigpen/nvim-coverage) : Displays coverage information in the sign column or in a pop-up window
  * [antoinemadec/fixcursorhold.nvim](https://github.com/antoinemadec/fixcursorhold.nvim) : fix neovim CursorHold and CursorHoldI AND decouple updatetime from CursorHold and CursorHoldI
  * [antonk52/bad-practices.nvim](https://github.com/antonk52/bad-practices.nvim) : plugin to help you break bad practices
  * [anuvyklack/help-vsplit.nvim](https://github.com/anuvyklack/help-vsplit.nvim) : open the help screen smartly
  * [ap/vim-templates](https://github.com/ap/vim-templates) : This is a Vim plugin for providing filetype-dependent templates for new files, using a simple but effective mechanism
  * [arp242/batchy.vim](https://github.com/arp242/batchy.vim) : perform batch operations on files
  * [arsham/arshamiser.nvim](https://github.com/arsham/arshamiser.nvim) : status bar, colour scheme, foldtext and tabline
  * [arthurxavierx/vim-caser](https://github.com/arthurxavierx/vim-caser) : Easily change word casing with motions, text objects or visual mode
  * [asins/vim-dict](https://github.com/asins/vim-dict) : VIM dictionary repository
  * [askfiy/nvim-picgo](https://github.com/askfiy/nvim-picgo) : a picture uploading tool based on Lua language
  * [asvetliakov/vscode-neovim](https://github.com/asvetliakov/vscode-neovim) : VSCode Neovim Integration
  * [axieax/urlview.nvim](https://github.com/axieax/urlview.nvim) : a Neovim plugin which displays links from a variety of contexts
  * [babab/vim-magickey](https://github.com/babab/vim-magickey) : preform magic actions (like updating license date)
  * [beeender/comrade](https://github.com/beeender/comrade) : Brings JetBrains/IntelliJ IDEs magic to Neovim with minimal setup
  * [bekaboo/dropbar.nvim](https://github.com/bekaboo/dropbar.nvim) : A polished winbar
  * [beloglazov/vim-online-thesaurus](https://github.com/beloglazov/vim-online-thesaurus) : look up words in an online thesaurus
  * [bfredl/nvim-ipy](https://github.com/bfredl/nvim-ipy) : Jupyter front-end for Neovim
  * [booperlv/cyclecolo.lua](https://github.com/booperlv/cyclecolo.lua) : floating colorscheme selector for neovim
  * [bounceme/remote-viewer](https://github.com/bounceme/remote-viewer) : vim-dirvish && (cURL || ssh)
  * [brendalf/mix.nvim](https://github.com/brendalf/mix.nvim) : A Mix (Elixir) wrapper for Neovim
  * [brenopacheco/vim-hydra](https://github.com/brenopacheco/vim-hydra) : allows you to create hydras similar to abo-abo's Emacs plugin
  * [brglng/vim-im-select](https://github.com/brglng/vim-im-select) : Improve Vim/Neovim experience with input methods
  * [brookhong/cscope.vim](https://github.com/brookhong/cscope.vim) : smart cscope helper for vim
  * [cappyzawa/trim.nvim](https://github.com/cappyzawa/trim.nvim) : trailing whitespace and lines
  * [cdelledonne/vim-cmake](https://github.com/cdelledonne/vim-cmake) : building CMake projects inside of vim, with a nice visual feedback
  * [chimay/wheel](https://github.com/chimay/wheel) : file group manager, navigation and refactoring in one
  * [chrisbra/nrrwrgn](https://github.com/chrisbra/nrrwrgn) : focus on a selected region while making the rest inaccessible
  * [chrisbra/unicode.vim](https://github.com/chrisbra/unicode.vim) : handling unicode and digraphs characters
  * [ckolkey/ts-node-action](https://github.com/ckolkey/ts-node-action) : framework for running function on tsnodes
  * [clojure-vim/acid.nvim](https://github.com/clojure-vim/acid.nvim) : clojure development
  * [clojure-vim/jazz.nvim](https://github.com/clojure-vim/jazz.nvim) : Acid + Impromptu = Jazz
  * [cometsong/commentframe.vim](https://github.com/cometsong/commentframe.vim) : generate fancy-looking comments/section dividers with centered titles and append them at the current cursor position
  * [cpea2506/relative-toggle.nvim](https://github.com/cpea2506/relative-toggle.nvim) : automatically toggle between relative and absolute line number
  * [dahu/vimple](https://github.com/dahu/vimple) : provides a few maps and commands to make the casual vimmer’s life a little easier
  * [danielo515/haxe-nvim](https://github.com/danielo515/haxe-nvim) : write neovim scripts in haxe
  * [danymat/neogen](https://github.com/danymat/neogen) : Your Annotation Toolkit
  * [davidgranstrom/osc.nvim](https://github.com/davidgranstrom/osc.nvim) : Open Sound Control (OSC) library for Neovim
  * [davidgranstrom/scnvim](https://github.com/davidgranstrom/scnvim) : Neovim frontend for SuperCollider
  * [derekwyatt/vim-scala](https://github.com/derekwyatt/vim-scala) : This is a "bundle" for Vim that builds off of the initial Scala plugin
  * [desdic/greyjoy.nvim](https://github.com/desdic/greyjoy.nvim) : a pluggable pattern/file based launcher
  * [dhananjaylatkar/cscope_maps.nvim](https://github.com/dhananjaylatkar/cscope_maps.nvim) : reimplements removed cscope in neovim
  * [dhruvasagar/vim-table-mode](https://github.com/dhruvasagar/vim-table-mode) : awesome automatic table creator & formatter
  * [doctorfree/nvim-lazyman](https://github.com/doctorfree/nvim-lazyman) : manage multiple configurations
  * [dosimple/workspace.vim](https://github.com/dosimple/workspace.vim) : make it easier to manage large number of buffers by keeping them grouped separately in workspaces
  * [dpzmick/neovim-hackernews](https://github.com/dpzmick/neovim-hackernews) : Hacker News in neovim
  * [dradtke/vim-dap](https://github.com/dradtke/vim-dap) : integrating with the Debug Adapter Protocol
  * [dstein64/vim-startuptime](https://github.com/dstein64/vim-startuptime) : viewing vim and nvimstartup event timing information
  * [duggiefresh/vim-easydir](https://github.com/duggiefresh/vim-easydir) : simple way to create, edit and save files and directories
  * [echasnovski/mini.nvim](https://github.com/echasnovski/mini.nvim) : Collection of minimal, independent, and fast Lua modules dedicated to improve Neovim experience
  * [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim) : This is an EditorConfig plugin for Vim
  * [ekickx/clipboard-image.nvim](https://github.com/ekickx/clipboard-image.nvim) : copy images and paste url/path
  * [ellisonleao/nvim-plugin-template](https://github.com/ellisonleao/nvim-plugin-template) : A template repository for Neovim plugins
  * [equilibris/nx.nvim](https://github.com/equilibris/nx.nvim) : nx for neovim
  * [esensar/nvim-dev-container](https://github.com/esensar/nvim-dev-container) : provide functionality similar to VSCode's remote container development plugin
  * [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace) : Intelligently reopen files at your last edit position
  * [ferrine/md-img-paste.vim](https://github.com/ferrine/md-img-paste.vim) : paste images into markdown
  * [fhill2/floating.nvim](https://github.com/fhill2/floating.nvim) : floating windows! [archived]
  * [filipdutescu/renamer.nvim](https://github.com/filipdutescu/renamer.nvim) : Visual-Studio-Code-like renaming UI
  * [folke/neoconf.nvim](https://github.com/folke/neoconf.nvim) : manage global/local configs
  * [fredeeb/alias.nvim](https://github.com/fredeeb/alias.nvim) : make terminal execute nvim functions
  * [fsharpasharp/vim-dirvinist](https://github.com/fsharpasharp/vim-dirvinist) : List all files defined by your projections with the Dirvish plugin
  * [furkanzmc/firvish.nvim](https://github.com/furkanzmc/firvish.nvim) : a buffer centric job control plug-in
  * [gaborvecsei/cryptoprice.nvim](https://github.com/gaborvecsei/cryptoprice.nvim) : There are a million ways to check the price of your favourite coins, let nvim be one of them
  * [gennaro-tedesco/nvim-jqx](https://github.com/gennaro-tedesco/nvim-jqx) : Populate the quickfix with json entries
  * [gioele/vim-autoswap](https://github.com/gioele/vim-autoswap) : auto handle swap file messages
  * [glacambre/firenvim](https://github.com/glacambre/firenvim) : Turn your browser¹ into a Neovim client
  * [google/executor.nvim](https://github.com/google/executor.nvim) : run command line task in the background
  * [gorbit99/codewindow.nvim](https://github.com/gorbit99/codewindow.nvim) : a minimap plugin for neovim
  * [gpanders/editorconfig.nvim](https://github.com/gpanders/editorconfig.nvim) : EditorConfig plugin for Neovim written in (NOT Lua) Fennel
  * [h-hg/fcitx.nvim](https://github.com/h-hg/fcitx.nvim) : switch and restore fcitx state for each buffer
  * [habamax/vim-evalvim](https://github.com/habamax/vim-evalvim) : Run vimscript from anywhere in vim and save output to `*` (clipboard) register
  * [haifengkao/insertleftbracket.nvim](https://github.com/haifengkao/insertleftbracket.nvim) : offers objective-c square bracket completion
  * [hardenedapple/vsh](https://github.com/hardenedapple/vsh) : Run shell commands in a modifiable buffer
  * [heavenshell/vim-pydocstring](https://github.com/heavenshell/vim-pydocstring) : a generator for Python docstrings and is capable of automatically
  * [henriquehbr/nvim-startup.lua](https://github.com/henriquehbr/nvim-startup.lua) : Displays neovim startup time [archived]
  * [hkupty/impromptu.nvim](https://github.com/hkupty/impromptu.nvim) : quickly create prompts
  * [hkupty/iron.nvim](https://github.com/hkupty/iron.nvim) : Interactive Repls Over Neovim
  * [hoschi/yode-nvim](https://github.com/hoschi/yode-nvim) : Yode plugin for NeoVim
  * [hrsh7th/vim-candle](https://github.com/hrsh7th/vim-candle) : Any candidates listing engine for vim/nvim built on yaegi
  * [groctel/jobsplit.nvim](https://gitlab.com/groctel/jobsplit.nvim) : Open your jobs in an asynchronous horizontal split
  * [huawenyu/vimgdb](https://github.com/huawenyu/vimgdb) : implement GDB front-end for c/c++ gdb base on Neovim + Tmux
  * [hupfdule/refactorvim](https://github.com/hupfdule/refactorvim) : Vim plugin for refactoring vimscript plugins
  * [hyiltiz/vim-plugins-profile](https://github.com/hyiltiz/vim-plugins-profile) : a profiler for your vim plugins
  * [idanarye/nvim-channelot](https://github.com/idanarye/nvim-channelot) : operate jobs from lua coroutine
  * [idanarye/nvim-moonicipal](https://github.com/idanarye/nvim-moonicipal) : a task runner
  * [iron-e/vim-libmodal](https://github.com/iron-e/vim-libmodal) : aimed at simplifying the creation of new "modes"
  * [iron-e/vim-tabmode](https://github.com/iron-e/vim-tabmode) : provides a new mode in vim for managing tabs
  * [jakemason/ouroboros](https://github.com/jakemason/ouroboros) : Neovim plugin that makes switching between header & implementation files in C/C++ quick and painless
  * [jakergrossman/tagurl.vim](https://github.com/jakergrossman/tagurl.vim) : Copy the URL for a help tag on vimhelp.org or neovim.io to the clipboard
  * [jalvesaq/vimcmdline](https://github.com/jalvesaq/vimcmdline) : Send lines to interpreter
  * [jameshiew/nvim-magic](https://github.com/jameshiew/nvim-magic) : pluggable framework for integrating AI code assistance into Neovim
  * [jayp0521/mason-null-ls.nvim](https://github.com/jayp0521/mason-null-ls.nvim) : bridges mason.nvim with the null-ls plugin
  * [jayp0521/mason-nvim-dap.nvim](https://github.com/jayp0521/mason-nvim-dap.nvim) : bridges mason.nvim with the nvim-dap plugin
  * [jbyuki/venn.nvim](https://github.com/jbyuki/venn.nvim) : Draw ASCII diagrams in Neovim
  * [jcdickinson/http.nvim](https://github.com/jcdickinson/http.nvim) : HTTP client
  * [jdonaldson/vaxe](https://github.com/jdonaldson/vaxe) : vim bundle for Haxe and Hss
  * [jedrzejboczar/toggletasks.nvim](https://github.com/jedrzejboczar/toggletasks.nvim) : JSON/YAML + toggleterm.nvim + telescope.nvim
  * [jeffkreeftmeijer/vim-numbertoggle](https://github.com/jeffkreeftmeijer/vim-numbertoggle) : switch to absolute line number automatically when relative numbers don't make sense
  * [jenterkin/vim-autosource](https://github.com/jenterkin/vim-autosource) : enables per project configuration by finding each Vim configuration file from your $HOME directory to the opened file
  * [jghauser/kitty-runner.nvim](https://github.com/jghauser/kitty-runner.nvim) : easily send lines from the current buffer to another kitty terminal
  * [jghauser/mkdir.nvim](https://github.com/jghauser/mkdir.nvim) : automatically creates missing directories on saving a file
  * [jghauser/papis.nvim](https://github.com/jghauser/papis.nvim) : companion plugin for the bibliography manager papis
  * [jmcantrell/vim-virtualenv](https://github.com/jmcantrell/vim-virtualenv) : make it possible to run `:python` with virtual environments
  * [jmcomets/vim-pony](https://github.com/jmcomets/vim-pony) : working with Django projects in Vim
  * [johmsalas/text-case.nvim](https://github.com/johmsalas/text-case.nvim) : An all in one plugin for converting text case in Neovim
  * [jrasmusbm/vim-peculiar](https://github.com/jrasmusbm/vim-peculiar) : provide shortcuts when working with the `:norm` command
  * [julian/lean.nvim](https://github.com/julian/lean.nvim) : support for the Lean Theorem Prover
  * [julienr/vim-cellmode](https://github.com/julienr/vim-cellmode) : enables MATLAB-style cell mode execution for python scripts in vim, assuming an ipython interpreter running in screen (or tmux)
  * [junegunn/vim-carbon-now-sh](https://github.com/junegunn/vim-carbon-now-sh) : open selected content in carbon.now.sh
  * [junegunn/vim-emoji](https://github.com/junegunn/vim-emoji) : Emoji in Vim
  * [junegunn/vim-pseudocl](https://github.com/junegunn/vim-pseudocl) : implements a command-line interface that mimics the native Vim command-line
  * [justinhj/battery.nvim](https://github.com/justinhj/battery.nvim) : get battery power level in nvim
  * [justinmk/vim-gtfo](https://github.com/justinmk/vim-gtfo) : Opens the file manager or terminal at the directory of the current file
  * [kabbamine/gulp-vim](https://github.com/kabbamine/gulp-vim) : a simple gulp wrapper for vim
  * [kana/vim-operator-user](https://github.com/kana/vim-operator-user) : Define your own operator easily
  * [kdheepak/panvimdoc](https://github.com/kdheepak/panvimdoc) : Decrease friction when writing documentation for your plugins
  * [keaising/im-select.nvim](https://github.com/keaising/im-select.nvim) : Switch Input Method automatically depends on Neovim's edit mode
  * [kevinhwang91/promise-async](https://github.com/kevinhwang91/promise-async) : port Promise & Async from JavaScript to Lua
  * [kezhenxu94/vim-mysql-plugin](https://github.com/kezhenxu94/vim-mysql-plugin) : A highly customizable MySQL VIM plugin
  * [killthemule/nvimpam](https://github.com/killthemule/nvimpam) : neovim rpc plugin for pamcrash files
  * [kiran94/edit-markdown-table.nvim](https://github.com/kiran94/edit-markdown-table.nvim) : updates markdown tables depending on context
  * [kiran94/maim.nvim](https://github.com/kiran94/maim.nvim) : take screenshot from neovim using maim
  * [kiran94/s3edit.nvim](https://github.com/kiran94/s3edit.nvim) : Edit files from S3 directly from Neovim
  * [kkharji/sqlite.lua](https://github.com/kkharji/sqlite.lua) : SQLite/LuaJIT binding and a highly opinionated wrapper for storing, retrieving, caching, and persisting SQLite databases
  * [klen/nvim-config-local](https://github.com/klen/nvim-config-local) : Secure load local config files
  * [klen/nvim-test](https://github.com/klen/nvim-test) : Test Runner for neovim
  * [kristijanhusak/vim-carbon-now-sh](https://github.com/kristijanhusak/vim-carbon-now-sh) : vim implementation plugin for opening selected content in https://carbon.now.sh
  * [kristijanhusak/vim-dadbod-ui](https://github.com/kristijanhusak/vim-dadbod-ui) : Simple UI for vim-dadbod
  * [lambdalisue/lista.nvim](https://github.com/lambdalisue/lista.nvim) : filter content lines and jump to where you want
  * [lambdalisue/neovim-prompt](https://github.com/lambdalisue/neovim-prompt) : A customizable command-line prompt module for Neovim/Vim
  * [lambdalisue/suda.vim](https://github.com/lambdalisue/suda.vim) : a plugin to read or write files with sudo command
  * [lewis6991/hover.nvim](https://github.com/lewis6991/hover.nvim) : framework for context aware hover providers
  * [lfilho/cosco.vim](https://github.com/lfilho/cosco.vim) : Comma and semi-colon insertion bliss for vim
  * [lhkipp/nvim-locationist](https://github.com/lhkipp/nvim-locationist) : Add your current cursor location to the quickfix list, location list or to the clipboard
  * [lilydjwg/fcitx.vim](https://github.com/lilydjwg/fcitx.vim) : Keep and restore fcitx state for each buffer separately when leaving/re-entering insert mode or search mode
  * [luchermitte/vimfold4c](https://github.com/luchermitte/vimfold4c) : Reactive vim fold plugin for C & C++
  * [m-demare/attempt.nvim](https://github.com/m-demare/attempt.nvim) : Manage your temporary buffers
  * [m00qek/plugin-template.nvim](https://github.com/m00qek/plugin-template.nvim) : A template to create Neovim plugins written in Lua
  * [m4xshen/hardtime.nvim](https://github.com/m4xshen/hardtime.nvim) : helpe you establish good command habits
  * [macthecadillac/vimdo](https://github.com/macthecadillac/vimdo) : execute external commands asynchronously
  * [marchamamji/runner.nvim](https://github.com/marchamamji/runner.nvim) : run code inside neovim
  * [marcweber/vim-addon-mw-utils](https://github.com/marcweber/vim-addon-mw-utils) : various utils such as caching interpreted contents of files or advanced glob like things
  * [massolari/forem.nvim](https://github.com/massolari/forem.nvim) : integrates Neovim with Forem platforms
  * [mattn/webapi-vim](https://github.com/mattn/webapi-vim) : Interface to web API
  * [max397574/dyn_help.nvim](https://github.com/max397574/dyn_help.nvim) : display help in float window
  * [max397574/healthy.nvim](https://github.com/max397574/healthy.nvim) : stay healthy, even while coding
  * [max397574/neovim-lua-plugin-template](https://github.com/max397574/neovim-lua-plugin-template) : a plugin template
  * [max397574/selection_popup.nvim](https://github.com/max397574/selection_popup.nvim) : the neorg popup in separate file
  * [mcauley-penney/tidy.nvim](https://github.com/mcauley-penney/tidy.nvim) : An autocommand that removes all trailing spaces/empty lines
  * [md-img-paste-devs/md-img-paste.vim](https://github.com/md-img-paste-devs/md-img-paste.vim) : Yet simple tool to paste images into markdown files
  * [meznaric/conmenu](https://github.com/meznaric/conmenu) : Powerful but minimal context menu for neovim
  * [mg979/tasks.vim](https://github.com/mg979/tasks.vim) : manage and run global and project-local tasks
  * [mg979/vim-visual-multi](https://github.com/mg979/vim-visual-multi) : create multiple visual regions and edit them (basically multiple cursor)
  * [mhinz/vim-rfc](https://github.com/mhinz/vim-rfc) : lists all existing RFCs and opens the selected one in a new buffer
  * [michaelb/do-nothing.vim](https://github.com/michaelb/do-nothing.vim) : this does nothing
  * [michaelb/sniprun](https://github.com/michaelb/sniprun) : code runner plugin for neovim written in rust and lua
  * [mickael-menu/shadowvim](https://github.com/mickael-menu/shadowvim) : Neovim inside Xcode
  * [milisims/nvim-luaref](https://github.com/milisims/nvim-luaref) : This 'plugin' simply adds a reference for builtin lua functions
  * [misanthropicbit/decipher.nvim](https://github.com/misanthropicbit/decipher.nvim) : cipher text with codex
  * [miversen33/import.nvim](https://github.com/miversen33/import.nvim) : A safe require replacement with niceties
  * [miversen33/netman.nvim](https://github.com/miversen33/netman.nvim) : Network Resource Manager
  * [mordechaihadad/bob](https://github.com/mordechaihadad/bob) : easy way to install and switch versions of nvim
  * [mrcjkb/haskell-snippets.nvim](https://github.com/mrcjkb/haskell-snippets.nvim) : collection of haskell snippets
  * [muniftanjim/exrc.nvim](https://github.com/muniftanjim/exrc.nvim) : Local config file with confirmation for Neovim [archived]
  * [mvaldes14/terraform.nvim](https://github.com/mvaldes14/terraform.nvim) : see the stat of terraform manifest objects
  * [nanotee/luv-vimdocs](https://github.com/nanotee/luv-vimdocs) : The luv docs in vimdoc format
  * [nanotee/nvim-if-lua-compat](https://github.com/nanotee/nvim-if-lua-compat) : An `if_lua` compatibility layer for Neovim
  * [nanotee/nvim-lua-guide](https://github.com/nanotee/nvim-lua-guide) : Getting started using Lua in Neovim, use this guide
  * [nanotee/zoxide.vim](https://github.com/nanotee/zoxide.vim) : Vim wrapper for zoxide
  * [ncm2/float-preview.nvim](https://github.com/ncm2/float-preview.nvim) : Completion preview window based on neovim's floating window
  * [neovim/node-client](https://github.com/neovim/node-client) : node client for neovim
  * [nfrid/treesitter-utils](https://github.com/nfrid/treesitter-utils) : some ts based utils
  * [niuiic/cp-image.nvim](https://github.com/niuiic/cp-image.nvim) : pase images path without problem
  * [nkakouros-original/numbers.nvim](https://github.com/nkakouros-original/numbers.nvim) : Disables relative line numbers when they don't make sense, e.g. when entering insert mode
  * [noahfrederick/vim-composer](https://github.com/noahfrederick/vim-composer) : Vim support for Composer PHP projects
  * [norcalli/nvim_utils](https://github.com/norcalli/nvim_utils) : utils to make it easier to convert from vim to lua
  * [noscript/taberian.vim](https://github.com/noscript/taberian.vim) : Clickable tabs per VIM window
  * [notomo/cmdbuf.nvim](https://github.com/notomo/cmdbuf.nvim) : provides command-line window functions by normal buffer and window
  * [ntbbloodbath/cheovim](https://github.com/ntbbloodbath/cheovim) : Neovim configuration switcher written in Lua
  * [ntbbloodbath/nvenv](https://github.com/ntbbloodbath/nvenv) : lightweight and blazing fast Neovim version manager
  * [ntbbloodbath/rest.nvim](https://github.com/ntbbloodbath/rest.nvim) : fast Neovim http client written in Lua
  * [nvim-lsp/try.nvim](https://github.com/nvim-lsp/try.nvim) : repository that contains various example self-contained neovim containers
  * [nvim-lua/neovim-ui](https://github.com/nvim-lua/neovim-ui) : a semi-official prototype for what will become neovim's new UI module
  * [nvim-lua/popup.nvim](https://github.com/nvim-lua/popup.nvim) : An implementation of the Popup API from vim in Neovim
  * [nvim-neorocks/luarocks-tag-release](https://github.com/nvim-neorocks/luarocks-tag-release) : auto releas to luarock
  * [nvim-treesitter/module-template](https://github.com/nvim-treesitter/module-template) : repository template to create you own nvim-treesitter module
  * [nvim-treesitter/nvim-tree-docs](https://github.com/nvim-treesitter/nvim-tree-docs) : Highly configurable documentation generator using treesitter
  * [nvimdev/template.nvim](https://github.com/nvimdev/template.nvim) : a plugin template
  * [nyngwang/neozoom.lua](https://github.com/nyngwang/neozoom.lua) : TL;DR: Using floating window instead of vim-tab to simulate "zoom-in"
  * [ofirgall/open.nvim](https://github.com/ofirgall/open.nvim) : Open the current word (or other text) with custom openers
  * [osyo-manga/vim-over](https://github.com/osyo-manga/vim-over) : preview command line window
  * [paulocesar/neovim-db](https://github.com/paulocesar/neovim-db) : Database plugin for neovim
  * [petobens/poet-v](https://github.com/petobens/poet-v) : detects and activates virtual environments in your python poetry or pipenv project
  * [pianocomposer321/project-templates.nvim](https://github.com/pianocomposer321/project-templates.nvim) : create project templates
  * [pixelneo/vim-python-docstring](https://github.com/pixelneo/vim-python-docstring) : easily create python docstring
  * [pocco81/autosave.nvim](https://github.com/pocco81/autosave.nvim) : saving your work before the world collapses or you type :qa!
  * [prabirshrestha/quickpick.vim](https://github.com/prabirshrestha/quickpick.vim) : A UI for Vim to let the user pick an item from a list similar to CtrlP
  * [preservim/vim-pencil](https://github.com/preservim/vim-pencil) : Rethinking Vim as a tool for writers
  * [prettier/vim-prettier](https://github.com/prettier/vim-prettier) : wrapper for prettier, pre-configured with custom default prettier settings
  * [qpkorr/vim-renamer](https://github.com/qpkorr/vim-renamer) : Show a list of file names in a directory, rename then in the vim buffer using vim editing commands, then have vim rename them on disk
  * [raghur/vim-ghost](https://github.com/raghur/vim-ghost) : Edit browser textarea content in Vim
  * [ray-x/web-tools.nvim](https://github.com/ray-x/web-tools.nvim) : Neovim Wrapper for heart browser-sync
  * [rbong/vim-buffest](https://github.com/rbong/vim-buffest) : Easily edit vim registers/macros and lists as buffers
  * [rbtnn/vim-ambiwidth](https://github.com/rbtnn/vim-ambiwidth) : auto set `'ambiwidth'` (i guess, the doc is in Japanese)
  * [rbtnn/vim-gloaded](https://github.com/rbtnn/vim-gloaded) : disable default vim plugins
  * [rbtnn/vim-vimscript_lasterror](https://github.com/rbtnn/vim-vimscript_lasterror) : provides to jump to the Vim script's last error
  * [rcarriga/nvim-dap-ui](https://github.com/rcarriga/nvim-dap-ui) : A UI for nvim-dap
  * [rgroli/other.nvim](https://github.com/rgroli/other.nvim) : you can open other/related files for the currently active buffer
  * [rhysd/conflict-marker.vim](https://github.com/rhysd/conflict-marker.vim) : Highlight, jump and resolve conflict markers quickly
  * [rhysd/vim-startuptime](https://github.com/rhysd/vim-startuptime) : measures startuptime
  * [rktjmp/fwatch.nvim](https://github.com/rktjmp/fwatch.nvim) : watch files or directories for changes and then run vim commands or lua functions
  * [rktjmp/paperplanes.nvim](https://github.com/rktjmp/paperplanes.nvim) : Post selections or buffers to online paste bins.
  * [rliang/termedit.nvim](https://github.com/rliang/termedit.nvim) : Sets the Neovim host instance as `$EDITOR`
  * [romainl/vim-devdocs](https://github.com/romainl/vim-devdocs) : Look up keywords on https://devdocs.io
  * [romgrk/kui.nvim](https://github.com/romgrk/kui.nvim) : uses Kitty graphics protocol to build interface
  * [roxma/nvim-yarp](https://github.com/roxma/nvim-yarp) : Yet Another Remote Plugin Framework for Neovim
  * [roxma/vim-hug-neovim-rpc](https://github.com/roxma/vim-hug-neovim-rpc) : trying to build a compatibility layer for neovim rpc client working on vim8
  * [rraks/pyro](https://github.com/rraks/pyro) : neovim interface to write simple list manipulating python snippets
  * [rrethy/nvim-animator](https://github.com/rrethy/nvim-animator) : Neovim plugin for that animates the change in a value for use in animations
  * [rrethy/nvim-carom](https://github.com/rrethy/nvim-carom) : macros and caroms
  * [rrethy/nvim-sourcerer](https://github.com/rrethy/nvim-sourcerer) : Automatically source your init.lua when it gets modified anywhere
  * [rrethy/vim-indexor](https://github.com/rrethy/vim-indexor) : adding indices to a list of items
  * [rrethy/vim-tranquille](https://github.com/rrethy/vim-tranquille) : searching without moving the cursor
  * [saecki/crates.nvim](https://github.com/saecki/crates.nvim) : neovim plugin that helps managing crates.io dependencies
  * [samjwill/nvim-unception](https://github.com/samjwill/nvim-unception) : leverages Neovim's native client-serverfeature to make opening files from within Neovim's terminal emulator without experiencing weird behavior easier and completely automatic
  * [samodostal/image.nvim](https://github.com/samodostal/image.nvim) : Image Viewer as ASCII Art
  * [sanhajio/synonyms.vim](https://github.com/sanhajio/synonyms.vim) : allows you to show synonyms in a vim split
  * [sbulav/jump-ray.nvim](https://github.com/sbulav/jump-ray.nvim) : keep that eye on the jumplist in floating window
  * [scrooloose/vim-slumlord](https://github.com/scrooloose/vim-slumlord) : is built atop the wang-hardeningly awesome plantuml
  * [severin-lemaignan/vim-minimap](https://github.com/severin-lemaignan/vim-minimap) : a vim minimap
  * [sgur/vim-editorconfig](https://github.com/sgur/vim-editorconfig) : Yet another Vim plugin for EditorConfig
  * [shadmansaleh/irc.nvim](https://github.com/shadmansaleh/irc.nvim) : Irc client for neovim
  * [shohi/neva](https://github.com/shohi/neva) : Neovim version manager [archived]
  * [shougo/neoinclude.vim](https://github.com/shougo/neoinclude.vim) : Include completion framework for neocomplete/deoplete/ncm
  * [shougo/neomru.vim](https://github.com/shougo/neomru.vim) : MRU plugin includes unite.vim MRU sources
  * [shougo/pum.vim](https://github.com/shougo/pum.vim) : implement original popup menu completion
  * [shougo/tabpagebuffer.vim](https://github.com/shougo/tabpagebuffer.vim) : Tabpage buffer interface
  * [simonefranza/nvim-conv](https://github.com/simonefranza/nvim-conv) : simple converter that allows you to convert
  * [sitiom/nvim-numbertoggle](https://github.com/sitiom/nvim-numbertoggle) : Neovim plugin to automatically toggle between relative and absolute line numbers
  * [sjl/clam.vim](https://github.com/sjl/clam.vim) : lightweight Vim plugin to easily run shell commands
  * [sjl/vitality.vim](https://github.com/sjl/vitality.vim) : makes vim play nicely with iTerm 2 and tmux
  * [skywind3000/asyncrun.vim](https://github.com/skywind3000/asyncrun.vim) : async run shell commands in qf window
  * [skywind3000/asynctasks.vim](https://github.com/skywind3000/asynctasks.vim) : modern task system
  * [skywind3000/quickmenu.vim](https://github.com/skywind3000/quickmenu.vim) : open up a `quickmenu` with often used commands
  * [skywind3000/vim-auto-popmenu](https://github.com/skywind3000/vim-auto-popmenu) : automatically open autocomplete menu
  * [skywind3000/vim-dict](https://github.com/skywind3000/vim-dict) : Automatically add dictionary files to current buffer according to the filetype
  * [skywind3000/vim-rt-format](https://github.com/skywind3000/vim-rt-format) : Format current line immediately in INSERT mode as soon as you press ENTER
  * [slashmili/alchemist.vim](https://github.com/slashmili/alchemist.vim) : This plugin uses ElixirSense to give inside information about your elixir project in vim
  * [smjonas/snippet-converter.nvim](https://github.com/smjonas/snippet-converter.nvim) : Parse, transform and convert snippets
  * [smzm/hydrovim](https://github.com/smzm/hydrovim) : runs Pythoncode and displays the result
  * [softinio/scaladex.nvim](https://github.com/softinio/scaladex.nvim) : provides both Telescope extension that allows you to search the scaladex index and provides a library that you can require and query the scaladex index
  * [strboul/urlview.vim](https://github.com/strboul/urlview.vim) : List and open URLs easily
  * [subnut/nvim-ghost.nvim](https://github.com/subnut/nvim-ghost.nvim) : nvim version of vim-ghost
  * [sudormrfbin/cheatsheet.nvim](https://github.com/sudormrfbin/cheatsheet.nvim) : A searchable cheatsheet for neovim
  * [sunaku/vim-dasht](https://github.com/sunaku/vim-dasht) : dasht integration
  * [svermeulen/vim-macrobatics](https://github.com/svermeulen/vim-macrobatics) : the goal of making vim macros easier to use
  * [szymonmaszke/vimpyter](https://github.com/szymonmaszke/vimpyter) : vim and jupyter [archived] [no maintain]
  * [t-troebst/perfanno.nvim](https://github.com/t-troebst/perfanno.nvim) : highlite lines from pref
  * [tami5/sqlite.lua](https://github.com/tami5/sqlite.lua) : SQLite/LuaJIT binding and a highly opinionated wrapper for storing, retrieving, caching, and persisting SQLite databases
  * [tastyep/structlog.nvim](https://github.com/tastyep/structlog.nvim) : Structured Logging for nvim, using Lua
  * [tek/chromatin.nvim](https://github.com/tek/chromatin.nvim) : provides management for plugins built with ribos and distributed over pypi
  * [tenfyzhong/tagbar-makefile.vim](https://github.com/tenfyzhong/tagbar-makefile.vim) : makefile for tagbar [archived]
  * [tenfyzhong/tagbar-proto.vim](https://github.com/tenfyzhong/tagbar-proto.vim) : protobuf for tagbar [archived]
  * [tenxsoydev/nx.nvim](https://github.com/tenxsoydev/nx.nvim) : nvim utility library to n^x
  * [theprimeagen/refactoring.nvim](https://github.com/theprimeagen/refactoring.nvim) : refactor code
  * [theprimeagen/vim-apm](https://github.com/theprimeagen/vim-apm) : keeps track of your APM by counting keystrokes and determining its worth
  * [thezeroalpha/vim-visualrun](https://github.com/thezeroalpha/vim-visualrun) : select some lines and run them as a Vim command
  * [thibthib18/mongo-nvim](https://github.com/thibthib18/mongo-nvim) : MongoDB Integration in Neovim
  * [thibthib18/ros-nvim](https://github.com/thibthib18/ros-nvim) : ROS in Neovim
  * [thirtythreeforty/lessspace.vim](https://github.com/thirtythreeforty/lessspace.vim) : strip the trailing whitespace from the file you are editing
  * [timeyyy/orchestra.nvim](https://github.com/timeyyy/orchestra.nvim) : lets you bind sound effects to different actions
  * [tokiory/neovim-boilerplate](https://github.com/tokiory/neovim-boilerplate) : simple template for configs
  * [tomasky/bookmarks.nvim](https://github.com/tomasky/bookmarks.nvim) : bookmarks with global file store
  * [tomiis4/hypersonic.nvim](https://github.com/tomiis4/hypersonic.nvim) : for regex writing/testing
  * [tpope/vim-apathy](https://github.com/tpope/vim-apathy) : sets the five path searching options for file types I don't care about enough to bother with creating a proper plugin
  * [tpope/vim-bundler](https://github.com/tpope/vim-bundler) : a lightweight bag of Vim goodies for Bundler
  * [tpope/vim-dadbod](https://github.com/tpope/vim-dadbod) : Vim plugin for interacting with databases
  * [tpope/vim-dispatch](https://github.com/tpope/vim-dispatch) : Leverage the power of Vim's compiler plugins without being bound by synchronicity
  * [tpope/vim-pathogen](https://github.com/tpope/vim-pathogen) : Manage your `runtimepath` with ease
  * [tpope/vim-scriptease](https://github.com/tpope/vim-scriptease) : a Vim plugin for making Vim plugins
  * [tracyone/neomake-multiprocess](https://github.com/tracyone/neomake-multiprocess) : vim plugin for running multiple process asynchronously base on neomake
  * [tweekmonster/helpful.vim](https://github.com/tweekmonster/helpful.vim) : A plugin for plugin developers to get the version of Vim and Neovim that introduced or removed features
  * [tweekmonster/startuptime.vim](https://github.com/tweekmonster/startuptime.vim) : breaks down the output of `--startuptime`
  * [tyru/open-browser-github.vim](https://github.com/tyru/open-browser-github.vim) : Opens GitHub URL of current file, etc.
  * [tyru/open-browser-unicode.vim](https://github.com/tyru/open-browser-unicode.vim) : Opens Unicode character information
  * [tyru/open-browser.vim](https://github.com/tyru/open-browser.vim) : Open URI with your favorite browser from your most favorite editor
  * [udayvir-singh/hibiscus.nvim](https://github.com/udayvir-singh/hibiscus.nvim) : Highly opinionated macros to elegantly write your neovim config
  * [udayvir-singh/tangerine.nvim](https://github.com/udayvir-singh/tangerine.nvim) : painless way to add fennel to your config
  * [uga-rosa/utf8.nvim](https://github.com/uga-rosa/utf8.nvim) : utf8 for neovim
  * [vim-jp/vital.vim](https://github.com/vim-jp/vital.vim) : A comprehensive Vim utility functions for Vim plugins
  * [vim-scripts/a.vim](https://github.com/vim-scripts/a.vim) : commands to swtich between source files and header files
  * [vim-scripts/autocomplpop](https://github.com/vim-scripts/autocomplpop) : automatically opens popup menu for completions
  * [vim-scripts/cyclecolor](https://github.com/vim-scripts/cyclecolor) : cycle through (almost) all available colorschemes
  * [vim-scripts/taglist.vim](https://github.com/vim-scripts/taglist.vim) : provides an overview of the structure of source code files
  * [voldikss/vim-browser-search](https://github.com/voldikss/vim-browser-search) : perform a quick web search for the text selected
  * [voldikss/vim-translator](https://github.com/voldikss/vim-translator) : tranlate stuff
  * [vonheikemen/fine-cmdline.nvim](https://github.com/vonheikemen/fine-cmdline.nvim) : a better cmdline
  * [vuki656/package-info.nvim](https://github.com/vuki656/package-info.nvim) : All the `npm`/`yarn`/`pnpm` commands I don't want to type
  * [vv-vim/vv](https://github.com/vv-vim/vv) : Neovim client for macOS
  * [wakatime/vim-wakatime](https://github.com/wakatime/vim-wakatime) : open source Vim plugin for metrics, insights, and time tracking automatically generated from your programming activity
  * [weilbith/nvim-code-action-menu](https://github.com/weilbith/nvim-code-action-menu) : provides a handy pop-up menu for code actions
  * [weissle/persistent-breakpoints.nvim](https://github.com/weissle/persistent-breakpoints.nvim) : save the nvim-daps checkpoints to file and automatically load them when you open neovim
  * [williamboman/mason-lspconfig.nvim](https://github.com/williamboman/mason-lspconfig.nvim) : bridges mason.nvim with the lspconfig plugin
  * [williamboman/mason.nvim](https://github.com/williamboman/mason.nvim) : easily manage external editor tooling such as LSP servers, DAP servers, linters, and formatters
  * [willothy/flatten.nvim](https://github.com/willothy/flatten.nvim) : open files from nvim embedded terminal
  * [willothy/veil.nvim](https://github.com/willothy/veil.nvim) : fast, animated, configurable dashboard
  * [windwp/nvim-projectconfig](https://github.com/windwp/nvim-projectconfig) : Load config depend on current directory
  * [winston0410/cmd-parser.nvim](https://github.com/winston0410/cmd-parser.nvim) : help other plugin authors to easily parse the command inputted by users and do awesome tricks with it
  * [wsdjeg/vim-autohotkey](https://github.com/wsdjeg/vim-autohotkey) : autohotkey support for vim
  * [wyattjsmith1/weather.nvim](https://github.com/wyattjsmith1/weather.nvim) : A simple plugin to display weather in nvim
  * [xiyaowong/link-visitor.nvim](https://github.com/xiyaowong/link-visitor.nvim) : Let me help you open the links
  * [xolox/vim-lua-ftplugin](https://github.com/xolox/vim-lua-ftplugin) : Lua file type plug-in for Vim
  * [yagiziskirik/airsupport.nvim](https://github.com/yagiziskirik/airsupport.nvim) : write shortcut reminders and forget them
  * [yegappan/mru](https://github.com/yegappan/mru) : provides an easy access to a list of recently opened/edited files
  * [zenbro/mirror.vim](https://github.com/zenbro/mirror.vim) : make it quick to do remote actions for each environment of project you working with
  * [ziontee113/icon-picker.nvim](https://github.com/ziontee113/icon-picker.nvim) : helps you pick 𝑨𝕃𝚻 Font Characters, Symbols Σ, Nerd Font Icons  & Emojis ✨
## comment
  * [b3nj5m1n/kommentary](https://github.com/b3nj5m1n/kommentary) : Neovim plugin to comment text in and out, written in lua
  * [gennaro-tedesco/nvim-commaround](https://github.com/gennaro-tedesco/nvim-commaround) : toggle comments on and off
  * [glepnir/prodoc.nvim](https://github.com/glepnir/prodoc.nvim) : comment and annotation plugin using coroutine
  * [lucastavaresa/singlecomment.nvim](https://github.com/lucastavaresa/singlecomment.nvim) : singe line commenting
  * [ludopinelli/comment-box.nvim](https://github.com/ludopinelli/comment-box.nvim) : giving you easy boxes and lines the way you want them to be
  * [numtostr/comment.nvim](https://github.com/numtostr/comment.nvim) : Smart and Powerful commenting plugin for neovim
  * [preservim/nerdcommenter](https://github.com/preservim/nerdcommenter) : Comment functions so powerful—no comment necessary
  * [s1n7ax/nvim-comment-frame](https://github.com/s1n7ax/nvim-comment-frame) : Basically when you give it some text it creates a comment frame like below
  * [suy/vim-context-commentstring](https://github.com/suy/vim-context-commentstring) : automatically set the 'commentstring' and 'comments' Vim options in file types which contain more than one syntax
  * [terrortylor/nvim-comment](https://github.com/terrortylor/nvim-comment) : Toggle comments in Neovim
  * [tomtom/tcomment_vim](https://github.com/tomtom/tcomment_vim) : provides easy to use, file-type sensible comments for Vim
  * [tpope/vim-commentary](https://github.com/tpope/vim-commentary) : Comment stuff out
  * [tyru/caw.vim](https://github.com/tyru/caw.vim) : Comment plugin: Operator/Dot-repeatable/300+ filetypes
  * [winston0410/commented.nvim](https://github.com/winston0410/commented.nvim) : A commenting plugin written in Lua that actually works
## library
  * [bkoropoff/bex.nvim](https://github.com/bkoropoff/bex.nvim) : Lua to Ex bridge library
  * [furkanzmc/options.nvim](https://github.com/furkanzmc/options.nvim) : A small library to create custom options for your plugins or your configuration
  * [glts/vim-magnum](https://github.com/glts/vim-magnum) : big integer library for Vim plugins written entirely in Vim script
  * [google/vim-maktaba](https://github.com/google/vim-maktaba) : a vimscript plugin library
  * [iron-e/nvim-libmodal](https://github.com/iron-e/nvim-libmodal) : a rewite of vim-libmodal using Neovim's Lua API
  * [raimondi/vimregstyle](https://github.com/raimondi/vimregstyle) : a Regular Expression Pattern Library
  * [ray-x/guihua.lua](https://github.com/ray-x/guihua.lua) : library for nvim plugins
  * [shougo/context_filetype.vim](https://github.com/shougo/context_filetype.vim) : Context filetype library for Vim script
  * [shougo/vimproc](https://github.com/shougo/vimproc) : a great asynchronous execution library for Vim
  * [shougo/vimproc.vim](https://github.com/shougo/vimproc.vim) : great asynchronous execution library for Vim
  * [sunjon/stylish.nvim](https://github.com/sunjon/stylish.nvim) : A collection of Stylish UI components for Neovim
  * [tomtom/tlib_vim](https://github.com/tomtom/tlib_vim) : This library provides some utility functions
  * [xolox/vim-misc](https://github.com/xolox/vim-misc) : Miscellaneous auto-load Vim scripts
## remote-colab
  * [floobits/floobits-neovim](https://github.com/floobits/floobits-neovim) : Real-time collaborative editing
  * [fredkschott/covim](https://github.com/fredkschott/covim) : Collaborative Editing for Vim
  * [jbyuki/instant.nvim](https://github.com/jbyuki/instant.nvim) : instant.nvim is a collaborative editing plugin for Neovim written in Lua with no dependencies
## chat
  * [aaronik/gptmodels.nvim](https://github.com/aaronik/gptmodels.nvim) : LLM AI plugin for neovim
  * [archibate/nvim-gpt](https://github.com/archibate/nvim-gpt) : chatgpt and bing-ai in neovim
  * [deifyed/navi](https://github.com/deifyed/navi) : natural language first based development
  * [dpayne/codegpt.nvim](https://github.com/dpayne/codegpt.nvim) : provides command interface to chat with ChatGPT
  * [jackmort/chatgpt.nvim](https://github.com/jackmort/chatgpt.nvim) : allows you to interact with Open AI's GPT-3
  * [martineausimon/nvim-bard](https://github.com/martineausimon/nvim-bard) : chat with bard
  * [terror/chatgpt.nvim](https://github.com/terror/chatgpt.nvim) : lest you query ChatGPT
  * [throughnothing/vimchat](https://github.com/throughnothing/vimchat) : do instant messaging from within the vim text editor
  * [vim-chat/vim-chat](https://github.com/vim-chat/vim-chat) : chat in neovim and vim8
  * [wsdjeg/vim-chat](https://github.com/wsdjeg/vim-chat) : The chatting client for vim
## mouse
  * [notomo/gesture.nvim](https://github.com/notomo/gesture.nvim) : is a mouse gesture plugin for Neovim
## windows
  * [anuvyklack/windows.nvim](https://github.com/anuvyklack/windows.nvim) : make the current window automatically bigger
  * [beauwilliams/focus.nvim](https://github.com/beauwilliams/focus.nvim) : Splits/Window Management Enhancements for Neovim
  * [blueyed/vim-diminactive](https://github.com/blueyed/vim-diminactive) : dim inactive windows
  * [camspiers/animate.vim](https://github.com/camspiers/animate.vim) : A Vim Window Animation Library
  * [camspiers/lens.vim](https://github.com/camspiers/lens.vim) : Vim Automatic Window Resizing Plugin
  * [declancm/windex.nvim](https://github.com/declancm/windex.nvim) : neovim plugin for cleeean neovim window (and tmux pane) functions
  * [delphinus/dwm.nvim](https://github.com/delphinus/dwm.nvim) : lua port of [spolu/dwm.vim](https://github.com/spolu/dwm.vim)
  * [dm1try/golden_size](https://github.com/dm1try/golden_size) : automatically resizing the active window to the "golden" size
  * [dstein64/vim-win](https://github.com/dstein64/vim-win) : a Vim plugin for managing windows
  * [yorickpeterse/nvim-window](https://gitlab.com/yorickpeterse/nvim-window) : quickly switching between windows
  * [luukvbaal/stabilize.nvim](https://github.com/luukvbaal/stabilize.nvim) : stabilize buffer content on window open/close events
  * [mattboehm/vim-accordion](https://github.com/mattboehm/vim-accordion) : set the maximum number of splits you want to see, and shrinks the rest to be one column wide
  * [mrjones2014/smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim) : Smart, directional Neovim split resizing and navigation
  * [simeji/winresizer](https://github.com/simeji/winresizer) : easily resizing windows
  * [sindrets/winshift.nvim](https://github.com/sindrets/winshift.nvim) : Rearrange your windows with ease
  * [smithbm2316/centerpad.nvim](https://github.com/smithbm2316/centerpad.nvim) : Center your single lonely buffer easily
  * [spolu/dwm.vim](https://github.com/spolu/dwm.vim) : tiled window manager for vim
  * [stevearc/stickybuf.nvim](https://github.com/stevearc/stickybuf.nvim) : Neovim plugin for locking a buffer to a window
  * [szw/vim-maximizer](https://github.com/szw/vim-maximizer) : Maximizes and restores the current window
  * [t9md/vim-choosewin](https://github.com/t9md/vim-choosewin) : enables you to choose a window interactively
  * [wellle/visual-split.vim](https://github.com/wellle/visual-split.vim) : Vim plugin to control splits with visual selections or text objects
  * [wesq3/vim-windowswap](https://github.com/wesq3/vim-windowswap) : Swap windows without ruining your layout
## detectindent
  * [ciaranm/detectindent](https://github.com/ciaranm/detectindent) : automatically detecting indent settings
  * [conormcd/matchindent.vim](https://github.com/conormcd/matchindent.vim) : scans through a file when it's opened and attempts to guess which style of indentation is being used
  * [hrsh7th/nvim-dansa](https://github.com/hrsh7th/nvim-dansa) : Guess the indent from lines of around.
  * [ldx/vim-indentfinder](https://github.com/ldx/vim-indentfinder) : vim plugin for automatically detecting indentation
  * [nmac427/guess-indent.nvim](https://github.com/nmac427/guess-indent.nvim) : Blazing fast indentation style detection for Neovim written in Lua
  * [raimondi/yaifa](https://github.com/raimondi/yaifa) : try to detect the kind of indentation used in your file and set the indenting options to the appropriate values
  * [timakro/vim-yadi](https://github.com/timakro/vim-yadi) : Yet Another Detect Indent
  * [tpope/vim-sleuth](https://github.com/tpope/vim-sleuth) : automatically adjusts `'shiftwidth'` and `'expandtab'` heuristically based on the current file
## indent
  * [darazaki/indent-o-matic](https://github.com/darazaki/indent-o-matic) : Dumb automatic fast indentation detection for Neovim written in Lua
  * [glepnir/indent-guides.nvim](https://github.com/glepnir/indent-guides.nvim) : async render indent guides
  * [hrsh7th/vim-gindent](https://github.com/hrsh7th/vim-gindent) : General indentexpr plugin
  * [nathanaelkane/vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides) : visually displaying indent levels in Vim [not maintain]
  * [nvimdev/indentmini.nvim](https://github.com/nvimdev/indentmini.nvim) : minimal indentline plugin
  * [rbtnn/vim-vimscript_indentexpr](https://github.com/rbtnn/vim-vimscript_indentexpr) : helps with line indentation
  * [vim-scripts/fortran.vim](https://github.com/vim-scripts/fortran.vim) : adds additional indentation rules
  * [zsugabubus/crazy8.nvim](https://github.com/zsugabubus/crazy8.nvim) : NeoVim plugin that automagically configures 'tabstop', 'shiftwidth', 'softtabstop' and 'expandtab'
## folds
  * [anuvyklack/fold-preview.nvim](https://github.com/anuvyklack/fold-preview.nvim) : preview closed folds
  * [anuvyklack/pretty-fold.nvim](https://github.com/anuvyklack/pretty-fold.nvim) : Folded region preview and Framework for easy foldtext customization
  * [dbmrq/vim-chalk](https://github.com/dbmrq/vim-chalk) : auto add fold text
  * [jghauser/fold-cycle.nvim](https://github.com/jghauser/fold-cycle.nvim) : allows you to cycle folds open or closed
  * [kaile256/vim-foldpeek](https://github.com/kaile256/vim-foldpeek) : peek at folds
  * [kalekundert/vim-coiled-snake](https://github.com/kalekundert/vim-coiled-snake) : Python Folding for Vim
  * [kevinhwang91/nvim-ufo](https://github.com/kevinhwang91/nvim-ufo) : make Neovim's fold look modern and keep high performance
  * [konfekt/fastfold](https://github.com/konfekt/fastfold) : only update folds whene you need to, thous improving speed
  * [konfekt/foldtext](https://github.com/konfekt/foldtext) : shows a modification of the CustomFoldText function by Christian Brabandt that is more amenable to syntax folds
  * [kshenoy/vim-origami](https://github.com/kshenoy/vim-origami) : Plugin to satisfy all your folding needs
  * [lambdalisue/readablefold.vim](https://github.com/lambdalisue/readablefold.vim) : improve `foldtext` for better looks
  * [leafcage/foldcc.vim](https://github.com/leafcage/foldcc.vim) : Provides a function to display the fold text `'foldtext'` in a nice way
  * [pseewald/vim-anyfold](https://github.com/pseewald/vim-anyfold) : Generic folding mechanism and motion based on indentation
  * [tmhedberg/simpylfold](https://github.com/tmhedberg/simpylfold) : simple, correct folding for Python
## quickfix
  * [bfrg/vim-qf-preview](https://github.com/bfrg/vim-qf-preview) : For the quickfix and location list window to quickly preview the file with the quickfix item under the cursor in a popup window
  * [gabrielpoca/replacer.nvim](https://github.com/gabrielpoca/replacer.nvim) : makes a quickfix window editable, allowing changes to both the content of a file as well as its path
  * [yorickpeterse/nvim-pqf](https://gitlab.com/yorickpeterse/nvim-pqf) : Pretty Quickfix windows for NeoVim
  * [joshmcguigan/estream](https://github.com/joshmcguigan/estream) : help you unlock the power of the quickfix window without dealing with the pain of Vim's `errorformat`
  * [kevinhwang91/nvim-bqf](https://github.com/kevinhwang91/nvim-bqf) : makes Neovim's quickfix window better
  * [nyngwang/neowell.lua](https://github.com/nyngwang/neowell.lua) : commands for quickfix window
  * [olical/vim-enmasse](https://github.com/olical/vim-enmasse) : Takes a quickfix list and makes it editable
  * [romainl/vim-qf](https://github.com/romainl/vim-qf) : is a growing collection of settings, commands and mappings put together to make working with the location list/window and the quickfix list/window smoother
  * [romainl/vim-qlist](https://github.com/romainl/vim-qlist) : make the results of "include-search" and "definition-search" easier to navigate and more persistent by using the quickfix list instead of the default list-like interface
  * [romainl/vim-quicklist](https://github.com/romainl/vim-quicklist) : Persist the result of list-like Ex commands to the quickfix list
  * [stefandtw/quickfix-reflector.vim](https://github.com/stefandtw/quickfix-reflector.vim) : edit direcly inside the quickfix window
  * [stevearc/qf_helper.nvim](https://github.com/stevearc/qf_helper.nvim) : A collection of improvements for neovim quickfix
  * [ten3roberts/qf.nvim](https://github.com/ten3roberts/qf.nvim) : qf and localist manager fo neovim
  * [yssl/qfenter](https://github.com/yssl/qfenter) : allows you to open items from Vim's quickfix or location list wherever you wish
## gui
  * [akiyosi/goneovim](https://github.com/akiyosi/goneovim) : Neovim GUI written in Go
  * [beeender/glrnvim](https://github.com/beeender/glrnvim) : really fast & stable neovim GUI could be accelated by GPU
  * [daa84/neovim-gtk](https://github.com/daa84/neovim-gtk) : GTK ui for neovim written in rust using gtk-rs bindings, with ligatures support
  * [dzhou121/gonvim](https://github.com/dzhou121/gonvim) : Neovim GUI written in Golang [archived]
  * [equalsraf/neovim-qt](https://github.com/equalsraf/neovim-qt)
  * [kethku/neovide](https://github.com/kethku/neovide) : This is a simple graphical user interface for Neovim
  * [lyude/neovim-gtk](https://github.com/lyude/neovim-gtk) : GTK ui for neovim written in rust using gtk-rs bindings
  * [neovide/neovide](https://github.com/neovide/neovide) : simple gui for neovim
  * [qvacua/vimr](https://github.com/qvacua/vimr) : Neovim GUI for macOS
  * [rmichelsen/nvy](https://github.com/rmichelsen/nvy) : minimal Neovim client for Windows written in C++
  * [rohit-px2/nvui](https://github.com/rohit-px2/nvui) : nvim gui written in cpp
  * [smolck/uivonim](https://github.com/smolck/uivonim) : fork of Veonim, written in Electron with WebGL GPU rendering and multithreading
  * [tk-shirasaka/envim](https://github.com/tk-shirasaka/envim) : neovim gui written in electron
  * [vhakulinen/gnvim](https://github.com/vhakulinen/gnvim) : Rich Neovim GUI without any web bloat
  * [yatli/fvim](https://github.com/yatli/fvim) : Cross platform Neovim front-end UI, built with F# + Avalonia
  * [yqlbu/neovim-server](https://github.com/yqlbu/neovim-server) : A containerized IDE-like text editor that runs on a web server
## ide
  * [abstract-ide/abstract](https://github.com/abstract-ide/abstract)
  * [artart222/codeart](https://github.com/artart222/codeart)
  * [askfiy/nvim](https://github.com/askfiy/nvim)
  * [astronvim/astronvim](https://github.com/astronvim/astronvim)
  * [cankolay3499/cnvim](https://github.com/cankolay3499/cnvim)
  * [charleschiugit/nvimdots.lua](https://github.com/charleschiugit/nvimdots.lua) : Neovim config
  * [cosmicnvim/cosmicnvim](https://github.com/cosmicnvim/cosmicnvim)
  * [crivotz/nv-ide](https://github.com/crivotz/nv-ide)
  * [cstsunfu/.sea.nvim](https://github.com/cstsunfu/.sea.nvim)
  * [folke/lua-dev.nvim](https://github.com/folke/lua-dev.nvim) : setup for init.lua and plugin development with full signature help, docs and completion for the nvim lua API
  * [frans-johansson/lazy-nvim-starter](https://github.com/frans-johansson/lazy-nvim-starter) : minimal neovim config
  * [hackorum/vapournvim](https://github.com/hackorum/vapournvim)
  * [ibnyusrat/vimcode](https://github.com/ibnyusrat/vimcode) : make vim look/work like vs code
  * [imbacraft/dusk.nvim](https://github.com/imbacraft/dusk.nvim)
  * [jonathandion/web-dev.nvim](https://github.com/jonathandion/web-dev.nvim) : Small, fast, simple, flexible
  * [jrychn/modulevim](https://github.com/jrychn/modulevim)
  * [jueqingsizhe66/windowvimfaster](https://github.com/jueqingsizhe66/windowvimfaster)
  * [klen/python-mode](https://github.com/klen/python-mode) : a Python IDE for Vim
  * [lazyvim/lazyvim](https://github.com/lazyvim/lazyvim) : the IDE for the lazy.nvim
  * [ldelossa/litee.nvim](https://github.com/ldelossa/litee.nvim) : a library for building "IDE-lite" experiences in Neovim
  * [ldelossa/nvim-ide](https://github.com/ldelossa/nvim-ide) : complete IDE layer for Neovim
  * [linrongbin16/lin.nvim](https://github.com/linrongbin16/lin.nvim) : highly configurable distribution
  * [lunarvim/lunarvim](https://github.com/lunarvim/lunarvim)
  * [lvim-tech/lvim](https://github.com/lvim-tech/lvim) : modular neovim configuration
  * [max397574/ignis-nvim](https://github.com/max397574/ignis-nvim) : Bloat but Blazing
  * [max397574/omega-nvim](https://github.com/max397574/omega-nvim) : a refactor of ignis-nvim
  * [normalnvim/normalnvim](https://github.com/normalnvim/normalnvim) : the most normal neovim config
  * [ntbbloodbath/doom-nvim](https://github.com/ntbbloodbath/doom-nvim)
  * [nvchad/nvchad](https://github.com/nvchad/nvchad) : neovim config written in lua aiming to provide a base configuration with very beautiful UI and blazing fast startuptime
  * [nvim-lua/kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) : A starting point for Neovim
  * [nvimdev/dope](https://github.com/nvimdev/dope) : the dopest config
  * [nvoid-lua/nvoid](https://github.com/nvoid-lua/nvoid)
  * [otavioschwanck/mood-nvim](https://github.com/otavioschwanck/mood-nvim) : a configuration
  * [pakrohk-dotfiles/nvpak](https://github.com/pakrohk-dotfiles/nvpak) : provide the defaults to the newest neovim
  * [pechorin/any-jump.vim](https://github.com/pechorin/any-jump.vim) : IDE madness without overhead for 40+ languages
  * [rafaeldelboni/nvim-fennel-lsp-conjure-as-clojure-ide](https://github.com/rafaeldelboni/nvim-fennel-lsp-conjure-as-clojure-ide) : Basic config to transform your NVIM in a powerful Clojure IDE using fennel, clojure-lsp and conjure
  * [shaeinst/roshnivim](https://github.com/shaeinst/roshnivim)
  * [shaunsingh/nyoom.nvim](https://github.com/shaunsingh/nyoom.nvim)
  * [siduck76/nvchad](https://github.com/siduck76/nvchad)
  * [spacevim/spacevim](https://github.com/spacevim/spacevim)
  * [tenxsoydev/nxvim](https://github.com/tenxsoydev/nxvim) : leverages 100 extensions to make fast and structured
  * [theory-of-everything/nii-nvim](https://github.com/theory-of-everything/nii-nvim) : no-nonsense neovim config
  * [usuim/usuim](https://github.com/usuim/usuim) : Neovim configured to look like Visual Studio Code
  * [vi-tality/neovitality](https://github.com/vi-tality/neovitality)
  * [wklken/k-vim](https://github.com/wklken/k-vim) : Just a Better Vim Config. Keep it Simple.
## sidebar
  * [lambdalisue/fern.vim](https://github.com/lambdalisue/fern.vim) : is a general purpose asynchronous tree viewer written in pure Vim script
  * [preservim/tagbar](https://github.com/preservim/tagbar) : a class outline viewer for Vim
  * [sidebar-nvim/sidebar.nvim](https://github.com/sidebar-nvim/sidebar.nvim) : A generic and modular lua sidebar inspired by lualine
## tag
  * [jsfaint/gen_tags.vim](https://github.com/jsfaint/gen_tags.vim) : Async plugin for Vim to ease the use of ctags/gtags
  * [ludovicchabant/vim-gutentags](https://github.com/ludovicchabant/vim-gutentags) : takes care of the much needed management of tags files in Vim
  * [rbtnn/vim-vimscript_tagfunc](https://github.com/rbtnn/vim-vimscript_tagfunc) : provides to set &tagfunc for Vim script
  * [skywind3000/gutentags_plus](https://github.com/skywind3000/gutentags_plus) : will update gtags database in background automatically
  * [spacevim/gtags.vim](https://github.com/spacevim/gtags.vim) : integrates the GNU GLOBAL source code tag system with Vim
  * [t9md/vim-quickhl](https://github.com/t9md/vim-quickhl) : highlight word and tags
  * [weilbith/nvim-floating-tag-preview](https://github.com/weilbith/nvim-floating-tag-preview) : easily preview tags in a floating window
## file
  * [bourgeoisbear/vim-rsvp](https://github.com/bourgeoisbear/vim-rsvp) : Why move your eyes to read when computers can move the words for us
  * [chrsm/impulse.nvim](https://github.com/chrsm/impulse.nvim) : a neovim plugin for viewing Notion.so pages
  * [dokwork/vim-hp](https://github.com/dokwork/vim-hp) : Helps to write a help
  * [donraphaco/neotex](https://github.com/donraphaco/neotex) : compiles latex files asynchronously while edditing [archived]
  * [dpelle/vim-languagetool](https://github.com/dpelle/vim-languagetool) : This plugin integrates the LanguageTool grammar checker into Vim
  * [ecthelionvi/neosave.nvim](https://github.com/ecthelionvi/neosave.nvim) : auto save file
  * [fmoralesc/nlanguagetool.nvim](https://github.com/fmoralesc/nlanguagetool.nvim) : Stupid simple language tool plugin for nvim
  * [jamessan/vim-gnupg](https://github.com/jamessan/vim-gnupg) : implements transparent editing of gpg encrypted files
  * [jghauser/follow-md-links.nvim](https://github.com/jghauser/follow-md-links.nvim) : allows you to follow markdown links by pressing enter when the cursor is positioned on a link
  * [luchermitte/lh-cpp](https://github.com/luchermitte/lh-cpp) : heterogeneous suite of helpers for C and C++ programming
  * [lunarvim/bigfile.nvim](https://github.com/lunarvim/bigfile.nvim) : disables certain features when opening big files
  * [mrshmllow/open-handlers.nvim](https://github.com/mrshmllow/open-handlers.nvim) : extend gx while allowing default behavior
  * [mtth/scratch.vim](https://github.com/mtth/scratch.vim) : Unobtrusive scratch window
  * [mzlogin/vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc) : generate table of contents for Markdown files
  * [okuuva/auto-save.nvim](https://github.com/okuuva/auto-save.nvim) : auto save file when change
  * [panozzaj/vim-autocorrect](https://github.com/panozzaj/vim-autocorrect) : add typo correctint abbreviations
  * [preservim/vim-litecorrect](https://github.com/preservim/vim-litecorrect) : add type correctint abbreviations
  * [previm/previm](https://github.com/previm/previm) : Vim plugin for preview
  * [reedes/vim-wordy](https://github.com/reedes/vim-wordy) : Uncover usage problems in your writing
  * [rhysd/vim-grammarous](https://github.com/rhysd/vim-grammarous) : a powerful grammar checker for Vim
  * [richardbizik/nvim-toc](https://github.com/richardbizik/nvim-toc) : generate ToC for markdown
  * [ron89/thesaurus_query.vim](https://github.com/ron89/thesaurus_query.vim) : plugin for user to lookupsynonyms of any word
  * [sidofc/mkdx](https://github.com/sidofc/mkdx) : reduce the time you spend formatting your markdown documents
  * [stevearc/gkeep.nvim](https://github.com/stevearc/gkeep.nvim) : Neovim integration for Google Keep, built using gkeepapi
  * [tmillr/sos.nvim](https://github.com/tmillr/sos.nvim) : never manually save again
  * [tobys/pdv](https://github.com/tobys/pdv) : your tool of choice for generating PHP doc blocks
  * [vim-pandoc/vim-pandoc](https://github.com/vim-pandoc/vim-pandoc) : provides facilities to integrate Vim with the pandoc document converter and work with documents written in its markdown variant
  * [vim-scripts/scratch.vim](https://github.com/vim-scripts/scratch.vim) : create a temporary scratch buffer to store and edit text that will be discarded
  * [vim-scripts/wordlist.vim](https://github.com/vim-scripts/wordlist.vim) : autocorrection of words
  * [weirongxu/plantuml-previewer.vim](https://github.com/weirongxu/plantuml-previewer.vim) : Vim/NeoVim plugin for preview PlantUML
## spell
  * [iamcco/coc-spell-checker](https://github.com/iamcco/coc-spell-checker) : Spelling Checker for vim
  * [inkarkat/vim-spellcheck](https://github.com/inkarkat/vim-spellcheck) : This plugin populates the |quickfix|-list with all spelling errors found in a buffer to give you that overview
  * [kamykn/spelunker.vim](https://github.com/kamykn/spelunker.vim) : improves Vim's spell checking function
  * [reedes/vim-lexical](https://github.com/reedes/vim-lexical) : extend vims spellchecker
## note
  * [2kabhishek/tdo.nvim](https://github.com/2kabhishek/tdo.nvim) : implement tdo in neovim
  * [ada0l/obsidian](https://github.com/ada0l/obsidian) : basic interaction with Obsidian
  * [ahmedkhalf/jupyter-nvim](https://github.com/ahmedkhalf/jupyter-nvim) : Read jupyter notebooks in neovim
  * [boson-joe/yanp](https://github.com/boson-joe/yanp) : Yes another notetaking plugin which supports recurring topics structure and customisable syntax
  * [dobrovolsky/kb-notes.nvim](https://github.com/dobrovolsky/kb-notes.nvim) : Yet another note management system for neovim
  * [epwalsh/obsidian.nvim](https://github.com/epwalsh/obsidian.nvim) : writing and navigating an Obsidian vault
  * [fmoralesc/vim-pad](https://github.com/fmoralesc/vim-pad) : quick notetaking plugin for vim
  * [goerz/jupytext.vim](https://github.com/goerz/jupytext.vim) : editing Jupyter notebook (ipynb) files through jupytext
  * [gu-fan/riv.vim](https://github.com/gu-fan/riv.vim) : Notes and wiki in rst
  * [jbyuki/nabla.nvim](https://github.com/jbyuki/nabla.nvim) : Take your scentific notes in Neovim
  * [jellyapple102/flote.nvim](https://github.com/jellyapple102/flote.nvim) : easy, minimal notes
  * [lervag/wiki.vim](https://github.com/lervag/wiki.vim) : This is for writing and maintaining a personal wiki
  * [linden-project/linny.vim](https://github.com/linden-project/linny.vim) : Personal wiki and document database
  * [mickael-menu/zk-nvim](https://github.com/mickael-menu/zk-nvim) : Neovim extension for the zk plain text note-taking assistant
  * [oberblastmeister/neuron.nvim](https://github.com/oberblastmeister/neuron.nvim) : Make neovim the best note taking application with neuron
  * [ostralyan/scribe.nvim](https://github.com/ostralyan/scribe.nvim) : convenient way to find and take notes
  * [phaazon/mind.nvim](https://github.com/phaazon/mind.nvim) : a new take on note taking and task workflows
  * [renerocksai/telekasten.nvim](https://github.com/renerocksai/telekasten.nvim) : A Neovim plugin for working with a text-based, markdown zettelkasten / wiki and mixing it with a journal, based on telescope.nvim
  * [rexagod/samwise.nvim](https://github.com/rexagod/samwise.nvim) : line-wise note-taking plugin for neovim
  * [rutatang/quicknote.nvim](https://github.com/rutatang/quicknote.nvim) : quick take that note
  * [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki) : VimWiki is a personal wiki for Vim
  * [xolox/vim-notes](https://github.com/xolox/vim-notes) : Easy note taking in Vim
## preview
  * [davidgranstrom/nvim-markdown-preview](https://github.com/davidgranstrom/nvim-markdown-preview) : Markdown preview in the browser using pandoc and live-server
  * [ellisonleao/glow.nvim](https://github.com/ellisonleao/glow.nvim) : Preview markdown code directly in your neovim terminal
  * [euclio/vim-markdown-composer](https://github.com/euclio/vim-markdown-composer) : adds asynchronous Markdown preview
  * [frabjous/knap](https://github.com/frabjous/knap) : live preview LaTeX or markdown (or even just HTML)
  * [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim) : Preview markdown on your modern browser with synchronised scrolling and flexible configuration
  * [instant-markdown/vim-instant-markdown](https://github.com/instant-markdown/vim-instant-markdown) : shows the compiled markdown in real-time
  * [junegunn/vim-xmark](https://github.com/junegunn/vim-xmark) : Markdown preview on OS X
  * [untitled-ai/jupyter_ascending](https://github.com/untitled-ai/jupyter_ascending) : Sync Jupyter Notebooks from any editor
## file-movment
  * [airblade/vim-rooter](https://github.com/airblade/vim-rooter) : go to projects root
  * [jedi2610/nvim-rooter.lua](https://github.com/jedi2610/nvim-rooter.lua) : high performance plugin to change your working directory to the project root when you open a file
  * [jinzhongjia/ps_manager.nvim](https://github.com/jinzhongjia/ps_manager.nvim) : auto change pwd in project
  * [leonheidelbach/trailblazer.nvim](https://github.com/leonheidelbach/trailblazer.nvim) : seamlessly move through project marks
  * [notjedi/nvim-rooter.lua](https://github.com/notjedi/nvim-rooter.lua) : change your working directory to the project root
  * [nyngwang/neoroot.lua](https://github.com/nyngwang/neoroot.lua) : toggle between own defined root and cwd of file
  * [oscarcreator/rsync.nvim](https://github.com/oscarcreator/rsync.nvim) : Async transfer files with `rsync` on save
  * [theprimeagen/harpoon](https://github.com/theprimeagen/harpoon) : mark files and more
  * [ygm2/rooter.nvim](https://github.com/ygm2/rooter.nvim) : changes current working directory to project root of the file opened in current buffer [archived] [no maintain]
## todo
  * [arnarg/todotxt.nvim](https://github.com/arnarg/todotxt.nvim) : view and add tasks stored in a todo.txt format
  * [aserebryakov/vim-todo-lists](https://github.com/aserebryakov/vim-todo-lists) : TODO lists management
  * [dhruvasagar/vim-dotoo](https://github.com/dhruvasagar/vim-dotoo) : awesome task manager & clocker inspired by org-mode
  * [folke/todo-comments.nvim](https://github.com/folke/todo-comments.nvim) : highlight and search for todo comments like TODO, HACK, BUG
  * [vuciv/vim-bujo](https://github.com/vuciv/vim-bujo) : easily manage todo manager
  * [wsdjeg/vim-todo](https://github.com/wsdjeg/vim-todo) : Better TODO manager plugin for neovim/vim
## markdown-langueges
  * [acksld/nvim-femaco.lua](https://github.com/acksld/nvim-femaco.lua) : Catalyze your Fenced Markdown Code-block editing
  * [axvr/org.vim](https://github.com/axvr/org.vim) : Org mode and Outline mode syntax highlighting for Vim
  * [gabrielelana/vim-markdown](https://github.com/gabrielelana/vim-markdown) : complete environment to create Markdown files with a syntax highlight that doesn't suck
  * [h2ero/vim-markdown-wiki](https://github.com/h2ero/vim-markdown-wiki) : markdown wiki pulgin for vim
  * [ixru/nvim-markdown](https://github.com/ixru/nvim-markdown) : Fork of vim-markdown with extra functionality
  * [jakewvincent/mkdnflow.nvim](https://github.com/jakewvincent/mkdnflow.nvim) : make it easy to navigate and manipulate markdown notebooks
  * [jceb/vim-orgmode](https://github.com/jceb/vim-orgmode) : Text outlining and task management for Vim based on Emacs’ Org-Mode
  * [jghauser/auto-pandoc.nvim](https://github.com/jghauser/auto-pandoc.nvim) : This plugin allows you to easily convert your markdown files using pandoc
  * [preservim/vim-markdown](https://github.com/preservim/vim-markdown) : Syntax highlighting, matching rules and mappings for the original Markdown and extensions
  * [ranjithshegde/orgwiki.nvim](https://github.com/ranjithshegde/orgwiki.nvim) : implements a subset of features from the popular vimwiki plugin for org filetype
  * [serenevoid/kiwi.nvim](https://github.com/serenevoid/kiwi.nvim) : stripped down version of vimwiki
  * [toppair/peek.nvim](https://github.com/toppair/peek.nvim) : Markdown preview plugin for Neovim
  * [vim-latex/vim-latex](https://github.com/vim-latex/vim-latex) : provides a rich tool of features for editing latex files
## snippets
  * [dcampos/nvim-snippy](https://github.com/dcampos/nvim-snippy) : A snippets plugin for Neovim 0.5.0+ written in Lua
  * [drmingdrmer/xptemplate](https://github.com/drmingdrmer/xptemplate) : Code snippets engine for Vim, And snippets library
  * [ellisonleao/carbon-now.nvim](https://github.com/ellisonleao/carbon-now.nvim) : Create beautiful code snippets directly from your neovim terminal
  * [garbas/vim-snipmate](https://github.com/garbas/vim-snipmate) : provide support for textual snippets, similar to TextMate or other Vim plugins like UltiSnips
  * [hauleth/usnip.vim](https://github.com/hauleth/usnip.vim) : Minimalistic snippet management for Vim
  * [honza/vim-snippets](https://github.com/honza/vim-snippets) : contains snippets files for various programming languages
  * [hrsh7th/vim-vsnip](https://github.com/hrsh7th/vim-vsnip) : VSCode(LSP)'s snippet feature in vim
  * [jorengarenar/minisnip](https://github.com/jorengarenar/minisnip) : miniSnipis lightweight and minimal snippet plugin written in Vim Script
  * [l3mon4d3/luasnip](https://github.com/l3mon4d3/luasnip) : snippet engine written in lua
  * [molleweide/luasnip-snippets.nvim](https://github.com/molleweide/luasnip-snippets.nvim) : community driven library of LuaSnipsnipets
  * [norcalli/snippets.nvim](https://github.com/norcalli/snippets.nvim) : snippets nvim
  * [quintik/snip](https://github.com/quintik/snip) : a vim plugin for creating and managing vim abbreviations [archived]
  * [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets) : Snippets collection for a set of different programming languages
  * [shougo/neosnippet-snippets](https://github.com/shougo/neosnippet-snippets) : The standard snippets repository for neosnippet
  * [shougo/neosnippet.vim](https://github.com/shougo/neosnippet.vim) : The Neosnippet plug-In adds snippet support to Vim
  * [sirver/ultisnips](https://github.com/sirver/ultisnips) : is the ultimate solution for snippets
## language
  * [akinsho/flutter-tools.nvim](https://github.com/akinsho/flutter-tools.nvim) : Build flutter and dart applications in neovim using the native LSP
  * [aldantas/vim-povray](https://github.com/aldantas/vim-povray) : povray filetype enhancement for vim
  * [amirrezaask/actions.nvim](https://github.com/amirrezaask/actions.nvim) : defines consistant interface for doing actions for multible languages
  * [anihm136/importmagic.nvim](https://github.com/anihm136/importmagic.nvim) : automatically import unresolved symbols in python
  * [aonemd/fmt.vim](https://github.com/aonemd/fmt.vim) : delegates the auto-formatting to a formatter
  * [arnaud-lb/vim-php-namespace](https://github.com/arnaud-lb/vim-php-namespace) : a vim plugin for inserting "use" statements automatically
  * [arp242/runbuf.vim](https://github.com/arp242/runbuf.vim) : makes it easy to run the contents of a buffer
  * [b0o/schemastore.nvim](https://github.com/b0o/schemastore.nvim) : Neovim Lua plugin providing access to the SchemaStore catalog
  * [benekastah/neomake](https://github.com/benekastah/neomake) : asynchronously run programs
  * [blindfs/vim-translator](https://github.com/blindfs/vim-translator) : A translation tool
  * [cademichael/zig.nvim](https://github.com/cademichael/zig.nvim) : Parody of emacs zig-mode
  * [chiel92/vim-autoformat](https://github.com/chiel92/vim-autoformat) : Format code with one button press (or automatically on save).
  * [civitasv/cmake-tools.nvim](https://github.com/civitasv/cmake-tools.nvim) : CMake Tools for Neovim
  * [code-biscuits/nvim-biscuits](https://github.com/code-biscuits/nvim-biscuits) : help you get the context of the end of that AST node
  * [crusj/hierarchy-tree-go.nvim](https://github.com/crusj/hierarchy-tree-go.nvim) : Hierarchy ui tree for go
  * [crusj/structrue-go.nvim](https://github.com/crusj/structrue-go.nvim) : A more intuitive display of the symbol structure of golang files
  * [cuducos/yaml.nvim](https://github.com/cuducos/yaml.nvim) : Simple tools to help developers working YAML in Neovim
  * [dag/vim-fish](https://github.com/dag/vim-fish) : support for editing fish scripts
  * [dahu/asif](https://github.com/dahu/asif) : uns a list of commands against a block of text (a list of lines) in a scratch buffer of a given filetype
  * [dbmrq/vim-dialect](https://github.com/dbmrq/vim-dialect) : quickly add to spellfile
  * [dccsillag/magma-nvim](https://github.com/dccsillag/magma-nvim) : NeoVim plugin for running code interactively with Jupyter
  * [devjoe/vim-codequery](https://github.com/devjoe/vim-codequery) : Search source code gracefully, Manage your database easily and Know your code more instantly
  * [dmmulroy/tsc.nvim](https://github.com/dmmulroy/tsc.nvim) : run typescript type-checking asynchronously
  * [elentok/format-on-save.nvim](https://github.com/elentok/format-on-save.nvim) : format on save
  * [erietz/vim-terminator](https://github.com/erietz/vim-terminator) : runs your current file
  * [ethanjwright/toolwindow.nvim](https://github.com/ethanjwright/toolwindow.nvim) : Easy management of a toolwindow
  * [figsoda/nix-develop.nvim](https://github.com/figsoda/nix-develop.nvim) : nix develop for neovim
  * [flow/vim-flow](https://github.com/flow/vim-flow) : A vim plugin for Flow
  * [gaodean/autolist.nvim](https://github.com/gaodean/autolist.nvim) : Automatic list continuation and formatting
  * [gbprod/phpactor.nvim](https://github.com/gbprod/phpactor.nvim) : Lua version of phpactor nvim plugin
  * [gleitz/howdoi](https://github.com/gleitz/howdoi) : Instant coding answers via the command line
  * [hanschen/vim-ipython-cell](https://github.com/hanschen/vim-ipython-cell) : Seamlessly run Python code from Vim in IPython
  * [is0n/jaq-nvim](https://github.com/is0n/jaq-nvim) : Just Another Quickrun plugin for Neovim that was inspired by quickrun.vim
  * [jaawerth/fennel-nvim](https://github.com/jaawerth/fennel-nvim) : adding native fennel support to nvim by utilizing neovim's native Lua support
  * [jakewvincent/texmagic.nvim](https://github.com/jakewvincent/texmagic.nvim) : TEXMagic is a very simple Neovimplugin that facilitates LaTeX build engine selection via magic comments
  * [jbyuki/carrot.nvim](https://github.com/jbyuki/carrot.nvim) : Markdown evaluator for Neovim Lua code blocks
  * [jdelkins/vim-correction](https://github.com/jdelkins/vim-correction) : automatically correct spelling
  * [jeetsukumaran/vim-pythonsense](https://github.com/jeetsukumaran/vim-pythonsense) : provides text objects and motions for Python classes, methods, functions, and doc strings
  * [jorengarenar/vim-sbnr](https://github.com/jorengarenar/vim-sbnr) : Simple Build&Run for Vim [archived]
  * [jorengarenar/vim-sql-upper](https://github.com/jorengarenar/vim-sql-upper) : Uppercase SQL keywords without the need of holding Shift or CAPS LOCK
  * [jose-elias-alvarez/nvim-lsp-ts-utils](https://github.com/jose-elias-alvarez/nvim-lsp-ts-utils) : Utilities to improve the TypeScript development experience for Neovim's built-in LSP client [archived]
  * [jsborjesson/vim-uppercase-sql](https://github.com/jsborjesson/vim-uppercase-sql) : auto uppercase sql keywords
  * [junegunn/vim-cfr](https://github.com/junegunn/vim-cfr) : Decompile Java class files using CFR
  * [justinmk/vim-printf](https://github.com/justinmk/vim-printf) : turn a line into a printf-style statment
  * [kovisoft/paredit](https://github.com/kovisoft/paredit) : Structured Editing of Lisp S-expressions
  * [kovisoft/slimv](https://github.com/kovisoft/slimv) : Superior Lisp Interaction Mode for Vim
  * [krady21/compiler-explorer.nvim](https://github.com/krady21/compiler-explorer.nvim) : compiler explorer inside neovim
  * [laytan/tailwind-sorter.nvim](https://github.com/laytan/tailwind-sorter.nvim) : sort tailwind classes
  * [ledesmablt/vim-run](https://github.com/ledesmablt/vim-run) : Run, view, and manage UNIX shell commands with ease
  * [llllvvuu/nvim-js-actions](https://github.com/llllvvuu/nvim-js-actions) : ts actions on javascript code
  * [max397574/lua-dev.nvim](https://github.com/max397574/lua-dev.nvim) : Dev setup for init.lua and plugin development
  * [mhartington/formatter.nvim](https://github.com/mhartington/formatter.nvim) : A format runner for Neovim
  * [mhartington/nvim-typescript](https://github.com/mhartington/nvim-typescript) : nvim language service plugin for typescript
  * [mhinz/vim-crates](https://github.com/mhinz/vim-crates) : When maintaining Rust projects, this plugin helps with updating the dependencies in `Cargo.toml` files
  * [mhinz/vim-mix-format](https://github.com/mhinz/vim-mix-format) : makes it easy to run elixirs `mix format` asynchronously
  * [micmine/jumpwire.nvim](https://github.com/micmine/jumpwire.nvim) : for moving in common File structures (like test and implementation files)
  * [millermedeiros/vim-esformatter](https://github.com/millermedeiros/vim-esformatter) : makes it easier to execute esformatter inside vim
  * [moll/vim-node](https://github.com/moll/vim-node) : Tools to make Vim superb for developing with Node.js
  * [nanotee/sqls.nvim](https://github.com/nanotee/sqls.nvim) : Neovim plugin for sqls that leverages the built-in LSP client
  * [neomake/neomake](https://github.com/neomake/neomake) : plugin for Vim to asynchronously run programs
  * [nfischer/vim-rainbows](https://github.com/nfischer/vim-rainbows) : Vim runtime files for my own language, Rainbows
  * [niuiic/format.nvim](https://github.com/niuiic/format.nvim) : Async, multitask, configurable formatter
  * [noib3/nvim-oxi](https://github.com/noib3/nvim-oxi) : provides first-class Rust bindings to the rich API exposed by nvim
  * [ntbbloodbath/zig-tools.nvim](https://github.com/ntbbloodbath/zig-tools.nvim) : tools for zig
  * [nvim-treesitter/nvim-treesitter-refactor](https://github.com/nvim-treesitter/nvim-treesitter-refactor) : Refactor modules for nvim-treesitter [treesitter]
  * [olexsmir/gopher.nvim](https://github.com/olexsmir/gopher.nvim) : Minimalistic plugin for Go development in Neovim written in Lua
  * [olical/aniseed](https://github.com/olical/aniseed) : bridges the gap between Fennel and Neovim
  * [olical/conjure](https://github.com/olical/conjure) : an interactive environment for evaluating code within your running program
  * [osyo-manga/vim-precious](https://github.com/osyo-manga/vim-precious) : Set the buffer filetype based on the code block the cursor currently resides in
  * [pangloss/vim-javascript](https://github.com/pangloss/vim-javascript) : JavaScript bundle for vim
  * [pappasam/vim-filetype-formatter](https://github.com/pappasam/vim-filetype-formatter) : simple, cross language Vim code formatter plugin supporting both range and full-file formatting
  * [pgdouyon/vim-accio](https://github.com/pgdouyon/vim-accio) : Accio asynchronously summons build/compiler/linter
  * [phpactor/phpactor](https://github.com/phpactor/phpactor) : aims to provide heavy-lifting refactoring and introspection tools
  * [pianocomposer321/yabs.nvim](https://github.com/pianocomposer321/yabs.nvim) : Yet Another Build System for Neovim
  * [pkazmier/java_getset.vim](https://github.com/pkazmier/java_getset.vim) : file type plugin for the creation of Java getters and setters
  * [potamides/pantran.nvim](https://github.com/potamides/pantran.nvim) : use your favorite machine translation engines without having to leave
  * [preservim/vim-lexical](https://github.com/preservim/vim-lexical) : a bunch of spellchecker improvments
  * [pwntester/codeql.nvim](https://github.com/pwntester/codeql.nvim) : help writing and testing CodeQL queries
  * [rafaelsq/nvim-goc.lua](https://github.com/rafaelsq/nvim-goc.lua) : easy go coverage
  * [rafcamlet/nvim-luapad](https://github.com/rafcamlet/nvim-luapad) : Interactive neovim scratchpad for lua
  * [ray-x/go.nvim](https://github.com/ray-x/go.nvim) : modern go neovim plugin based on treesitter, nvim-lsp and dap debugger
  * [rescript-lang/vim-rescript](https://github.com/rescript-lang/vim-rescript) : the official vim plugin for ReScript
  * [rest-nvim/rest.nvim](https://github.com/rest-nvim/rest.nvim) : fast http client
  * [romgrk/nvim-treesitter-context](https://github.com/romgrk/nvim-treesitter-context) : Lightweight alternative to context.vim implemented with nvim-treesitter
  * [sbdchd/neoformat](https://github.com/sbdchd/neoformat) : vim plugin for formatting code
  * [scalameta/nvim-metals](https://github.com/scalameta/nvim-metals) : provide a better experience while using Metals
  * [shatur/neovim-tasks](https://github.com/shatur/neovim-tasks) : provides a stateful task system
  * [sheerun/vim-polyglot](https://github.com/sheerun/vim-polyglot) : A collection of language packs for Vim
  * [shinglyu/vim-codespell](https://github.com/shinglyu/vim-codespell) : checking the spelling for source code
  * [sigmasd/deno-nvim](https://github.com/sigmasd/deno-nvim) : improve deno experience
  * [simrat39/rust-tools.nvim](https://github.com/simrat39/rust-tools.nvim) : Extra rust tools for writing applications in neovim using the native lsp
  * [skanehira/denops-translate.vim](https://github.com/skanehira/denops-translate.vim) : A translation tool using denops
  * [stephpy/vim-php-cs-fixer](https://github.com/stephpy/vim-php-cs-fixer) : will execute the `php-cs-fixercommand` on the directory or file
  * [stevearc/overseer.nvim](https://github.com/stevearc/overseer.nvim) : task runner and job management plugin for Neovim
  * [sukima/xmledit](https://github.com/sukima/xmledit) : a file type plugin to help edit XML
  * [t9md/vim-ruby-xmpfilter](https://github.com/t9md/vim-ruby-xmpfilter) : Support rcodetools and seeing_is_believing
  * [teal-language/vim-teal](https://github.com/teal-language/vim-teal) : provides Teal language support for Vim
  * [ternjs/tern_for_vim](https://github.com/ternjs/tern_for_vim) : provides Tern-based JavaScript editing support
  * [tjdevries/nlua.nvim](https://github.com/tjdevries/nlua.nvim) : Lua Development for Neovim
  * [tpope/vim-endwise](https://github.com/tpope/vim-endwise) : helps to end certain structures automatically, like adding `end` after `if`,`while`... in lua.
  * [tpope/vim-liquid](https://github.com/tpope/vim-liquid) : liquid support for vim
  * [tpope/vim-rails](https://github.com/tpope/vim-rails) : Vim plugin for editing Ruby on Rails applications
  * [tpope/vim-rake](https://github.com/tpope/vim-rake) : a plugin leveraging projectionist.vim to enable you to use all those parts of rails.vim that you wish you could use on your other Ruby projects
  * [tpope/vim-salve](https://github.com/tpope/vim-salve) : Static Vim support for Leiningen, Boot, and the Clojure CLI
  * [turbio/bracey.vim](https://github.com/turbio/bracey.vim) : live html,css,js editing in vim
  * [tweekmonster/django-plus.vim](https://github.com/tweekmonster/django-plus.vim) : improves django development
  * [tweekmonster/gofmt.vim](https://github.com/tweekmonster/gofmt.vim) : runs gofmtwhen you save
  * [tweekmonster/hl-goimport.vim](https://github.com/tweekmonster/hl-goimport.vim) : Highlights imported packages in Go
  * [tweekmonster/impsort.vim](https://github.com/tweekmonster/impsort.vim) : sorting and highlighting Python imports
  * [valpackett/intero.nvim](https://github.com/valpackett/intero.nvim) : really fast omnicomplete for haskell
  * [vim-denops/denops.vim](https://github.com/vim-denops/denops.vim) : An ecosystem of Vim/Neovim which allows developers to write plugins in Deno
  * [vim-scripts/java_getset.vim](https://github.com/vim-scripts/java_getset.vim) : automatically add getter/setter
  * [vimjas/vim-python-pep8-indent](https://github.com/vimjas/vim-python-pep8-indent) : modifies vim’s indentation behavior to comply with PEP8 and my aesthetic preferences
  * [vincentcordobes/vim-translate](https://github.com/vincentcordobes/vim-translate) : A tiny translate-shell wrapper
  * [wbthomason/buildit.nvim](https://github.com/wbthomason/buildit.nvim) : A better async project builder for Neovim
  * [wsdjeg/vim-assembly](https://github.com/wsdjeg/vim-assembly) : Vim mode for assembly languages
  * [yioneko/nvim-yati](https://github.com/yioneko/nvim-yati) : Yet another tree-sitter indent plugin for Neovim
  * [zeioth/compiler.nvim](https://github.com/zeioth/compiler.nvim) : build/run code with zero config
## lsp
  * [ahmedkhalf/lsp-rooter.nvim](https://github.com/ahmedkhalf/lsp-rooter.nvim) : change the current working directory to the project's root directory[archived]
  * [alexaandru/nvim-lspupdate](https://github.com/alexaandru/nvim-lspupdate) : Updates installed (or auto installs if missing) LSP servers, that are already configured in your init.vim
  * [amrbashir/nvim-docs-view](https://github.com/amrbashir/nvim-docs-view) : neovim plugin to display lsp hover documentation in a side panel
  * [anott03/nvim-lspinstall](https://github.com/anott03/nvim-lspinstall) : the plugin makes it really easy to install language servers for nvims built in lsp
  * [artempyanykh/marksman](https://github.com/artempyanykh/marksman) : Markdown LSP server providing completion, goto, references, diagnostics, and more
  * [artur-shaik/jc.nvim](https://github.com/artur-shaik/jc.nvim) : jc LSP
  * [autozimu/languageclient-neovim](https://github.com/autozimu/languageclient-neovim) : LSP support
  * [aznhe21/actions-preview.nvim](https://github.com/aznhe21/actions-preview.nvim) : preview lsp actions
  * [creativenull/diagnosticls-configs-nvim](https://github.com/creativenull/diagnosticls-configs-nvim) : a list of diagnostic configs for diagnostic-langaugeserver
  * [davidhalter/jedi-vim](https://github.com/davidhalter/jedi-vim) : awesome Python autocompletion with VIM
  * [dnlhc/glance.nvim](https://github.com/dnlhc/glance.nvim) : preview, navigate and edit LSP locations
  * [folke/lsp-colors.nvim](https://github.com/folke/lsp-colors.nvim) : Automatically creates missing LSP diagnostics highlight groups for color schemes that don't yet support the Neovim 0.5 builtin lsp client
  * [folke/trouble.nvim](https://github.com/folke/trouble.nvim) : A pretty list for showing diagnostics, references, telescope results, quickfix and location lists to help you solve all the trouble your code is causing
  * [glepnir/lspsaga.nvim](https://github.com/glepnir/lspsaga.nvim) : A light-weight lsp plugin based on neovim's built-in lsp with a highly performant UI
  * [hrsh7th/vim-lamp](https://github.com/hrsh7th/vim-lamp) : Language Server Protocol client for Vim
  * [idanarye/nvim-buffls](https://github.com/idanarye/nvim-buffls) : a [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) source
  * [j-hui/fidget.nvim](https://github.com/j-hui/fidget.nvim) : Standalone UI for nvim-lsp progress
  * [jbyuki/one-small-step-for-vimkind](https://github.com/jbyuki/one-small-step-for-vimkind) : an adapter for the Neovim lua language
  * [jinzhongjia/lspui.nvim](https://github.com/jinzhongjia/lspui.nvim) : UI that wraps lsp operations
  * [jmbuhr/otter.nvim](https://github.com/jmbuhr/otter.nvim) : lsp for embedded code
  * [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) : Use Neovim as a language server to inject LSP diagnostics, code actions, and more via Lua
  * [junnplus/nvim-lsp-setup](https://github.com/junnplus/nvim-lsp-setup) : simple wrapper for nvim-lspconfig and nvim-lsp-installer to easily setup LSP servers
  * [kkharji/lspsaga.nvim](https://github.com/kkharji/lspsaga.nvim) : light-weight lsp plugin based on neovim built-in lsp with highly a performant UI
  * [kosayoda/nvim-lightbulb](https://github.com/kosayoda/nvim-lightbulb) : VSCode bulb for neovim's built-in LSP
  * [linrongbin16/lsp-progress.nvim](https://github.com/linrongbin16/lsp-progress.nvim) : performant lsp progress status
  * [liuchengxu/vista.vim](https://github.com/liuchengxu/vista.vim) : View and search LSP symbols, tags
  * [lukas-reineke/lsp-format.nvim](https://github.com/lukas-reineke/lsp-format.nvim) : a wrapper around Neovims native LSP formatting
  * [mfussenegger/nvim-jdtls](https://github.com/mfussenegger/nvim-jdtls) : Extensions for the built-in Language Server Protocol support in Neovim (>= 0.6.0) for eclipse.jdt.ls
  * [muniftanjim/prettier.nvim](https://github.com/muniftanjim/prettier.nvim) : Prettier plugin for Neovim's built-in LSP client
  * [nanotee/nvim-lsp-basics](https://github.com/nanotee/nvim-lsp-basics) : The shiny new built-in LSP client
  * [natebosch/vim-lsc](https://github.com/natebosch/vim-lsc) : Adds language-aware tooling to vim by communicating with a language server following the language server protocol
  * [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) : Configs for the Nvim LSP client
  * [niuiic/part-edit.nvim](https://github.com/niuiic/part-edit.nvim) : create a separate buffer for codeblocks to with with lsp
  * [nvim-lua/lsp_extensions.nvim](https://github.com/nvim-lua/lsp_extensions.nvim) : various lsp extensions [archived]
  * [onsails/diaglist.nvim](https://github.com/onsails/diaglist.nvim) : Live-updating Neovim LSP diagnostics in quickfix and loclist
  * [onsails/lspkind-nvim](https://github.com/onsails/lspkind-nvim) : tiny plugin adds vscode-like pictograms to neovim built-in lsp
  * [onsails/lspkind.nvim](https://github.com/onsails/lspkind.nvim) : adds vscode-like pictograms to neovim built-in lsp
  * [prabirshrestha/vim-lsp](https://github.com/prabirshrestha/vim-lsp) : Async Language Server Protocol plugin for vim8 and neovim
  * [ranjithshegde/ccls.nvim](https://github.com/ranjithshegde/ccls.nvim) : neovim plugin to configure ccls language server
  * [ray-x/lsp_signature.nvim](https://github.com/ray-x/lsp_signature.nvim) : Show function signature when you type
  * [ray-x/navigator.lua](https://github.com/ray-x/navigator.lua) : lsp navigation and highlighting and more
  * [rishabhrd/nvim-lsputils](https://github.com/rishabhrd/nvim-lsputils) : focuses on making nvim LSP actions highly user friendly
  * [rmagatti/goto-preview](https://github.com/rmagatti/goto-preview) : previewing native LSP's goto definition calls in floating windows
  * [smjonas/inc-rename.nvim](https://github.com/smjonas/inc-rename.nvim) : provides a command for LSP renaming with immediate visual feedback
  * [tamago324/nlsp-settings.nvim](https://github.com/tamago324/nlsp-settings.nvim) : configure Neovim LSP using json/yaml files like coc-settings.json
  * [vonheikemen/lsp-zero.nvim](https://github.com/vonheikemen/lsp-zero.nvim) : "boilerplate code" to make cmp and lspconf work
  * [wbthomason/lsp-status.nvim](https://github.com/wbthomason/lsp-status.nvim) : generating statusline components from the built-in LSP client
  * [weilbith/nvim-lsp-bacomp](https://github.com/weilbith/nvim-lsp-bacomp) : NeoVim Language Server Backwards Compatibility
  * [weilbith/nvim-lsp-smag](https://github.com/weilbith/nvim-lsp-smag) : allows to seamlessly integrate the language server protocol into NeoVim
  * [williamboman/nvim-lsp-installer](https://github.com/williamboman/nvim-lsp-installer) : allow you to manage LSP servers
## lint
  * [creativenull/efmls-configs-nvim](https://github.com/creativenull/efmls-configs-nvim) : a list of lint configs for efm-langserver
  * [dense-analysis/ale](https://github.com/dense-analysis/ale) : Asynchronous Lint Engine
  * [mfussenegger/nvim-lint](https://github.com/mfussenegger/nvim-lint) : An asynchronous linter plugin for Neovim
  * [nvie/vim-flake8](https://github.com/nvie/vim-flake8) : runs the currently open file through Flake8, a static syntax and style checker for Python source code
  * [nvimdev/guard.nvim](https://github.com/nvimdev/guard.nvim) : Async format and lint
  * [vim-syntastic/syntastic](https://github.com/vim-syntastic/syntastic) : Syntastic is a syntax checking plugin for Vim [no maintain]
  * [w0rp/ale](https://github.com/w0rp/ale) : ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax checking and semantic errors)
## autocomplete
  * [ackyshake/vimcompletesme](https://github.com/ackyshake/vimcompletesme) : super simple, super minimal, super light-weight tab-completion plugin
  * [ajh17/vimcompletesme](https://github.com/ajh17/vimcompletesme)
  * [exafunction/codeium.vim](https://github.com/exafunction/codeium.vim) : free ai autocompletion
  * [folke/neodev.nvim](https://github.com/folke/neodev.nvim) : adds full signature support for autocompletion of vim
  * [furkanzmc/sekme.nvim](https://github.com/furkanzmc/sekme.nvim) : a chain-completion plugin that complements Neovim's own completion functions
  * [github/copilot.vim](https://github.com/github/copilot.vim) : Vim plugin for GitHub Copilot
  * [haorenw1025/completion-nvim](https://github.com/haorenw1025/completion-nvim) : an auto completion framework
  * [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming) : provides statistical whole lines completions for git projects
  * [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp) : A completion engine plugin for neovim written in Lua
  * [hrsh7th/nvim-compe](https://github.com/hrsh7th/nvim-compe) : Auto completion plugin for nvim [archived]
  * [inkarkat/vim-patterncomplete](https://github.com/inkarkat/vim-patterncomplete) : offers completions that either use the last search pattern or query for a regular expression
  * [jimmyhuang454/easycompleteyou](https://github.com/jimmyhuang454/easycompleteyou) : Easily complete you "Keep It Simple, Stupid."
  * [kristijanhusak/vim-dadbod-completion](https://github.com/kristijanhusak/vim-dadbod-completion) : Database auto completion powered by vim-dadbod
  * [lifepillar/vim-mucomplete](https://github.com/lifepillar/vim-mucomplete) : minimalist autocompletion plugin for Vim
  * [maralla/completor.vim](https://github.com/maralla/completor.vim)
  * [mfussenegger/nvim-lsp-compl](https://github.com/mfussenegger/nvim-lsp-compl) : A fast and asynchronous auto-completion plugin for Neovim >= 0.7.0, focused on LSP
  * [mjbrownie/vim-htmldjango_omnicomplete](https://github.com/mjbrownie/vim-htmldjango_omnicomplete) : Vim htmldjango autocomplete
  * [ms-jpq/coq_nvim](https://github.com/ms-jpq/coq_nvim) : autocoplete wich is fast and has loads of features
  * [ncm2/ncm2](https://github.com/ncm2/ncm2) : is a slim, fast and hackable completion framework for neovim
  * [neoclide/coc.nvim](https://github.com/neoclide/coc.nvim) : conquer of completion
  * [noib3/nvim-compleet](https://github.com/noib3/nvim-compleet)
  * [nvim-lua/completion-nvim](https://github.com/nvim-lua/completion-nvim) : auto completion framework that aims to provide a better completion experience with neovim's built-in LSP [archived]
  * [prabirshrestha/asyncomplete.vim](https://github.com/prabirshrestha/asyncomplete.vim) : Async autocompletion for Vim 8 and Neovim with |timers|.
  * [rip-rip/clang_complete](https://github.com/rip-rip/clang_complete) : This plugin uses clang for accurately completing C and C++ code
  * [roxma/nvim-completion-manager](https://github.com/roxma/nvim-completion-manager) : A Completion Framework for Neovim [archived]
  * [shawncplus/phpcomplete.vim](https://github.com/shawncplus/phpcomplete.vim) : Improved PHP omni-completion
  * [shougo/ddc.vim](https://github.com/shougo/ddc.vim) : Dark deno-powered completion framework for neovim/Vim8
  * [shougo/deoplete.nvim](https://github.com/shougo/deoplete.nvim) : dark powered neo-completion [no development]
  * [shougo/neocomplcache.vim](https://github.com/shougo/neocomplcache.vim) : provides keyword completion system by maintaining a cache of keywords in the current buffer
  * [shougo/neocomplete.vim](https://github.com/shougo/neocomplete.vim) : provides keyword completion system by maintaining a cache of keywords in the current buffer [no development]
  * [vigoux/complementree.nvim](https://github.com/vigoux/complementree.nvim)
  * [ycm-core/youcompleteme](https://github.com/ycm-core/youcompleteme)
  * [zbirenbaum/copilot.lua](https://github.com/zbirenbaum/copilot.lua) : pure lua replacement for [github/copilot.vim](https://github.com/github/copilot.vim)
## syntax
  * [aklt/plantuml-syntax](https://github.com/aklt/plantuml-syntax) : Vim PlantUML Syntax/Plugin/FTDetect
  * [akz92/vim-ionic2](https://github.com/akz92/vim-ionic2) : ionic2 syntax highlight
  * [cespare/vim-toml](https://github.com/cespare/vim-toml) : toml syntax highlight
  * [dagwieers/asciidoc-vim](https://github.com/dagwieers/asciidoc-vim) : AsciiDoc syntax highlighting
  * [euclidianace/betterlua.vim](https://github.com/euclidianace/betterlua.vim) : Better Lua Syntax For Vim
  * [fladson/vim-kitty](https://github.com/fladson/vim-kitty) : Syntax highlighting for Kitty terminal config files
  * [glench/vim-jinja2-syntax](https://github.com/glench/vim-jinja2-syntax) : Jinja2 syntax file for vim with the ability to detect either HTML or Jinja
  * [google/vim-jsonnet](https://github.com/google/vim-jsonnet) : Jsonnet filetype plugin for Vim
  * [groenewege/vim-less](https://github.com/groenewege/vim-less) : adds syntax highlighting, indenting and autocompletion for the dynamic stylesheet language LESS
  * [herringtondarkholme/yats.vim](https://github.com/herringtondarkholme/yats.vim) : Yet Another TypeScript Syntax
  * [honza/dockerfile.vim](https://github.com/honza/dockerfile.vim) : Syntax highlighting for Dockerfiles [archived]
  * [iron-e/vim-ungrammar](https://github.com/iron-e/vim-ungrammar) : syntax for Ungrammar filetype
  * [jackguo380/vim-lsp-cxx-highlight](https://github.com/jackguo380/vim-lsp-cxx-highlight) : provides C/C++/Cuda/ObjC semantic highlighting using LSP
  * [jelera/vim-javascript-syntax](https://github.com/jelera/vim-javascript-syntax) : Enhanced JavaScript Syntax for Vim
  * [junegunn/vim-journal](https://github.com/junegunn/vim-journal) : syntax for journal file type
  * [jwalton512/vim-blade](https://github.com/jwalton512/vim-blade) : blade template syntax highlight
  * [kchmck/vim-coffee-script](https://github.com/kchmck/vim-coffee-script) : adds CoffeeScript support to vim
  * [kovetskiy/sxhkd-vim](https://github.com/kovetskiy/sxhkd-vim) : sxhkd syntax highlight
  * [leafgarland/typescript-vim](https://github.com/leafgarland/typescript-vim) : typeScript syntax for vim
  * [ledger/vim-ledger](https://github.com/ledger/vim-ledger) : Filetype detection, syntax highlighting, auto-formatting, auto-completion, and other tools for working with ledger files
  * [lervag/vimtex](https://github.com/lervag/vimtex) : modern Vim filetype and syntax plugin for LaTeX files
  * [lifepillar/pgsql.vim](https://github.com/lifepillar/pgsql.vim) : provides syntax highlighting and auto-completion support for PostgreSQL
  * [maxmellon/vim-jsx-pretty](https://github.com/maxmellon/vim-jsx-pretty) : The React syntax highlighting and indenting plugin (Also supports the typescript tsx file)
  * [milisims/tree-sitter-org](https://github.com/milisims/tree-sitter-org) : Org grammar for tree-sitter
  * [mxw/vim-jsx](https://github.com/mxw/vim-jsx) : Syntax highlighting and indenting for JSX [deprecated]
  * [nathanalderson/yang.vim](https://github.com/nathanalderson/yang.vim) : YANG syntax highlighting and other niceties for VIM
  * [neovimhaskell/haskell-vim](https://github.com/neovimhaskell/haskell-vim) : Syntax Highlighting and Indentation for Haskell and Cabal
  * [nickeb96/fish.vim](https://github.com/nickeb96/fish.vim) : fish syntax for vim
  * [nickhutchinson/vim-cmake-syntax](https://github.com/nickhutchinson/vim-cmake-syntax) : Vim syntax highlighting rules for modern CMake [archived]
  * [octol/vim-cpp-enhanced-highlight](https://github.com/octol/vim-cpp-enhanced-highlight) : contains additional syntax highlighting that I use for C++11/14/17 development in Vim
  * [othree/es.next.syntax.vim](https://github.com/othree/es.next.syntax.vim) : This syntax file is for ECMAScript future syntax
  * [othree/html5.vim](https://github.com/othree/html5.vim) : HTML5 + inline SVG omnicomplete function, indent and syntax for Vim
  * [othree/javascript-libraries-syntax.vim](https://github.com/othree/javascript-libraries-syntax.vim) : Syntax file for JavaScript libraries
  * [othree/yajs.vim](https://github.com/othree/yajs.vim) : Yet Another JavaScript Syntax file for Vim
  * [pboettch/vim-cmake-syntax](https://github.com/pboettch/vim-cmake-syntax) : Vim syntax highlighting rules for modern CMakeLists.txt
  * [peitalin/vim-jsx-typescript](https://github.com/peitalin/vim-jsx-typescript) : Syntax highlighting and indentation for JSX in Typescript
  * [plasticboy/vim-markdown](https://github.com/plasticboy/vim-markdown) : Syntax highlighting, matching rules and mappings for the original Markdown and extensions
  * [potatoesmaster/i3-vim-syntax](https://github.com/potatoesmaster/i3-vim-syntax) : i3 config syntax highlight
  * [shougo/neco-syntax](https://github.com/shougo/neco-syntax) : Syntax source for neocomplete/deoplete/ncm
  * [slim-template/vim-slim](https://github.com/slim-template/vim-slim) : slim syntax highlighting for vim
  * [solarnz/thrift.vim](https://github.com/solarnz/thrift.vim) : thrift syntax plugin for vim
  * [stanangeloff/php.vim](https://github.com/stanangeloff/php.vim) : An up-to-date Vim syntax for PHP [archived]
  * [stephpy/vim-yaml](https://github.com/stephpy/vim-yaml) : Syntax file for yaml
  * [tbastos/vim-lua](https://github.com/tbastos/vim-lua) : Improved Lua 5.3 syntax and indentation support for Vim
  * [tetralux/odin.vim](https://github.com/tetralux/odin.vim) : syntax highlite for Odin
  * [tomlion/vim-solidity](https://github.com/tomlion/vim-solidity) : Syntax files for Solidity
  * [towolf/vim-helm](https://github.com/towolf/vim-helm) : vim syntax for helm templates
  * [vhda/verilog_systemverilog.vim](https://github.com/vhda/verilog_systemverilog.vim) : Vim Syntax Plugin for Verilog and SystemVerilog
  * [vim-python/python-syntax](https://github.com/vim-python/python-syntax) : Python syntax highlighting for Vim
  * [vim-ruby/vim-ruby](https://github.com/vim-ruby/vim-ruby) : includes syntax highlighting, indentation, omnicompletion, and various useful tools and mappings for writing ruby code
  * [vim-scripts/gitignore.vim](https://github.com/vim-scripts/gitignore.vim) : adds syntax highlighting, code snippets for .gitignore files
  * [vim-scripts/php.vim--garvin](https://github.com/vim-scripts/php.vim--garvin) : an updated version of the php.vim syntax file distributed with VIM
  * [wsdjeg/syntastic](https://github.com/wsdjeg/syntastic) : syntax checking plugin
## integration
  * [acksld/nvim-gfold.lua](https://github.com/acksld/nvim-gfold.lua) : nvim plugin for gfold
  * [adoy/vim-php-refactoring-toolbox](https://github.com/adoy/vim-php-refactoring-toolbox) : PHP refactoring toolbox
  * [ccchapman/watson.nvim](https://github.com/ccchapman/watson.nvim) : An integration for Watson in Neovim
  * [crispgm/nvim-go](https://github.com/crispgm/nvim-go) : A minimal implementation of Golang development plugin written in Lua for Neovim
  * [david-kunz/jester](https://github.com/david-kunz/jester) : A Neovim plugin to easily run and debug Jest tests
  * [elixir-editors/vim-elixir](https://github.com/elixir-editors/vim-elixir) : Elixir support for vim
  * [guns/vim-clojure-static](https://github.com/guns/vim-clojure-static) : clojure and ClojureScript highlighting/indentation/Basic insert mode completion
  * [guns/vim-slamhound](https://github.com/guns/vim-slamhound) : Slamhound integration for vim
  * [jalvesaq/nvim-r](https://github.com/jalvesaq/nvim-r) : improves Vim's support to edit R code
  * [jose-elias-alvarez/typescript.nvim](https://github.com/jose-elias-alvarez/typescript.nvim) : minimal `typescript-language-serverintegration` plugin to set up the language server via nvim-lspconfigand add commands for convenience
  * [jupyter-vim/jupyter-vim](https://github.com/jupyter-vim/jupyter-vim) : A two-way integration between Vim and Jupyter
  * [keith/swift.vim](https://github.com/keith/swift.vim) : syntax and indent for swift
  * [lhkipp/nvim-nu](https://github.com/lhkipp/nvim-nu) : support for the nushell language
  * [madskjeldgaard/reaper-nvim](https://github.com/madskjeldgaard/reaper-nvim) : controlling the Reaper DAW
  * [mrcjkb/haskell-tools.nvim](https://github.com/mrcjkb/haskell-tools.nvim) : Supercharge your Haskell experience in Neovim
  * [neovim/go-client](https://github.com/neovim/go-client) : Neovim/go-client is a Neovim client and plugin host for Go
  * [racer-rust/vim-racer](https://github.com/racer-rust/vim-racer) : allows vim to use Racer for Rust code completion and navigation
  * [rust-lang/rust.vim](https://github.com/rust-lang/rust.vim) : Vim plugin that provides Rust file detection, syntax highlighting, formatting, Syntastic integration, and more
  * [sakhnik/nvim-gdb](https://github.com/sakhnik/nvim-gdb) : Gdb, LLDB, pdb/pdb++ and BASHDB integration with NeoVim
  * [someone-stole-my-name/yaml-companion.nvim](https://github.com/someone-stole-my-name/yaml-companion.nvim) : yaml integration for vim
  * [stsewd/sphinx.nvim](https://github.com/stsewd/sphinx.nvim) : Sphinx integrations for Neovim
  * [svermeulen/nvim-moonmaker](https://github.com/svermeulen/nvim-moonmaker) : adds support for writing moonscript plugins
## fennel
  * [olical/nfnl](https://github.com/olical/nfnl) : better fennel inside neovim
  * [rktjmp/hotpot.nvim](https://github.com/rktjmp/hotpot.nvim) : Seamless Fennel inside Neovim
## test
  * [hkupty/runes.nvim](https://github.com/hkupty/runes.nvim) : Lua test framework for neovim plugins
  * [janko-m/vim-test](https://github.com/janko-m/vim-test) : A Vim wrapper for running tests on different granularities
  * [junegunn/vader.vim](https://github.com/junegunn/vader.vim) : I use Vader to test Vimscript
  * [nvim-neotest/neotest](https://github.com/nvim-neotest/neotest) : A framework for interacting with tests within NeoVim
  * [p00f/cphelper.nvim](https://github.com/p00f/cphelper.nvim) : automating tasks in competitive programming like downloading test cases, compiling and testing
  * [rcarriga/vim-ultest](https://github.com/rcarriga/vim-ultest) : The ultimate testing plugin for NeoVim
  * [thinca/vim-themis](https://github.com/thinca/vim-themis) : testing framework for Vim script
  * [vim-php/vim-phpunit](https://github.com/vim-php/vim-phpunit) : allows you to run PHP Unit tests easily
  * [vim-test/vim-test](https://github.com/vim-test/vim-test) : Vim wrapper for running tests on different granularities
  * [wsdjeg/javaunit.vim](https://github.com/wsdjeg/javaunit.vim) : test the current methond
  * [xeluxee/competitest.nvim](https://github.com/xeluxee/competitest.nvim) : a testcase manager and checker
## debug
  * [andrewferrier/debugprint.nvim](https://github.com/andrewferrier/debugprint.nvim) : simply print debug messages
  * [dbgx/lldb.nvim](https://github.com/dbgx/lldb.nvim) : provides LLDB debugger integration for Neovim [no maintain]
  * [jodosha/vim-godebug](https://github.com/jodosha/vim-godebug) : Go debugging for Vim
  * [mfussenegger/nvim-dap](https://github.com/mfussenegger/nvim-dap) : Debug Adapter Protocol client implementation for Neovim
  * [niuiic/dap-utils.nvim](https://github.com/niuiic/dap-utils.nvim) : utilities for nvim-dap
  * [pocco81/dap-buddy.nvim](https://github.com/pocco81/dap-buddy.nvim) : Dap Buddy allows you to manage debuggers provided by nvim-dap
  * [pocco81/dapinstall.nvim](https://github.com/pocco81/dapinstall.nvim) : Debug Adapter Protocol manager for Neovim
  * [puremourning/vimspector](https://github.com/puremourning/vimspector) : The plugin is a capable Vim graphical debugger for multiple languages
  * [sidorares/node-vim-debugger](https://github.com/sidorares/node-vim-debugger) : Node.js debugger client and vim driver
  * [tweekmonster/exception.vim](https://github.com/tweekmonster/exception.vim) : tracing exceptions thrown by VimL scripts
  * [vim-vdebug/vdebug](https://github.com/vim-vdebug/vdebug) : a new, fast, powerful debugger client for Vim
## repl
  * [gcballesteros/notebooknavigator.nvim](https://github.com/gcballesteros/notebooknavigator.nvim) : manipulate and send code ceels to REPL
  * [hiphish/repl.nvim](https://github.com/hiphish/repl.nvim) : REPL for nvim
  * [hiphish/repl.nvim](https://gitlab.com/hiphish/repl.nvim) : The universal, extendible and configurable REPL plugin
  * [jpalardy/vim-slime](https://github.com/jpalardy/vim-slime) : type text in a file, send it to a live REPL,
  * [justinmk/nvim-repl](https://github.com/justinmk/nvim-repl) : a minimal REPL plugin
  * [luk400/vim-jukit](https://github.com/luk400/vim-jukit) : REPL plugin and Jupyter-Notebook alternative for Vim
  * [milanglacier/yarepl.nvim](https://github.com/milanglacier/yarepl.nvim) : yet another REPL
  * [rhysd/reply.vim](https://github.com/rhysd/reply.vim) : make editing buffers with REPLs nicely
  * [tpope/vim-fireplace](https://github.com/tpope/vim-fireplace) : There's a REPL in Fireplace, but you probably wouldn't have noticed if I hadn't told you
## color
  * [4e554c4c/darkman.nvim](https://github.com/4e554c4c/darkman.nvim) : change the background depending on the Freedesktop Dark-mode standard
  * [amadeus/vim-convert-color-to](https://github.com/amadeus/vim-convert-color-to) : simple and easy to use plugin that can convert various color strings to different formats
  * [ap/vim-css-color](https://github.com/ap/vim-css-color) : preview colours in source code while editing
  * [brenoprata10/nvim-highlight-colors](https://github.com/brenoprata10/nvim-highlight-colors) : Highlight colors with neovim
  * [chrisbra/colorizer](https://github.com/chrisbra/colorizer) : color colornames and codes
  * [dharmx/nvim-colo](https://github.com/dharmx/nvim-colo) : theming utils
  * [f-person/auto-dark-mode.nvim](https://github.com/f-person/auto-dark-mode.nvim) : change editor appearance based on macOS system settings
  * [folke/paint.nvim](https://github.com/folke/paint.nvim) : add additional highlighting to buffer
  * [jeaye/color_coded](https://github.com/jeaye/color_coded) : semantic highlighting with vim
  * [lifepillar/vim-colortemplate](https://github.com/lifepillar/vim-colortemplate) : makes it easy to develop color schemes
  * [m00qek/baleia.nvim](https://github.com/m00qek/baleia.nvim) : Colorize text with ANSI escape sequences
  * [norcalli/nvim-base16.lua](https://github.com/norcalli/nvim-base16.lua) : Programmatic lua library for setting base16 themes in Neovim
  * [norcalli/nvim-colorizer.lua](https://github.com/norcalli/nvim-colorizer.lua) : A high-performance color highlighter for Neovim which has no external dependencies
  * [ntbbloodbath/color-converter.nvim](https://github.com/ntbbloodbath/color-converter.nvim) : Easily convert your CSS colors
  * [nvim-colortils/colortils.nvim](https://github.com/nvim-colortils/colortils.nvim) : Neovim color utils
  * [preservim/vim-thematic](https://github.com/preservim/vim-thematic) : have themes for vim
  * [rbtnn/vim-coloredit](https://github.com/rbtnn/vim-coloredit) : provides to edit RGB and HSL
  * [rktjmp/lush.nvim](https://github.com/rktjmp/lush.nvim) : colorscheme creation aid for Neovim
  * [rrethy/vim-hexokinase](https://github.com/rrethy/vim-hexokinase) : The fastest (Neo)Vim plugin for asynchronously displaying the colours
  * [themercorp/themer.lua](https://github.com/themercorp/themer.lua) : THEMER - AN ORGANISED COLORSCHEME WORLD
  * [tjdevries/colorbuddy.nvim](https://github.com/tjdevries/colorbuddy.nvim) : A colorscheme maker for Neovim
  * [tjdevries/colorbuddy.vim](https://github.com/tjdevries/colorbuddy.vim) : A colorscheme helper for Neovim
  * [uga-rosa/ccc.nvim](https://github.com/uga-rosa/ccc.nvim) : Create Color Code
  * [xiyaowong/nvim-transparent](https://github.com/xiyaowong/nvim-transparent) : Remove all background colors to make nvim transparent
  * [ziontee113/color-picker.nvim](https://github.com/ziontee113/color-picker.nvim) : lets Neovim Users choose & modify colors
## tabline
  * [akinsho/bufferline.nvim](https://github.com/akinsho/bufferline.nvim)
  * [akinsho/nvim-bufferline.lua](https://github.com/akinsho/nvim-bufferline.lua)
  * [alvarosevilla95/luatab.nvim](https://github.com/alvarosevilla95/luatab.nvim)
  * [chrboesch/vim-tabline](https://github.com/chrboesch/vim-tabline)
  * [crispgm/nvim-tabline](https://github.com/crispgm/nvim-tabline)
  * [johann2357/nvim-smartbufs](https://github.com/johann2357/nvim-smartbufs)
  * [kdheepak/tabline.nvim](https://github.com/kdheepak/tabline.nvim)
  * [koenverburg/minimal-tabline.nvim](https://github.com/koenverburg/minimal-tabline.nvim) : minimal tabline
  * [lukelbd/vim-tabline](https://github.com/lukelbd/vim-tabline) : providing a simple black-and-white "tabline"
  * [nanozuki/tabby.nvim](https://github.com/nanozuki/tabby.nvim)
  * [noib3/cokeline.nvim](https://github.com/noib3/cokeline.nvim)
  * [pacha/vem-tabline](https://github.com/pacha/vem-tabline) : a lightweight Vim plugin to display your tabs and buffers at the top of your screen
  * [rafcamlet/tabline-framework.nvim](https://github.com/rafcamlet/tabline-framework.nvim)
  * [romgrk/barbar.nvim](https://github.com/romgrk/barbar.nvim)
  * [tomiis4/buffertabs.nvim](https://github.com/tomiis4/buffertabs.nvim) : simple, fancy tabline
  * [webdevel/tabulous](https://github.com/webdevel/tabulous) : Lightweight Vim plugin to enhance the tabline including numbered tab page labels
## visual
  * [3rd/image.nvim](https://github.com/3rd/image.nvim) : attempt to add image support to neovim
  * [acksld/messages.nvim](https://github.com/acksld/messages.nvim) : Capture and show any messages in a customisable floating window
  * [adelarsq/image_preview.nvim](https://github.com/adelarsq/image_preview.nvim) : Neovim plugin for image previews
  * [ahmedkhalf/notif.nvim](https://github.com/ahmedkhalf/notif.nvim) : Notification system
  * [ameertaweel/todo.nvim](https://github.com/ameertaweel/todo.nvim) : Lua plugin for Neovim to highlight and search for todo comments like TODO, FIXME, BUG
  * [anuvyklack/animation.nvim](https://github.com/anuvyklack/animation.nvim) : An OOP library to create animations in Neovim
  * [ashfinal/qfview.nvim](https://github.com/ashfinal/qfview.nvim) : make quickfix window look better
  * [axlebedev/footprints](https://github.com/axlebedev/footprints) : Highlight last edited lines
  * [ayosec/hltermpaste.vim](https://github.com/ayosec/hltermpaste.vim) : highlight terminal paste
  * [bekaboo/deadcolumn.nvim](https://github.com/bekaboo/deadcolumn.nvim) : assist maintaining a maximum code width
  * [bennypowers/nvim-regexplainer](https://github.com/bennypowers/nvim-regexplainer) : Describe the regular expression under the cursor
  * [bronson/vim-trailing-whitespace](https://github.com/bronson/vim-trailing-whitespace) : causes trailing whitespace to be highlighted in red
  * [chrisbra/changesplugin](https://github.com/chrisbra/changesplugin) : visualize which lines have been changed since editing started
  * [chrisbra/dynamicsigns](https://github.com/chrisbra/dynamicsigns) : Using Signs for different things (visualy)
  * [chrisbra/vim-diff-enhanced](https://github.com/chrisbra/vim-diff-enhanced) : A Vim plugin for creating better diffs
  * [cosmicnvim/cosmic-ui](https://github.com/cosmicnvim/cosmic-ui) : simple wrapper around specific vim functionality
  * [danilamihailov/beacon.nvim](https://github.com/danilamihailov/beacon.nvim) : Whenever cursor jumps some distance or moves between windows, it will flash so you can see where it is
  * [dbmrq/vim-ditto](https://github.com/dbmrq/vim-ditto) : highlights overused words
  * [dbmrq/vim-redacted](https://github.com/dbmrq/vim-redacted) : Just redact some text
  * [delphinus/auto-cursorline.nvim](https://github.com/delphinus/auto-cursorline.nvim) : Show / hide cursorline in connection with cursor moving
  * [delphinus/vim-auto-cursorline](https://github.com/delphinus/vim-auto-cursorline) : Show / hide cursorline in connection with cursor moving
  * [eandrju/cellular-automaton.nvim](https://github.com/eandrju/cellular-automaton.nvim) : Do animation with code in buffer
  * [ecthelionvi/neocolumn.nvim](https://github.com/ecthelionvi/neocolumn.nvim) : highlight character at specific column
  * [edluffy/hologram.nvim](https://github.com/edluffy/hologram.nvim) : cross platform terminal image viewer for Neovim
  * [edluffy/specs.nvim](https://github.com/edluffy/specs.nvim) : Show where your cursor moves when jumping large distances
  * [emileferreira/nvim-strict](https://github.com/emileferreira/nvim-strict) : Strictly enforce configurable, best-practice code style
  * [folke/drop.nvim](https://github.com/folke/drop.nvim) : fun little screen saver
  * [folke/noice.nvim](https://github.com/folke/noice.nvim) : completely replaces the UI for messages, cmdline and the popupmenu
  * [frazrepo/vim-rainbow](https://github.com/frazrepo/vim-rainbow) : Rainbow Parentheses Improved
  * [gelguy/wilder.nvim](https://github.com/gelguy/wilder.nvim) : A more adventurous wildmenu
  * [gen740/smoothcursor.nvim](https://github.com/gen740/smoothcursor.nvim) : add sub-cursor to show scroll direction
  * [gennaro-tedesco/nvim-peekup](https://github.com/gennaro-tedesco/nvim-peekup) : peek registers befor pasting them
  * [haringsrob/nvim_context_vt](https://github.com/haringsrob/nvim_context_vt) : Shows virtual text of the current context after functions, methods, statements, etc.
  * [hiphish/nvim-ts-rainbow2](https://github.com/hiphish/nvim-ts-rainbow2) : rainbow parentheses
  * [hiphish/rainbow-delimiters.nvim](https://github.com/hiphish/rainbow-delimiters.nvim) : rainbow-delimiters
  * [hood/popui.nvim](https://github.com/hood/popui.nvim) : NeoVim UI sweetness powered by popfix
  * [ivyl/vim-bling](https://github.com/ivyl/vim-bling) : blinks search result after jumping
  * [jceb/blinds.nvim](https://github.com/jceb/blinds.nvim) : shade the other windows
  * [joeytwiddle/sexy_scroller.vim](https://github.com/joeytwiddle/sexy_scroller.vim) : smooth cursor and page movement
  * [johnfrankmorgan/whitespace.nvim](https://github.com/johnfrankmorgan/whitespace.nvim) : highlight/remove trailing whitespace
  * [jubnzv/virtual-types.nvim](https://github.com/jubnzv/virtual-types.nvim) : shows type annotations for functions in virtual text using built-in LSP client
  * [junegunn/rainbow_parentheses.vim](https://github.com/junegunn/rainbow_parentheses.vim) : Much simpler Rainbow Parentheses
  * [jxstxs/conceal.nvim](https://github.com/jxstxs/conceal.nvim) : conceals typical boiler code using treesitter
  * [kaitlynethylia/treepin](https://github.com/kaitlynethylia/treepin) : pin code to always stay on screen
  * [karb94/neoscroll.nvim](https://github.com/karb94/neoscroll.nvim) : smooth scrolling neovim plugin written in lua
  * [kevinhwang91/nvim-ffhighlight](https://github.com/kevinhwang91/nvim-ffhighlight) : Highlight the chars and words searched by `f` and `F`
  * [kevinhwang91/nvim-hlslens](https://github.com/kevinhwang91/nvim-hlslens) : search with more visuals
  * [kien/rainbow_parentheses.vim](https://github.com/kien/rainbow_parentheses.vim) : Better Rainbow Parentheses
  * [ktunprasert/gui-font-resize.nvim](https://github.com/ktunprasert/gui-font-resize.nvim) : easily resize gui fonts
  * [kyazdani42/nvim-web-devicons](https://github.com/kyazdani42/nvim-web-devicons) : lua fork of vim-devicons
  * [levouh/tint.nvim](https://github.com/levouh/tint.nvim) : tint inactive windows
  * [lewis6991/nvim-treesitter-context](https://github.com/lewis6991/nvim-treesitter-context) : Lightweight alternative to context.vim implemented with nvim-treesitter
  * [lucastavaresa/simpleindentguides.nvim](https://github.com/lucastavaresa/simpleindentguides.nvim) : indentation guide
  * [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim) : indentation guides to all lines
  * [lukas-reineke/virt-column.nvim](https://github.com/lukas-reineke/virt-column.nvim) : Display a character as the colorcolumn
  * [luochen1990/rainbow](https://github.com/luochen1990/rainbow) : Rainbow Parentheses Improved
  * [luukvbaal/statuscol.nvim](https://github.com/luukvbaal/statuscol.nvim) : provides a configurable and clickable statuscolumn
  * [m-demare/hlargs.nvim](https://github.com/m-demare/hlargs.nvim) : Highlight arguments' definitions and usages, asynchronously, using Treesitter
  * [m4xshen/smartcolumn.nvim](https://github.com/m4xshen/smartcolumn.nvim) : hide colorcolumn if no character nearby
  * [machakann/vim-highlightedyank](https://github.com/machakann/vim-highlightedyank) : Make the yanked region apparent
  * [malbertzard/inline-fold.nvim](https://github.com/malbertzard/inline-fold.nvim) : easily define patterns that get concealed inline
  * [markonm/traces.vim](https://github.com/markonm/traces.vim) : highlights patterns and ranges for Ex commands in Command-line mode
  * [mawkler/modicator.nvim](https://github.com/mawkler/modicator.nvim) : Cursor line mode indicator
  * [max397574/footprints.nvim](https://github.com/max397574/footprints.nvim) : highlights recently changed lines
  * [max397574/mark-ray.nvim](https://github.com/max397574/mark-ray.nvim) : show context of marks
  * [maximilianlloyd/ascii.nvim](https://github.com/maximilianlloyd/ascii.nvim) : collection of ascii art
  * [mhinz/vim-signify](https://github.com/mhinz/vim-signify) : uses the sign column to indicate added, modified and removed lines in a file that is managed by a version control system
  * [monkoose/matchparen.nvim](https://github.com/monkoose/matchparen.nvim) : highlight matching parentheses
  * [myusuf3/numbers.vim](https://github.com/myusuf3/numbers.vim) : intelligently toggling line numbers
  * [nacro90/numb.nvim](https://github.com/nacro90/numb.nvim) : Peeking the buffer while entering command :[number]
  * [nagy135/visualmark-nvim](https://github.com/nagy135/visualmark-nvim) : shows where marks are stored visually in buffer using virtual_text
  * [narutoxy/dim.lua](https://github.com/narutoxy/dim.lua) : dim the unused variables and functions using lsp and treesitter
  * [nfrid/due.nvim](https://github.com/nfrid/due.nvim) : provides you due for the date string
  * [niuiic/divider.nvim](https://github.com/niuiic/divider.nvim) : dividers for neovim
  * [norcalli/nvim-terminal.lua](https://github.com/norcalli/nvim-terminal.lua) : high performance filetype mode for Neovim which leverages `concealand` highlights your buffer with the correct color codes
  * [ntpeters/vim-better-whitespace](https://github.com/ntpeters/vim-better-whitespace) : causes all trailing whitespace characters to be highlighted
  * [nvim-lua/lsp-status.nvim](https://github.com/nvim-lua/lsp-status.nvim) : generating statusline components from the built-in LSP client
  * [nvim-tree/nvim-web-devicons](https://github.com/nvim-tree/nvim-web-devicons) : lua fork of vim-devicons
  * [nvim-treesitter/nvim-treesitter-context](https://github.com/nvim-treesitter/nvim-treesitter-context) : Lightweight alternative to context.vim implemented with nvim-treesitter
  * [nvim-zh/colorful-winsep.nvim](https://github.com/nvim-zh/colorful-winsep.nvim) : configurable window separtor
  * [ojroques/vim-scrollstatus](https://github.com/ojroques/vim-scrollstatus) : A scrollbar for Vim statusline
  * [pgdouyon/vim-evanesco](https://github.com/pgdouyon/vim-evanesco) : automatically clearing Vim's search highlighting whenever the cursor moves or insert mode is entered
  * [pocco81/noclc.nvim](https://github.com/pocco81/noclc.nvim) : disabling the cursor-line/column in unused windows/buffers
  * [powerman/vim-plugin-ansiesc](https://github.com/powerman/vim-plugin-ansiesc) : will conceal Ansi escape sequences but will cause subsequent text to be colored as the escape sequence specifies
  * [psliwka/vim-smoothie](https://github.com/psliwka/vim-smoothie) : makes scrolling nice and smooth
  * [qxxxb/vim-searchhi](https://github.com/qxxxb/vim-searchhi) : Highlight the current search result in a different style than the other search results
  * [rainbowhxch/beacon.nvim](https://github.com/rainbowhxch/beacon.nvim) : flash when big jump
  * [rcarriga/nvim-notify](https://github.com/rcarriga/nvim-notify) : fancy, configurable, notification manager
  * [rickhowe/diffchar.vim](https://github.com/rickhowe/diffchar.vim) : make diff mode more useful
  * [rktjmp/highlight-current-n.nvim](https://github.com/rktjmp/highlight-current-n.nvim) : highlights the current /, ? or * match under your cursor when pressing n or N and gets out of the way afterwards
  * [romainl/vim-cool](https://github.com/romainl/vim-cool) : disables search highlighting when you are done searching and re-enables it when you search again
  * [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons) : Adds icons to your plugins
  * [segeljakt/vim-silicon](https://github.com/segeljakt/vim-silicon) : your selected code to a pretty picture
  * [shellraining/hlchunk.nvim](https://github.com/shellraining/hlchunk.nvim) : highlight that chunck
  * [siuoly/typing_speed.vim](https://github.com/siuoly/typing_speed.vim) : Displaying the typing speed
  * [smiteshp/nvim-gps](https://github.com/smiteshp/nvim-gps) : Take this handy dandy gps with you on your coding adventures and always know where you are
  * [smiteshp/nvim-navic](https://github.com/smiteshp/nvim-navic) : A simple statusline/winbar component that uses LSP to show your current code context
  * [smjonas/live-command.nvim](https://github.com/smjonas/live-command.nvim) : Preview macros, the :norm command & more
  * [tadaa/vimade](https://github.com/tadaa/vimade) : fades your inactive buffers and preserves syntax highlighting
  * [tenxsoydev/tabs-vs-spaces.nvim](https://github.com/tenxsoydev/tabs-vs-spaces.nvim) : highlights when the wrong indentation char is used
  * [thehamsta/nvim-dap-virtual-text](https://github.com/thehamsta/nvim-dap-virtual-text) : adds virtual text support to nvim-dap
  * [tjdevries/overlength.vim](https://github.com/tjdevries/overlength.vim) : hlight when lines go over the length that you want them
  * [tjdevries/train.nvim](https://github.com/tjdevries/train.nvim) : Train yourself with vim motions and make your own train tracks
  * [tobinpalmer/rayso.nvim](https://github.com/tobinpalmer/rayso.nvim) : Create code snippets using ray.so
  * [tummetott/reticle.nvim](https://github.com/tummetott/reticle.nvim) : disable cursor line for not used windows
  * [tversteeg/registers.nvim](https://github.com/tversteeg/registers.nvim) : Show register content when you try to access it
  * [tzachar/highlight-undo.nvim](https://github.com/tzachar/highlight-undo.nvim) : highlight undo
  * [unblevable/quick-scope](https://github.com/unblevable/quick-scope) : An always-on highlight for a unique character in every word on a line
  * [utilyre/barbecue.nvim](https://github.com/utilyre/barbecue.nvim) : VS Code like winbar that uses nvim-navic
  * [utilyre/sentiment.nvim](https://github.com/utilyre/sentiment.nvim) : better matchparen for neovim
  * [valloric/matchtagalways](https://github.com/valloric/matchtagalways) : Always highlight enclosing tags
  * [vidocqh/lsp-lens.nvim](https://github.com/vidocqh/lsp-lens.nvim) : display reference and definitions with lsp
  * [vim-scripts/csapprox](https://github.com/vim-scripts/csapprox) : This plugin makes GVim-only colorschemes Just Work in terminal Vim
  * [vim-scripts/syntaxrange](https://github.com/vim-scripts/syntaxrange) : provides commands and functions to set up regions in the current buffer that either use a syntax different from the buffer's 'filetype', or completely ignore the syntax
  * [vonheikemen/searchbox.nvim](https://github.com/vonheikemen/searchbox.nvim) : Start your search from a more comfortable place, say the upper right corner
  * [weirdsmiley/bionically](https://github.com/weirdsmiley/bionically) : convert text on current buffer into a bionic reading font
  * [wellle/context.vim](https://github.com/wellle/context.vim) : shows the context of the currently visible buffer contents
  * [wincent/pinnacle](https://github.com/wincent/pinnacle) : provides functions for manipulating `:highlight` groups in Vimscript and Lua
  * [winston0410/range-highlight.nvim](https://github.com/winston0410/range-highlight.nvim) : hightlights ranges you have entered in commandline
  * [xiyaowong/virtcolumn.nvim](https://github.com/xiyaowong/virtcolumn.nvim) : Display a character as the colorcolumn
  * [xolox/vim-lua-inspect](https://github.com/xolox/vim-lua-inspect) : Semantic highlighting for Lua in Vim
  * [yaocccc/nvim-foldsign](https://github.com/yaocccc/nvim-foldsign) : display folds on sign column
  * [yaocccc/nvim-hl-mdcodeblock.lua](https://github.com/yaocccc/nvim-hl-mdcodeblock.lua) : just do highlight markdown codeblock
  * [yaocccc/nvim-hlchunk](https://github.com/yaocccc/nvim-hlchunk) : hignlight chunk signcolumn plug of nvim
  * [yaocccc/vim-hlchunk](https://github.com/yaocccc/vim-hlchunk) : hignlight chunk signcolumn plug of vim
  * [yggdroot/indentline](https://github.com/yggdroot/indentline) : is used for displaying thin vertical lines at each indentation level for code indented with spaces
## scrollbar
  * [dstein64/nvim-scrollview](https://github.com/dstein64/nvim-scrollview) : displays interactive vertical scrollbars
  * [lewis6991/satellite.nvim](https://github.com/lewis6991/satellite.nvim) : displays decorated scrollbars
  * [petertriho/nvim-scrollbar](https://github.com/petertriho/nvim-scrollbar) : Extensible Neovim Scrollbar
  * [rbtnn/vim-winsbar](https://github.com/rbtnn/vim-winsbar) : provides that each window has a scrollbar
  * [sslivkoff/vim-scroll-barnacle](https://github.com/sslivkoff/vim-scroll-barnacle) : a scrollbar for vim in the terminal
  * [xuyuanp/scrollbar.nvim](https://github.com/xuyuanp/scrollbar.nvim) : scrollbar for neovim
## statusline
  * [abeldekat/harpoonline](https://github.com/abeldekat/harpoonline) : add harpoon information to the statusline
  * [adelarsq/neoline.vim](https://github.com/adelarsq/neoline.vim)
  * [b0o/incline.nvim](https://github.com/b0o/incline.nvim)
  * [beauwilliams/statusline.lua](https://github.com/beauwilliams/statusline.lua)
  * [bluz71/vim-mistfly-statusline](https://github.com/bluz71/vim-mistfly-statusline) : a simple, fast and informative statusline for Vim
  * [datwaft/bubbly.nvim](https://github.com/datwaft/bubbly.nvim)
  * [doums/barow](https://github.com/doums/barow) : A minimalist statusline [archived]
  * [famiu/feline.nvim](https://github.com/famiu/feline.nvim) : A minimal, stylish and customizable statusline / winbar for Neovim written in Lua
  * [feline-nvim/feline.nvim](https://github.com/feline-nvim/feline.nvim)
  * [fmoralesc/worldslice](https://github.com/fmoralesc/worldslice) : minimalistic statusline and tabline configuration
  * [freddiehaddad/feline.nvim](https://github.com/freddiehaddad/feline.nvim) : minimal statusline, statuscolumn, and winbar
  * [glepnir/galaxyline.nvim](https://github.com/glepnir/galaxyline.nvim) : light-weight and Super Fast statusline plugin
  * [glepnir/spaceline.vim](https://github.com/glepnir/spaceline.vim) : The best vim statusline plugin
  * [hoob3rt/lualine.nvim](https://github.com/hoob3rt/lualine.nvim) : A blazing fast and easy to configure Neovim statusline written in Lua
  * [itchyny/lightline.vim](https://github.com/itchyny/lightline.vim)
  * [konapun/vacuumline.nvim](https://github.com/konapun/vacuumline.nvim)
  * [liuchengxu/eleline.vim](https://github.com/liuchengxu/eleline.vim) : Another elegant statusline for vim
  * [ntbbloodbath/galaxyline.nvim](https://github.com/ntbbloodbath/galaxyline.nvim)
  * [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)
  * [nvimdev/whiskyline.nvim](https://github.com/nvimdev/whiskyline.nvim) : async, lsp, event driven statusline
  * [ojroques/nvim-hardline](https://github.com/ojroques/nvim-hardline)
  * [powerline/powerline](https://github.com/powerline/powerline)
  * [r1ri/suffer](https://github.com/r1ri/suffer) : simple bufferline plugin, in less the 30 lines of lua
  * [rbong/vim-crystalline](https://github.com/rbong/vim-crystalline) : the plugin lets you build your own statusline and tabline in a vanilla vim style. It also comes with a bufferline
  * [rebelot/heirline.nvim](https://github.com/rebelot/heirline.nvim)
  * [roobert/statusline-action-hints.nvim](https://github.com/roobert/statusline-action-hints.nvim) : shows statusline information on the current word
  * [rrethy/nvim-hotline](https://github.com/rrethy/nvim-hotline) : Minimal Lua wrappers for setting your 'statusline' and 'tabline'
  * [strash/everybody-wants-that-line.nvim](https://github.com/strash/everybody-wants-that-line.nvim) : minimal, informative, elegant statusline
  * [tamago324/vim-gaming-line](https://github.com/tamago324/vim-gaming-line) : animated gaming statusline
  * [tamton-aquib/staline.nvim](https://github.com/tamton-aquib/staline.nvim)
  * [tjdevries/express_line.nvim](https://github.com/tjdevries/express_line.nvim)
  * [tpope/vim-flagship](https://github.com/tpope/vim-flagship)
  * [vim-airline/vim-airline](https://github.com/vim-airline/vim-airline)
  * [windwp/windline.nvim](https://github.com/windwp/windline.nvim)
  * [yaocccc/nvim-lines.lua](https://github.com/yaocccc/nvim-lines.lua) : simple statusline & tabline
## highlight
  * [0xadk/full_visual_line.nvim](https://github.com/0xadk/full_visual_line.nvim) : highlight the whole line when in visual_line mode
  * [aaron-p1/match-visual.nvim](https://github.com/aaron-p1/match-visual.nvim) : highlight text matching visual selection in all windows
  * [galicarnax/vim-regex-syntax](https://github.com/galicarnax/vim-regex-syntax) : Syntax highlight for regular expressions
  * [guns/vim-clojure-highlight](https://github.com/guns/vim-clojure-highlight) : Extend builtin syntax highlighting to local, referred, and aliased vars in Clojure buffers
  * [kasama/nvim-custom-diagnostic-highlight](https://github.com/kasama/nvim-custom-diagnostic-highlight) : apply a highlight group to unused variables and functions using LSP
  * [lcheylus/overlength.nvim](https://github.com/lcheylus/overlength.nvim) : highlight the part of a line that doesn't fit into textwidth
  * [lfv89/vim-interestingwords](https://github.com/lfv89/vim-interestingwords) : Word highlighting and navigation throughout out the buffer
  * [lpinilla/vim-codepainter](https://github.com/lpinilla/vim-codepainter) : color different parts of code making the use of text properties
  * [melkster/modicator.nvim](https://github.com/melkster/modicator.nvim) : changes the foreground color of the CursorLineNr highlight based on the current Vim mode
  * [mr-lllll/interestingwords.nvim](https://github.com/mr-lllll/interestingwords.nvim) : highlights word with differing colors
  * [numirias/semshi](https://github.com/numirias/semshi) : provides semantic highlighting for Python in Neovim
  * [nvchad/nvim-colorizer.lua](https://github.com/nvchad/nvim-colorizer.lua) : high-performance color highlighter
  * [nyngwang/murmur.lua](https://github.com/nyngwang/murmur.lua) : Cursorword highlighting with callbacks support
  * [pocco81/high-str.nvim](https://github.com/pocco81/high-str.nvim) : highlight selected
  * [zbirenbaum/neodim](https://github.com/zbirenbaum/neodim) : dimming the highlights of unused functions, variables, parameters, and more
## zen
  * [amix/vim-zenroom2](https://github.com/amix/vim-zenroom2) : emulates iA Writer environment
  * [folke/twilight.nvim](https://github.com/folke/twilight.nvim) : dims inactive portions of the code you're editing
  * [folke/zen-mode.nvim](https://github.com/folke/zen-mode.nvim) : Distraction-free coding for Neovim
  * [henriquehbr/ataraxis.lua](https://github.com/henriquehbr/ataraxis.lua) : absence of mental stress or anxiety, a state of serene calmness
  * [junegunn/goyo.vim](https://github.com/junegunn/goyo.vim) : Distraction-free writing in Vim
  * [junegunn/limelight.vim](https://github.com/junegunn/limelight.vim) : Hyperfocus-writing in Vim
  * [koenverburg/peepsight.nvim](https://github.com/koenverburg/peepsight.nvim) : just focus on one function at the time
  * [pocco81/true-zen.nvim](https://github.com/pocco81/true-zen.nvim) : Clean and elegant distraction-free writing
  * [pocco81/truezen.nvim](https://github.com/pocco81/truezen.nvim) : Clean and elegant distraction-free writing
  * [shortcuts/no-neck-pain.nvim](https://github.com/shortcuts/no-neck-pain.nvim) : center the currently focused buffer to the middle of the screen
  * [sunjon/shade.nvim](https://github.com/sunjon/shade.nvim) : dims your inactive windows
## colorscheme
  * [0xstepit/flow.nvim](https://github.com/0xstepit/flow.nvim)
  * [1995parham/naz.vim](https://github.com/1995parham/naz.vim)
  * [2giosangmitom/nightfall.nvim](https://github.com/2giosangmitom/nightfall.nvim)
  * [2nthony/vitesse.nvim](https://github.com/2nthony/vitesse.nvim)
  * [abstract-ide/abstract-cs](https://github.com/abstract-ide/abstract-cs)
  * [adisen99/apprentice.nvim](https://github.com/adisen99/apprentice.nvim)
  * [adisen99/codeschool.nvim](https://github.com/adisen99/codeschool.nvim)
  * [alessandroyorba/despacio](https://github.com/alessandroyorba/despacio)
  * [alexis12119/nightly.nvim](https://github.com/alexis12119/nightly.nvim)
  * [alexvzyl/nordic.nvim](https://github.com/alexvzyl/nordic.nvim)
  * [altercation/vim-colors-solarized](https://github.com/altercation/vim-colors-solarized)
  * [andersevenrud/nordic.nvim](https://github.com/andersevenrud/nordic.nvim)
  * [antonk52/lake.nvim](https://github.com/antonk52/lake.nvim)
  * [arcticicestudio/nord-vim](https://github.com/arcticicestudio/nord-vim)
  * [arthurealike/vim-j](https://github.com/arthurealike/vim-j)
  * [arzg/vim-substrata](https://github.com/arzg/vim-substrata)
  * [askfiy/catppuccin](https://github.com/askfiy/catppuccin)
  * [askfiy/visual_studio_code](https://github.com/askfiy/visual_studio_code)
  * [axvr/photon.vim](https://github.com/axvr/photon.vim)
  * [axvr/raider.vim](https://github.com/axvr/raider.vim)
  * [base16-project/base16-vim](https://github.com/base16-project/base16-vim)
  * [benwr/tuftish](https://github.com/benwr/tuftish)
  * [bkegley/gloombuddy](https://github.com/bkegley/gloombuddy)
  * [blueshirts/darcula](https://github.com/blueshirts/darcula)
  * [bluz71/vim-moonfly-colors](https://github.com/bluz71/vim-moonfly-colors)
  * [bluz71/vim-nightfly-colors](https://github.com/bluz71/vim-nightfly-colors)
  * [bluz71/vim-nightfly-guicolors](https://github.com/bluz71/vim-nightfly-guicolors)
  * [briones-gabriel/darcula-solid.nvim](https://github.com/briones-gabriel/darcula-solid.nvim)
  * [catppuccin/nvim](https://github.com/catppuccin/nvim)
  * [challenger-deep-theme/vim](https://github.com/challenger-deep-theme/vim)
  * [chriskempson/base16-vim](https://github.com/chriskempson/base16-vim)
  * [christianchiarulli/nvcode-color-schemes.vim](https://github.com/christianchiarulli/nvcode-color-schemes.vim)
  * [chrsm/paramount-ng.nvim](https://github.com/chrsm/paramount-ng.nvim)
  * [cocopon/iceberg.vim](https://github.com/cocopon/iceberg.vim)
  * [cpea2506/one_monokai.nvim](https://github.com/cpea2506/one_monokai.nvim)
  * [decaycs/decay.nvim](https://github.com/decaycs/decay.nvim)
  * [dilangmb/nightbuddy](https://github.com/dilangmb/nightbuddy)
  * [dracula/vim](https://github.com/dracula/vim)
  * [dundargoc/fakedonalds.nvim](https://github.com/dundargoc/fakedonalds.nvim)
  * [edeneast/nightfox.nvim](https://github.com/edeneast/nightfox.nvim)
  * [elianiva/gruvy.nvim](https://github.com/elianiva/gruvy.nvim)
  * [elianiva/icy.nvim](https://github.com/elianiva/icy.nvim)
  * [ellisonleao/gruvbox.nvim](https://github.com/ellisonleao/gruvbox.nvim)
  * [elvessousa/sobrio](https://github.com/elvessousa/sobrio)
  * [embark-theme/vim](https://github.com/embark-theme/vim)
  * [everblush/everblush.nvim](https://github.com/everblush/everblush.nvim)
  * [felipec/vim-felipec](https://github.com/felipec/vim-felipec)
  * [fenetikm/falcon](https://github.com/fenetikm/falcon)
  * [flazz/vim-colorschemes](https://github.com/flazz/vim-colorschemes)
  * [folke/styler.nvim](https://github.com/folke/styler.nvim) : set a different colorscheme per filetype
  * [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim)
  * [frenzyexists/aquarium-vim](https://github.com/frenzyexists/aquarium-vim)
  * [ful1e5/onedark.nvim](https://github.com/ful1e5/onedark.nvim)
  * [gbprod/nord.nvim](https://github.com/gbprod/nord.nvim)
  * [ghifarit53/tokyonight-vim](https://github.com/ghifarit53/tokyonight-vim)
  * [glepnir/zephyr-nvim](https://github.com/glepnir/zephyr-nvim)
  * [gruvbox-community/gruvbox](https://github.com/gruvbox-community/gruvbox)
  * [hardselius/warlock](https://github.com/hardselius/warlock)
  * [heraldofsolace/nisha-vim](https://github.com/heraldofsolace/nisha-vim)
  * [yorickpeterse/nvim-grey](https://gitlab.com/yorickpeterse/nvim-grey)
  * [yorickpeterse/vim-paper](https://gitlab.com/yorickpeterse/vim-paper)
  * [icymind/neosolarized](https://github.com/icymind/neosolarized)
  * [iron-e/nvim-highlite](https://github.com/iron-e/nvim-highlite)
  * [ishan9299/modus-theme-vim](https://github.com/ishan9299/modus-theme-vim)
  * [ishan9299/nvim-solarized-lua](https://github.com/ishan9299/nvim-solarized-lua)
  * [jaredgorski/spacecamp](https://github.com/jaredgorski/spacecamp)
  * [jayhowie/crystal-cove](https://github.com/jayhowie/crystal-cove)
  * [jeffkreeftmeijer/vim-dim](https://github.com/jeffkreeftmeijer/vim-dim) : improved vim default colorscheme
  * [jesseleite/nvim-noirbuddy](https://github.com/jesseleite/nvim-noirbuddy)
  * [jim-at-jibba/ariake-vim-colors](https://github.com/jim-at-jibba/ariake-vim-colors)
  * [jnurmine/zenburn](https://github.com/jnurmine/zenburn)
  * [jonathanfilip/vim-lucius](https://github.com/jonathanfilip/vim-lucius)
  * [joshdick/onedark.vim](https://github.com/joshdick/onedark.vim)
  * [jpo/vim-railscasts-theme](https://github.com/jpo/vim-railscasts-theme)
  * [jsit/toast.vim](https://github.com/jsit/toast.vim)
  * [junegunn/seoul256.vim](https://github.com/junegunn/seoul256.vim)
  * [kabbamine/yowish.vim](https://github.com/kabbamine/yowish.vim)
  * [kaiuri/nvim-juliana](https://github.com/kaiuri/nvim-juliana)
  * [kaiuri/nvim-mariana](https://github.com/kaiuri/nvim-mariana)
  * [kdheepak/monochrome.nvim](https://github.com/kdheepak/monochrome.nvim)
  * [klooj/noogies](https://github.com/klooj/noogies)
  * [kuznetsss/meadow-nvim](https://github.com/kuznetsss/meadow-nvim)
  * [kvrohit/mellow.nvim](https://github.com/kvrohit/mellow.nvim)
  * [kvrohit/rasmus.nvim](https://github.com/kvrohit/rasmus.nvim)
  * [kvrohit/substrata.nvim](https://github.com/kvrohit/substrata.nvim)
  * [kyazdani42/blue-moon](https://github.com/kyazdani42/blue-moon)
  * [kyazdani42/nvim-palenight.lua](https://github.com/kyazdani42/nvim-palenight.lua)
  * [ladge/antarctic-vim](https://github.com/ladge/antarctic-vim)
  * [lalitmee/cobalt2.nvim](https://github.com/lalitmee/cobalt2.nvim)
  * [ldelossa/vimdark](https://github.com/ldelossa/vimdark)
  * [lewpoly/sherbet.nvim](https://github.com/lewpoly/sherbet.nvim)
  * [lifepillar/vim-gruvbox8](https://github.com/lifepillar/vim-gruvbox8)
  * [lifepillar/vim-solarized8](https://github.com/lifepillar/vim-solarized8)
  * [lmburns/kimbox](https://github.com/lmburns/kimbox)
  * [lourenci/github-colors](https://github.com/lourenci/github-colors)
  * [luisiacc/gruvbox-baby](https://github.com/luisiacc/gruvbox-baby)
  * [lunarvim/colorschemes](https://github.com/lunarvim/colorschemes) : Collection of colorschemes made to be compatible with LunarVim
  * [lunarvim/darkplus.nvim](https://github.com/lunarvim/darkplus.nvim)
  * [lunarvim/onedarker.nvim](https://github.com/lunarvim/onedarker.nvim)
  * [maaslalani/nordbuddy](https://github.com/maaslalani/nordbuddy)
  * [mangeshrex/uwu.vim](https://github.com/mangeshrex/uwu.vim)
  * [markeganfuller/vim-journeyman](https://github.com/markeganfuller/vim-journeyman)
  * [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim)
  * [matsuuu/pinkmare](https://github.com/matsuuu/pinkmare)
  * [max397574/omega-themes](https://github.com/max397574/omega-themes)
  * [max397574/tomato.nvim](https://github.com/max397574/tomato.nvim)
  * [maxmx03/fluoromachine.nvim](https://github.com/maxmx03/fluoromachine.nvim)
  * [maxst/flatcolor](https://github.com/maxst/flatcolor)
  * [mcchrish/zenbones.nvim](https://github.com/mcchrish/zenbones.nvim)
  * [meliora-theme/neovim](https://github.com/meliora-theme/neovim)
  * [metalelf0/jellybeans-nvim](https://github.com/metalelf0/jellybeans-nvim)
  * [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next)
  * [mhinz/vim-janah](https://github.com/mhinz/vim-janah)
  * [mjlbach/onedark.nvim](https://github.com/mjlbach/onedark.nvim)
  * [mofiqul/adwaita.nvim](https://github.com/mofiqul/adwaita.nvim)
  * [mofiqul/dracula.nvim](https://github.com/mofiqul/dracula.nvim)
  * [mofiqul/vim-code-dark](https://github.com/mofiqul/vim-code-dark)
  * [mofiqul/vscode.nvim](https://github.com/mofiqul/vscode.nvim)
  * [mordechaihadad/nvim-papadark](https://github.com/mordechaihadad/nvim-papadark)
  * [morhetz/gruvbox](https://github.com/morhetz/gruvbox)
  * [nanotech/jellybeans.vim](https://github.com/nanotech/jellybeans.vim)
  * [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim)
  * [neanias/everforest-nvim](https://github.com/neanias/everforest-nvim)
  * [nekonako/xresources-nvim](https://github.com/nekonako/xresources-nvim)
  * [nightsense/cosmic_latte](https://github.com/nightsense/cosmic_latte)
  * [nightsense/snow](https://github.com/nightsense/snow)
  * [nightsense/stellarized](https://github.com/nightsense/stellarized)
  * [norflin321/bicolors](https://github.com/norflin321/bicolors)
  * [novakne/kosmikoa.nvim](https://github.com/novakne/kosmikoa.nvim)
  * [npxbr/gruvbox](https://github.com/npxbr/gruvbox)
  * [ntbbloodbath/doom-one.nvim](https://github.com/ntbbloodbath/doom-one.nvim)
  * [nxvu699134/vn-night.nvim](https://github.com/nxvu699134/vn-night.nvim)
  * [nyngwang/nvimgelion](https://github.com/nyngwang/nvimgelion)
  * [nyoom-engineering/oxocarbon.nvim](https://github.com/nyoom-engineering/oxocarbon.nvim)
  * [ofirgall/ofirkai.nvim](https://github.com/ofirgall/ofirkai.nvim)
  * [olimorris/onedark.nvim](https://github.com/olimorris/onedark.nvim)
  * [olimorris/onedarkpro.nvim](https://github.com/olimorris/onedarkpro.nvim)
  * [olivercederborg/poimandres.nvim](https://github.com/olivercederborg/poimandres.nvim)
  * [overcache/neosolarized](https://github.com/overcache/neosolarized)
  * [owickstrom/vim-colors-paramount](https://github.com/owickstrom/vim-colors-paramount)
  * [phha/zenburn.nvim](https://github.com/phha/zenburn.nvim)
  * [phsix/nvim-hybrid](https://github.com/phsix/nvim-hybrid)
  * [plan9-for-vimspace/acme-colors](https://github.com/plan9-for-vimspace/acme-colors)
  * [preservim/vim-colors-pencil](https://github.com/preservim/vim-colors-pencil)
  * [projekt0n/github-nvim-theme](https://github.com/projekt0n/github-nvim-theme)
  * [pygamer0/darc.nvim](https://github.com/pygamer0/darc.nvim)
  * [rafamadriz/neon](https://github.com/rafamadriz/neon)
  * [rafi/awesome-vim-colorschemes](https://github.com/rafi/awesome-vim-colorschemes)
  * [rakr/vim-one](https://github.com/rakr/vim-one)
  * [ramojus/mellifluous.nvim](https://github.com/ramojus/mellifluous.nvim)
  * [ray-x/aurora](https://github.com/ray-x/aurora)
  * [ray-x/starry.nvim](https://github.com/ray-x/starry.nvim)
  * [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim)
  * [rishabhrd/gruvy](https://github.com/rishabhrd/gruvy)
  * [rishabhrd/nvim-rdark](https://github.com/rishabhrd/nvim-rdark)
  * [rmehri01/onenord.nvim](https://github.com/rmehri01/onenord.nvim)
  * [robertmeta/nofrils](https://github.com/robertmeta/nofrils)
  * [roboron3042/cyberpunk-neon](https://github.com/roboron3042/cyberpunk-neon)
  * [rockerboo/boo-colorscheme-nvim](https://github.com/rockerboo/boo-colorscheme-nvim)
  * [rockyzhang24/arctic.nvim](https://github.com/rockyzhang24/arctic.nvim)
  * [romainl/apprentice](https://github.com/romainl/apprentice)
  * [romainl/flattened](https://github.com/romainl/flattened)
  * [romainl/vim-bruin](https://github.com/romainl/vim-bruin)
  * [romainl/vim-dichromatic](https://github.com/romainl/vim-dichromatic)
  * [romainl/vim-malotru](https://github.com/romainl/vim-malotru)
  * [romainl/vim-sweet16](https://github.com/romainl/vim-sweet16)
  * [romgrk/doom-one.vim](https://github.com/romgrk/doom-one.vim)
  * [rose-pine/neovim](https://github.com/rose-pine/neovim)
  * [rrethy/nvim-base16](https://github.com/rrethy/nvim-base16)
  * [rsms/sublime-theme](https://github.com/rsms/sublime-theme)
  * [sainnhe/edge](https://github.com/sainnhe/edge)
  * [sainnhe/everforest](https://github.com/sainnhe/everforest)
  * [sainnhe/gruvbox-material](https://github.com/sainnhe/gruvbox-material)
  * [sainnhe/sonokai](https://github.com/sainnhe/sonokai)
  * [saurabhdaware/vscode-calvera-dark](https://github.com/saurabhdaware/vscode-calvera-dark)
  * [savq/melange](https://github.com/savq/melange)
  * [savq/melange-nvim](https://github.com/savq/melange-nvim)
  * [shaeinst/roshnivim-cs](https://github.com/shaeinst/roshnivim-cs)
  * [shatur/neovim-ayu](https://github.com/shatur/neovim-ayu)
  * [shaunsingh/moonlight.nvim](https://github.com/shaunsingh/moonlight.nvim)
  * [shaunsingh/nord.nvim](https://github.com/shaunsingh/nord.nvim)
  * [shaunsingh/seoul256.nvim](https://github.com/shaunsingh/seoul256.nvim)
  * [shaunsingh/solarized.nvim](https://github.com/shaunsingh/solarized.nvim)
  * [shrimpram/vim-stella](https://github.com/shrimpram/vim-stella)
  * [sickill/vim-monokai](https://github.com/sickill/vim-monokai)
  * [softmotions/vim-dark-frost-theme](https://github.com/softmotions/vim-dark-frost-theme)
  * [svermeulen/text-to-colorscheme](https://github.com/svermeulen/text-to-colorscheme) : generate colorschemes from text
  * [svrana/neosolarized.nvim](https://github.com/svrana/neosolarized.nvim)
  * [swalladge/paper.vim](https://github.com/swalladge/paper.vim)
  * [tanvirtin/monokai.nvim](https://github.com/tanvirtin/monokai.nvim)
  * [tanvirtin/nvim-monokai](https://github.com/tanvirtin/nvim-monokai)
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
  * [tyrannicaltoucan/vim-deep-space](https://github.com/tyrannicaltoucan/vim-deep-space)
  * [u03c1/outrun-vim](https://github.com/u03c1/outrun-vim)
  * [uloco/bluloco.nvim](https://github.com/uloco/bluloco.nvim)
  * [vigoux/oak](https://github.com/vigoux/oak)
  * [vim-conf-live/vimconflive2021-colorscheme](https://github.com/vim-conf-live/vimconflive2021-colorscheme)
  * [vim-scripts/mayansmoke](https://github.com/vim-scripts/mayansmoke)
  * [vim-scripts/peaksea](https://github.com/vim-scripts/peaksea)
  * [w0ng/vim-hybrid](https://github.com/w0ng/vim-hybrid)
  * [wgibbs/vim-irblack](https://github.com/wgibbs/vim-irblack)
  * [whatyouhide/vim-gotham](https://github.com/whatyouhide/vim-gotham)
  * [windwp/wind-colors](https://github.com/windwp/wind-colors)
  * [wittyjudge/gruvbox-material.nvim](https://github.com/wittyjudge/gruvbox-material.nvim)
  * [wuelnerdotexe/vim-enfocado](https://github.com/wuelnerdotexe/vim-enfocado)
  * [xero/miasma.nvim](https://github.com/xero/miasma.nvim)
  * [xiyaowong/transparent.nvim](https://github.com/xiyaowong/transparent.nvim) : remove background color to make transparent
  * [yagua/nebulous.nvim](https://github.com/yagua/nebulous.nvim)
  * [yashguptaz/calvera-dark.nvim](https://github.com/yashguptaz/calvera-dark.nvim)
  * [yazeed1s/minimal.nvim](https://github.com/yazeed1s/minimal.nvim)
  * [yazeed1s/oh-lucy.nvim](https://github.com/yazeed1s/oh-lucy.nvim)
  * [yong1le/darkplus.nvim](https://github.com/yong1le/darkplus.nvim)
  * [yonlu/omni.vim](https://github.com/yonlu/omni.vim)
  * [yuttie/hydrangea-vim](https://github.com/yuttie/hydrangea-vim)
  * [zaldih/themery.nvim](https://github.com/zaldih/themery.nvim) : switch between themes easy
  * [zootedb0t/citruszest.nvim](https://github.com/zootedb0t/citruszest.nvim)
## bufferline
  * [ap/vim-buftabline](https://github.com/ap/vim-buftabline)
  * [bagrat/vim-buffet](https://github.com/bagrat/vim-buffet) : takes your buffers and tabs, and shows them combined in the tabline
  * [bling/vim-bufferline](https://github.com/bling/vim-bufferline)
  * [jose-elias-alvarez/buftabline.nvim](https://github.com/jose-elias-alvarez/buftabline.nvim) : A low-config, minimalistic buffer tabline Neovim plugin written in Lua, [archived]
  * [ojroques/nvim-bufbar](https://github.com/ojroques/nvim-bufbar) : simple and very light bufferline for Neovim
  * [willothy/nvim-cokeline](https://github.com/willothy/nvim-cokeline) : for people with addictive personalties
  * [zefei/vim-wintabs](https://github.com/zefei/vim-wintabs)
## yanklist
  * [acksld/nvim-neoclip.lua](https://github.com/acksld/nvim-neoclip.lua)
  * [bfredl/nvim-miniyank](https://github.com/bfredl/nvim-miniyank)
  * [cyansprite/extract](https://github.com/cyansprite/extract)
  * [gbprod/yanky.nvim](https://github.com/gbprod/yanky.nvim)
  * [hrsh7th/nvim-pasta](https://github.com/hrsh7th/nvim-pasta) : The yank/paste enhancement plugin for neovim
  * [maxbrunsfeld/vim-yankstack](https://github.com/maxbrunsfeld/vim-yankstack)
  * [shougo/neoyank.vim](https://github.com/shougo/neoyank.vim) : Saves yank history
  * [svermeulen/vim-yoink](https://github.com/svermeulen/vim-yoink)
  * [tenxsoydev/karen-yank.nvim](https://github.com/tenxsoydev/karen-yank.nvim) : yanks your way
  * [vim-scripts/yankring.vim](https://github.com/vim-scripts/yankring.vim) : allows the user to configure the number of yanked, deleted and changed text
  * [yazgoo/yank-history](https://github.com/yazgoo/yank-history) : historize vim yanks and allow to search and paste from history based on FZF
## hop
  * [atusy/leap-search.nvim](https://github.com/atusy/leap-search.nvim) : leap oto a search pattern
  * [cbochs/portal.nvim](https://github.com/cbochs/portal.nvim) : aims to build upon and enhance existing jumplist motions
  * [folke/flash.nvim](https://github.com/folke/flash.nvim) : navigate your code faster
  * [haya14busa/vim-easyoperator-line](https://github.com/haya14busa/vim-easyoperator-line) : provides a much simpler way to use some operator for line in Vim
  * [haya14busa/vim-easyoperator-phrase](https://github.com/haya14busa/vim-easyoperator-phrase) : provides a much simpler way to use some operator for phrase than vim-easymotion
  * [mfussenegger/nvim-ts-hint-textobject](https://github.com/mfussenegger/nvim-ts-hint-textobject) : Treesitter hint textobject
  * [osyo-manga/vim-hopping](https://github.com/osyo-manga/vim-hopping) : This is a plugin that incrementally narrows down buffer lines
  * [ripxorip/aerojump.nvim](https://github.com/ripxorip/aerojump.nvim) : Aerojump is a fuzzy-match searcher/jumper for Neovim
  * [s1n7ax/nvim-window-picker](https://github.com/s1n7ax/nvim-window-picker) : This plugins prompts the user to pick a window and returns the window id of the picked window
  * [woosaaahh/sj.nvim](https://github.com/woosaaahh/sj.nvim) : Search based navigation combined with quick jump features
  * [yuki-yano/fuzzy-motion.vim](https://github.com/yuki-yano/fuzzy-motion.vim) : Jump to fuzzy match word
## movment
  * [abecodes/tabout.nvim](https://github.com/abecodes/tabout.nvim) : tabbing out from parentheses
  * [acksld/nvim-anywise-reg.lua](https://github.com/acksld/nvim-anywise-reg.lua) : paste a function somewhere else
  * [arp242/jumpy.vim](https://github.com/arp242/jumpy.vim) : filetype-specific mappings for [[, ]], g[, and g] to jump to the next or previous section
  * [chrisbra/improvedft](https://github.com/chrisbra/improvedft) : makes `f`, `t`, `T`, `F` have the ability to jump multiple lines
  * [dahu/vim-fanfingtastic](https://github.com/dahu/vim-fanfingtastic) : multiline, case insensitive and aliasing for `f`, `t`, `T`, `F`
  * [drybalka/tree-climber.nvim](https://github.com/drybalka/tree-climber.nvim) : easy navigation around the syntax-tree produced by the treesitter that also works in comments and multi-language files [treesitter]
  * [easymotion/vim-easymotion](https://github.com/easymotion/vim-easymotion) : Jump fast to any place to the screen by preesing only up to three keys
  * [fedepujol/move.nvim](https://github.com/fedepujol/move.nvim) : Gain the power to move lines and blocks
  * [ggandor/flit.nvim](https://github.com/ggandor/flit.nvim) : `f`/`t` on steroids
  * [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim) : general-purpose motion plugin for Neovim
  * [ggandor/lightspeed.nvim](https://github.com/ggandor/lightspeed.nvim) : Lightspeed is a motion plugin for Neovim, with a relatively small interface and lots of innovative ideas
  * [goldfeld/vim-seek](https://github.com/goldfeld/vim-seek) : like `f` but for two characters
  * [harrisoncramer/jump-tag](https://github.com/harrisoncramer/jump-tag) : extremely lightweight Neovim plugin that enables jumping to parent, sibling, and child tags
  * [haya14busa/is.vim](https://github.com/haya14busa/is.vim) : incremental search improved
  * [haya14busa/vim-asterisk](https://github.com/haya14busa/vim-asterisk) : provides improved * motions
  * [haya14busa/vim-edgemotion](https://github.com/haya14busa/vim-edgemotion) : like `jk` but stops at edge only
  * [hrsh7th/nvim-gtd](https://github.com/hrsh7th/nvim-gtd) : LSP's Go To Definition plugin for neovim
  * [hrsh7th/vim-feeling-move](https://github.com/hrsh7th/vim-feeling-move) : do you ever wish to be able to move only by feeling.
  * [hrsh7th/vim-foolish-move](https://github.com/hrsh7th/vim-foolish-move) : foolishly speed across the window with the cursor
  * [hrsh7th/vim-insert-point](https://github.com/hrsh7th/vim-insert-point) : cursor move on insert mode
  * [jinh0/eyeliner.nvim](https://github.com/jinh0/eyeliner.nvim) : unique `f` indicator for each word
  * [jorengarenar/vim-mvvis](https://github.com/jorengarenar/vim-mvvis) : Move visually selected text
  * [justinmk/vim-sneak](https://github.com/justinmk/vim-sneak) : Jump to any location specified by two characters
  * [liangxianzhe/nap.nvim](https://github.com/liangxianzhe/nap.nvim) : quickly jump between and previous buffer/tab/file/...
  * [mhinz/vim-lookup](https://github.com/mhinz/vim-lookup) : jumps to definitions of variables, functions, and commands as if tags were used, without needing a tags file
  * [phaazon/hop.nvim](https://github.com/phaazon/hop.nvim) : Hop is an EasyMotion-like plugin allowing you to jump anywhere in a document with as few keystrokes as possible
  * [phsix/faster.nvim](https://github.com/phsix/faster.nvim) : accelerate j or k moving
  * [preservim/vim-wheel](https://github.com/preservim/vim-wheel) : Screen-anchored cursor movement
  * [rasukarusan/nvim-select-multi-line](https://github.com/rasukarusan/nvim-select-multi-line) : Yank lines not adjacent
  * [rhysd/clever-f.vim](https://github.com/rhysd/clever-f.vim) : extends f, F, t and T mappings for more convenience. Instead of `;`, `f` is available to repeat
  * [rlane/pounce.nvim](https://github.com/rlane/pounce.nvim) : It's based on incremental fuzzy search.
  * [smiteshp/nvim-navbuddy](https://github.com/smiteshp/nvim-navbuddy) : easily navigate objects in a list
  * [svermeulen/vim-extended-ft](https://github.com/svermeulen/vim-extended-ft) : multiline, smart case, highlighting and more for `f`, `t`, `T`, `F`
  * [t9md/vim-smalls](https://github.com/t9md/vim-smalls) : Search and jump with easymotion style
  * [t9md/vim-textmanip](https://github.com/t9md/vim-textmanip) : move/duplicate blocks of text
  * [willothy/moveline.nvim](https://github.com/willothy/moveline.nvim) : move lines easy
  * [ziontee113/selectease](https://github.com/ziontee113/selectease) : easily select and jump between ts queries
  * [zirrostig/vim-schlepp](https://github.com/zirrostig/vim-schlepp) : allow the movement of lines (or blocks) of text around easily
## textobject
  * [adriaanzon/vim-textobj-blade-directive](https://github.com/adriaanzon/vim-textobj-blade-directive) : textobject for blade directive
  * [adriaanzon/vim-textobj-matchit](https://github.com/adriaanzon/vim-textobj-matchit) : creates text objects from matchit pairs (example: `if…end`)
  * [andrewferrier/textobj-diagnostic.nvim](https://github.com/andrewferrier/textobj-diagnostic.nvim) : textobj for diagnostics [no maintain]
  * [chaoren/vim-wordmotion](https://github.com/chaoren/vim-wordmotion) : treat uppercase/lowercase words next to each other as different words
  * [chrisgrieser/nvim-various-textobjs](https://github.com/chrisgrieser/nvim-various-textobjs) : Bundle of more than a dozen new text objects
  * [coderifous/textobj-word-column.vim](https://github.com/coderifous/textobj-word-column.vim) : makes operating on columns of code conceptually simpler and reduces keystrokes
  * [d4ku/vim-pushover](https://github.com/d4ku/vim-pushover) : provides an interface to easily create mappings to push around text-objects
  * [deathlyfrantic/vim-textobj-blanklines](https://github.com/deathlyfrantic/vim-textobj-blanklines) : provides a text object for groups of empty lines
  * [gcmt/wildfire.vim](https://github.com/gcmt/wildfire.vim) : quickly select the closest text object among a group of candidates
  * [jeetsukumaran/vim-indentwise](https://github.com/jeetsukumaran/vim-indentwise) : provides for motions based on indent depths or levels
  * [julian/vim-textobj-variable-segment](https://github.com/julian/vim-textobj-variable-segment) : providing a single text object for variable segments
  * [junegunn/vim-after-object](https://github.com/junegunn/vim-after-object) : Defines text objects to target text after the designated characters
  * [kana/vim-textobj-entire](https://github.com/kana/vim-textobj-entire) : Text objects for entire buffers
  * [kana/vim-textobj-indent](https://github.com/kana/vim-textobj-indent) : provide text objects to select a block of lines which are similarly indented to the current line
  * [kana/vim-textobj-line](https://github.com/kana/vim-textobj-line) : select a portion of the current line
  * [kana/vim-textobj-user](https://github.com/kana/vim-textobj-user) : creat your own text objects
  * [machakann/vim-sandwich](https://github.com/machakann/vim-sandwich) : a set of operator and textobject plugins to add/delete/replace surroundings of a sandwiched textobject
  * [michaeljsmith/vim-indent-object](https://github.com/michaeljsmith/vim-indent-object) : adds indentation based text objects
  * [misanthropicbit/vim-numbers](https://github.com/misanthropicbit/vim-numbers) : adds textobject to numbers
  * [nilsboy/vim-textobj-cindent](https://github.com/nilsboy/vim-textobj-cindent) : provides text objects to select a block of lines that have the same or higher indentation as the current line
  * [nvim-treesitter/nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects) : Syntax aware text-objects, select, move, swap, and peek support
  * [preservim/vim-textobj-quote](https://github.com/preservim/vim-textobj-quote) : better support for typographic quote characters
  * [preservim/vim-textobj-sentence](https://github.com/preservim/vim-textobj-sentence) : better sentence textobject
  * [rbtnn/vim-textobj-string](https://github.com/rbtnn/vim-textobj-string) : provide text objects to select a string
  * [rbtnn/vim-textobj-verbatimstring](https://github.com/rbtnn/vim-textobj-verbatimstring) : provide text objects (a@ and i@ by default) to select a verbatim string
  * [rbtnn/vim-textobj-vimfunctionname](https://github.com/rbtnn/vim-textobj-vimfunctionname) : provide text objects to select a vim function name
  * [reedes/vim-textobj-quote](https://github.com/reedes/vim-textobj-quote) : Extending Vim to better support typographic (‘curly’) quote characters
  * [rhysd/vim-textobj-anyblock](https://github.com/rhysd/vim-textobj-anyblock) : make `ib` and `ab` match all parentheses and not just brackets
  * [tkhren/vim-textobj-numeral](https://github.com/tkhren/vim-textobj-numeral) : Text objects for numbers
  * [tweekmonster/braceless.vim](https://github.com/tweekmonster/braceless.vim) : Text objects, folding, and more for Python and other indented languages
  * [vim-scripts/argtextobj.vim](https://github.com/vim-scripts/argtextobj.vim) : provides a as argument textobject
  * [wellle/targets.vim](https://github.com/wellle/targets.vim) : adds more bracket baised text objects.
  * [xxiaoa/ns-textobject.nvim](https://github.com/xxiaoa/ns-textobject.nvim) : A textobejct plugin with nvim-surround
## game
  * [alanfortlink/blackjack.nvim](https://github.com/alanfortlink/blackjack.nvim) : A simple game of blackjack
  * [alec-gibson/nvim-tetris](https://github.com/alec-gibson/nvim-tetris) : tetris game
  * [amix/vim-2048](https://github.com/amix/vim-2048) : 2048 game
  * [iqxd/vim-mine-sweeping](https://github.com/iqxd/vim-mine-sweeping) : mine sweeping game in vim
  * [jim-fx/sudoku.nvim](https://github.com/jim-fx/sudoku.nvim) : a game of sudoku
  * [max397574/hangman.nvim](https://github.com/max397574/hangman.nvim) : a game of hangman
  * [rbtnn/vim-game_engine](https://github.com/rbtnn/vim-game_engine) : vim-game_engine
  * [rbtnn/vim-mario](https://github.com/rbtnn/vim-mario) : Mario on Vim
  * [rbtnn/vim-puyo](https://github.com/rbtnn/vim-puyo) : Puyo on Vim
  * [rktjmp/shenzhen-solitaire.nvim](https://github.com/rktjmp/shenzhen-solitaire.nvim) : is a bit like FreeCell
  * [seandewar/killersheep.nvim](https://github.com/seandewar/killersheep.nvim) : A port of killersheep for Neovim
  * [seandewar/nvimesweeper](https://github.com/seandewar/nvimesweeper) : Play Minesweeper in Neovim
  * [sunjon/extmark-toy.nvim](https://github.com/sunjon/extmark-toy.nvim) : experimental demos and games
  * [theprimeagen/vim-be-good](https://github.com/theprimeagen/vim-be-good) : designed to make you better at vim by creating a game to practice basic movements in
  * [vim-scripts/tetris.vim](https://github.com/vim-scripts/tetris.vim) : A funny way to get used to VIM's h k l and <Space> key
  * [vim/killersheep](https://github.com/vim/killersheep) : Silly game to show off the new features of Vim 8.2
## startscreen
  * [chaitanyabsprip/present.nvim](https://github.com/chaitanyabsprip/present.nvim) : A Presentation plugin written for Neovim
  * [dbmrq/vim-howdy](https://github.com/dbmrq/vim-howdy) : tiny MRU start screen
  * [mhinz/vim-startify](https://github.com/mhinz/vim-startify) : the fancy start screen for vim
  * [startup-nvim/startup.nvim](https://github.com/startup-nvim/startup.nvim) : The fully customizable greeter for neovim
## projects-seessions
  * [ahmedkhalf/project.nvim](https://github.com/ahmedkhalf/project.nvim) : provides superior project management
  * [charludo/projectmgr.nvim](https://github.com/charludo/projectmgr.nvim) : projects and startup tasks
  * [dhruvasagar/vim-prosession](https://github.com/dhruvasagar/vim-prosession) : handle sessions like a pro
  * [ecthelionvi/neoview.nvim](https://github.com/ecthelionvi/neoview.nvim) : save and restore views and cursor across sessions
  * [ethanholz/nvim-lastplace](https://github.com/ethanholz/nvim-lastplace) : A Lua rewrite of [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace)
  * [folke/persistence.nvim](https://github.com/folke/persistence.nvim) : simple lua plugin for automated session management
  * [gennaro-tedesco/nvim-possession](https://github.com/gennaro-tedesco/nvim-possession) : no-nonsense session manager
  * [gnikdroy/projections.nvim](https://github.com/gnikdroy/projections.nvim) : A tiny project + sessions manager for neovim
  * [nvpm/nvpm](https://gitlab.com/nvpm/nvpm) : Neovim Project Manager
  * [jedrzejboczar/possession.nvim](https://github.com/jedrzejboczar/possession.nvim) : Flexible session management for Neovim
  * [natecraddock/sessions.nvim](https://github.com/natecraddock/sessions.nvim) : a simple session manager plugin
  * [natecraddock/workspaces.nvim](https://github.com/natecraddock/workspaces.nvim) : a simple plugin to manage workspace directories in neovim
  * [niuiic/multiple-session.nvim](https://github.com/niuiic/multiple-session.nvim) : multiple session manager
  * [nyngwang/suave.lua](https://github.com/nyngwang/suave.lua) : a quasi-acronym of "Session in LUA for Vim Enthusiasts."
  * [olimorris/persisted.nvim](https://github.com/olimorris/persisted.nvim) : simple lua plugin for automated session management within Neovim
  * [pluffie/neoproj](https://github.com/pluffie/neoproj) : Small yet powerful project manager
  * [rmagatti/auto-session](https://github.com/rmagatti/auto-session) : provide seamless automatic session management
  * [rmagatti/session-lens](https://github.com/rmagatti/session-lens) : extends auto-session through Telescope.nvim, creating a simple session switcher with fuzzy finding capabilities
  * [rutatang/spectacle.nvim](https://github.com/rutatang/spectacle.nvim) : easily work with multiple sessions
  * [shaeinst/penvim](https://github.com/shaeinst/penvim) : project's root directory and documents indentation detector with project based config loader
  * [shatur/neovim-session-manager](https://github.com/shatur/neovim-session-manager) : use built-in mksession to manage sessions like folders in VSCode
  * [sheodox/projectlaunch.nvim](https://github.com/sheodox/projectlaunch.nvim) : plugin for running commands in your project
  * [stevearc/resession.nvim](https://github.com/stevearc/resession.nvim) : replacement for :mksession with better api
  * [thaerkh/vim-workspace](https://github.com/thaerkh/vim-workspace) : mainteins sessions
  * [timotheesai/git-sessions.nvim](https://github.com/timotheesai/git-sessions.nvim) : Make :mksession work with keeping in sync git branch
  * [tpope/vim-obsession](https://github.com/tpope/vim-obsession) : automatically run `:mksession` on exit
  * [tpope/vim-projectionist](https://github.com/tpope/vim-projectionist) : provides granular project configuration using "projections"
  * [vim-scripts/sessionman.vim](https://github.com/vim-scripts/sessionman.vim) : keep session files in their decided folder and list all sessions, open session, open last session, close session, save session or show last session
  * [vim-volt/volt](https://github.com/vim-volt/volt) : Multi-platform CLI tool managing Vim plugin life
  * [xolox/vim-session](https://github.com/xolox/vim-session) : Extended session management for Vim
  * [zhimsel/vim-stay](https://github.com/zhimsel/vim-stay) : vim-stay adds automated view session creation and restoration whenever editing a buffer, across Vim sessions and window life cycles
## undotree
  * [jiaoshijie/undotree](https://github.com/jiaoshijie/undotree) : A neovim undotree plugin written in lua
  * [mbbill/undotree](https://github.com/mbbill/undotree) : visualizes undo history and makes it easier to browse and switch between different undo branches
  * [simnalamburt/vim-mundo](https://github.com/simnalamburt/vim-mundo) : visualizes the Vim undo tree written in python
  * [sjl/gundo.vim](https://github.com/sjl/gundo.vim) : visualize your Vim undo tree
## command
  * [ackeraa/todo.nvim](https://github.com/ackeraa/todo.nvim) : It helps you manage your to-do list
  * [andreicristianpetcu/vim-van](https://github.com/andreicristianpetcu/vim-van) : Read Unix man pages faster than a speeding bullet
  * [apeoplescalendar/apc.nvim](https://github.com/apeoplescalendar/apc.nvim) : A people's Calender in neovim
  * [asheq/close-buffers.vim](https://github.com/asheq/close-buffers.vim) : allows you to quickly bdeleteseveral buffers at once
  * [cespare/vim-sbd](https://github.com/cespare/vim-sbd) : Close buffers smartly [archived]
  * [chrisgrieser/nvim-genghis](https://github.com/chrisgrieser/nvim-genghis) : Convenience file operations for neovim
  * [crag666/code_runner.nvim](https://github.com/crag666/code_runner.nvim) : Code Runner for Neovim written in pure lua
  * [d0n9x1n/quickrun.vim](https://github.com/d0n9x1n/quickrun.vim) : Yet, just another quickrun plugin for vim
  * [dbeniamine/vim-mail](https://github.com/dbeniamine/vim-mail) : a small helper for writing mail from vim
  * [duane9/nvim-rg](https://github.com/duane9/nvim-rg) : allows you to run ripgrep from Neovim or Vim
  * [echuraev/translate-shell.vim](https://github.com/echuraev/translate-shell.vim) : a plugin for translating text without leaving Vim
  * [felipec/notmuch-vim](https://github.com/felipec/notmuch-vim) : provides a fully usable mail client interface, utilizing the notmuch framework
  * [dbeniamine/vim-mail](https://gitlab.com/dbeniamine/vim-mail) : a small helper for writing mail from vim
  * [inkarkat/vim-advancedsorters](https://github.com/inkarkat/vim-advancedsorters) : Dose sorting block wise instead of line wise
  * [itchyny/calendar.vim](https://github.com/itchyny/calendar.vim) : A calendar application for Vim
  * [kkoomen/vim-doge](https://github.com/kkoomen/vim-doge) : will generate a proper documentation skeleton based on certain expressions
  * [koenverburg/cmd-palette.nvim](https://github.com/koenverburg/cmd-palette.nvim) : a simple command pallet
  * [kovetskiy/neovim-move](https://github.com/kovetskiy/neovim-move) : provides a way to move files
  * [mattn/emmet-vim](https://github.com/mattn/emmet-vim) : a vim plug-in which provides support for expanding abbreviations similar to emmet
  * [max397574/markdownhelp.nvim](https://github.com/max397574/markdownhelp.nvim) : Helps with markdown
  * [max397574/vmath.nvim](https://github.com/max397574/vmath.nvim) : neovim version of vmath
  * [mhinz/vim-sayonara](https://github.com/mhinz/vim-sayonara) : single command that deletes the current buffer and handles the current window in a smart way
  * [moll/vim-bbye](https://github.com/moll/vim-bbye) : delete buffers without closing your windows or messing up your layout
  * [niuiic/translate.nvim](https://github.com/niuiic/translate.nvim) : translator for neovim
  * [ojroques/nvim-bufdel](https://github.com/ojroques/nvim-bufdel) : A very small Neovim plugin to improve the deletion of buffers
  * [orlp/vim-bunlink](https://github.com/orlp/vim-bunlink) : this plugin can delete your buffers without destroying your windows/splits
  * [qpkorr/vim-bufkill](https://github.com/qpkorr/vim-bufkill) : trying to unload, delete or wipe a buffer without closing the window or split? You'll like this
  * [rbgrouleff/bclose.vim](https://github.com/rbgrouleff/bclose.vim) : deleting a buffer in Vim without closing the window
  * [rrethy/vim-spotlight](https://github.com/rrethy/vim-spotlight) : `:Spotlight` and that's it.
  * [saverio976/music.nvim](https://github.com/saverio976/music.nvim) : play music with mpv in nvim
  * [sidofc/carbon.nvim](https://github.com/sidofc/carbon.nvim) : provides a simple tree view of the directory Neovim was opened with/in
  * [skanehira/google-map.vim](https://github.com/skanehira/google-map.vim) : open google map in neovim
  * [stevearc/aerial.nvim](https://github.com/stevearc/aerial.nvim) : code outline window for skimming and quick navigation
  * [tyru/capture.vim](https://github.com/tyru/capture.vim) : Show Ex command output in a buffer
  * [uga-rosa/translate.nvim](https://github.com/uga-rosa/translate.nvim) : nvim plugin to translate text
  * [vim-scripts/tagbar](https://github.com/vim-scripts/tagbar) : vim plugin for browsing the tags of source code files
  * [vim-utils/vim-man](https://github.com/vim-utils/vim-man) : View man pages in vim
  * [will133/vim-dirdiff](https://github.com/will133/vim-dirdiff) : If you like Vim's diff mode, you would love to do this recursively on two directories
  * [wsdjeg/vim-cheat](https://github.com/wsdjeg/vim-cheat) : cheat in vim
  * [yehuohan/popc](https://github.com/yehuohan/popc) : Popc in layer manager,including layers of buffer, bookmark, worksapce.....
  * [yuratomo/w3m.vim](https://github.com/yuratomo/w3m.vim) : w3m inside vim
## replace
  * [acksld/muren.nvim](https://github.com/acksld/muren.nvim) : do multiple search and replace with ease
  * [chrisgrieser/nvim-alt-substitute](https://github.com/chrisgrieser/nvim-alt-substitute) : search using lua patterns instead of vim regex
  * [cshuaimin/ssr.nvim](https://github.com/cshuaimin/ssr.nvim) : Structural search and replace
  * [dkprice/vim-easygrep](https://github.com/dkprice/vim-easygrep) : Fast and Easy Find and Replace Across Multiple Files
  * [eugen0329/vim-esearch](https://github.com/eugen0329/vim-esearch) : for easy async search and replace across multiple files
  * [junegunn/vim-fnr](https://github.com/junegunn/vim-fnr) : Find-N-Replace in Vim with live preview
  * [ray-x/sad.nvim](https://github.com/ray-x/sad.nvim) : project wide find and replace
  * [romgrk/searchreplace.vim](https://github.com/romgrk/searchreplace.vim) : search thru multiple files and replace the search
  * [roobert/search-replace.nvim](https://github.com/roobert/search-replace.nvim) : supercharge search and replace
  * [s1n7ax/nvim-search-and-replace](https://github.com/s1n7ax/nvim-search-and-replace) : Absolutly minimal plugin to search and replace multiple files in current working directory
  * [windwp/nvim-spectre](https://github.com/windwp/nvim-spectre) : search and replace panel
## terminal
  * [2kabhishek/termim.nvim](https://github.com/2kabhishek/termim.nvim) : improved terminal usage
  * [akinsho/nvim-toggleterm.lua](https://github.com/akinsho/nvim-toggleterm.lua) : A neovim plugin to persist and toggle multiple terminals during an editing session
  * [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim) : persist and toggle multiple terminals
  * [brettanomyces/nvim-editcommand](https://github.com/brettanomyces/nvim-editcommand) : Edit your current shell command inside a scratch buffer
  * [brettanomyces/nvim-terminus](https://github.com/brettanomyces/nvim-terminus) : Edit your current command in a scratch buffer
  * [bronzehedwick/vim-primary-terminal](https://github.com/bronzehedwick/vim-primary-terminal) : Simple terminal management for Neovim.
  * [caenrique/nvim-toggle-terminal](https://github.com/caenrique/nvim-toggle-terminal) : Toggle terminal buffer or create new one if there is none
  * [chengzeyi/multiterm.vim](https://github.com/chengzeyi/multiterm.vim) : Toggle and Switch Between Multiple Floating Terminals
  * [chomosuke/term-edit.nvim](https://github.com/chomosuke/term-edit.nvim) : edit commands in the terminal like any other buffer
  * [itmecho/bufterm.nvim](https://github.com/itmecho/bufterm.nvim) : simple neovim plugin to manage a terminal buffer for your session
  * [itmecho/neoterm.nvim](https://github.com/itmecho/neoterm.nvim) : Simple neovim terminal plugin written in lua
  * [jlesquembre/nterm.nvim](https://github.com/jlesquembre/nterm.nvim) : neovim plugin to interact with the terminal emulator, with notifications
  * [kassio/neoterm](https://github.com/kassio/neoterm) : Use the same terminal for everything
  * [lenovsky/nuake](https://github.com/lenovsky/nuake) : A Quake-style terminal panel
  * [loricandre/oneterm](https://github.com/loricandre/oneterm) : One terminal plugin to rule them all (eventually)
  * [loricandre/oneterm.nvim](https://github.com/loricandre/oneterm.nvim) : One terminal plugin to rule them all (eventually)
  * [mizlan/termbufm](https://github.com/mizlan/termbufm) : A wrapper around the Neovim terminal window
  * [nikvdp/neomux](https://github.com/nikvdp/neomux) : a neovim <> terminal integration plugin
  * [numtostr/fterm.nvim](https://github.com/numtostr/fterm.nvim) : No-nonsense floating terminal plugin for neovim
  * [nyngwang/neoterm.lua](https://github.com/nyngwang/neoterm.lua) : Attach a terminal for each buffer
  * [oberblastmeister/termwrapper.nvim](https://github.com/oberblastmeister/termwrapper.nvim) : a wrapper for neovim's terminal features to make them more user friendly
  * [pianocomposer321/consolation.nvim](https://github.com/pianocomposer321/consolation.nvim) : A general-perpose terminal wrapper and management plugin for neovim
  * [s1n7ax/nvim-terminal](https://github.com/s1n7ax/nvim-terminal) : open/toggle the terminals in Neovim
  * [shougo/deol.nvim](https://github.com/shougo/deol.nvim) : dark powered shell for Neovim
  * [skywind3000/vim-terminal-help](https://github.com/skywind3000/vim-terminal-help) : make working with terminal easier
  * [toniz4/vim-stt](https://github.com/toniz4/vim-stt) : Simple Togglable Terminal
  * [voldikss/vim-floaterm](https://github.com/voldikss/vim-floaterm) : Use vim terminal in the floating/popup window
## file-explorer
  * [ap/vim-readdir](https://github.com/ap/vim-readdir) : minimal directory browser in ~100 lines of code
  * [dinhhuy258/sfm.nvim](https://github.com/dinhhuy258/sfm.nvim) : simple tree viewer
  * [francoiscabrol/ranger.vim](https://github.com/francoiscabrol/ranger.vim) : Ranger integration in vim
  * [ipod825/vim-netranger](https://github.com/ipod825/vim-netranger) : not just a tree file manager
  * [is0n/fm-nvim](https://github.com/is0n/fm-nvim) : a Neovim plugin that lets you use your favorite terminal file managers
  * [justinmk/vim-dirvish](https://github.com/justinmk/vim-dirvish) : Path navigator designed to work with Vim's built-in mechanisms and complementary plugins
  * [kelly-lin/ranger.nvim](https://github.com/kelly-lin/ranger.nvim) : ranger integration
  * [kevinhwang91/rnvimr](https://github.com/kevinhwang91/rnvimr) : use Ranger in a floating window
  * [lmburns/lf.nvim](https://github.com/lmburns/lf.nvim) : plugin for the `lf` file manager
  * [luukvbaal/nnn.nvim](https://github.com/luukvbaal/nnn.nvim) : File manager for Neovim powered by nnnp
  * [mattn/vim-molder](https://github.com/mattn/vim-molder) : Minimal File Explorer
  * [mcchrish/nnn.vim](https://github.com/mcchrish/nnn.vim) : File manager for vim/neovim powered by n³
  * [nvim-neo-tree/neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim) : Neovim plugin to browse the file system and other tree like structures
  * [obaland/vfiler.vim](https://github.com/obaland/vfiler.vim) : File explorer plugin for Vim
  * [preservim/nerdtree](https://github.com/preservim/nerdtree) : a file system explorer for the Vim editor
  * [ptzz/lf.vim](https://github.com/ptzz/lf.vim) : lf integration in vim and neovim
  * [ripxorip/bolt.nvim](https://github.com/ripxorip/bolt.nvim) : Filter-as-you-type file manager for Neovim
  * [scjangra/files-nvim](https://github.com/scjangra/files-nvim) : external file explorers
  * [scrooloose/nerdtree](https://github.com/scrooloose/nerdtree) : a file system Explorer for the vim editor
  * [shougo/defx.nvim](https://github.com/shougo/defx.nvim) : a dark powered plugin for Neovim/Vim to browse files
  * [shougo/vimfiler.vim](https://github.com/shougo/vimfiler.vim) : powerful file explorer implemented in Vim script [no development]
  * [stevearc/oil.nvim](https://github.com/stevearc/oil.nvim) : vim-vinegar like file explorer
  * [tamago324/lir.nvim](https://github.com/tamago324/lir.nvim) : A simple file explorer
  * [theblob42/drex.nvim](https://github.com/theblob42/drex.nvim) : Another DiRectory EXplorer for Neovim
  * [timuntersberger/neofs](https://github.com/timuntersberger/neofs) : file manager for neovim written in lua
  * [troydm/easytree.vim](https://github.com/troydm/easytree.vim) : a simple tree file manager for vim
  * [vifm/neovim-vifm](https://github.com/vifm/neovim-vifm) : Integration between vifm (the vi file manager) and vim [archived]
  * [vifm/vifm.vim](https://github.com/vifm/vifm.vim) : provides integration with Vifm
## plugin-maneger
  * [chiyadev/dep](https://github.com/chiyadev/dep) : A versatile, declarative and correct neovim package manager
  * [egalpin/apt-vim](https://github.com/egalpin/apt-vim) : Yet another Plugin Manager
  * [faerryn/plogins.nvim](https://github.com/faerryn/plogins.nvim) : A fast, simple, and elegant Neovim plugin manager written in Lua
  * [faerryn/user.nvim](https://github.com/faerryn/user.nvim) : Well, here's another plugin manager, inspired by Emacs' straight.el and use-package
  * [folke/lazy.nvim](https://github.com/folke/lazy.nvim) : modern plugin manager for Neovim
  * [gmarik/vundle.vim](https://github.com/gmarik/vundle.vim) : a vim plugin manager
  * [jorengarenar/minplug](https://github.com/jorengarenar/minplug) : Its function is simple: download, update and enable plugins
  * [junegunn/vim-plug](https://github.com/junegunn/vim-plug) : minimalist Vim plugin manager
  * [k-takata/minpac](https://github.com/k-takata/minpac) : A minimal package manager for Vim 8 (and Neovim)
  * [kristijanhusak/vim-packager](https://github.com/kristijanhusak/vim-packager) : Yet Another plugin manager for Vim
  * [marcweber/vim-addon-manager](https://github.com/marcweber/vim-addon-manager) : fetch & activate plugins at startup or runtime depending on your needs
  * [rbtnn/vim-pkgsync](https://github.com/rbtnn/vim-pkgsync) : The minimalist plugin manager for Vim
  * [rktjmp/pact.nvim](https://github.com/rktjmp/pact.nvim) : a semver focused, pessimistic plugin manager for Neovim
  * [savq/paq-nvim](https://github.com/savq/paq-nvim) : Neovim package manager written in Lua
  * [shougo/dein.vim](https://github.com/shougo/dein.vim) : dark powered Vim/Neovim plugin manager
  * [shougo/neobundle.vim](https://github.com/shougo/neobundle.vim) : a next generation Vim plugin manager [no development]
  * [tek/chromatin](https://github.com/tek/chromatin) : a manager for plugins built in Haskell with nvim-hs and ribosome
  * [tek/proteome.nvim](https://github.com/tek/proteome.nvim) : [deprecated] use [tek/chromatin](https://github.com/tek/chromatin) instead
  * [vundlevim/vundle.vim](https://github.com/vundlevim/vundle.vim) : is short for Vim bundle and is a Vim plugin manager
  * [wbthomason/packer.nvim](https://github.com/wbthomason/packer.nvim) : use-package inspired plugin/package management for Neovim
  * [zgpio/brew.nvim](https://github.com/zgpio/brew.nvim) : plugin manager, rewrite dein with neovim builtin lua
## git
  * [airblade/vim-gitgutter](https://github.com/airblade/vim-gitgutter) : git diff
  * [akinsho/git-conflict.nvim](https://github.com/akinsho/git-conflict.nvim) : A plugin to visualise and resolve conflicts
  * [almo7aya/openingh.nvim](https://github.com/almo7aya/openingh.nvim) : Open the current file in github
  * [apzelos/blamer.nvim](https://github.com/apzelos/blamer.nvim) : a git blamer plugin
  * [bobrown101/git_blame.nvim](https://github.com/bobrown101/git_blame.nvim) : An unapologetic ripoff of vim-fugitives GBlame .... but written in lua
  * [braxtons12/blame_line.nvim](https://github.com/braxtons12/blame_line.nvim) : A simple and configurable git blame line using virtual text for Neovim
  * [christoomey/vim-conflicted](https://github.com/christoomey/vim-conflicted) : aids in resolving git merge and rebase conflicts
  * [cohama/agit.vim](https://github.com/cohama/agit.vim) : Yet another gitk clone for Vim
  * [dinhhuy258/git.nvim](https://github.com/dinhhuy258/git.nvim) : is the simple clone of the plugin vim-fugitive which is written in Lua
  * [dm1try/git_fastfix](https://github.com/dm1try/git_fastfix) : Neovim plugin for applying "fast git fixups"(using UI) to the current development branch
  * [drzel/vim-repo-edit](https://github.com/drzel/vim-repo-edit) : One second to read GitHub code with vim
  * [dundargoc/gh.nvim](https://github.com/dundargoc/gh.nvim) : gh in neovim
  * [f-person/git-blame.nvim](https://github.com/f-person/git-blame.nvim) : git blame plugin for Neovim
  * [iberianpig/tig-explorer.vim](https://github.com/iberianpig/tig-explorer.vim) : Vim plugin to use Tig as a git client
  * [idanarye/vim-merginal](https://github.com/idanarye/vim-merginal) : aims to provide a nice interface for dealing with Git branches
  * [int3/vim-extradite](https://github.com/int3/vim-extradite) : A git commit browser / git log wrapper that extends fugitive.vim
  * [ipod825/igit.nvim](https://github.com/ipod825/igit.nvim) : A git plugin for neovim
  * [jaxbot/github-issues.vim](https://github.com/jaxbot/github-issues.vim) : Github issue integration in Vim
  * [jreybert/vimagit](https://github.com/jreybert/vimagit) : Ease your git workflow within vim
  * [junegunn/gv.vim](https://github.com/junegunn/gv.vim) : A git commit browser
  * [junegunn/vim-github-dashboard](https://github.com/junegunn/vim-github-dashboard) : Browse GitHub events (user dashboard, user/repo activity
  * [junkblocker/git-time-lapse](https://github.com/junkblocker/git-time-lapse) : git timeline inside buffer
  * [kdheepak/lazygit.nvim](https://github.com/kdheepak/lazygit.nvim) : Plugin for calling lazygit from within neovim
  * [lambdalisue/gin.vim](https://github.com/lambdalisue/gin.vim) : handle git repository from Vim
  * [lambdalisue/gina.vim](https://github.com/lambdalisue/gina.vim) : asynchronously control git repositories
  * [ldelossa/gh.nvim](https://github.com/ldelossa/gh.nvim) : a plugin for interactive code reviews which take place on the GitHub platform
  * [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim) : Super fast git decorations implemented
  * [mattn/gist-vim](https://github.com/mattn/gist-vim) : This is a vimscript for creating gists
  * [mattn/vim-gist](https://github.com/mattn/vim-gist) : a vimscript for creating gists
  * [neogitorg/neogit](https://github.com/neogitorg/neogit) : magit clone for neovim
  * [odie/gitabra](https://github.com/odie/gitabra) : A little Magit in neovim
  * [pwntester/octo.nvim](https://github.com/pwntester/octo.nvim) : Edit and review GitHub issues and pull requests
  * [rawnly/gist.nvim](https://github.com/rawnly/gist.nvim) : create gist from the current file
  * [rbong/vim-flog](https://github.com/rbong/vim-flog) : lightweight and powerful git branch viewer
  * [rhysd/committia.vim](https://github.com/rhysd/committia.vim) : This plugin improves the git commit buffer
  * [rhysd/git-messenger.vim](https://github.com/rhysd/git-messenger.vim) : reveal the hidden message from Git under the cursor quickly
  * [ruifm/gitlinker.nvim](https://github.com/ruifm/gitlinker.nvim) : generate shareable file permalinks (with line ranges) for several git web frontend hosts
  * [samoshkin/vim-mergetool](https://github.com/samoshkin/vim-mergetool) : Efficient way of using Vim as a Git mergetool
  * [sindrets/diffview.nvim](https://github.com/sindrets/diffview.nvim) : Single tabpage interface for easily cycling through diffs for all modified files for any git rev
  * [sodapopcan/vim-twiggy](https://github.com/sodapopcan/vim-twiggy) : Maintain your bearings while branching with Git
  * [stsewd/fzf-checkout.vim](https://github.com/stsewd/fzf-checkout.vim) : Manage branches and tags with fzf
  * [tanvirtin/vgit.nvim](https://github.com/tanvirtin/vgit.nvim) : Visual Git Plugin for Neovim to enhance your git experience
  * [theprimeagen/git-worktree.nvim](https://github.com/theprimeagen/git-worktree.nvim) : simple wrapper around git worktree operations, create, switch, and delete
  * [timuntersberger/neogit](https://github.com/timuntersberger/neogit) : Magit clone for Neovim
  * [topaxi/gh-actions.nvim](https://github.com/topaxi/gh-actions.nvim) : do github actions from neovim
  * [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive) : Fugitive is the premier Vim plugin for Git
  * [tpope/vim-rhubarb](https://github.com/tpope/vim-rhubarb) : If fugitive.vim is the Git, rhubarb.vim is the Hub
  * [tveskag/nvim-blame-line](https://github.com/tveskag/nvim-blame-line) : uses neovims virtual text to print git blame info
  * [wsdjeg/github.vim](https://github.com/wsdjeg/github.vim) : Another github v3 api implemented in viml
## finder
  * [2kabhishek/nerdy.nvim](https://github.com/2kabhishek/nerdy.nvim) : search nerd-font icons
  * [aaronhallaert/advanced-git-search.nvim](https://github.com/aaronhallaert/advanced-git-search.nvim) : git search extension for Telescope or fzf-lua
  * [amirrezaask/fuzzy.nvim](https://github.com/amirrezaask/fuzzy.nvim) : Fast, Simple, Powerfull fuzzy finder all in lua
  * [cbochs/grapple.nvim](https://github.com/cbochs/grapple.nvim) : aims to provide immediate navigation to important files
  * [conweller/findr.vim](https://github.com/conweller/findr.vim) : An incremental narrowing engine
  * [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim) : Full path fuzzy file, buffer, mru, tag, ... finder for Vim.
  * [dyng/ctrlsf.vim](https://github.com/dyng/ctrlsf.vim) : An ack/ag/pt/rg powered code search and view tool
  * [everduin94/nvim-quick-switcher](https://github.com/everduin94/nvim-quick-switcher) : Quickly navigate to related/alternate files/extensions based on the current file name
  * [fholgado/minibufexpl.vim](https://github.com/fholgado/minibufexpl.vim) : fork of Bindu Wavell's MiniBufExpl with impovments
  * [fiatjaf/neuron.vim](https://github.com/fiatjaf/neuron.vim) : Manage your Zettelkasten with the help of neuron
  * [gaborvecsei/memento.nvim](https://github.com/gaborvecsei/memento.nvim) : remembers where you've been
  * [gfanto/fzf-lsp.nvim](https://github.com/gfanto/fzf-lsp.nvim) : search for symbols using the neovim builtin lsp
  * [ibhagwan/fzf-lua](https://github.com/ibhagwan/fzf-lua) : fzf loves lua
  * [ido-nvim/ido.nvim](https://github.com/ido-nvim/ido.nvim) : Emacs inspired narrowing system
  * [jlanzarotta/bufexplorer](https://github.com/jlanzarotta/bufexplorer) : BufExplorer Plugin for Vim
  * [junegunn/fzf](https://github.com/junegunn/fzf) : FZF Vim integration
  * [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim) : Things you can do with fzf and Vim
  * [liuchengxu/vim-clap](https://github.com/liuchengxu/vim-clap) : modern generic interactive finder and dispatcher, based on the newly feature: floating_win of neovim or popup of vim
  * [loricandre/fzterm.nvim](https://github.com/loricandre/fzterm.nvim) : a fuzzy finder plugin, using a floating terminal and basically nothing else [depreciated]
  * [lotabout/skim.vim](https://github.com/lotabout/skim.vim) : This is a fork of fzf.vim but for skim
  * [mhinz/vim-grepper](https://github.com/mhinz/vim-grepper) : Use your favorite grep tool to start an asynchronous search
  * [mileszs/ack.vim](https://github.com/mileszs/ack.vim) : Run your favorite search tool from Vim, with an enhanced results list
  * [mrjones2014/dash.nvim](https://github.com/mrjones2014/dash.nvim) : Query Dash.app within Neovim with your fuzzy finder
  * [nvim-pack/nvim-spectre](https://github.com/nvim-pack/nvim-spectre) : A search panel for neovim
  * [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) : is a highly extendable fuzzy finder over list
  * [ojroques/nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy) : This plugin makes the Neovim LSP client use FZF to display results and navigate the code
  * [romgrk/kirby.nvim](https://github.com/romgrk/kirby.nvim) : picker based on kui.nvim
  * [roosta/fzf-folds.vim](https://github.com/roosta/fzf-folds.vim) : lets you fuzzy search for folds in a file
  * [samoshkin/vim-find-files](https://github.com/samoshkin/vim-find-files) : Search for files and show results in a quickfix list, a new buffer
  * [shougo/ddu.vim](https://github.com/shougo/ddu.vim) : provides an asynchronous fuzzy finder UI
  * [shougo/denite.nvim](https://github.com/shougo/denite.nvim) : It is like a fuzzy finder, but is more generic [no development]
  * [shougo/unite.vim](https://github.com/shougo/unite.vim) : search and display information from arbitrary sources like files, buffers, recently used files or registers [no development]
  * [shoumodip/helm.nvim](https://github.com/shoumodip/helm.nvim) : The completion framework for love and life
  * [skywind3000/leaderf-snippet](https://github.com/skywind3000/leaderf-snippet) : takes the advantage of the well-known fuzzy finder Leaderf to provide an intuitive way to input snippets
  * [svermeulen/nvim-marksman](https://github.com/svermeulen/nvim-marksman) : lightweight file finder
  * [tamago324/leaderf-neosnippet](https://github.com/tamago324/leaderf-neosnippet) : LeaderF support for neosnippet
  * [toppair/reach.nvim](https://github.com/toppair/reach.nvim) : buffer / mark / tabpage / colorscheme switcher
  * [tzachar/fuzzy.nvim](https://github.com/tzachar/fuzzy.nvim) : An abstraction layer on top of fzf and fzy
  * [vigoux/azy.nvim](https://github.com/vigoux/azy.nvim) : fuzzy finder based on fzy
  * [vijaymarupudi/nvim-fzf](https://github.com/vijaymarupudi/nvim-fzf) : An asynchronous Lua API for using fzf in Neovim
  * [vijaymarupudi/nvim-fzf-commands](https://github.com/vijaymarupudi/nvim-fzf-commands) : A repository for commands using the nvim-fzf library
  * [vim-ctrlspace/vim-ctrlspace](https://github.com/vim-ctrlspace/vim-ctrlspace) : open finder by pressing `<C-space>`
  * [vim-scripts/bufexplorer.zip](https://github.com/vim-scripts/bufexplorer.zip) : quickly and easily switch between buffers
  * [vim-scripts/grep.vim](https://github.com/vim-scripts/grep.vim) : integrates the grep, fgrep, egrep, and agrep tools with Vim
  * [willthbill/opener.nvim](https://github.com/willthbill/opener.nvim) : A workspace/context switcher for neovim
  * [wincent/command-t](https://github.com/wincent/command-t) : provides an extremely fast "fuzzy" mechanism
  * [wincent/ferret](https://github.com/wincent/ferret) : improves Vim's multi-file search in four ways
  * [wsdjeg/flygrep.vim](https://github.com/wsdjeg/flygrep.vim) : Fly grep in vim
  * [x3ero0/dired.nvim](https://github.com/x3ero0/dired.nvim) : file browser inspired from Emacs Dired
  * [yggdroot/leaderf](https://github.com/yggdroot/leaderf) : An efficient fuzzy finder that helps to locate files, buffers, mrus, gtags, etc
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
## repalce
  * [brooth/far.vim](https://github.com/brooth/far.vim) : replace text through multiple files
  * [gbprod/substitute.nvim](https://github.com/gbprod/substitute.nvim) : very easy to perform quick substitutions and exchange
  * [svermeulen/vim-subversive](https://github.com/svermeulen/vim-subversive) : make it very easy to perform quick substitutions
## filemanager
  * [airodactyl/neovim-ranger](https://github.com/airodactyl/neovim-ranger) : ranger for neovim
  * [camspiers/snap](https://github.com/camspiers/snap) : fast finder system
  * [kyazdani42/nvim-tree.lua](https://github.com/kyazdani42/nvim-tree.lua) : A File Explorer For Neovim Written In Lua
  * [ms-jpq/chadtree](https://github.com/ms-jpq/chadtree) : File Manager for Neovim, Better than NERDTree
  * [xuyuanp/yanil](https://github.com/xuyuanp/yanil) : Yet Another Nerdtree In Lua
  * [zgpio/tree.nvim](https://github.com/zgpio/tree.nvim) : File explorer powered by C++
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
## abbreviations
  * [0styx0/abbreinder.nvim](https://github.com/0styx0/abbreinder.nvim) : shows abbreviations if the whole thing is typed
  * [pocco81/abbrevman.nvim](https://github.com/pocco81/abbrevman.nvim) : that manages abbreviations for various natural and programming languages
  * [tpope/vim-abolish](https://github.com/tpope/vim-abolish) : easily create similar abbreviations
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
## pairs
  * [alvan/vim-closetag](https://github.com/alvan/vim-closetag) : Auto close (X)HTML tags
  * [andymass/vim-matchup](https://github.com/andymass/vim-matchup) : highlight, navigate, and operate on sets of matching text
  * [max-0406/autoclose.nvim](https://github.com/max-0406/autoclose.nvim) : minimalist autoclose plugin for Neovim
  * [steelsojka/pears.nvim](https://github.com/steelsojka/pears.nvim) : Auto pair plugin for neovim
  * [windwp/nvim-autopairs](https://github.com/windwp/nvim-autopairs) : A super powerful autopair plugin for Neovim that supports multiple characters
  * [zhiyuanlck/smart-pairs](https://github.com/zhiyuanlck/smart-pairs) : provides pairs completion, deletion and jump
## remote
  * [chipsenkbeil/distant.nvim](https://github.com/chipsenkbeil/distant.nvim) : A wrapper around distant that enables users to edit remote files from the comfort of their local environment
  * [esensar/nvim-dev-containera](https://github.com/esensar/nvim-dev-containera) : provide functionality similar to VSCode's remote container development plugin
  * [jamestthompson3/nvim-remote-containers](https://github.com/jamestthompson3/nvim-remote-containers) : give you the functionality of VSCode's remote container development plugin
## highlight-underline
  * [azabiong/vim-highlighter](https://github.com/azabiong/vim-highlighter) : highlight words and expressions
  * [itchyny/vim-cursorword](https://github.com/itchyny/vim-cursorword) : Underlines the word under the cursor
  * [pocco81/highstr.nvim](https://github.com/pocco81/highstr.nvim) : highlighting visual selections like in a normal document editor
  * [rrethy/vim-illuminate](https://github.com/rrethy/vim-illuminate) : automatically highlighting other uses of the current word under the cursor
  * [xiyaowong/nvim-cursorword](https://github.com/xiyaowong/nvim-cursorword) : part of [yamatsum/nvim-cursorline](https://github.com/yamatsum/nvim-cursorline)
  * [yamatsum/nvim-cursorline](https://github.com/yamatsum/nvim-cursorline) : Highlight words and lines on the cursor
## marks
  * [chentoast/marks.nvim](https://github.com/chentoast/marks.nvim) : A better user experience for interacting with and manipulating Vim marks
  * [crusj/bookmarks.nvim](https://github.com/crusj/bookmarks.nvim) : Remember file locations and sort by time and frequency
  * [kshenoy/vim-signature](https://github.com/kshenoy/vim-signature) : place, toggle and display marks
  * [mattesgroeger/vim-bookmarks](https://github.com/mattesgroeger/vim-bookmarks) : toggling bookmarks per line and more
## markdown-org-neorg
  * [jubnzv/mdeval.nvim](https://github.com/jubnzv/mdeval.nvim) : allows you evaluate code blocks inside markdown, vimwiki, orgmode.nvim and norg documents
  * [lukas-reineke/headlines.nvim](https://github.com/lukas-reineke/headlines.nvim) : adds highlights for text filetypes, like markdown, orgmode, and neorg
  * [nvim-neorg/neorg](https://github.com/nvim-neorg/neorg) : neorg Integration
  * [nvim-orgmode/orgmode](https://github.com/nvim-orgmode/orgmode) : org Integration
  * [suan/vim-instant-markdown](https://github.com/suan/vim-instant-markdown) : preview markdown files in your browser
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
  * [terryma/vim-multiple-cursors](https://github.com/terryma/vim-multiple-cursors) : is not maineind/depreciated, use [mg979/vim-visual-multi](https://github.com/mg979/vim-visual-multi) instead
## libs
  * [0styx0/abbremand.nvim](https://github.com/0styx0/abbremand.nvim) : is library for [0styx0/abbreinder.nvim](https://github.com/0styx0/abbreinder.nvim)
  * [anuvyklack/keymap-layer.nvim](https://github.com/anuvyklack/keymap-layer.nvim) : is library for [anuvyklack/hydra.nvim](https://github.com/anuvyklack/hydra.nvim)
## starter-page
  * [glepnir/dashboard-nvim](https://github.com/glepnir/dashboard-nvim)
  * [goolord/alpha-nvim](https://github.com/goolord/alpha-nvim)
# Not-documented
  * [adaszko/tree_climber_rust.nvim](https://github.com/adaszko/tree_climber_rust.nvim)
  * [adeattwood/ivy.nvim](https://github.com/adeattwood/ivy.nvim)
  * [adelarsq/snake_cursor.nvim](https://github.com/adelarsq/snake_cursor.nvim)
  * [adia-dev/cpy_buffers.nvim](https://github.com/adia-dev/cpy_buffers.nvim)
  * [agoodshort/telescope-git-submodules.nvim](https://github.com/agoodshort/telescope-git-submodules.nvim)
  * [agusdolard/backout.nvim](https://github.com/agusdolard/backout.nvim)
  * [ahollister/nota.nvim](https://github.com/ahollister/nota.nvim)
  * [aikooo7/funnyfiles.nvim](https://github.com/aikooo7/funnyfiles.nvim)
  * [airpods69/yagp.nvim](https://github.com/airpods69/yagp.nvim)
  * [aityz/usage.nvim](https://github.com/aityz/usage.nvim)
  * [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)
  * [ajnasz/notify-send.nvim](https://github.com/ajnasz/notify-send.nvim)
  * [ajnasz/nvim-rfind](https://github.com/ajnasz/nvim-rfind)
  * [ajnasz/telescope-runcmd.nvim](https://github.com/ajnasz/telescope-runcmd.nvim)
  * [akinsho/org-bullets.nvim](https://github.com/akinsho/org-bullets.nvim)
  * [al1-ce/just.nvim](https://github.com/al1-ce/just.nvim)
  * [albingroen/quick.nvim](https://github.com/albingroen/quick.nvim)
  * [alejandrosuero/freeze-code.nvim](https://github.com/alejandrosuero/freeze-code.nvim)
  * [alexshelto/boringcomment.nvim](https://github.com/alexshelto/boringcomment.nvim)
  * [alextricity25/nvim_weekly_plugin_configs](https://github.com/alextricity25/nvim_weekly_plugin_configs)
  * [allaman/emoji.nvim](https://github.com/allaman/emoji.nvim)
  * [alpha2phi/modern-neovim](https://github.com/alpha2phi/modern-neovim)
  * [altermo/beacon.nvim](https://github.com/altermo/beacon.nvim)
  * [altermo/iedit.nvim](https://github.com/altermo/iedit.nvim)
  * [altermo/nwm](https://github.com/altermo/nwm)
  * [altermo/nxwm](https://github.com/altermo/nxwm)
  * [altermo/small.nvim](https://github.com/altermo/small.nvim)
  * [amadanmath/diag_ignore.nvim](https://github.com/amadanmath/diag_ignore.nvim)
  * [amarakon/nvim-cmp-fonts](https://github.com/amarakon/nvim-cmp-fonts)
  * [amarakon/nvim-cmp-lua-latex-symbols](https://github.com/amarakon/nvim-cmp-lua-latex-symbols)
  * [amitds1997/remote-nvim.nvim](https://github.com/amitds1997/remote-nvim.nvim)
  * [anasinnyk/nvim-k8s-crd](https://github.com/anasinnyk/nvim-k8s-crd)
  * [andersevenrud/nvim_context_vt](https://github.com/andersevenrud/nvim_context_vt)
  * [andrewferrier/wrapping.nvim](https://github.com/andrewferrier/wrapping.nvim)
  * [andrew-george/telescope-themes](https://github.com/andrew-george/telescope-themes)
  * [andrewradev/dealwithit.vim](https://github.com/andrewradev/dealwithit.vim)
  * [andrewradev/discotheque.vim](https://github.com/andrewradev/discotheque.vim)
  * [andrewradev/inline_edit.vim](https://github.com/andrewradev/inline_edit.vim)
  * [andrewradev/iseven.vim](https://github.com/andrewradev/iseven.vim)
  * [andrewradev/typewriter.vim](https://github.com/andrewradev/typewriter.vim)
  * [anfigeno/mestizo.nvim](https://github.com/anfigeno/mestizo.nvim)
  * [antosha417/nvim-compare-with-clipboard](https://github.com/antosha417/nvim-compare-with-clipboard)
  * [antosha417/nvim-lsp-file-operations](https://github.com/antosha417/nvim-lsp-file-operations)
  * [anurag3301/nvim-platformio.lua](https://github.com/anurag3301/nvim-platformio.lua)
  * [anuvyklack/middleclass](https://github.com/anuvyklack/middleclass)
  * [apple/pkl-neovim](https://github.com/apple/pkl-neovim)
  * [ariel-frischer/bmessages.nvim](https://github.com/ariel-frischer/bmessages.nvim)
  * [arjunmahishi/flow.nvim](https://github.com/arjunmahishi/flow.nvim)
  * [arminfro/hand-side-fix.nvim](https://github.com/arminfro/hand-side-fix.nvim)
  * [arminveres/md-pdf.nvim](https://github.com/arminveres/md-pdf.nvim)
  * [arsham/arshlib.nvim](https://github.com/arsham/arshlib.nvim)
  * [arsham/indent-tools.nvim](https://github.com/arsham/indent-tools.nvim)
  * [artemave/workspace-diagnostics.nvim](https://github.com/artemave/workspace-diagnostics.nvim)
  * [ashfinal/vim-colors-paper](https://github.com/ashfinal/vim-colors-paper)
  * [aspeddro/cmp-pandoc.nvim](https://github.com/aspeddro/cmp-pandoc.nvim)
  * [aspeddro/lsp_menu.nvim](https://github.com/aspeddro/lsp_menu.nvim)
  * [astronvim/astrolsp](https://github.com/astronvim/astrolsp)
  * [atinylittleshell/comment-repl.nvim](https://github.com/atinylittleshell/comment-repl.nvim)
  * [atmosuwiryo/vim-winteriscoming](https://github.com/atmosuwiryo/vim-winteriscoming)
  * [atusy/treemonkey.nvim](https://github.com/atusy/treemonkey.nvim)
  * [atusy/tsnode-marker.nvim](https://github.com/atusy/tsnode-marker.nvim)
  * [ausgefuchster/quickselect.nvim](https://github.com/ausgefuchster/quickselect.nvim)
  * [axelf4/vim-strip-trailing-whitespace](https://github.com/axelf4/vim-strip-trailing-whitespace)
  * [axelvc/template-string.nvim](https://github.com/axelvc/template-string.nvim)
  * [ayga2k/freeze.nvim](https://github.com/ayga2k/freeze.nvim)
  * [azatakmyradov/easyswitch.nvim](https://github.com/azatakmyradov/easyswitch.nvim)
  * [b0o/lavi.nvim](https://github.com/b0o/lavi.nvim)
  * [b0o/nvim-tree-preview.lua](https://github.com/b0o/nvim-tree-preview.lua)
  * [backdround/global-note.nvim](https://github.com/backdround/global-note.nvim)
  * [backdround/improved-ft.nvim](https://github.com/backdround/improved-ft.nvim)
  * [backdround/improved-search.nvim](https://github.com/backdround/improved-search.nvim)
  * [backdround/neowords.nvim](https://github.com/backdround/neowords.nvim)
  * [badhi/nvim-treesitter-cpp-tools](https://github.com/badhi/nvim-treesitter-cpp-tools)
  * [bakks/butterfish.nvim](https://github.com/bakks/butterfish.nvim)
  * [barklan/capslock.nvim](https://github.com/barklan/capslock.nvim)
  * [barreiroleo/ltex_extra.nvim](https://github.com/barreiroleo/ltex_extra.nvim)
  * [bartman/history-select.nvim](https://github.com/bartman/history-select.nvim)
  * [bartste/nvim-projectrc](https://github.com/bartste/nvim-projectrc)
  * [beeender/comradeneovim](https://github.com/beeender/comradeneovim)
  * [benlubas/image-save.nvim](https://github.com/benlubas/image-save.nvim)
  * [benlubas/molten-nvim](https://github.com/benlubas/molten-nvim)
  * [benlubas/wrapping-paper.nvim](https://github.com/benlubas/wrapping-paper.nvim)
  * [bennypowers/changesets.nvim](https://github.com/bennypowers/changesets.nvim)
  * [bergercookie/vim-debugstring](https://github.com/bergercookie/vim-debugstring)
  * [bgaillard/readonly.nvim](https://github.com/bgaillard/readonly.nvim)
  * [birdeehub/nixcats-nvim](https://github.com/birdeehub/nixcats-nvim)
  * [blazkowolf/gruber-darker.nvim](https://github.com/blazkowolf/gruber-darker.nvim)
  * [bleksak/diffthis.nvim](https://github.com/bleksak/diffthis.nvim)
  * [bleksak/laravel-ide-helper.nvim](https://github.com/bleksak/laravel-ide-helper.nvim)
  * [bloznelis/before.nvim](https://github.com/bloznelis/before.nvim)
  * [blumaa/octopus.nvim](https://github.com/blumaa/octopus.nvim)
  * [blumaa/ohne-accidents](https://github.com/blumaa/ohne-accidents)
  * [blumaa/ohne-accidents.nvim](https://github.com/blumaa/ohne-accidents.nvim)
  * [bluz71/nvim-linefly](https://github.com/bluz71/nvim-linefly)
  * [boltlessengineer/smart-tab.nvim](https://github.com/boltlessengineer/smart-tab.nvim)
  * [branimire/fix-auto-scroll.nvim](https://github.com/branimire/fix-auto-scroll.nvim)
  * [brenton-leighton/multiple-cursors.nvim](https://github.com/brenton-leighton/multiple-cursors.nvim)
  * [brianaung/yasl.nvim](https://github.com/brianaung/yasl.nvim)
  * [briangwaltney/paren-hint.nvim](https://github.com/briangwaltney/paren-hint.nvim)
  * [brymer-meneses/grammar-guard.nvim](https://github.com/brymer-meneses/grammar-guard.nvim)
  * [b-src/lazy-nix-helper.nvim](https://github.com/b-src/lazy-nix-helper.nvim)
  * [bullets-vim/bullets.vim](https://github.com/bullets-vim/bullets.vim)
  * [cademichael/gotest.nvim](https://github.com/cademichael/gotest.nvim)
  * [calind/selenized.nvim](https://github.com/calind/selenized.nvim)
  * [calops/hmts.nvim](https://github.com/calops/hmts.nvim)
  * [camdenclark/flyboy](https://github.com/camdenclark/flyboy)
  * [cameron-wags/rainbow_csv.nvim](https://github.com/cameron-wags/rainbow_csv.nvim)
  * [camnw/lf-vim](https://github.com/camnw/lf-vim)
  * [carbon-steel/detour.nvim](https://github.com/carbon-steel/detour.nvim)
  * [carlosrocha/chrome-remote.nvim](https://github.com/carlosrocha/chrome-remote.nvim)
  * [catgoose/angler.nvim](https://github.com/catgoose/angler.nvim)
  * [catgoose/coderunner.nvim](https://github.com/catgoose/coderunner.nvim)
  * [catgoose/do-the-needful](https://github.com/catgoose/do-the-needful)
  * [catgoose/do-the-needful.nvim](https://github.com/catgoose/do-the-needful.nvim)
  * [catgoose/telescope-helpgrep.nvim](https://github.com/catgoose/telescope-helpgrep.nvim)
  * [catgoose/vue-goto-definition.nvim](https://github.com/catgoose/vue-goto-definition.nvim)
  * [ccaglak/larago.nvim](https://github.com/ccaglak/larago.nvim)
  * [ccaglak/namespace.nvim](https://github.com/ccaglak/namespace.nvim)
  * [ccaglak/phptools.nvim](https://github.com/ccaglak/phptools.nvim)
  * [ccaglak/phputils.nvim](https://github.com/ccaglak/phputils.nvim)
  * [cdelledonne/vim-utest](https://github.com/cdelledonne/vim-utest)
  * [cdmill/neomodern.nvim](https://github.com/cdmill/neomodern.nvim)
  * [chadcat7/prism](https://github.com/chadcat7/prism)
  * [chaitanyabsprip/fastaction.nvim](https://github.com/chaitanyabsprip/fastaction.nvim)
  * [chaitanyabsprip/hashish.nvim](https://github.com/chaitanyabsprip/hashish.nvim)
  * [chen244/csv-tools.lua](https://github.com/chen244/csv-tools.lua)
  * [chiendo97/intellij.vim](https://github.com/chiendo97/intellij.vim)
  * [chipsenkbeil/org-roam.nvim](https://github.com/chipsenkbeil/org-roam.nvim)
  * [chomosuke/typst-preview.nvim](https://github.com/chomosuke/typst-preview.nvim)
  * [chrisbra/csv.vim](https://github.com/chrisbra/csv.vim)
  * [chrisgrieser/cmp-nerdfont](https://github.com/chrisgrieser/cmp-nerdfont)
  * [chrisgrieser/nvim-chainsaw](https://github.com/chrisgrieser/nvim-chainsaw)
  * [chrisgrieser/nvim-kickstart-python](https://github.com/chrisgrieser/nvim-kickstart-python)
  * [chrisgrieser/nvim-lsp-endhints](https://github.com/chrisgrieser/nvim-lsp-endhints)
  * [chrisgrieser/nvim-origami](https://github.com/chrisgrieser/nvim-origami)
  * [chrisgrieser/nvim-puppeteer](https://github.com/chrisgrieser/nvim-puppeteer)
  * [chrisgrieser/nvim-rip-substitute](https://github.com/chrisgrieser/nvim-rip-substitute)
  * [chrisgrieser/nvim-rulebook](https://github.com/chrisgrieser/nvim-rulebook)
  * [chrisgrieser/nvim-scissors](https://github.com/chrisgrieser/nvim-scissors)
  * [chrisgrieser/nvim-tinygit](https://github.com/chrisgrieser/nvim-tinygit)
  * [chrishrb/gx.nvim](https://github.com/chrishrb/gx.nvim)
  * [christianchiarulli/bookmark.nvim](https://github.com/christianchiarulli/bookmark.nvim)
  * [chuufmaster/buffer-vacuum](https://github.com/chuufmaster/buffer-vacuum)
  * [chuufmaster/markdown-toc](https://github.com/chuufmaster/markdown-toc)
  * [chuwy/ucm.nvim](https://github.com/chuwy/ucm.nvim)
  * [cjodo/convert.nvim](https://github.com/cjodo/convert.nvim)
  * [ckipp01/stylua-nvim](https://github.com/ckipp01/stylua-nvim)
  * [cnshsliu/smp.nvim](https://github.com/cnshsliu/smp.nvim)
  * [codota/tabnine-nvim](https://github.com/codota/tabnine-nvim)
  * [codybuell/cmp-lbdb](https://github.com/codybuell/cmp-lbdb)
  * [coffebar/neovim-project](https://github.com/coffebar/neovim-project)
  * [coffebar/transfer.nvim](https://github.com/coffebar/transfer.nvim)
  * [comatory/gh-co.nvim](https://github.com/comatory/gh-co.nvim)
  * [comfysage/chaivim](https://github.com/comfysage/chaivim)
  * [comfysage/evergarden](https://github.com/comfysage/evergarden)
  * [comfysage/keymaps.nvim](https://github.com/comfysage/keymaps.nvim)
  * [comfysage/shelf.nvim](https://github.com/comfysage/shelf.nvim)
  * [configs/nvim-dap.lua](https://github.com/configs/nvim-dap.lua)
  * [creativecreature/pulse](https://github.com/creativecreature/pulse)
  * [creativenull/dotfyle-metadata.nvim](https://github.com/creativenull/dotfyle-metadata.nvim)
  * [cris-lml007/neoplus](https://github.com/cris-lml007/neoplus)
  * [crispgm/cmp-beancount](https://github.com/crispgm/cmp-beancount)
  * [crispybaccoon/chaivim](https://github.com/crispybaccoon/chaivim)
  * [crispybaccoon/evergarden](https://github.com/crispybaccoon/evergarden)
  * [cryptomilk/nightcity.nvim](https://github.com/cryptomilk/nightcity.nvim)
  * [cseelus/vim-colors-lucid](https://github.com/cseelus/vim-colors-lucid)
  * [cvigilv/esqueleto.nvim](https://github.com/cvigilv/esqueleto.nvim)
  * [cvigilv/patana.nvim](https://github.com/cvigilv/patana.nvim)
  * [cvusmo/linuxunrealbuildtool.nvim](https://github.com/cvusmo/linuxunrealbuildtool.nvim)
  * [cwood-sdf/pineapple](https://github.com/cwood-sdf/pineapple)
  * [cwood-sdf/spaceport.nvim](https://github.com/cwood-sdf/spaceport.nvim)
  * [d00h/telescope-any](https://github.com/d00h/telescope-any)
  * [daenikon/marknav.nvim](https://github.com/daenikon/marknav.nvim)
  * [daic0r/dap-helper.nvim](https://github.com/daic0r/dap-helper.nvim)
  * [daniilrozanov/cmake.nvim](https://github.com/daniilrozanov/cmake.nvim)
  * [danilshvalov/org-modern.nvim](https://github.com/danilshvalov/org-modern.nvim)
  * [dapc11/telescope-yaml.nvim](https://github.com/dapc11/telescope-yaml.nvim)
  * [dasgandlaf/cmp-nvim-autohotkey](https://github.com/dasgandlaf/cmp-nvim-autohotkey)
  * [dasupradyumna/launch.nvim](https://github.com/dasupradyumna/launch.nvim)
  * [databases/neoclip.sqlite3](https://github.com/databases/neoclip.sqlite3)
  * [datsfilipe/vesper.nvim](https://github.com/datsfilipe/vesper.nvim)
  * [david-kunz/gen.nvim](https://github.com/david-kunz/gen.nvim)
  * [david-kunz/markid](https://github.com/david-kunz/markid)
  * [david-kunz/treesitter-unit](https://github.com/david-kunz/treesitter-unit)
  * [davidosomething/format-ts-errors.nvim](https://github.com/davidosomething/format-ts-errors.nvim)
  * [davidsierradz/cmp-conventionalcommits](https://github.com/davidsierradz/cmp-conventionalcommits)
  * [dawsers/navigator.nvim](https://github.com/dawsers/navigator.nvim)
  * [dax89/automaton.nvim](https://github.com/dax89/automaton.nvim)
  * [ddl004/poop.nvim](https://github.com/ddl004/poop.nvim)
  * [deanrumsby/tree-sitter-blade](https://github.com/deanrumsby/tree-sitter-blade)
  * [deathbeam/autocomplete.nvim](https://github.com/deathbeam/autocomplete.nvim)
  * [deathbeam/lspecho.nvim](https://github.com/deathbeam/lspecho.nvim)
  * [delphinus/cellwidths.nvim](https://github.com/delphinus/cellwidths.nvim)
  * [delphinus/cmp-ctags](https://github.com/delphinus/cmp-ctags)
  * [dense-analysis/neural](https://github.com/dense-analysis/neural)
  * [denstiny/styledoc.nvim](https://github.com/denstiny/styledoc.nvim)
  * [desdic/macrothis.nvim](https://github.com/desdic/macrothis.nvim)
  * [desdic/marlin.nvim](https://github.com/desdic/marlin.nvim)
  * [dev-cycles/contextive](https://github.com/dev-cycles/contextive)
  * [dgagn/diagflow.nvim](https://github.com/dgagn/diagflow.nvim)
  * [dgox16/devicon-colorscheme.nvim](https://github.com/dgox16/devicon-colorscheme.nvim)
  * [dgox16/oldworld.nvim](https://github.com/dgox16/oldworld.nvim)
  * [dhanus3133/leetbuddy.nvim](https://github.com/dhanus3133/leetbuddy.nvim)
  * [dharmx-lua/nvim](https://github.com/dharmx-lua/nvim)
  * [dharmx/telescope-media.nvim](https://github.com/dharmx/telescope-media.nvim)
  * [dharmx/toml.nvim](https://github.com/dharmx/toml.nvim)
  * [dharmx/track.nvim](https://github.com/dharmx/track.nvim)
  * [dhruvasagar/packup](https://github.com/dhruvasagar/packup)
  * [dhruvasagar/vim-audiobox](https://github.com/dhruvasagar/vim-audiobox)
  * [dhruvasagar/vim-highlight-word](https://github.com/dhruvasagar/vim-highlight-word)
  * [diegoulloao/neofusion.nvim](https://github.com/diegoulloao/neofusion.nvim)
  * [dimmed/brightened.](https://github.com/dimmed/brightened.)
  * [diogo-ss/42-header.nvim](https://github.com/diogo-ss/42-header.nvim)
  * [diogo-ss/five-server.nvim](https://github.com/diogo-ss/five-server.nvim)
  * [djancyp/better-comments.nvim](https://github.com/djancyp/better-comments.nvim)
  * [dkendal/nvim-kitty](https://github.com/dkendal/nvim-kitty)
  * [dlvhdr/gh-addressed.nvim](https://github.com/dlvhdr/gh-addressed.nvim)
  * [dlvhdr/gh-blame.nvim](https://github.com/dlvhdr/gh-blame.nvim)
  * [dmitmel/cmp-vim-lsp](https://github.com/dmitmel/cmp-vim-lsp)
  * [dmmulroy/ts-error-translator.nvim](https://github.com/dmmulroy/ts-error-translator.nvim)
  * [doctorfree/cheatsheet.nvim](https://github.com/doctorfree/cheatsheet.nvim)
  * [doganalper/template.nvim](https://github.com/doganalper/template.nvim)
  * [dokwork/lualine-ex](https://github.com/dokwork/lualine-ex)
  * [domsch1988/mattern.nvim](https://github.com/domsch1988/mattern.nvim)
  * [doom-neovim/doom-nvim](https://github.com/doom-neovim/doom-nvim)
  * [dorage/ts-manual-import.nvim](https://github.com/dorage/ts-manual-import.nvim)
  * [dosx001/cmp-commit](https://github.com/dosx001/cmp-commit)
  * [doums/tenaille.nvim](https://github.com/doums/tenaille.nvim)
  * [dronakurl/injectme.nvim](https://github.com/dronakurl/injectme.nvim)
  * [drop-stones/im-switch.nvim](https://github.com/drop-stones/im-switch.nvim)
  * [drybalka/clean.nvim](https://github.com/drybalka/clean.nvim)
  * [dseum/window.nvim](https://github.com/dseum/window.nvim)
  * [dsummersl/nvim-sluice](https://github.com/dsummersl/nvim-sluice)
  * [dundalek/lazy-lsp.nvim](https://github.com/dundalek/lazy-lsp.nvim)
  * [dunstontc/vim-vscode-theme](https://github.com/dunstontc/vim-vscode-theme)
  * [dvrlabs/takeout.nvim](https://github.com/dvrlabs/takeout.nvim)
  * [dwrdx/mywords.nvim](https://github.com/dwrdx/mywords.nvim)
  * [dzfrias/arena.nvim](https://github.com/dzfrias/arena.nvim)
  * [e-cal/askgpt](https://github.com/e-cal/askgpt)
  * [echasnovski/mini.ai](https://github.com/echasnovski/mini.ai)
  * [echasnovski/mini.clue](https://github.com/echasnovski/mini.clue)
  * [echasnovski/mini.completion](https://github.com/echasnovski/mini.completion)
  * [echasnovski/mini.diff](https://github.com/echasnovski/mini.diff)
  * [echasnovski/mini-git](https://github.com/echasnovski/mini-git)
  * [echasnovski/mini.indentscope](https://github.com/echasnovski/mini.indentscope)
  * [echasnovski/mini.map](https://github.com/echasnovski/mini.map)
  * [echasnovski/mini.operators](https://github.com/echasnovski/mini.operators)
  * [echasnovski/mini.pick](https://github.com/echasnovski/mini.pick)
  * [edte/normal-colon.nvim](https://github.com/edte/normal-colon.nvim)
  * [efueyo/td.nvim](https://github.com/efueyo/td.nvim)
  * [ejrichards/baredot.nvim](https://github.com/ejrichards/baredot.nvim)
  * [ejrichards/mise.nvim](https://github.com/ejrichards/mise.nvim)
  * [ej-shafran/compile-mode.nvim](https://github.com/ej-shafran/compile-mode.nvim)
  * [eldritch-theme/eldritch](https://github.com/eldritch-theme/eldritch)
  * [eldritch-theme/eldritch.nvim](https://github.com/eldritch-theme/eldritch.nvim)
  * [elias-gill/makeman](https://github.com/elias-gill/makeman)
  * [emmanueltouzery/code-compass.nvim](https://github.com/emmanueltouzery/code-compass.nvim)
  * [emmanueltouzery/decisive.nvim](https://github.com/emmanueltouzery/decisive.nvim)
  * [emmanueltouzery/elixir-extras.nvim](https://github.com/emmanueltouzery/elixir-extras.nvim)
  * [eoh-bse/minintro.nvim](https://github.com/eoh-bse/minintro.nvim)
  * [epwalsh/pomo.nvim](https://github.com/epwalsh/pomo.nvim)
  * [e-q/okcolors.nvim](https://github.com/e-q/okcolors.nvim)
  * [erichlf/devcontainer-cli.nvim](https://github.com/erichlf/devcontainer-cli.nvim)
  * [erickkramer/nvim-ros2](https://github.com/erickkramer/nvim-ros2)
  * [ernstwi/juggler.nvim](https://github.com/ernstwi/juggler.nvim)
  * [evesdropper/luasnip-latex-snippets.nvim](https://github.com/evesdropper/luasnip-latex-snippets.nvim)
  * [f3fora/nvim-texlabconfig](https://github.com/f3fora/nvim-texlabconfig)
  * [fabianwirth/search.nvim](https://github.com/fabianwirth/search.nvim)
  * [fabijanzulj/blame.nvim](https://github.com/fabijanzulj/blame.nvim)
  * [fasterius/simple-zoom.nvim](https://github.com/fasterius/simple-zoom.nvim)
  * [fbuchlak/cmp-symfony-router](https://github.com/fbuchlak/cmp-symfony-router)
  * [fbuchlak/telescope-directory.nvim](https://github.com/fbuchlak/telescope-directory.nvim)
  * [fcancelinha/northern.nvim](https://github.com/fcancelinha/northern.nvim)
  * [fdschmidt93/telescope-egrepify.nvim](https://github.com/fdschmidt93/telescope-egrepify.nvim)
  * [febri-i/auto-require](https://github.com/febri-i/auto-require)
  * [febri-i/snake.nvim](https://github.com/febri-i/snake.nvim)
  * [feel-ix-343/markdown-oxide](https://github.com/feel-ix-343/markdown-oxide)
  * [feiyoug/commander.nvim](https://github.com/feiyoug/commander.nvim)
  * [felipejz/i18n-menu.nvim](https://github.com/felipejz/i18n-menu.nvim)
  * [felipelema/cmp-async-path](https://github.com/felipelema/cmp-async-path)
  * [felipesanchezsoberanis/copy-path](https://github.com/felipesanchezsoberanis/copy-path)
  * [fildo7525/reloader.nvim](https://github.com/fildo7525/reloader.nvim)
  * [fireisgood/spaceman.nvim](https://github.com/fireisgood/spaceman.nvim)
  * [fnune/recall.nvim](https://github.com/fnune/recall.nvim)
  * [folke/edgy.nvim](https://github.com/folke/edgy.nvim)
  * [folke/lazydev.nvim](https://github.com/folke/lazydev.nvim)
  * [folke/ts-comments.nvim](https://github.com/folke/ts-comments.nvim)
  * [fowlie/open-github-repo](https://github.com/fowlie/open-github-repo)
  * [franespeche/strawberry](https://github.com/franespeche/strawberry)
  * [frankroeder/parrot.nvim](https://github.com/frankroeder/parrot.nvim)
  * [fraserlee/scratchpad](https://github.com/fraserlee/scratchpad)
  * [frayzen/cpp-tools.nvim](https://github.com/frayzen/cpp-tools.nvim)
  * [fredeeb/tardis.nvim](https://github.com/fredeeb/tardis.nvim)
  * [fredrikaverpil/neotest-golang](https://github.com/fredrikaverpil/neotest-golang)
  * [frostplexx/mason-bridge.nvim](https://github.com/frostplexx/mason-bridge.nvim)
  * [furkanzmc/zettelkasten.nvim](https://github.com/furkanzmc/zettelkasten.nvim)
  * [fynnfluegge/monet.nvim](https://github.com/fynnfluegge/monet.nvim)
  * [g0sapo/visual.nvim](https://github.com/g0sapo/visual.nvim)
  * [gaborvecsei/usage-tracker.nvim](https://github.com/gaborvecsei/usage-tracker.nvim)
  * [gabrigutiz/termacro.nvim](https://github.com/gabrigutiz/termacro.nvim)
  * [gaelph/logsitter.nvim](https://github.com/gaelph/logsitter.nvim)
  * [garyhurtz/cmp_bulma.nvim](https://github.com/garyhurtz/cmp_bulma.nvim)
  * [garyhurtz/cmp_kitty](https://github.com/garyhurtz/cmp_kitty)
  * [garymjr/nvim-snippets](https://github.com/garymjr/nvim-snippets)
  * [gcballesteros/jupytext.nvim](https://github.com/gcballesteros/jupytext.nvim)
  * [gczcn/antonym.nvim](https://github.com/gczcn/antonym.nvim)
  * [geg2102/nvim-python-repl](https://github.com/geg2102/nvim-python-repl)
  * [gelio/cmp-natdat](https://github.com/gelio/cmp-natdat)
  * [ggandor/spooky.nvim](https://github.com/ggandor/spooky.nvim)
  * [gh-liu/fold_line.nvim](https://github.com/gh-liu/fold_line.nvim)
  * [giannibyoung/chezmoi-telescope.nvim](https://github.com/giannibyoung/chezmoi-telescope.nvim)
  * [giusgad/pets.nvim](https://github.com/giusgad/pets.nvim)
  * [gloggers99/build.nvim](https://github.com/gloggers99/build.nvim)
  * [gr3yh4tt3r93/zellij-nav.nvim](https://github.com/gr3yh4tt3r93/zellij-nav.nvim)
  * [graphql/graphiql](https://github.com/graphql/graphiql)
  * [grapp-dev/nui-components.nvim](https://github.com/grapp-dev/nui-components.nvim)
  * [gregorias/coerce.nvim](https://github.com/gregorias/coerce.nvim)
  * [gregorias/toggle.nvim](https://github.com/gregorias/toggle.nvim)
  * [gsuuon/llm.nvim](https://github.com/gsuuon/llm.nvim)
  * [gsuuon/note.nvim](https://github.com/gsuuon/note.nvim)
  * [gsuuon/tshjkl.nvim](https://github.com/gsuuon/tshjkl.nvim)
  * [guilherme-puida/tesoura.nvim](https://github.com/guilherme-puida/tesoura.nvim)
  * [gustaveikaas/easy-dotnet.nvim](https://github.com/gustaveikaas/easy-dotnet.nvim)
  * [gustavokatel/sidebar.nvim](https://github.com/gustavokatel/sidebar.nvim)
  * [h4ckm1n-dev/kube-utils-nvim](https://github.com/h4ckm1n-dev/kube-utils-nvim)
  * [hajime-suzuki/vuffers.nvim](https://github.com/hajime-suzuki/vuffers.nvim)
  * [hakonharnes/img-clip.nvim](https://github.com/hakonharnes/img-clip.nvim)
  * [harrisoncramer/gitlab.nvim](https://github.com/harrisoncramer/gitlab.nvim)
  * [haydenmeade/neotest-jest](https://github.com/haydenmeade/neotest-jest)
  * [hedyhli/outline.nvim](https://github.com/hedyhli/outline.nvim)
  * [hek14/symbol-overlay.nvim](https://github.com/hek14/symbol-overlay.nvim)
  * [henriqueartur/neo-gitmoji.nvim](https://github.com/henriqueartur/neo-gitmoji.nvim)
  * [hesiod-au/fastkeywins.nvim](https://github.com/hesiod-au/fastkeywins.nvim)
  * [hiberabyss/bzlops.vim](https://github.com/hiberabyss/bzlops.vim)
  * [hinell/duplicate.nvim](https://github.com/hinell/duplicate.nvim)
  * [hinell/lsp-timeout.nvim](https://github.com/hinell/lsp-timeout.nvim)
  * [hiphish/neotest-busted](https://github.com/hiphish/neotest-busted)
  * [hiphish/nvim-cmp-vlime](https://github.com/hiphish/nvim-cmp-vlime)
  * [hiphish/yo-dawg.nvim](https://github.com/hiphish/yo-dawg.nvim)
  * [hkupty/neovim-bridge](https://github.com/hkupty/neovim-bridge)
  * [hoganmcdonald/rails-rspec-toggle.nvim](https://github.com/hoganmcdonald/rails-rspec-toggle.nvim)
  * [homerours/jumper.nvim](https://github.com/homerours/jumper.nvim)
  * [honamduong/hybrid.nvim](https://github.com/honamduong/hybrid.nvim)
  * [hotwatermorning/auto-git-diff](https://github.com/hotwatermorning/auto-git-diff)
  * [hougesen/blame-me.nvim](https://github.com/hougesen/blame-me.nvim)
  * [hprior/telescope-gpt](https://github.com/hprior/telescope-gpt)
  * [hrsh7th/cmp-copilot](https://github.com/hrsh7th/cmp-copilot)
  * [hrsh7th/cmp-emoji](https://github.com/hrsh7th/cmp-emoji)
  * [hrsh7th/cmp-omni](https://github.com/hrsh7th/cmp-omni)
  * [https://git.sr.ht/~swaits/thethethe.nvim](https://github.com/https://git.sr.ht/~swaits/thethethe.nvim)
  * [https://git.sr.ht/~swaits/zellij-nav.nvim](https://github.com/https://git.sr.ht/~swaits/zellij-nav.nvim)
  * [https://git.sr.ht/~tomleb/repo-url.nvim](https://github.com/https://git.sr.ht/~tomleb/repo-url.nvim)
  * [huantrinh1802/m_taskwarrior_d.nvim](https://github.com/huantrinh1802/m_taskwarrior_d.nvim)
  * [hubro/nvim-splitrun](https://github.com/hubro/nvim-splitrun)
  * [huggingface/llm.nvim](https://github.com/huggingface/llm.nvim)
  * [huynle/ogpt.nvim](https://github.com/huynle/ogpt.nvim)
  * [iabdelkareem/csharp.nvim](https://github.com/iabdelkareem/csharp.nvim)
  * [ibhagwan/smartyank.nvim](https://github.com/ibhagwan/smartyank.nvim)
  * [icholy/lsplinks.nvim](https://github.com/icholy/lsplinks.nvim)
  * [icholy/nvim-lsplinks](https://github.com/icholy/nvim-lsplinks)
  * [idanarye/nvim-blunder](https://github.com/idanarye/nvim-blunder)
  * [idanarye/nvim-days-without](https://github.com/idanarye/nvim-days-without)
  * [idanarye/nvim-impairative](https://github.com/idanarye/nvim-impairative)
  * [ilyasyoy/obs.nvim](https://github.com/ilyasyoy/obs.nvim)
  * [imnel/monorepo.nvim](https://github.com/imnel/monorepo.nvim)
  * [indianboy42/tree-sitter-just](https://github.com/indianboy42/tree-sitter-just)
  * [inkarkat/vim-ingo-librar](https://github.com/inkarkat/vim-ingo-librar)
  * [inkarkat/vim-visualrepeat](https://github.com/inkarkat/vim-visualrepeat)
  * [iruzo/ripgrep.nvim](https://github.com/iruzo/ripgrep.nvim)
  * [isak102/telescope-git-file-history.nvim](https://github.com/isak102/telescope-git-file-history.nvim)
  * [isrothy/neominimap.nvim](https://github.com/isrothy/neominimap.nvim)
  * [iswladi/gittory](https://github.com/iswladi/gittory)
  * [itchyny/vim-highlighturl](https://github.com/itchyny/vim-highlighturl)
  * [itchyny/vim-qfedit](https://github.com/itchyny/vim-qfedit)
  * [ivanjermakov/troublesum.nvim](https://github.com/ivanjermakov/troublesum.nvim)
  * [jackielii/neo-tree-harpoon.nvim](https://github.com/jackielii/neo-tree-harpoon.nvim)
  * [jack-rabe/impl.nvim](https://github.com/jack-rabe/impl.nvim)
  * [jacoborus/tender.vim](https://github.com/jacoborus/tender.vim)
  * [jake-stewart/slide.nvim](https://github.com/jake-stewart/slide.nvim)
  * [jakobkhansen/journal.nvim](https://github.com/jakobkhansen/journal.nvim)
  * [jalvesaq/cmp-nvim-r](https://github.com/jalvesaq/cmp-nvim-r)
  * [jamesblckwell/nvimkit.nvim](https://github.com/jamesblckwell/nvimkit.nvim)
  * [jasonboyett/goethe.nvim](https://github.com/jasonboyett/goethe.nvim)
  * [javahello/spring-boot.nvim](https://github.com/javahello/spring-boot.nvim)
  * [jayanthd04/asctris.nvim](https://github.com/jayanthd04/asctris.nvim)
  * [jay-babu/mason-nvim-dap.nvim](https://github.com/jay-babu/mason-nvim-dap.nvim)
  * [jaytyrrell13/static.nvim](https://github.com/jaytyrrell13/static.nvim)
  * [jcdampil23/note_navigation.nvim](https://github.com/jcdampil23/note_navigation.nvim)
  * [jc-doyle/cmp-pandoc-references](https://github.com/jc-doyle/cmp-pandoc-references)
  * [jcha0713/cmp-tw2css](https://github.com/jcha0713/cmp-tw2css)
  * [jdrupal-dev/code-refactor.nvim](https://github.com/jdrupal-dev/code-refactor.nvim)
  * [jdrupal-dev/css-vars.nvim](https://github.com/jdrupal-dev/css-vars.nvim)
  * [jdrupal-dev/drupal.nvim](https://github.com/jdrupal-dev/drupal.nvim)
  * [jdrupal-dev/parcel.nvim](https://github.com/jdrupal-dev/parcel.nvim)
  * [jedrzejboczar/exrc.nvim](https://github.com/jedrzejboczar/exrc.nvim)
  * [jeffnguyen695/tmux-zoxide-session](https://github.com/jeffnguyen695/tmux-zoxide-session)
  * [jellydn/hurl.nvim](https://github.com/jellydn/hurl.nvim)
  * [jellydn/my-note.nvim](https://github.com/jellydn/my-note.nvim)
  * [jellydn/quick-code-runner.nvim](https://github.com/jellydn/quick-code-runner.nvim)
  * [jellydn/spinner.nvim](https://github.com/jellydn/spinner.nvim)
  * [jellydn/typecheck.nvim](https://github.com/jellydn/typecheck.nvim)
  * [jesperlundberg/projektgunnar.nvim](https://github.com/jesperlundberg/projektgunnar.nvim)
  * [jesperlundberg/svartafanan.nvim](https://github.com/jesperlundberg/svartafanan.nvim)
  * [jezda1337/cmp_bootstrap](https://github.com/jezda1337/cmp_bootstrap)
  * [jezda1337/nvim-html-css](https://github.com/jezda1337/nvim-html-css)
  * [jim-at-jibba/ariake.nvim](https://github.com/jim-at-jibba/ariake.nvim)
  * [jim-at-jibba/micropython.nvim](https://github.com/jim-at-jibba/micropython.nvim)
  * [jjshoots/betterf.nvim](https://github.com/jjshoots/betterf.nvim)
  * [jla2000/lazydocs.nvim](https://github.com/jla2000/lazydocs.nvim)
  * [jmarkin/cmp-diag-codes](https://github.com/jmarkin/cmp-diag-codes)
  * [jmarkin/gentags.lua](https://github.com/jmarkin/gentags.lua)
  * [joeldotdias/jsdoc-switch.nvim](https://github.com/joeldotdias/jsdoc-switch.nvim)
  * [johanw123/avalonia.nvim](https://github.com/johanw123/avalonia.nvim)
  * [jojomakesgames/git-remote-url.nvim](https://github.com/jojomakesgames/git-remote-url.nvim)
  * [jonarrien/telescope-cmdline.nvim](https://github.com/jonarrien/telescope-cmdline.nvim)
  * [jonathanmorris180/salesforce.nvim](https://github.com/jonathanmorris180/salesforce.nvim)
  * [jonboh/nvim-dap-rr](https://github.com/jonboh/nvim-dap-rr)
  * [joorjeh/robby](https://github.com/joorjeh/robby)
  * [joosepalviste/palenightfall.nvim](https://github.com/joosepalviste/palenightfall.nvim)
  * [jorgebucaran/hydro](https://github.com/jorgebucaran/hydro)
  * [joshuadanpeterson/typewriter.nvim](https://github.com/joshuadanpeterson/typewriter.nvim)
  * [jpmcb/nvim-llama](https://github.com/jpmcb/nvim-llama)
  * [jsongerber/nvim-px-to-rem](https://github.com/jsongerber/nvim-px-to-rem)
  * [jsongerber/thanks.nvim](https://github.com/jsongerber/thanks.nvim)
  * [juansalvatore/git-dashboard-nvim](https://github.com/juansalvatore/git-dashboard-nvim)
  * [judaew/ronny.nvim](https://github.com/judaew/ronny.nvim)
  * [julienvincent/nvim-paredit](https://github.com/julienvincent/nvim-paredit)
  * [justinmk/vim-dirvish.git](https://github.com/justinmk/vim-dirvish.git)
  * [justinmk/vim-gtfo.git](https://github.com/justinmk/vim-gtfo.git)
  * [justinmk/vim-ipmotion](https://github.com/justinmk/vim-ipmotion)
  * [justinmk/vim-ipmotion.git](https://github.com/justinmk/vim-ipmotion.git)
  * [justinmk/vim-sneak.git](https://github.com/justinmk/vim-sneak.git)
  * [jyscao/ventana.nvim](https://github.com/jyscao/ventana.nvim)
  * [kaarmu/typst.vim](https://github.com/kaarmu/typst.vim)
  * [kabbamine/vcoolor.vim](https://github.com/kabbamine/vcoolor.vim)
  * [kadobot/cmp-plugins](https://github.com/kadobot/cmp-plugins)
  * [kamalsacranie/nvim-mapper](https://github.com/kamalsacranie/nvim-mapper)
  * [kamou/gpt-vim](https://github.com/kamou/gpt-vim)
  * [kana/vim-niceblock](https://github.com/kana/vim-niceblock)
  * [kaplanz/deku.nvim](https://github.com/kaplanz/deku.nvim)
  * [karshprime/only-tmux.nvim](https://github.com/karshprime/only-tmux.nvim)
  * [karshprime/tmux-compile.nvim](https://github.com/karshprime/tmux-compile.nvim)
  * [karvla/term-toggle.nvim](https://github.com/karvla/term-toggle.nvim)
  * [kawre/leetcode.nvim](https://github.com/kawre/leetcode.nvim)
  * [kawre/neotab.nvim](https://github.com/kawre/neotab.nvim)
  * [kdesp73/project-starter.nvim](https://github.com/kdesp73/project-starter.nvim)
  * [kdheepak/cmp-latex-symbols](https://github.com/kdheepak/cmp-latex-symbols)
  * [kento-ogata/cmp-tsnip](https://github.com/kento-ogata/cmp-tsnip)
  * [kevinm6/kurayami.nvim](https://github.com/kevinm6/kurayami.nvim)
  * [kiddos/gemini.nvim](https://github.com/kiddos/gemini.nvim)
  * [kilavila/nvim-bufferlist](https://github.com/kilavila/nvim-bufferlist)
  * [kilavila/nvim-gitignore](https://github.com/kilavila/nvim-gitignore)
  * [kilavila/nvim-yoink](https://github.com/kilavila/nvim-yoink)
  * [kingmichaelpark/age.nvim](https://github.com/kingmichaelpark/age.nvim)
  * [kizza/actionmenu.nvim](https://github.com/kizza/actionmenu.nvim)
  * [kjuq/sixelview.nvim](https://github.com/kjuq/sixelview.nvim)
  * [klebster2/cmp-rogets-thesaurus](https://github.com/klebster2/cmp-rogets-thesaurus)
  * [kndndrj/nvim-dbee](https://github.com/kndndrj/nvim-dbee)
  * [kolja/loriini.nvim](https://github.com/kolja/loriini.nvim)
  * [koron/nyancat-vim](https://github.com/koron/nyancat-vim)
  * [kr40/nvim-macros](https://github.com/kr40/nvim-macros)
  * [krischik/vim-backup](https://github.com/krischik/vim-backup)
  * [kristijanhusak/line-notes.nvim](https://github.com/kristijanhusak/line-notes.nvim)
  * [krivahtoo/silicon.nvim](https://github.com/krivahtoo/silicon.nvim)
  * [kungfusheep/i.nvim](https://github.com/kungfusheep/i.nvim)
  * [kungfusheep/randomquote.nvim](https://github.com/kungfusheep/randomquote.nvim)
  * [kungfusheep/randomword.nvim](https://github.com/kungfusheep/randomword.nvim)
  * [kutiny/colors.nvim](https://github.com/kutiny/colors.nvim)
  * [kuznetsss/delegate.nvim](https://github.com/kuznetsss/delegate.nvim)
  * [l3k4n/justmake.nvim](https://github.com/l3k4n/justmake.nvim)
  * [l3mon4d3/cmp-luasnip-choice](https://github.com/l3mon4d3/cmp-luasnip-choice)
  * [lalitmee/browse.nvim](https://github.com/lalitmee/browse.nvim)
  * [lambdalisue/vim-gin](https://github.com/lambdalisue/vim-gin)
  * [laytan/cloak.nvim](https://github.com/laytan/cloak.nvim)
  * [lazymaniac/wttr.nvim](https://github.com/lazymaniac/wttr.nvim)
  * [l-colombo/atlantic-dark.nvim](https://github.com/l-colombo/atlantic-dark.nvim)
  * [leet0rz/modified-moonlight.nvim](https://github.com/leet0rz/modified-moonlight.nvim)
  * [legobeat/l7-devenv](https://github.com/legobeat/l7-devenv)
  * [leocus/codeassistant.vim](https://github.com/leocus/codeassistant.vim)
  * [letieu/btw.nvim](https://github.com/letieu/btw.nvim)
  * [letieu/hacker.nvim](https://github.com/letieu/hacker.nvim)
  * [letieu/harpoon-lualine](https://github.com/letieu/harpoon-lualine)
  * [letieu/jot.lua](https://github.com/letieu/jot.lua)
  * [letieu/wezterm-move.nvim](https://github.com/letieu/wezterm-move.nvim)
  * [lewis6991/brodir.nvim](https://github.com/lewis6991/brodir.nvim)
  * [lewis6991/fileline.nvim](https://github.com/lewis6991/fileline.nvim)
  * [lewis6991/nvim-test](https://github.com/lewis6991/nvim-test)
  * [lewis6991/pckr.nvim](https://github.com/lewis6991/pckr.nvim)
  * [lewis6991/spaceless.nvim](https://github.com/lewis6991/spaceless.nvim)
  * [lewis6991/whatthejump.nvim](https://github.com/lewis6991/whatthejump.nvim)
  * [liadoz/nvim-dap-repl-highlights](https://github.com/liadoz/nvim-dap-repl-highlights)
  * [lilja/telescope-swap-files](https://github.com/lilja/telescope-swap-files)
  * [linguini1/pulse.nvim](https://github.com/linguini1/pulse.nvim)
  * [linrongbin16/colorbox.nvim](https://github.com/linrongbin16/colorbox.nvim)
  * [linrongbin16/fzfx.nvim](https://github.com/linrongbin16/fzfx.nvim)
  * [linrongbin16/gentags.nvim](https://github.com/linrongbin16/gentags.nvim)
  * [linrongbin16/gitlinker.nvim](https://github.com/linrongbin16/gitlinker.nvim)
  * [lintaoamons/bookmarks.nvim](https://github.com/lintaoamons/bookmarks.nvim)
  * [lintaoamons/cd-project.nvim](https://github.com/lintaoamons/cd-project.nvim)
  * [lintaoamons/context-menu.nvim](https://github.com/lintaoamons/context-menu.nvim)
  * [lintaoamons/easy-commands.nvim](https://github.com/lintaoamons/easy-commands.nvim)
  * [lintaoamons/scratch.nvim](https://github.com/lintaoamons/scratch.nvim)
  * [loganswartz/polychrome.nvim](https://github.com/loganswartz/polychrome.nvim)
  * [loganswartz/sunburn.nvim](https://github.com/loganswartz/sunburn.nvim)
  * [lopi-py/luau-lsp.nvim](https://github.com/lopi-py/luau-lsp.nvim)
  * [lsig/messenger.nvim](https://github.com/lsig/messenger.nvim)
  * [lsvmello/elastictabstops.nvim](https://github.com/lsvmello/elastictabstops.nvim)
  * [lucario387/nvim-ts-format](https://github.com/lucario387/nvim-ts-format)
  * [luckasranarison/clear-action.nvim](https://github.com/luckasranarison/clear-action.nvim)
  * [luckasranarison/nvim-devdocs](https://github.com/luckasranarison/nvim-devdocs)
  * [luckasranarison/tailwind-tools.nvim](https://github.com/luckasranarison/tailwind-tools.nvim)
  * [lucobellic/edgy-group.nvim](https://github.com/lucobellic/edgy-group.nvim)
  * [lukaspietzschmann/boo.nvim](https://github.com/lukaspietzschmann/boo.nvim)
  * [lunacookies/vim-colors-xcode](https://github.com/lunacookies/vim-colors-xcode)
  * [lunarvim/breadcrumbs.nvim](https://github.com/lunarvim/breadcrumbs.nvim)
  * [lunarvim/colorgen-nvim](https://github.com/lunarvim/colorgen-nvim)
  * [lunarvim/horizon.nvim](https://github.com/lunarvim/horizon.nvim)
  * [lunarvim/lualine.nvim](https://github.com/lunarvim/lualine.nvim)
  * [lunarvim/lunar.nvim](https://github.com/lunarvim/lunar.nvim)
  * [lunarvim/lvim-themes](https://github.com/lunarvim/lvim-themes)
  * [lunarvim/peek.lua](https://github.com/lunarvim/peek.lua)
  * [lunarvim/primer.nvim](https://github.com/lunarvim/primer.nvim)
  * [lunarvim/starter.lvim](https://github.com/lunarvim/starter.lvim)
  * [lunarvim/synthwave84.nvim](https://github.com/lunarvim/synthwave84.nvim)
  * [lunarvim/templeos.nvim](https://github.com/lunarvim/templeos.nvim)
  * [lvimuser/lsp-inlayhints.nvim](https://github.com/lvimuser/lsp-inlayhints.nvim)
  * [lzdq/umbra.nvim](https://github.com/lzdq/umbra.nvim)
  * [m15a/flake-awesome-neovim-plugins](https://github.com/m15a/flake-awesome-neovim-plugins)
  * [m7medvision/lazycommit](https://github.com/m7medvision/lazycommit)
  * [mackeper/seshmgr.nvim](https://github.com/mackeper/seshmgr.nvim)
  * [madskjeldgaard/cppman.nvim](https://github.com/madskjeldgaard/cppman.nvim)
  * [magicduck/grug-far.nvim](https://github.com/magicduck/grug-far.nvim)
  * [magicmonty/sonicpi.nvim](https://github.com/magicmonty/sonicpi.nvim)
  * [makaze/watch.nvim](https://github.com/makaze/watch.nvim)
  * [mangelozzi/rgflow.nvim](https://github.com/mangelozzi/rgflow.nvim)
  * [marcosantos98/clang-format.nvim](https://github.com/marcosantos98/clang-format.nvim)
  * [marco-souza/ollero.nvim](https://github.com/marco-souza/ollero.nvim)
  * [marco-souza/term.nvim](https://github.com/marco-souza/term.nvim)
  * [marskey/telescope-sg](https://github.com/marskey/telescope-sg)
  * [massix/org-checkbox.nvim](https://github.com/massix/org-checkbox.nvim)
  * [massix/termux.nvim](https://github.com/massix/termux.nvim)
  * [matarina/nvim_ds_repl](https://github.com/matarina/nvim_ds_repl)
  * [mateiadrielrafael/scrap.nvim](https://github.com/mateiadrielrafael/scrap.nvim)
  * [mateuszwieloch/automkdir.nvim](https://github.com/mateuszwieloch/automkdir.nvim)
  * [matthiasweiss/angular-quickswitch.nvim](https://github.com/matthiasweiss/angular-quickswitch.nvim)
  * [mattkubej/jest.nvim](https://github.com/mattkubej/jest.nvim)
  * [mawkler/friendly-snippets](https://github.com/mawkler/friendly-snippets)
  * [mawkler/onedark.nvim](https://github.com/mawkler/onedark.nvim)
  * [maximilianlloyd/tw-values.nvim](https://github.com/maximilianlloyd/tw-values.nvim)
  * [maxmx03/schemecraft](https://github.com/maxmx03/schemecraft)
  * [mcauley-penney/visual-whitespace.nvim](https://github.com/mcauley-penney/visual-whitespace.nvim)
  * [meain/vim-printer](https://github.com/meain/vim-printer)
  * [meanderingprogrammer/markdown.nvim](https://github.com/meanderingprogrammer/markdown.nvim)
  * [meanderingprogrammer/py-requirements.nvim](https://github.com/meanderingprogrammer/py-requirements.nvim)
  * [mei28/luminate.nvim](https://github.com/mei28/luminate.nvim)
  * [mei28/qfc.nvim](https://github.com/mei28/qfc.nvim)
  * [meuter/lualine-so-fancy.nvim](https://github.com/meuter/lualine-so-fancy.nvim)
  * [mfussenegger/nvim-dap-python](https://github.com/mfussenegger/nvim-dap-python)
  * [mfussenegger/nvim-fzy](https://github.com/mfussenegger/nvim-fzy)
  * [mfussenegger/nvim-qwahl](https://github.com/mfussenegger/nvim-qwahl)
  * [mg979/tabline.nvim](https://github.com/mg979/tabline.nvim)
  * [mhanberg/output-panel.nvim](https://github.com/mhanberg/output-panel.nvim)
  * [micangl/cmp-vimtex](https://github.com/micangl/cmp-vimtex)
  * [michaelrommel/nvim-silicon](https://github.com/michaelrommel/nvim-silicon)
  * [miguelcrespo/scratch-buffer.nvim](https://github.com/miguelcrespo/scratch-buffer.nvim)
  * [mihaifm/bufstop](https://github.com/mihaifm/bufstop)
  * [miikanissi/modus-themes.nvim](https://github.com/miikanissi/modus-themes.nvim)
  * [mike-jl/harpoonex](https://github.com/mike-jl/harpoonex)
  * [mikeslattery/ax.nvim](https://github.com/mikeslattery/ax.nvim)
  * [mikesmithgh/git-prompt-string-lualine.nvim](https://github.com/mikesmithgh/git-prompt-string-lualine.nvim)
  * [mikesmithgh/kitty-scrollback.nvim](https://github.com/mikesmithgh/kitty-scrollback.nvim)
  * [milkias17/reloader.nvim](https://github.com/milkias17/reloader.nvim)
  * [milkypostman/vim-togglelist](https://github.com/milkypostman/vim-togglelist)
  * [mimikun/human-rights.nvim](https://github.com/mimikun/human-rights.nvim)
  * [minamorl/nvim-clean-paste](https://github.com/minamorl/nvim-clean-paste)
  * [miragiancycle/oviwrite](https://github.com/miragiancycle/oviwrite)
  * [mireq/large_file](https://github.com/mireq/large_file)
  * [mireq/luasnip-snippets](https://github.com/mireq/luasnip-snippets)
  * [mistgc/pinmd.nvim](https://github.com/mistgc/pinmd.nvim)
  * [mistricky/codesnap.nvim](https://github.com/mistricky/codesnap.nvim)
  * [mistweaverco/kulala.nvim](https://github.com/mistweaverco/kulala.nvim)
  * [miversen33/sunglasses.nvim](https://github.com/miversen33/sunglasses.nvim)
  * [mizlan/delimited.nvim](https://github.com/mizlan/delimited.nvim)
  * [mizlan/longbow.nvim](https://github.com/mizlan/longbow.nvim)
  * [mjlbach/lsp_signature.nvim](https://github.com/mjlbach/lsp_signature.nvim)
  * [mktip/adaptive-theme.nvim](https://github.com/mktip/adaptive-theme.nvim)
  * [mluders/comfy-line-numbers.nvim](https://github.com/mluders/comfy-line-numbers.nvim)
  * [mmolhoek/cmp-scss](https://github.com/mmolhoek/cmp-scss)
  * [mo1ein/vimplayer](https://github.com/mo1ein/vimplayer)
  * [mong8se/actually.nvim](https://github.com/mong8se/actually.nvim)
  * [mong8se/buffish.nvim](https://github.com/mong8se/buffish.nvim)
  * [monkoose/neocodeium](https://github.com/monkoose/neocodeium)
  * [moyiz/command-and-cursor.nvim](https://github.com/moyiz/command-and-cursor.nvim)
  * [moyiz/git-dev.nvim](https://github.com/moyiz/git-dev.nvim)
  * [mpas/marp-nvim](https://github.com/mpas/marp-nvim)
  * [mptre/vim-printf](https://github.com/mptre/vim-printf)
  * [mrcjkb/ferris.nvim](https://github.com/mrcjkb/ferris.nvim)
  * [mrcjkb/kickstart-nix.nvim](https://github.com/mrcjkb/kickstart-nix.nvim)
  * [mrcjkb/rustaceanvim](https://github.com/mrcjkb/rustaceanvim)
  * [mr-lllll/cool-chunk.nvim](https://github.com/mr-lllll/cool-chunk.nvim)
  * [mr-lllll/lualine-ext.nvim](https://github.com/mr-lllll/lualine-ext.nvim)
  * [mr-lllll/treesitter-outer](https://github.com/mr-lllll/treesitter-outer)
  * [mr-lllll/utilities.nvim](https://github.com/mr-lllll/utilities.nvim)
  * [mrloop/telescope-git-branch.nvim](https://github.com/mrloop/telescope-git-branch.nvim)
  * [mrquantumcodes/bufferchad.nvim](https://github.com/mrquantumcodes/bufferchad.nvim)
  * [mrquantumcodes/configpulse](https://github.com/mrquantumcodes/configpulse)
  * [mrquantumcodes/retrospect.nvim](https://github.com/mrquantumcodes/retrospect.nvim)
  * [muniftanjim/nougat.nvim](https://github.com/muniftanjim/nougat.nvim)
  * [murtaza-u/ez.nvim](https://github.com/murtaza-u/ez.nvim)
  * [mvllow/matcha.nvim](https://github.com/mvllow/matcha.nvim)
  * [mvllow/modes.nvim](https://github.com/mvllow/modes.nvim)
  * [mvllow/stand.nvim](https://github.com/mvllow/stand.nvim)
  * [mwh/dragon](https://github.com/mwh/dragon)
  * [mxsdev/nvim-dap-vscode-js](https://github.com/mxsdev/nvim-dap-vscode-js)
  * [myypo/borrowed.nvim](https://github.com/myypo/borrowed.nvim)
  * [myzel394/easytables.nvim](https://github.com/myzel394/easytables.nvim)
  * [myzel394/jsonfly.nvim](https://github.com/myzel394/jsonfly.nvim)
  * [nabekou29/js-i18n.nvim](https://github.com/nabekou29/js-i18n.nvim)
  * [napisani/nvim-dadbod-bg](https://github.com/napisani/nvim-dadbod-bg)
  * [nat-418/cmp-color-names.nvim](https://github.com/nat-418/cmp-color-names.nvim)
  * [nedra1998/nvim-mdlink](https://github.com/nedra1998/nvim-mdlink)
  * [neoclide/coc-highlight](https://github.com/neoclide/coc-highlight)
  * [neoclide/coc-tabnine](https://github.com/neoclide/coc-tabnine)
  * [neovim/neovim-ruby](https://github.com/neovim/neovim-ruby)
  * [neuromaancer/readup.nvim](https://github.com/neuromaancer/readup.nvim)
  * [neviraide/nekifoch.nvim](https://github.com/neviraide/nekifoch.nvim)
  * [nhurlock/clownshow.nvim](https://github.com/nhurlock/clownshow.nvim)
  * [nihancj/plugin-switcher.nvim](https://github.com/nihancj/plugin-switcher.nvim)
  * [nil70n/floating-help](https://github.com/nil70n/floating-help)
  * [niuiic/code-shot.nvim](https://github.com/niuiic/code-shot.nvim)
  * [niuiic/core.nvim](https://github.com/niuiic/core.nvim)
  * [niuiic/git-log.nvim](https://github.com/niuiic/git-log.nvim)
  * [niuiic/quickfix.nvim](https://github.com/niuiic/quickfix.nvim)
  * [niuiic/remote.nvim](https://github.com/niuiic/remote.nvim)
  * [niuiic/scroll.nvim](https://github.com/niuiic/scroll.nvim)
  * [niuiic/task.nvim](https://github.com/niuiic/task.nvim)
  * [niuiic/terminal.nvim](https://github.com/niuiic/terminal.nvim)
  * [niuiic/track.nvim](https://github.com/niuiic/track.nvim)
  * [niuiic/typst-preview.nvim](https://github.com/niuiic/typst-preview.nvim)
  * [nivek77pur/midi-input.nvim](https://github.com/nivek77pur/midi-input.nvim)
  * [nkakouros-original/scrollofffraction.nvim](https://github.com/nkakouros-original/scrollofffraction.nvim)
  * [notelgnis/fetchfact.nvim](https://github.com/notelgnis/fetchfact.nvim)
  * [nstefan002/15puzzle.nvim](https://github.com/nstefan002/15puzzle.nvim)
  * [nstefan002/2048.nvim](https://github.com/nstefan002/2048.nvim)
  * [nstefan002/donut.nvim](https://github.com/nstefan002/donut.nvim)
  * [nstefan002/screenkey.nvim](https://github.com/nstefan002/screenkey.nvim)
  * [nstefan002/speedtyper.nvim](https://github.com/nstefan002/speedtyper.nvim)
  * [nstefan002/visual-surround.nvim](https://github.com/nstefan002/visual-surround.nvim)
  * [ntbbloodbath/sweetie.nvim](https://github.com/ntbbloodbath/sweetie.nvim)
  * [nvchad/ui](https://github.com/nvchad/ui)
  * [nvimdev/dashboard-nvim](https://github.com/nvimdev/dashboard-nvim)
  * [nvimdev/epo.nvim](https://github.com/nvimdev/epo.nvim)
  * [nvimdev/galaxyline.nvim](https://github.com/nvimdev/galaxyline.nvim)
  * [nvimdev/hlsearch.nvim](https://github.com/nvimdev/hlsearch.nvim)
  * [nvimdev/lspsaga.nvim](https://github.com/nvimdev/lspsaga.nvim)
  * [nvim-focus/focus.nvim](https://github.com/nvim-focus/focus.nvim)
  * [nvim-java/nvim-java](https://github.com/nvim-java/nvim-java)
  * [nvim-java/play-lazyvim](https://github.com/nvim-java/play-lazyvim)
  * [nvim-neorocks/nvim-busted-action](https://github.com/nvim-neorocks/nvim-busted-action)
  * [nvim-neorocks/rocks-lazy.nvim](https://github.com/nvim-neorocks/rocks-lazy.nvim)
  * [nvim-neorocks/rocks.nvim](https://github.com/nvim-neorocks/rocks.nvim)
  * [nvim-neorocks/rocks-scoop](https://github.com/nvim-neorocks/rocks-scoop)
  * [nvim-neotest/nvim-nio](https://github.com/nvim-neotest/nvim-nio)
  * [nvimtools/hydra.nvim](https://github.com/nvimtools/hydra.nvim)
  * [nvimtools/none-ls.nvim](https://github.com/nvimtools/none-ls.nvim)
  * [nvim-tree/nvim-tree.lua](https://github.com/nvim-tree/nvim-tree.lua)
  * [nyoom-engineering/nyoom.nvim](https://github.com/nyoom-engineering/nyoom.nvim)
  * [observeroftime/notifications.nvim](https://github.com/observeroftime/notifications.nvim)
  * [observeroftime/nvimcord](https://github.com/observeroftime/nvimcord)
  * [octaltree/cmp-look](https://github.com/octaltree/cmp-look)
  * [old-farmer/im-autoswitch.nvim](https://github.com/old-farmer/im-autoswitch.nvim)
  * [oleggulevskyy/better-ts-errors.nvim](https://github.com/oleggulevskyy/better-ts-errors.nvim)
  * [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim)
  * [omarcospo/dumbnotes.nvim](https://github.com/omarcospo/dumbnotes.nvim)
  * [omerxx/tmux-sessionx](https://github.com/omerxx/tmux-sessionx)
  * [oneslash/helix-nvim](https://github.com/oneslash/helix-nvim)
  * [otavioschwanck/arrow.nvim](https://github.com/otavioschwanck/arrow.nvim)
  * [otavioschwanck/cool-substitute.nvim](https://github.com/otavioschwanck/cool-substitute.nvim)
  * [otavioschwanck/telescope-cmdline-word.nvim](https://github.com/otavioschwanck/telescope-cmdline-word.nvim)
  * [othree/eregex.vim](https://github.com/othree/eregex.vim)
  * [oxfist/night-owl.nvim](https://github.com/oxfist/night-owl.nvim)
  * [oxy2dev/intro.nvim](https://github.com/oxy2dev/intro.nvim)
  * [oxy2dev/markview.nvim](https://github.com/oxy2dev/markview.nvim)
  * [oysandvik94/curl.nvim](https://github.com/oysandvik94/curl.nvim)
  * [ozthemagician/alpha-cowsays-nvim](https://github.com/ozthemagician/alpha-cowsays-nvim)
  * [p00f/godbolt.nvim](https://github.com/p00f/godbolt.nvim)
  * [p5quared/apple-music.nvim](https://github.com/p5quared/apple-music.nvim)
  * [paopaol/cmp-doxygen](https://github.com/paopaol/cmp-doxygen)
  * [pasky/claude.vim](https://github.com/pasky/claude.vim)
  * [paulfrische/mpd.nvim](https://github.com/paulfrische/mpd.nvim)
  * [paul-gauthier/aider](https://github.com/paul-gauthier/aider)
  * [phanen/broker.nvim](https://github.com/phanen/broker.nvim)
  * [phanen/dirstack.nvim](https://github.com/phanen/dirstack.nvim)
  * [phanen/fzf-lua-overlay](https://github.com/phanen/fzf-lua-overlay)
  * [phanen/lazy-help.nvim](https://github.com/phanen/lazy-help.nvim)
  * [phanen/mder.nvim](https://github.com/phanen/mder.nvim)
  * [pheon-dev/buffalo-nvim](https://github.com/pheon-dev/buffalo-nvim)
  * [pheon-dev/pigeon](https://github.com/pheon-dev/pigeon)
  * [philrunninger/cmp-rpncalc](https://github.com/philrunninger/cmp-rpncalc)
  * [pianocomposer321/officer.nvim](https://github.com/pianocomposer321/officer.nvim)
  * [piersolenski/telescope-import.nvim](https://github.com/piersolenski/telescope-import.nvim)
  * [piersolenski/wtf.nvim](https://github.com/piersolenski/wtf.nvim)
  * [piotr1215/toggler.nvim](https://github.com/piotr1215/toggler.nvim)
  * [plax-00/endscroll.nvim](https://github.com/plax-00/endscroll.nvim)
  * [pmizio/typescript-tools.nvim](https://github.com/pmizio/typescript-tools.nvim)
  * [pogyomo/submode.nvim](https://github.com/pogyomo/submode.nvim)
  * [pogyomo/winresize.nvim](https://github.com/pogyomo/winresize.nvim)
  * [polirritmico/monokai-nightasty.nvim](https://github.com/polirritmico/monokai-nightasty.nvim)
  * [polirritmico/telescope-lazy-plugins.nvim](https://github.com/polirritmico/telescope-lazy-plugins.nvim)
  * [pontusk/cmp-sass-variables](https://github.com/pontusk/cmp-sass-variables)
  * [pontusk/cmp-vimwiki-tags](https://github.com/pontusk/cmp-vimwiki-tags)
  * [popkat412/nvim-scratchpad](https://github.com/popkat412/nvim-scratchpad)
  * [pranphy/nevl.nvim](https://github.com/pranphy/nevl.nvim)
  * [presindent/coddit.nvim](https://github.com/presindent/coddit.nvim)
  * [prichrd/netrw.nvim](https://github.com/prichrd/netrw.nvim)
  * [prichrd/refgo.nvim](https://github.com/prichrd/refgo.nvim)
  * [prichrd/vwd.nvim](https://github.com/prichrd/vwd.nvim)
  * [prochri/telescope-picker-history-action](https://github.com/prochri/telescope-picker-history-action)
  * [protex/better-digraphs.nvim](https://github.com/protex/better-digraphs.nvim)
  * [psjay/buffer-closer.nvim](https://github.com/psjay/buffer-closer.nvim)
  * [ptdewey/darkearth-nvim](https://github.com/ptdewey/darkearth-nvim)
  * [ptdewey/yankbank-nvim](https://github.com/ptdewey/yankbank-nvim)
  * [pteroctopus/faster.nvim](https://github.com/pteroctopus/faster.nvim)
  * [pysan3/pathlib.nvim](https://github.com/pysan3/pathlib.nvim)
  * [qaptor-nvim/fantableous.nvim](https://github.com/qaptor-nvim/fantableous.nvim)
  * [quarto-dev/quarto-nvim](https://github.com/quarto-dev/quarto-nvim)
  * [quolpr/quicktest.nvim](https://github.com/quolpr/quicktest.nvim)
  * [raafatturki/corn.nvim](https://github.com/raafatturki/corn.nvim)
  * [raafatturki/hex.nvim](https://github.com/raafatturki/hex.nvim)
  * [rachartier/tiny-devicons-auto-colors.nvim](https://github.com/rachartier/tiny-devicons-auto-colors.nvim)
  * [rachartier/tiny-inline-diagnostic.nvim](https://github.com/rachartier/tiny-inline-diagnostic.nvim)
  * [radioactivepb/vbpreview](https://github.com/radioactivepb/vbpreview)
  * [ragnarok22/whereami.nvim](https://github.com/ragnarok22/whereami.nvim)
  * [rakr/vim-two-firewatch](https://github.com/rakr/vim-two-firewatch)
  * [ramilito/kubectl.nvim](https://github.com/ramilito/kubectl.nvim)
  * [ramilito/winbar.nvim](https://github.com/ramilito/winbar.nvim)
  * [rapan931/lasterisk.nvim](https://github.com/rapan931/lasterisk.nvim)
  * [rapan931/utahraptor.nvim](https://github.com/rapan931/utahraptor.nvim)
  * [raphaelladinig/nvim-projectmanager](https://github.com/raphaelladinig/nvim-projectmanager)
  * [raprogramm/nekifoch](https://github.com/raprogramm/nekifoch)
  * [rareitems/printer.nvim](https://github.com/rareitems/printer.nvim)
  * [rareitems/put_at_end.nvim](https://github.com/rareitems/put_at_end.nvim)
  * [rasulomaroff/reactive.nvim](https://github.com/rasulomaroff/reactive.nvim)
  * [rasulomaroff/telepath.nvim](https://github.com/rasulomaroff/telepath.nvim)
  * [ravibrock/spellwarn.nvim](https://github.com/ravibrock/spellwarn.nvim)
  * [ray-x/telescope-ast-grep.nvim](https://github.com/ray-x/telescope-ast-grep.nvim)
  * [rdpopov/nvim-sak](https://github.com/rdpopov/nvim-sak)
  * [redoxahmii/json-to-types.nvim](https://github.com/redoxahmii/json-to-types.nvim)
  * [renerocksai/calendar-vim](https://github.com/renerocksai/calendar-vim)
  * [rentib/cliff.nvim](https://github.com/rentib/cliff.nvim)
  * [reo101/nix-update.nvim](https://github.com/reo101/nix-update.nvim)
  * [rguruprakash/simple-note.nvim](https://github.com/rguruprakash/simple-note.nvim)
  * [rhysd/vim-syntax-christmas-tree](https://github.com/rhysd/vim-syntax-christmas-tree)
  * [ribru17/bamboo.nvim](https://github.com/ribru17/bamboo.nvim)
  * [ricardoramirezr/blade-nav.nvim](https://github.com/ricardoramirezr/blade-nav.nvim)
  * [ricardoramirezr/lali-components.nvim](https://github.com/ricardoramirezr/lali-components.nvim)
  * [ricardoramirezr/php-use-sort.nvim](https://github.com/ricardoramirezr/php-use-sort.nvim)
  * [rileytwo/kiss](https://github.com/rileytwo/kiss)
  * [rimuhrimu/runthis.nvim](https://github.com/rimuhrimu/runthis.nvim)
  * [rinx/nvim-minimap](https://github.com/rinx/nvim-minimap)
  * [rishabhrd/nvim-cheat.sh](https://github.com/rishabhrd/nvim-cheat.sh)
  * [rishabhrd/popfix](https://github.com/rishabhrd/popfix)
  * [rizwanelansyah/simplyfile.nvim](https://github.com/rizwanelansyah/simplyfile.nvim)
  * [rktjmp/playtime.nvim](https://github.com/rktjmp/playtime.nvim)
  * [rlychrisg/keepcursor.nvim](https://github.com/rlychrisg/keepcursor.nvim)
  * [rmassaroni/nvim-gpush](https://github.com/rmassaroni/nvim-gpush)
  * [robitx/gp.nvim](https://github.com/robitx/gp.nvim)
  * [rodolfojsv/reminders.nvim](https://github.com/rodolfojsv/reminders.nvim)
  * [rolv-apneseth/tfm.nvim](https://github.com/rolv-apneseth/tfm.nvim)
  * [romanozumbe/yanki.nvim](https://github.com/romanozumbe/yanki.nvim)
  * [romgrk/fzy-lua-native](https://github.com/romgrk/fzy-lua-native)
  * [ronylee11/gitcontrib.nvim](https://github.com/ronylee11/gitcontrib.nvim)
  * [roobert/action-hints.nvim](https://github.com/roobert/action-hints.nvim)
  * [roobert/activate.nvim](https://github.com/roobert/activate.nvim)
  * [roobert/bufferline-cycle-windowless.nvim](https://github.com/roobert/bufferline-cycle-windowless.nvim)
  * [roobert/f-string-toggle.nvim](https://github.com/roobert/f-string-toggle.nvim)
  * [roobert/hoversplit.nvim](https://github.com/roobert/hoversplit.nvim)
  * [roobert/palette.nvim](https://github.com/roobert/palette.nvim)
  * [roobert/tabtree.nvim](https://github.com/roobert/tabtree.nvim)
  * [rorynesbitt/dotfyle-cli](https://github.com/rorynesbitt/dotfyle-cli)
  * [rouge8/neotest-rust](https://github.com/rouge8/neotest-rust)
  * [roxma/nvim-ascript](https://github.com/roxma/nvim-ascript)
  * [rshkarin/mason-nvim-lint](https://github.com/rshkarin/mason-nvim-lint)
  * [rudionrails/quarry.nvim](https://github.com/rudionrails/quarry.nvim)
  * [rushjs1/clock.nvim](https://github.com/rushjs1/clock.nvim)
  * [rushjs1/nuxt-goto-alias.nvim](https://github.com/rushjs1/nuxt-goto-alias.nvim)
  * [rusticbard/runner](https://github.com/rusticbard/runner)
  * [ryanmsnyder/toggleterm-manager.nvim](https://github.com/ryanmsnyder/toggleterm-manager.nvim)
  * [rydwxz/bhs](https://github.com/rydwxz/bhs)
  * [ryo33/nvim-cmp-rust](https://github.com/ryo33/nvim-cmp-rust)
  * [s1m0n38/dante.nvim](https://github.com/s1m0n38/dante.nvim)
  * [s1m0n38/love2d.nvim](https://github.com/s1m0n38/love2d.nvim)
  * [saccarosium/neomarks](https://github.com/saccarosium/neomarks)
  * [sachinsenal0x64/hot.nvim](https://github.com/sachinsenal0x64/hot.nvim)
  * [sahlte/timed-highlight.nvim](https://github.com/sahlte/timed-highlight.nvim)
  * [sajjathossain/nvim-npm](https://github.com/sajjathossain/nvim-npm)
  * [salorak/whaler.nvim](https://github.com/salorak/whaler.nvim)
  * [samharju/synthweave.nvim](https://github.com/samharju/synthweave.nvim)
  * [samharju/yeet.nvim](https://github.com/samharju/yeet.nvim)
  * [sammce/fleeting.nvim](https://github.com/sammce/fleeting.nvim)
  * [sam-programs/cmdline-hl.nvim](https://github.com/sam-programs/cmdline-hl.nvim)
  * [sam-programs/expand.nvim](https://github.com/sam-programs/expand.nvim)
  * [sarrisv/readermode.nvim](https://github.com/sarrisv/readermode.nvim)
  * [sathishmanohar/quick-buffer-jump](https://github.com/sathishmanohar/quick-buffer-jump)
  * [sbulav/nredir.nvim](https://github.com/sbulav/nredir.nvim)
  * [scheisa/relpointers.nvim](https://github.com/scheisa/relpointers.nvim)
  * [scottmckendry/cyberdream.nvim](https://github.com/scottmckendry/cyberdream.nvim)
  * [scottmckendry/telescope-resession.nvim](https://github.com/scottmckendry/telescope-resession.nvim)
  * [scottmckendry/windots](https://github.com/scottmckendry/windots)
  * [selyss/mind.nvim](https://github.com/selyss/mind.nvim)
  * [sergioribera/cmp-dotenv](https://github.com/sergioribera/cmp-dotenv)
  * [sergioribera/codeshot.nvim](https://github.com/sergioribera/codeshot.nvim)
  * [sgauvin/ctest-telescope.nvim](https://github.com/sgauvin/ctest-telescope.nvim)
  * [shadyalfred/electric-quotes.nvim](https://github.com/shadyalfred/electric-quotes.nvim)
  * [shaobin-jiang/icenvim](https://github.com/shaobin-jiang/icenvim)
  * [sharonex/edit-list.nvim](https://github.com/sharonex/edit-list.nvim)
  * [sharonex/grape.nvim](https://github.com/sharonex/grape.nvim)
  * [shellheim/ashaar.nvim](https://github.com/shellheim/ashaar.nvim)
  * [shmerl/neogotham](https://github.com/shmerl/neogotham)
  * [shmerl/session-keys](https://github.com/shmerl/session-keys)
  * [sho-87/kanagawa-paper.nvim](https://github.com/sho-87/kanagawa-paper.nvim)
  * [shortcuts/neovim-plugin-boilerplate](https://github.com/shortcuts/neovim-plugin-boilerplate)
  * [shougo/vinarise.vim](https://github.com/shougo/vinarise.vim)
  * [siadat/shell.nvim](https://github.com/siadat/shell.nvim)
  * [siawkz/nvim-cheatsh](https://github.com/siawkz/nvim-cheatsh)
  * [sigasigasiga/neovim-dark-monitor](https://github.com/sigasigasiga/neovim-dark-monitor)
  * [simaxme/java.nvim](https://github.com/simaxme/java.nvim)
  * [simonmclean/triptych.nvim](https://github.com/simonmclean/triptych.nvim)
  * [sinabyr/analogue.nvim](https://github.com/sinabyr/analogue.nvim)
  * [sirzenith/oil-vcs-status](https://github.com/sirzenith/oil-vcs-status)
  * [sjbach/lusty](https://github.com/sjbach/lusty)
  * [skalyaeve/a-nvim-theme](https://github.com/skalyaeve/a-nvim-theme)
  * [skwee357/nvim-prose](https://github.com/skwee357/nvim-prose)
  * [skywind3000/vim-color-export](https://github.com/skywind3000/vim-color-export)
  * [sleepyswords/change-function.nvim](https://github.com/sleepyswords/change-function.nvim)
  * [slugbyte/lackluster.nvim](https://github.com/slugbyte/lackluster.nvim)
  * [slugbyte/unruly-worker.nvim](https://github.com/slugbyte/unruly-worker.nvim)
  * [smartinellimarco/nvcheatsheet.nvim](https://github.com/smartinellimarco/nvcheatsheet.nvim)
  * [smilhey/cabinet.nvim](https://github.com/smilhey/cabinet.nvim)
  * [smjonas/editree.nvim](https://github.com/smjonas/editree.nvim)
  * [smoka7/hop.nvim](https://github.com/smoka7/hop.nvim)
  * [smoka7/hydra.nvim](https://github.com/smoka7/hydra.nvim)
  * [smoka7/multicursors.nvim](https://github.com/smoka7/multicursors.nvim)
  * [snehlsen/pomo.nvim](https://github.com/snehlsen/pomo.nvim)
  * [snikimonkd/yazmp](https://github.com/snikimonkd/yazmp)
  * [softoika/ngswitcher.vim](https://github.com/softoika/ngswitcher.vim)
  * [somesover/accidentslipt](https://github.com/somesover/accidentslipt)
  * [sontungexpt/better-diagnostic-virtual-text](https://github.com/sontungexpt/better-diagnostic-virtual-text)
  * [sontungexpt/buffer-closer](https://github.com/sontungexpt/buffer-closer)
  * [sontungexpt/nvim-highlight-colors](https://github.com/sontungexpt/nvim-highlight-colors)
  * [sontungexpt/stcursorword](https://github.com/sontungexpt/stcursorword)
  * [sontungexpt/stinvim](https://github.com/sontungexpt/stinvim)
  * [sontungexpt/sttusline](https://github.com/sontungexpt/sttusline)
  * [sontungexpt/url-open](https://github.com/sontungexpt/url-open)
  * [sontungexpt/witch](https://github.com/sontungexpt/witch)
  * [soulis-1256/eagle.nvim](https://github.com/soulis-1256/eagle.nvim)
  * [soulis-1256/hoverhints.nvim](https://github.com/soulis-1256/hoverhints.nvim)
  * [sourcegraph/sg.nvim](https://github.com/sourcegraph/sg.nvim)
  * [speelbarrow/splauncher.nvim](https://github.com/speelbarrow/splauncher.nvim)
  * [sqlait/monoconf.nvim](https://github.com/sqlait/monoconf.nvim)
  * [sshelll/telescope-gott.nvim](https://github.com/sshelll/telescope-gott.nvim)
  * [sshelll/telescope-switch.nvim](https://github.com/sshelll/telescope-switch.nvim)
  * [stefanlogue/hydrate.nvim](https://github.com/stefanlogue/hydrate.nvim)
  * [stephengunn/sveltecheck.nvim](https://github.com/stephengunn/sveltecheck.nvim)
  * [stevanmilic/nvim-lspimport](https://github.com/stevanmilic/nvim-lspimport)
  * [stevearc/conform.nvim](https://github.com/stevearc/conform.nvim)
  * [stevearc/profile.nvim](https://github.com/stevearc/profile.nvim)
  * [stratos-linux/stratvim](https://github.com/stratos-linux/stratvim)
  * [suhaan-bhandary/notes.nvim](https://github.com/suhaan-bhandary/notes.nvim)
  * [sunjon/telescope-arecibo.nvim](https://github.com/sunjon/telescope-arecibo.nvim)
  * [superbo/fugit2.nvim](https://github.com/superbo/fugit2.nvim)
  * [sustech-data/neopyter](https://github.com/sustech-data/neopyter)
  * [sustech-data/wildfire.nvim](https://github.com/sustech-data/wildfire.nvim)
  * [svampkorg/moody.nvim](https://github.com/svampkorg/moody.nvim)
  * [svban/yankassassin.nvim](https://github.com/svban/yankassassin.nvim)
  * [svermeulen/nvim-lusc](https://github.com/svermeulen/nvim-lusc)
  * [swaits/colorsaver.nvim](https://github.com/swaits/colorsaver.nvim)
  * [swaits/scratch.nvim](https://github.com/swaits/scratch.nvim)
  * [swaits/thethethe.nvim](https://github.com/swaits/thethethe.nvim)
  * [swaits/zellij-nav.nvim](https://github.com/swaits/zellij-nav.nvim)
  * [synic/telescope-dirpicker.nvim](https://github.com/synic/telescope-dirpicker.nvim)
  * [tadmccorkle/markdown.nvim](https://github.com/tadmccorkle/markdown.nvim)
  * [talha-akram/noctis.nvim](https://github.com/talha-akram/noctis.nvim)
  * [tamago324/cmp-zsh](https://github.com/tamago324/cmp-zsh)
  * [tamamcglinn/vim-termhelp](https://github.com/tamamcglinn/vim-termhelp)
  * [tamton-aquib/duck.nvim](https://github.com/tamton-aquib/duck.nvim)
  * [tamton-aquib/essentials.nvim](https://github.com/tamton-aquib/essentials.nvim)
  * [tamton-aquib/flirt.nvim](https://github.com/tamton-aquib/flirt.nvim)
  * [tamton-aquib/keys.nvim](https://github.com/tamton-aquib/keys.nvim)
  * [tamton-aquib/zone.nvim](https://github.com/tamton-aquib/zone.nvim)
  * [ta-tikoma/php.easy.nvim](https://github.com/ta-tikoma/php.easy.nvim)
  * [teatek/gdscript-extended-lsp.nvim](https://github.com/teatek/gdscript-extended-lsp.nvim)
  * [tefanlogue/hydrate.nvim](https://github.com/tefanlogue/hydrate.nvim)
  * [terje/simctl.nvim](https://github.com/terje/simctl.nvim)
  * [theglander/indent-rainbowline.nvim](https://github.com/theglander/indent-rainbowline.nvim)
  * [theknightsofrohan/csvlens.nvim](https://github.com/theknightsofrohan/csvlens.nvim)
  * [theleop/powershell.nvim](https://github.com/theleop/powershell.nvim)
  * [thunder-coding/zincoxide](https://github.com/thunder-coding/zincoxide)
  * [tiagomdg/react-comp-gen.nvim](https://github.com/tiagomdg/react-comp-gen.nvim)
  * [tiagovla/scope.nvim](https://github.com/tiagovla/scope.nvim)
  * [tigion/nvim-asciidoc-preview](https://github.com/tigion/nvim-asciidoc-preview)
  * [tjdevries/manillua.nvim](https://github.com/tjdevries/manillua.nvim)
  * [tobinpalmer/tip.nvim](https://github.com/tobinpalmer/tip.nvim)
  * [ton/vim-bufsurf](https://github.com/ton/vim-bufsurf)
  * [tovarishfin/vim-solidity](https://github.com/tovarishfin/vim-solidity)
  * [tpope/vim-markdown](https://github.com/tpope/vim-markdown)
  * [tpope/vim-repea](https://github.com/tpope/vim-repea)
  * [traap/nvims](https://github.com/traap/nvims)
  * [trapd00r/vidir](https://github.com/trapd00r/vidir)
  * [treybastian/nvim-jack-in](https://github.com/treybastian/nvim-jack-in)
  * [tribela/transparent.nvim](https://github.com/tribela/transparent.nvim)
  * [trimclain/builder.nvim](https://github.com/trimclain/builder.nvim)
  * [tris203/hawtkeys.nvim](https://github.com/tris203/hawtkeys.nvim)
  * [tris203/precognition.nvim](https://github.com/tris203/precognition.nvim)
  * [tris203/rzls.nvim](https://github.com/tris203/rzls.nvim)
  * [tristone13th/lspmark.nvim](https://github.com/tristone13th/lspmark.nvim)
  * [trstringer/psql.nvim](https://github.com/trstringer/psql.nvim)
  * [tummetott/unimpaired.nvim](https://github.com/tummetott/unimpaired.nvim)
  * [tvaintrob/bicep.vim](https://github.com/tvaintrob/bicep.vim)
  * [tweekmonster/deoplete-clang2](https://github.com/tweekmonster/deoplete-clang2)
  * [twistoy/luasnip-snippets](https://github.com/twistoy/luasnip-snippets)
  * [tyler-barham/floating-help.nvim](https://github.com/tyler-barham/floating-help.nvim)
  * [tzachar/cmp-ai](https://github.com/tzachar/cmp-ai)
  * [tzachar/local-highlight.nvim](https://github.com/tzachar/local-highlight.nvim)
  * [uga-rosa/cmp-dynamic](https://github.com/uga-rosa/cmp-dynamic)
  * [uga-rosa/denippet.vim](https://github.com/uga-rosa/denippet.vim)
  * [umlx5h/gtrash](https://github.com/umlx5h/gtrash)
  * [utfeight/neoproj](https://github.com/utfeight/neoproj)
  * [utfeight/vim-case-change](https://github.com/utfeight/vim-case-change)
  * [vague2k/huez.nvim](https://github.com/vague2k/huez.nvim)
  * [vappolinario/cmp-clippy](https://github.com/vappolinario/cmp-clippy)
  * [vebbnix/lf-vim](https://github.com/vebbnix/lf-vim)
  * [verf/deepwhite.nvim](https://github.com/verf/deepwhite.nvim)
  * [vidocqh/auto-indent.nvim](https://github.com/vidocqh/auto-indent.nvim)
  * [vidocqh/data-viewer.nvim](https://github.com/vidocqh/data-viewer.nvim)
  * [vigoux/notifier.nvim](https://github.com/vigoux/notifier.nvim)
  * [vim-scripts/fountain.vim](https://github.com/vim-scripts/fountain.vim)
  * [volskaya/windovigation.nvim](https://github.com/volskaya/windovigation.nvim)
  * [voxelprismatic/rabbit.nvim](https://github.com/voxelprismatic/rabbit.nvim)
  * [vpavliashvili/json-nvim](https://github.com/vpavliashvili/json-nvim)
  * [vxpm/ferris.nvim](https://github.com/vxpm/ferris.nvim)
  * [vyfor/cord.nvim](https://github.com/vyfor/cord.nvim)
  * [wa11breaker/flutter-bloc.nvim](https://github.com/wa11breaker/flutter-bloc.nvim)
  * [wadackel/nvim-syntax-info](https://github.com/wadackel/nvim-syntax-info)
  * [wallpants/github-preview.nvim](https://github.com/wallpants/github-preview.nvim)
  * [wansmer/symbol-usage.nvim](https://github.com/wansmer/symbol-usage.nvim)
  * [weizheheng/ror.nvim](https://github.com/weizheheng/ror.nvim)
  * [wesleimp/stylua.nvim](https://github.com/wesleimp/stylua.nvim)
  * [wet-sandwich/hyper.nvim](https://github.com/wet-sandwich/hyper.nvim)
  * [wilfreddenton/history.nvim](https://github.com/wilfreddenton/history.nvim)
  * [willem-j-an/adopure.nvim](https://github.com/willem-j-an/adopure.nvim)
  * [willem-j-an/nvim-dap-powershell](https://github.com/willem-j-an/nvim-dap-powershell)
  * [willem-j-an/visidata.nvim](https://github.com/willem-j-an/visidata.nvim)
  * [will-lynas/grapple-line.nvim](https://github.com/will-lynas/grapple-line.nvim)
  * [willothy/savior.nvim](https://github.com/willothy/savior.nvim)
  * [willothy/strat-hero.nvim](https://github.com/willothy/strat-hero.nvim)
  * [willothy/wezterm.nvim](https://github.com/willothy/wezterm.nvim)
  * [wincent/scalpel](https://github.com/wincent/scalpel)
  * [wllfaria/scheming.nvim](https://github.com/wllfaria/scheming.nvim)
  * [wojciech-kulik/xcodebuild.nvim](https://github.com/wojciech-kulik/xcodebuild.nvim)
  * [wolfecub/harpeek.nvim](https://github.com/wolfecub/harpeek.nvim)
  * [wordluc/fromcstotypescript_pluginnvim](https://github.com/wordluc/fromcstotypescript_pluginnvim)
  * [wsdjeg/cpicker.nvim](https://github.com/wsdjeg/cpicker.nvim)
  * [xiantang/darcula-dark.nvim](https://github.com/xiantang/darcula-dark.nvim)
  * [xiaoshihou514/squirrel.nvim](https://github.com/xiaoshihou514/squirrel.nvim)
  * [xixiaofinland/sf.nvim](https://github.com/xixiaofinland/sf.nvim)
  * [yanskun/gotests.nvim](https://github.com/yanskun/gotests.nvim)
  * [yehuohan/cmp-im](https://github.com/yehuohan/cmp-im)
  * [yorickpeterse/nvim-pqf](https://github.com/yorickpeterse/nvim-pqf)
  * [yorickpeterse/nvim-tree-pairs](https://github.com/yorickpeterse/nvim-tree-pairs)
  * [yorickpeterse/nvim-window](https://github.com/yorickpeterse/nvim-window)
  * [you-n-g/simplegpt.nvim](https://github.com/you-n-g/simplegpt.nvim)
  * [ysmb-wtsg/in-and-out.nvim](https://github.com/ysmb-wtsg/in-and-out.nvim)
  * [yujinyuz/gitpad.nvim](https://github.com/yujinyuz/gitpad.nvim)
  * [yuki-uthman/vimpad.nvim](https://github.com/yuki-uthman/vimpad.nvim)
  * [yuki-yano/fzf-preview.vim](https://github.com/yuki-yano/fzf-preview.vim)
  * [yuriescl/minimal-bookmarks.nvim](https://github.com/yuriescl/minimal-bookmarks.nvim)
  * [yutkat/cmp-mocword](https://github.com/yutkat/cmp-mocword)
  * [yutkat/confirm-quit.nvim](https://github.com/yutkat/confirm-quit.nvim)
  * [yutkat/convert-git-url.nvim](https://github.com/yutkat/convert-git-url.nvim)
  * [yutkat/delete-word-to-chars.nvim](https://github.com/yutkat/delete-word-to-chars.nvim)
  * [yutkat/git-rebase-auto-diff.nvim](https://github.com/yutkat/git-rebase-auto-diff.nvim)
  * [yutkat/history-ignore.nvim](https://github.com/yutkat/history-ignore.nvim)
  * [yutkat/osc52.nvim](https://github.com/yutkat/osc52.nvim)
  * [yutkat/save-clipboard-on-exit.nvim](https://github.com/yutkat/save-clipboard-on-exit.nvim)
  * [yutkat/spiral-split.nvim](https://github.com/yutkat/spiral-split.nvim)
  * [yutkat/taskrun.nvim](https://github.com/yutkat/taskrun.nvim)
  * [yutkat/term-gf.nvim](https://github.com/yutkat/term-gf.nvim)
  * [yutkat/wb-only-current-line.nvim](https://github.com/yutkat/wb-only-current-line.nvim)
  * [zadirion/unreal.nvim](https://github.com/zadirion/unreal.nvim)
  * [zeioth/distroupdate.nvim](https://github.com/zeioth/distroupdate.nvim)
  * [zeioth/dooku.nvim](https://github.com/zeioth/dooku.nvim)
  * [zeioth/garbage-day.nvim](https://github.com/zeioth/garbage-day.nvim)
  * [zeioth/heirline-components.nvim](https://github.com/zeioth/heirline-components.nvim)
  * [zeioth/makeit.nvim](https://github.com/zeioth/makeit.nvim)
  * [zeioth/markmap.nvim](https://github.com/zeioth/markmap.nvim)
  * [zeioth/none-ls-autoload.nvim](https://github.com/zeioth/none-ls-autoload.nvim)
  * [zeioth/none-ls-external-sources.nvim](https://github.com/zeioth/none-ls-external-sources.nvim)
  * [zerochae/telescope-spring.nvim](https://github.com/zerochae/telescope-spring.nvim)
  * [zidhuss/neotest-minitest](https://github.com/zidhuss/neotest-minitest)
  * [ziontee113/deliberate.nvim](https://github.com/ziontee113/deliberate.nvim)
  * [zjp-cn/nvim-cmp-lsp-rs](https://github.com/zjp-cn/nvim-cmp-lsp-rs)
  * [zotlann/docker-nvim](https://github.com/zotlann/docker-nvim)
  * [zsnails/neoneedskey](https://github.com/zsnails/neoneedskey)

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