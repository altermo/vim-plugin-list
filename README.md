# vim-plugin-list
This is a list of plugins.

_NOTE: this list may contain: mirrors, extensions to plugins, links that are not working and other things that are not related to vim plugins._

_NOTE: only 70% of the plugins are documented._

_Other BETER vim plugin lists: [awesome-vim](https://github.com/akrawchyk/awesome-vim), [awesome-nvim](https://github.com/rockerBOO/awesome-neovim), [neovim-official-list](https://github.com/neovim/neovim/wiki/Related-projects#plugins), [vim-galore](https://github.com/mhinz/vim-galore/blob/master/PLUGINS.md), [](https://github.com/astier/vlugins)_

# Jump list
  * [extensions/options/readmore/...](#extensionsreadmoreoptions)
  * [documented](#documented)
    * [plugin-maneger](#plugin-maneger)
    * [git](#git)
    * [projects-seessions](#projects-seessions)
    * [undotree](#undotree)
    * [finder](#finder)
    * [file-explorer](#file-explorer)
    * [replace](#replace)
    * [command](#command)
    * [game](#game)
    * [startscreen](#startscreen)
    * [terminal](#terminal)
    * [deoplete-extensions](#deoplete-extensions)
    * [extension](#extension)
    * [telescope-extensions](#telescope-extensions)
    * [tmux](#tmux)
    * [nvim-cmp-extensions](#nvim-cmp-extensions)
    * [visual](#visual)
    * [scroolbar](#scroolbar)
    * [bufferline](#bufferline)
    * [syntax](#syntax)
    * [zen](#zen)
    * [tabline](#tabline)
    * [color](#color)
    * [statusline](#statusline)
    * [highlight](#highlight)
    * [colorscheme](#colorscheme)
    * [movment](#movment)
    * [yanklist](#yanklist)
    * [hop](#hop)
    * [textobject](#textobject)
    * [file-movment](#file-movment)
    * [file](#file)
    * [note](#note)
    * [spell](#spell)
    * [markdown-langueges](#markdown-langueges)
    * [preview](#preview)
    * [todo](#todo)
    * [gui](#gui)
    * [sidebar](#sidebar)
    * [other](#other)
    * [ide](#ide)
    * [tag](#tag)
    * [remote-colab](#remote-colab)
    * [indent](#indent)
    * [buffers](#buffers)
    * [detectindent](#detectindent)
    * [asyncrun](#asyncrun)
    * [windows](#windows)
    * [folds](#folds)
    * [mouse](#mouse)
    * [quickfix](#quickfix)
    * [chat](#chat)
    * [comment](#comment)
    * [key](#key)
    * [toggle](#toggle)
    * [aligner](#aligner)
    * [auto-pairs](#auto-pairs)
    * [fennel](#fennel)
    * [language](#language)
    * [integration](#integration)
    * [lsp](#lsp)
    * [lint](#lint)
    * [debug](#debug)
    * [autocomplete](#autocomplete)
    * [test](#test)
    * [snippets](#snippets)
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
## plugin-maneger
  * [egalpin/apt-vim](https://github.com/egalpin/apt-vim) : Yet another Plugin Manager
  * [faerryn/plogins.nvim](https://github.com/faerryn/plogins.nvim) : A fast, simple, and elegant Neovim plugin manager written in Lua
  * [faerryn/user.nvim](https://github.com/faerryn/user.nvim) : Well, here's another plugin manager, inspired by Emacs' straight.el and use-package
  * [gmarik/vundle.vim](https://github.com/gmarik/vundle.vim) : short for Vim bundle and is a Vim plugin manager
  * [jorengarenar/minplug](https://github.com/jorengarenar/minplug) : Its function is simple: download, update and enable plugins
  * [k-takata/minpac](https://github.com/k-takata/minpac) : A minimal package manager for Vim 8 (and Neovim)
  * [kristijanhusak/vim-packager](https://github.com/kristijanhusak/vim-packager) : Yet Another plugin manager for Vim
  * [marcweber/vim-addon-manager](https://github.com/marcweber/vim-addon-manager) : fetch & activate plugins at startup or runtime depending on your needs
  * [savq/paq-nvim](https://github.com/savq/paq-nvim) : Neovim package manager written in Lua
  * [shougo/dein.vim](https://github.com/shougo/dein.vim) : dark powered Vim/Neovim plugin manager
  * [shougo/neobundle.vim](https://github.com/shougo/neobundle.vim) : a next generation Vim plugin manager [no development]
  * [tek/chromatin](https://github.com/tek/chromatin) : a manager for plugins built in Haskell with nvim-hs and ribosome
  * [tek/proteome.nvim](https://github.com/tek/proteome.nvim) : [deprecated] use [tek/chromatin](https://github.com/tek/chromatin) instead
  * [wbthomason/packer.nvim](https://github.com/wbthomason/packer.nvim) : use-package inspired plugin/package management for Neovim
  * [zgpio/brew.nvim](https://github.com/zgpio/brew.nvim) : plugin manager, rewrite dein with neovim builtin lua
## git
  * [airblade/vim-gitgutter](https://github.com/airblade/vim-gitgutter) : git diff
  * [apzelos/blamer.nvim](https://github.com/apzelos/blamer.nvim) : a git blamer plugin
  * [dinhhuy258/git.nvim](https://github.com/dinhhuy258/git.nvim) : is the simple clone of the plugin vim-fugitive which is written in Lua
  * [drzel/vim-repo-edit](https://github.com/drzel/vim-repo-edit) : One second to read GitHub code with vim
  * [iberianpig/tig-explorer.vim](https://github.com/iberianpig/tig-explorer.vim) : Vim plugin to use Tig as a git client
  * [int3/vim-extradite](https://github.com/int3/vim-extradite) : A git commit browser / git log wrapper that extends fugitive.vim
  * [jaxbot/github-issues.vim](https://github.com/jaxbot/github-issues.vim) : Github issue integration in Vim
  * [jreybert/vimagit](https://github.com/jreybert/vimagit) : Ease your git workflow within vim
  * [junegunn/gv.vim](https://github.com/junegunn/gv.vim) : A git commit browser
  * [junegunn/vim-github-dashboard](https://github.com/junegunn/vim-github-dashboard) : Browse GitHub events (user dashboard, user/repo activity
  * [junkblocker/git-time-lapse](https://github.com/junkblocker/git-time-lapse) : git timeline inside buffer
  * [kdheepak/lazygit.nvim](https://github.com/kdheepak/lazygit.nvim) : Plugin for calling lazygit from within neovim
  * [ldelossa/gh.nvim](https://github.com/ldelossa/gh.nvim) : a plugin for interactive code reviews which take place on the GitHub platform
  * [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim) : Super fast git decorations implemented
  * [mattn/gist-vim](https://github.com/mattn/gist-vim) : This is a vimscript for creating gists
  * [mattn/vim-gist](https://github.com/mattn/vim-gist) : a vimscript for creating gists
  * [odie/gitabra](https://github.com/odie/gitabra) : A little Magit in neovim
  * [pwntester/octo.nvim](https://github.com/pwntester/octo.nvim) : Edit and review GitHub issues and pull requests
  * [rbong/vim-flog](https://github.com/rbong/vim-flog) : lightweight and powerful git branch viewer
  * [rhysd/committia.vim](https://github.com/rhysd/committia.vim) : This plugin improves the git commit buffer
  * [rhysd/git-messenger.vim](https://github.com/rhysd/git-messenger.vim) : reveal the hidden message from Git under the cursor quickly
  * [samoshkin/vim-mergetool](https://github.com/samoshkin/vim-mergetool) : Efficient way of using Vim as a Git mergetool
  * [sindrets/diffview.nvim](https://github.com/sindrets/diffview.nvim) : Single tabpage interface for easily cycling through diffs for all modified files for any git rev
  * [sodapopcan/vim-twiggy](https://github.com/sodapopcan/vim-twiggy) : Maintain your bearings while branching with Git
  * [stsewd/fzf-checkout.vim](https://github.com/stsewd/fzf-checkout.vim) : Manage branches and tags with fzf
  * [tanvirtin/vgit.nvim](https://github.com/tanvirtin/vgit.nvim) : Visual Git Plugin for Neovim to enhance your git experience
  * [timuntersberger/neogit](https://github.com/timuntersberger/neogit) : Magit clone for Neovim
  * [tpope/vim-fugitive](https://github.com/tpope/vim-fugitive) : Fugitive is the premier Vim plugin for Git
  * [tpope/vim-rhubarb](https://github.com/tpope/vim-rhubarb) : If fugitive.vim is the Git, rhubarb.vim is the Hub
  * [wsdjeg/github.vim](https://github.com/wsdjeg/github.vim) : Another github v3 api implemented in viml
## projects-seessions
  * [ahmedkhalf/project.nvim](https://github.com/ahmedkhalf/project.nvim) : provides superior project management
  * [dhruvasagar/vim-prosession](https://github.com/dhruvasagar/vim-prosession) : handle sessions like a pro
  * [ethanholz/nvim-lastplace](https://github.com/ethanholz/nvim-lastplace) : A Lua rewrite of [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace)
  * [jedrzejboczar/possession.nvim](https://github.com/jedrzejboczar/possession.nvim) : Flexible session management for Neovim
  * [natecraddock/sessions.nvim](https://github.com/natecraddock/sessions.nvim) : a simple session manager plugin
  * [natecraddock/workspaces.nvim](https://github.com/natecraddock/workspaces.nvim) : a simple plugin to manage workspace directories in neovim
  * [olimorris/persisted.nvim](https://github.com/olimorris/persisted.nvim) : simple lua plugin for automated session management within Neovim
  * [rmagatti/auto-session](https://github.com/rmagatti/auto-session) : provide seamless automatic session management
  * [shaeinst/penvim](https://github.com/shaeinst/penvim) : project's root directory and documents indentation detector with project based config loader
  * [shatur/neovim-session-manager](https://github.com/shatur/neovim-session-manager) : use built-in mksession to manage sessions like folders in VSCode
  * [sheodox/projectlaunch.nvim](https://github.com/sheodox/projectlaunch.nvim) : plugin for running commands in your project
  * [thaerkh/vim-workspace](https://github.com/thaerkh/vim-workspace) : mainteins sessions
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
## finder
  * [amirrezaask/fuzzy.nvim](https://github.com/amirrezaask/fuzzy.nvim) : Fast, Simple, Powerfull fuzzy finder all in lua
  * [dyng/ctrlsf.vim](https://github.com/dyng/ctrlsf.vim) : An ack/ag/pt/rg powered code search and view tool
  * [fholgado/minibufexpl.vim](https://github.com/fholgado/minibufexpl.vim) : fork of Bindu Wavell's MiniBufExpl with impovments
  * [fiatjaf/neuron.vim](https://github.com/fiatjaf/neuron.vim) : Manage your Zettelkasten with the help of neuron
  * [gfanto/fzf-lsp.nvim](https://github.com/gfanto/fzf-lsp.nvim) : search for symbols using the neovim builtin lsp
  * [ibhagwan/fzf-lua](https://github.com/ibhagwan/fzf-lua) : fzf loves lua
  * [jlanzarotta/bufexplorer](https://github.com/jlanzarotta/bufexplorer) : BufExplorer Plugin for Vim
  * [junegunn/fzf](https://github.com/junegunn/fzf) : FZF Vim integration
  * [liuchengxu/vim-clap](https://github.com/liuchengxu/vim-clap) : modern generic interactive finder and dispatcher, based on the newly feature: floating_win of neovim or popup of vim
  * [lotabout/skim.vim](https://github.com/lotabout/skim.vim) : This is a fork of fzf.vim but for skim
  * [mhinz/vim-grepper](https://github.com/mhinz/vim-grepper) : Use your favorite grep tool to start an asynchronous search
  * [nvim-pack/nvim-spectre](https://github.com/nvim-pack/nvim-spectre) : A search panel for neovim
  * [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) : is a highly extendable fuzzy finder over list
  * [ojroques/nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy) : This plugin makes the Neovim LSP client use FZF to display results and navigate the code
  * [samoshkin/vim-find-files](https://github.com/samoshkin/vim-find-files) : Search for files and show results in a quickfix list, a new buffer
  * [shougo/ddu.vim](https://github.com/shougo/ddu.vim) : provides an asynchronous fuzzy finder UI
  * [shougo/denite.nvim](https://github.com/shougo/denite.nvim) : It is like a fuzzy finder, but is more generic [no development]
  * [shougo/unite.vim](https://github.com/shougo/unite.vim) : search and display information from arbitrary sources like files, buffers, recently used files or registers [no development]
  * [skywind3000/leaderf-snippet](https://github.com/skywind3000/leaderf-snippet) : takes the advantage of the well-known fuzzy finder Leaderf to provide an intuitive way to input snippets
  * [svermeulen/nvim-marksman](https://github.com/svermeulen/nvim-marksman) : lightweight file finder
  * [toppair/reach.nvim](https://github.com/toppair/reach.nvim) : buffer / mark / tabpage / colorscheme switcher
  * [tzachar/fuzzy.nvim](https://github.com/tzachar/fuzzy.nvim) : An abstraction layer on top of fzf and fzy
  * [vijaymarupudi/nvim-fzf](https://github.com/vijaymarupudi/nvim-fzf) : An asynchronous Lua API for using fzf in Neovim
  * [vijaymarupudi/nvim-fzf-commands](https://github.com/vijaymarupudi/nvim-fzf-commands) : A repository for commands using the nvim-fzf library
  * [vim-ctrlspace/vim-ctrlspace](https://github.com/vim-ctrlspace/vim-ctrlspace) : open finder by pressing `<C-space>`
  * [vim-scripts/bufexplorer.zip](https://github.com/vim-scripts/bufexplorer.zip) : quickly and easily switch between buffers
  * [willthbill/opener.nvim](https://github.com/willthbill/opener.nvim) : A workspace/context switcher for neovim
  * [wincent/ferret](https://github.com/wincent/ferret) : improves Vim's multi-file search in four ways
  * [wsdjeg/flygrep.vim](https://github.com/wsdjeg/flygrep.vim) : Fly grep in vim
  * [yggdroot/leaderf](https://github.com/yggdroot/leaderf) : An efficient fuzzy finder that helps to locate files, buffers, mrus, gtags, etc
## file-explorer
  * [francoiscabrol/ranger.vim](https://github.com/francoiscabrol/ranger.vim) : Ranger integration in vim
  * [kevinhwang91/rnvimr](https://github.com/kevinhwang91/rnvimr) : use Ranger in a floating window
  * [luukvbaal/nnn.nvim](https://github.com/luukvbaal/nnn.nvim) : File manager for Neovim powered by nnnp
  * [mattn/vim-molder](https://github.com/mattn/vim-molder) : Minimal File Explorer
  * [mcchrish/nnn.vim](https://github.com/mcchrish/nnn.vim) : File manager for vim/neovim powered by n??
  * [nvim-neo-tree/neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim) : Neovim plugin to browse the file system and other tree like structures
  * [preservim/nerdtree](https://github.com/preservim/nerdtree) : a file system explorer for the Vim editor
  * [ptzz/lf.vim](https://github.com/ptzz/lf.vim) : lf integration in vim and neovim
  * [ripxorip/bolt.nvim](https://github.com/ripxorip/bolt.nvim) : Filter-as-you-type file manager for Neovim
  * [scjangra/files-nvim](https://github.com/scjangra/files-nvim) : external file explorers
  * [shougo/defx.nvim](https://github.com/shougo/defx.nvim) : a dark powered plugin for Neovim/Vim to browse files
  * [shougo/vimfiler.vim](https://github.com/shougo/vimfiler.vim) : powerful file explorer implemented in Vim script [no development]
  * [theblob42/drex.nvim](https://github.com/theblob42/drex.nvim) : Another DiRectory EXplorer for Neovim
  * [timuntersberger/neofs](https://github.com/timuntersberger/neofs) : file manager for neovim written in lua
  * [vifm/neovim-vifm](https://github.com/vifm/neovim-vifm) : Integration between vifm (the vi file manager) and vim [archived]
  * [vifm/vifm.vim](https://github.com/vifm/vifm.vim) : provides integration with Vifm
## replace
  * [dkprice/vim-easygrep](https://github.com/dkprice/vim-easygrep) : Fast and Easy Find and Replace Across Multiple Files
  * [eugen0329/vim-esearch](https://github.com/eugen0329/vim-esearch) : for easy async search and replace across multiple files
  * [junegunn/vim-fnr](https://github.com/junegunn/vim-fnr) : Find-N-Replace in Vim with live preview
## command
  * [ackeraa/todo.nvim](https://github.com/ackeraa/todo.nvim) : It helps you manage your to-do list
  * [andreicristianpetcu/vim-van](https://github.com/andreicristianpetcu/vim-van) : Read Unix man pages faster than a speeding bullet
  * [cespare/vim-sbd](https://github.com/cespare/vim-sbd) : Close buffers smartly [archived]
  * [dbeniamine/vim-mail](https://github.com/dbeniamine/vim-mail) : a small helper for writing mail from vim
  * [duane9/nvim-rg](https://github.com/duane9/nvim-rg) : allows you to run ripgrep from Neovim or Vim
  * [felipec/notmuch-vim](https://github.com/felipec/notmuch-vim) : provides a fully usable mail client interface, utilizing the notmuch framework
  * [dbeniamine/vim-mail](https://gitlab.com/dbeniamine/vim-mail) : a small helper for writing mail from vim
  * [inkarkat/vim-advancedsorters](https://github.com/inkarkat/vim-advancedsorters) : Dose sorting block wise instead of line wise
  * [itchyny/calendar.vim](https://github.com/itchyny/calendar.vim) : A calendar application for Vim
  * [kovetskiy/neovim-move](https://github.com/kovetskiy/neovim-move) : provides a way to move files
  * [mattn/emmet-vim](https://github.com/mattn/emmet-vim) : a vim plug-in which provides support for expanding abbreviations similar to emmet
  * [moll/vim-bbye](https://github.com/moll/vim-bbye) : delete buffers without closing your windows or messing up your layout
  * [ojroques/nvim-bufdel](https://github.com/ojroques/nvim-bufdel) : A very small Neovim plugin to improve the deletion of buffers
  * [rbgrouleff/bclose.vim](https://github.com/rbgrouleff/bclose.vim) : deleting a buffer in Vim without closing the window
  * [vim-utils/vim-man](https://github.com/vim-utils/vim-man) : View man pages in vim
  * [wsdjeg/vim-cheat](https://github.com/wsdjeg/vim-cheat) : cheat in vim
  * [yuratomo/w3m.vim](https://github.com/yuratomo/w3m.vim) : w3m inside vim
## game
  * [alec-gibson/nvim-tetris](https://github.com/alec-gibson/nvim-tetris) : tetris game
  * [amix/vim-2048](https://github.com/amix/vim-2048) : 2048 game
  * [iqxd/vim-mine-sweeping](https://github.com/iqxd/vim-mine-sweeping) : mine sweeping game in vim
  * [rbtnn/vim-game_engine](https://github.com/rbtnn/vim-game_engine) : vim-game_engine
  * [rbtnn/vim-mario](https://github.com/rbtnn/vim-mario) : Mario on Vim
  * [rbtnn/vim-puyo](https://github.com/rbtnn/vim-puyo) : Puyo on Vim
  * [seandewar/killersheep.nvim](https://github.com/seandewar/killersheep.nvim) : A port of killersheep for Neovim
  * [seandewar/nvimesweeper](https://github.com/seandewar/nvimesweeper) : Play Minesweeper in Neovim
  * [theprimeagen/vim-be-good](https://github.com/theprimeagen/vim-be-good) : designed to make you better at vim by creating a game to practice basic movements in
  * [vim-scripts/tetris.vim](https://github.com/vim-scripts/tetris.vim) : A funny way to get used to VIM's h k l and <Space> key
  * [vim/killersheep](https://github.com/vim/killersheep) : Silly game to show off the new features of Vim 8.2
## startscreen
  * [mhinz/vim-startify](https://github.com/mhinz/vim-startify) : the fancy start screen for vim
  * [startup-nvim/startup.nvim](https://github.com/startup-nvim/startup.nvim) : The fully customizable greeter for neovim
## terminal
  * [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim) : persist and toggle multiple terminals
  * [brettanomyces/nvim-editcommand](https://github.com/brettanomyces/nvim-editcommand) : Edit your current shell command inside a scratch buffer
  * [brettanomyces/nvim-terminus](https://github.com/brettanomyces/nvim-terminus) : Edit your current command in a scratch buffer
  * [bronzehedwick/vim-primary-terminal](https://github.com/bronzehedwick/vim-primary-terminal) : Simple terminal management for Neovim.
  * [caenrique/nvim-toggle-terminal](https://github.com/caenrique/nvim-toggle-terminal) : Toggle terminal buffer or create new one if there is none
  * [chengzeyi/multiterm.vim](https://github.com/chengzeyi/multiterm.vim) : Toggle and Switch Between Multiple Floating Terminals
  * [itmecho/neoterm.nvim](https://github.com/itmecho/neoterm.nvim) : Simple neovim terminal plugin written in lua
  * [jlesquembre/nterm.nvim](https://github.com/jlesquembre/nterm.nvim) : neovim plugin to interact with the terminal emulator, with notifications
  * [kassio/neoterm](https://github.com/kassio/neoterm) : Use the same terminal for everything
  * [lenovsky/nuake](https://github.com/lenovsky/nuake) : A Quake-style terminal panel
  * [loricandre/oneterm.nvim](https://github.com/loricandre/oneterm.nvim) : One terminal plugin to rule them all (eventually)
  * [mizlan/termbufm](https://github.com/mizlan/termbufm) : A wrapper around the Neovim terminal window
  * [nikvdp/neomux](https://github.com/nikvdp/neomux) : a neovim <> terminal integration plugin
  * [pianocomposer321/consolation.nvim](https://github.com/pianocomposer321/consolation.nvim) : A general-perpose terminal wrapper and management plugin for neovim
  * [s1n7ax/nvim-terminal](https://github.com/s1n7ax/nvim-terminal) : open/toggle the terminals in Neovim
  * [shougo/deol.nvim](https://github.com/shougo/deol.nvim) : dark powered shell for Neovim
  * [voldikss/vim-floaterm](https://github.com/voldikss/vim-floaterm) : Use vim terminal in the floating/popup window
## deoplete-extensions
  * [carlitux/deoplete-ternjs](https://github.com/carlitux/deoplete-ternjs) : deoplete.nvim source for javascript
  * [deoplete-plugins/deoplete-terminal](https://github.com/deoplete-plugins/deoplete-terminal) : Terminal completion for deoplete.nvim
  * [juliaeditorsupport/deoplete-julia](https://github.com/juliaeditorsupport/deoplete-julia) : This package supplements julia-vim by providing syntax completions, through Deoplete [archived]
  * [kristijanhusak/deoplete-phpactor](https://github.com/kristijanhusak/deoplete-phpactor) : Phpactor integration for deoplete.nvim
  * [ponko2/deoplete-fish](https://github.com/ponko2/deoplete-fish) : deoplete.nvim source for fish
## extension
  * [haya14busa/incsearch-fuzzy.vim](https://github.com/haya14busa/incsearch-fuzzy.vim) : incremantal fuzzy search extension for incsearch.vim
  * [kristijanhusak/defx-git](https://github.com/kristijanhusak/defx-git) : Git status implementation for defx.nvim
  * [kristijanhusak/defx-icons](https://github.com/kristijanhusak/defx-icons) : Custom implementation of vim-devicons for defx.nvim
  * [matsui54/defx-sftp](https://github.com/matsui54/defx-sftp) : a defx source for sftp
  * [philrunninger/nerdtree-buffer-ops](https://github.com/philrunninger/nerdtree-buffer-ops) : a NERDTree plugin that highlights all visible nodes that are open in Vim
  * [scrooloose/nerdtree-project-plugin](https://github.com/scrooloose/nerdtree-project-plugin) : nerd extension which preserves Tree state (open/closed dirs) between sessions
  * [thehamsta/nvim-treesitter-commonlisp](https://github.com/thehamsta/nvim-treesitter-commonlisp) : extends the standard highlighting of nvim-treesitter for Common Lisp
  * [thomasfaingnaert/vim-lsp-neosnippet](https://github.com/thomasfaingnaert/vim-lsp-neosnippet) : integrates neosnippet.vim in vim-lsp
  * [tiagofumo/vim-nerdtree-syntax-highlight](https://github.com/tiagofumo/vim-nerdtree-syntax-highlight) : adds syntax for nerdtree on most common file extensions
  * [tjdevries/tree-sitter-lua](https://github.com/tjdevries/tree-sitter-lua) : Tree sitter grammar for Lua built to be used inside of Neovim
  * [tommcdo/vim-fugitive-blame-ext](https://github.com/tommcdo/vim-fugitive-blame-ext) : extends the functionality of tpope's fugitive plugin by showing first line of the commit message
  * [vim-airline/vim-airline-themes](https://github.com/vim-airline/vim-airline-themes) : official theme repository for vim-airline
  * [wellle/tmux-complete.vim](https://github.com/wellle/tmux-complete.vim) : insert mode completion of words in adjacent tmux panes
  * [wsdjeg/dein-ui.vim](https://github.com/wsdjeg/dein-ui.vim) : UI for Shougo's dein.vim
  * [xuyuanp/nerdtree-git-plugin](https://github.com/xuyuanp/nerdtree-git-plugin) : A plugin of NERDTree showing git status flags
  * [yamatsum/nvim-nonicons](https://github.com/yamatsum/nvim-nonicons) : Collection of configurations for nvim-web-devicons
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
  * [elpiloto/telescope-vimwiki.nvim](https://github.com/elpiloto/telescope-vimwiki.nvim) : Look for your vimwiki pages using telescope
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
  * [slarwise/telescope-args.nvim](https://github.com/slarwise/telescope-args.nvim) : telescopeextension for navigating the argument list
  * [tamago324/telescope-openbrowser.nvim](https://github.com/tamago324/telescope-openbrowser.nvim) : Integration for open-browser.vim with telescope.nvim
  * [tc72/telescope-tele-tabby.nvim](https://github.com/tc72/telescope-tele-tabby.nvim) : A tab switcher extension for Telescope
  * [tom-anders/telescope-vim-bookmarks.nvim](https://github.com/tom-anders/telescope-vim-bookmarks.nvim) : telescope extensions to integrate with [mattesgroeger/vim-bookmarks](https://github.com/mattesgroeger/vim-bookmarks)
  * [wesleimp/telescope-windowizer.nvim](https://github.com/wesleimp/telescope-windowizer.nvim) : telescope extensions to Create new tmux window ready for edit your selected file inside vim
  * [xiyaowong/telescope-emoji.nvim](https://github.com/xiyaowong/telescope-emoji.nvim) : telescope extensions to search emoji
  * [zane-/cder.nvim](https://github.com/zane-/cder.nvim) : A telescope.nvimextension for quickly changing your working directory
  * [zane-/howdoi.nvim](https://github.com/zane-/howdoi.nvim) : telescope extension for previewing howdoi results
## tmux
  * [aserowy/tmux.nvim](https://github.com/aserowy/tmux.nvim) : a few features making vim and tmux work beautifully together
  * [christoomey/vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator) : navigate seamlessly between vim and tmux splits using a consistent set of hotkeys
  * [hkupty/nvimux](https://github.com/hkupty/nvimux) : Nvimux allows neovim to work as a tmux replacement
  * [junegunn/heytmux](https://github.com/junegunn/heytmux) : Tmux scripting made easy
  * [numtostr/navigator.nvim](https://github.com/numtostr/navigator.nvim) : Smoothly navigate between splits and panes
  * [preservim/vimux](https://github.com/preservim/vimux) : easily interact with tmux from vim
  * [shivamashtikar/tmuxjump.vim](https://github.com/shivamashtikar/tmuxjump.vim) : A plugin to open file from file paths printed in sibling tmux pane
## nvim-cmp-extensions
  * [david-kunz/cmp-npm](https://github.com/david-kunz/cmp-npm) : nvim-cmp extension for npm autocomplete
  * [dmitmel/cmp-cmdline-history](https://github.com/dmitmel/cmp-cmdline-history) : nvim-cmp source for getting completions from command-line or search histories.
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
  * [lukas-reineke/cmp-rg](https://github.com/lukas-reineke/cmp-rg) : nvim-cmp extension for rg autocomplete
  * [lukas-reineke/cmp-under-comparator](https://github.com/lukas-reineke/cmp-under-comparator) : A tiny function for nvim-cmpto better sort completion items that start with one or more underlines
  * [mtoohey31/cmp-fish](https://github.com/mtoohey31/cmp-fish) : nvim-cmp extension for fish autocomplete
  * [notomo/cmp-neosnippet](https://github.com/notomo/cmp-neosnippet) : nvim-cmp source for neosnippet
  * [petertriho/cmp-git](https://github.com/petertriho/cmp-git) : nvim-cmp extension for git autocomplete
  * [quangnguyen30192/cmp-nvim-tags](https://github.com/quangnguyen30192/cmp-nvim-tags) : nvim-cmp extension for tag autocomplete
  * [quangnguyen30192/cmp-nvim-ultisnips](https://github.com/quangnguyen30192/cmp-nvim-ultisnips) : nvim-cmp extension for ultisnips autocomplete
  * [ray-x/cmp-treesitter](https://github.com/ray-x/cmp-treesitter) : nvim-cmp extension for treesitter autocomplete
  * [rcarriga/cmp-dap](https://github.com/rcarriga/cmp-dap) : nvim-cmp extension for dap autocomplete
  * [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip) : nvim-cmp extension for luasnip autocomplete
  * [tzachar/cmp-fuzzy-buffer](https://github.com/tzachar/cmp-fuzzy-buffer) : nvim-cmp source for fuzzy matched items from using the current buffer
  * [tzachar/cmp-fuzzy-path](https://github.com/tzachar/cmp-fuzzy-path) : nvim-cmp source for filesystem paths, employing `fd` and regular expressions to find files
  * [tzachar/cmp-tabnine](https://github.com/tzachar/cmp-tabnine) : nvim-cmp extension for tabline autocomplete
  * [uga-rosa/cmp-dictionary](https://github.com/uga-rosa/cmp-dictionary) : Dictionary completion source for nvim-cmp
  * [zbirenbaum/copilot-cmp](https://github.com/zbirenbaum/copilot-cmp) : nvim-cmp extension for copilot autocomplete
## visual
  * [ahmedkhalf/notif.nvim](https://github.com/ahmedkhalf/notif.nvim) : Notification system
  * [axlebedev/footprints](https://github.com/axlebedev/footprints) : Highlight last edited lines
  * [ayosec/hltermpaste.vim](https://github.com/ayosec/hltermpaste.vim) : highlight terminal paste
  * [bennypowers/nvim-regexplainer](https://github.com/bennypowers/nvim-regexplainer) : Describe the regular expression under the cursor
  * [chrisbra/changesplugin](https://github.com/chrisbra/changesplugin) : visualize which lines have been changed since editing started
  * [chrisbra/dynamicsigns](https://github.com/chrisbra/dynamicsigns) : Using Signs for different things (visualy)
  * [cosmicnvim/cosmic-ui](https://github.com/cosmicnvim/cosmic-ui) : simple wrapper around specific vim functionality
  * [danilamihailov/beacon.nvim](https://github.com/danilamihailov/beacon.nvim) : Whenever cursor jumps some distance or moves between windows, it will flash so you can see where it is
  * [dbmrq/vim-ditto](https://github.com/dbmrq/vim-ditto) : highlights overused words
  * [delphinus/vim-auto-cursorline](https://github.com/delphinus/vim-auto-cursorline) : Show / hide cursorline in connection with cursor moving
  * [edluffy/specs.nvim](https://github.com/edluffy/specs.nvim) : Show where your cursor moves when jumping large distances
  * [gelguy/wilder.nvim](https://github.com/gelguy/wilder.nvim) : A more adventurous wildmenu
  * [gennaro-tedesco/nvim-peekup](https://github.com/gennaro-tedesco/nvim-peekup) : peek registers befor pasting them
  * [haringsrob/nvim_context_vt](https://github.com/haringsrob/nvim_context_vt) : Shows virtual text of the current context after functions, methods, statements, etc.
  * [ivyl/vim-bling](https://github.com/ivyl/vim-bling) : blinks search result after jumping
  * [jubnzv/virtual-types.nvim](https://github.com/jubnzv/virtual-types.nvim) : shows type annotations for functions in virtual text using built-in LSP client
  * [junegunn/rainbow_parentheses.vim](https://github.com/junegunn/rainbow_parentheses.vim) : Much simpler Rainbow Parentheses
  * [karb94/neoscroll.nvim](https://github.com/karb94/neoscroll.nvim) : smooth scrolling neovim plugin written in lua
  * [kevinhwang91/nvim-ffhighlight](https://github.com/kevinhwang91/nvim-ffhighlight) : Highlight the chars and words searched by `f` and `F`
  * [kevinhwang91/nvim-hlslens](https://github.com/kevinhwang91/nvim-hlslens) : search with more visuals
  * [kien/rainbow_parentheses.vim](https://github.com/kien/rainbow_parentheses.vim) : Better Rainbow Parentheses
  * [lewis6991/nvim-treesitter-context](https://github.com/lewis6991/nvim-treesitter-context) : Lightweight alternative to context.vim implemented with nvim-treesitter
  * [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim) : indentation guides to all lines
  * [lukas-reineke/virt-column.nvim](https://github.com/lukas-reineke/virt-column.nvim) : Display a character as the colorcolumn
  * [luochen1990/rainbow](https://github.com/luochen1990/rainbow) : Rainbow Parentheses Improved
  * [machakann/vim-highlightedyank](https://github.com/machakann/vim-highlightedyank) : Make the yanked region apparent
  * [mhinz/vim-signify](https://github.com/mhinz/vim-signify) : uses the sign column to indicate added, modified and removed lines in a file that is managed by a version control system
  * [monkoose/matchparen.nvim](https://github.com/monkoose/matchparen.nvim) : highlight matching parentheses
  * [myusuf3/numbers.vim](https://github.com/myusuf3/numbers.vim) : intelligently toggling line numbers
  * [nacro90/numb.nvim](https://github.com/nacro90/numb.nvim) : Peeking the buffer while entering command :[number]
  * [nagy135/visualmark-nvim](https://github.com/nagy135/visualmark-nvim) : shows where marks are stored visually in buffer using virtual_text
  * [narutoxy/dim.lua](https://github.com/narutoxy/dim.lua) : dim the unused variables and functions using lsp and treesitter
  * [nfrid/due.nvim](https://github.com/nfrid/due.nvim) : provides you due for the date string
  * [norcalli/nvim-terminal.lua](https://github.com/norcalli/nvim-terminal.lua) : high performance filetype mode for Neovim which leverages `concealand` highlights your buffer with the correct color codes
  * [ntpeters/vim-better-whitespace](https://github.com/ntpeters/vim-better-whitespace) : causes all trailing whitespace characters to be highlighted
  * [nvim-lua/lsp-status.nvim](https://github.com/nvim-lua/lsp-status.nvim) : generating statusline components from the built-in LSP client
  * [pgdouyon/vim-evanesco](https://github.com/pgdouyon/vim-evanesco) : automatically clearing Vim's search highlighting whenever the cursor moves or insert mode is entered
  * [pocco81/noclc.nvim](https://github.com/pocco81/noclc.nvim) : disabling the cursor-line/column in unused windows/buffers
  * [powerman/vim-plugin-ansiesc](https://github.com/powerman/vim-plugin-ansiesc) : will conceal Ansi escape sequences but will cause subsequent text to be colored as the escape sequence specifies
  * [psliwka/vim-smoothie](https://github.com/psliwka/vim-smoothie) : makes scrolling nice and smooth
  * [qxxxb/vim-searchhi](https://github.com/qxxxb/vim-searchhi) : Highlight the current search result in a different style than the other search results
  * [rcarriga/nvim-notify](https://github.com/rcarriga/nvim-notify) : fancy, configurable, notification manager
  * [rickhowe/diffchar.vim](https://github.com/rickhowe/diffchar.vim) : make diff mode more useful
  * [rktjmp/highlight-current-n.nvim](https://github.com/rktjmp/highlight-current-n.nvim) : highlights the current /, ? or * match under your cursor when pressing n or N and gets out of the way afterwards
  * [romainl/vim-cool](https://github.com/romainl/vim-cool) : disables search highlighting when you are done searching and re-enables it when you search again
  * [ryanoasis/vim-devicons](https://github.com/ryanoasis/vim-devicons) : Adds icons to your plugins
  * [smiteshp/nvim-gps](https://github.com/smiteshp/nvim-gps) : Take this handy dandy gps with you on your coding adventures and always know where you are
  * [smiteshp/nvim-navic](https://github.com/smiteshp/nvim-navic) : A simple statusline/winbar component that uses LSP to show your current code context
  * [tadaa/vimade](https://github.com/tadaa/vimade) : fades your inactive buffers and preserves syntax highlighting
  * [thehamsta/nvim-dap-virtual-text](https://github.com/thehamsta/nvim-dap-virtual-text) : adds virtual text support to nvim-dap
  * [tjdevries/overlength.vim](https://github.com/tjdevries/overlength.vim) : hlight when lines go over the length that you want them
  * [tjdevries/train.nvim](https://github.com/tjdevries/train.nvim) : Train yourself with vim motions and make your own train tracks
  * [tversteeg/registers.nvim](https://github.com/tversteeg/registers.nvim) : Show register content when you try to access it
  * [valloric/matchtagalways](https://github.com/valloric/matchtagalways) : Always highlight enclosing tags
  * [vim-scripts/csapprox](https://github.com/vim-scripts/csapprox) : This plugin makes GVim-only colorschemes Just Work in terminal Vim
  * [vim-scripts/syntaxrange](https://github.com/vim-scripts/syntaxrange) : provides commands and functions to set up regions in the current buffer that either use a syntax different from the buffer's 'filetype', or completely ignore the syntax
  * [weirdsmiley/bionically](https://github.com/weirdsmiley/bionically) : convert text on current buffer into a bionic reading font
  * [wellle/context.vim](https://github.com/wellle/context.vim) : shows the context of the currently visible buffer contents
  * [winston0410/range-highlight.nvim](https://github.com/winston0410/range-highlight.nvim) : hightlights ranges you have entered in commandline
  * [xiyaowong/virtcolumn.nvim](https://github.com/xiyaowong/virtcolumn.nvim) : Display a character as the colorcolumn
  * [xolox/vim-lua-inspect](https://github.com/xolox/vim-lua-inspect) : Semantic highlighting for Lua in Vim
  * [yggdroot/indentline](https://github.com/yggdroot/indentline) : is used for displaying thin vertical lines at each indentation level for code indented with spaces
## scroolbar
  * [dstein64/nvim-scrollview](https://github.com/dstein64/nvim-scrollview) : Neovim plugin that displays interactive vertical scrollbars
  * [lewis6991/satellite.nvim](https://github.com/lewis6991/satellite.nvim) : displays decorated scrollbars
  * [petertriho/nvim-scrollbar](https://github.com/petertriho/nvim-scrollbar) : Extensible Neovim Scrollbar
  * [sslivkoff/vim-scroll-barnacle](https://github.com/sslivkoff/vim-scroll-barnacle) : a scrollbar for vim in the terminal
## bufferline
  * [ap/vim-buftabline](https://github.com/ap/vim-buftabline)
  * [bagrat/vim-buffet](https://github.com/bagrat/vim-buffet) : takes your buffers and tabs, and shows them combined in the tabline
  * [bling/vim-bufferline](https://github.com/bling/vim-bufferline)
  * [jose-elias-alvarez/buftabline.nvim](https://github.com/jose-elias-alvarez/buftabline.nvim) : A low-config, minimalistic buffer tabline Neovim plugin written in Lua, [archived]
  * [zefei/vim-wintabs](https://github.com/zefei/vim-wintabs)
## syntax
  * [akz92/vim-ionic2](https://github.com/akz92/vim-ionic2) : ionic2 syntax highlight
  * [cespare/vim-toml](https://github.com/cespare/vim-toml) : toml syntax highlight
  * [dagwieers/asciidoc-vim](https://github.com/dagwieers/asciidoc-vim) : AsciiDoc syntax highlighting
  * [euclidianace/betterlua.vim](https://github.com/euclidianace/betterlua.vim) : Better Lua Syntax For Vim
  * [fladson/vim-kitty](https://github.com/fladson/vim-kitty) : Syntax highlighting for Kitty terminal config files
  * [glench/vim-jinja2-syntax](https://github.com/glench/vim-jinja2-syntax) : Jinja2 syntax file for vim with the ability to detect either HTML or Jinja
  * [herringtondarkholme/yats.vim](https://github.com/herringtondarkholme/yats.vim) : Yet Another TypeScript Syntax
  * [jackguo380/vim-lsp-cxx-highlight](https://github.com/jackguo380/vim-lsp-cxx-highlight) : provides C/C++/Cuda/ObjC semantic highlighting using LSP
  * [jelera/vim-javascript-syntax](https://github.com/jelera/vim-javascript-syntax) : Enhanced JavaScript Syntax for Vim
  * [junegunn/vim-journal](https://github.com/junegunn/vim-journal) : syntax for journal file type
  * [jwalton512/vim-blade](https://github.com/jwalton512/vim-blade) : blade template syntax highlight
  * [kovetskiy/sxhkd-vim](https://github.com/kovetskiy/sxhkd-vim) : sxhkd syntax highlight
  * [ledger/vim-ledger](https://github.com/ledger/vim-ledger) : Filetype detection, syntax highlighting, auto-formatting, auto-completion, and other tools for working with ledger files
  * [lifepillar/pgsql.vim](https://github.com/lifepillar/pgsql.vim) : provides syntax highlighting and auto-completion support for PostgreSQL
  * [maxmellon/vim-jsx-pretty](https://github.com/maxmellon/vim-jsx-pretty) : The React syntax highlighting and indenting plugin (Also supports the typescript tsx file)
  * [neovimhaskell/haskell-vim](https://github.com/neovimhaskell/haskell-vim) : Syntax Highlighting and Indentation for Haskell and Cabal
  * [nickhutchinson/vim-cmake-syntax](https://github.com/nickhutchinson/vim-cmake-syntax) : Vim syntax highlighting rules for modern CMake [archived]
  * [octol/vim-cpp-enhanced-highlight](https://github.com/octol/vim-cpp-enhanced-highlight) : contains additional syntax highlighting that I use for C++11/14/17 development in Vim
  * [othree/yajs.vim](https://github.com/othree/yajs.vim) : Yet Another JavaScript Syntax file for Vim
  * [peitalin/vim-jsx-typescript](https://github.com/peitalin/vim-jsx-typescript) : Syntax highlighting and indentation for JSX in Typescript
  * [plasticboy/vim-markdown](https://github.com/plasticboy/vim-markdown) : Syntax highlighting, matching rules and mappings for the original Markdown and extensions
  * [potatoesmaster/i3-vim-syntax](https://github.com/potatoesmaster/i3-vim-syntax) : i3 config syntax highlight
  * [shougo/neco-syntax](https://github.com/shougo/neco-syntax) : Syntax source for neocomplete/deoplete/ncm
  * [solarnz/thrift.vim](https://github.com/solarnz/thrift.vim) : thrift syntax plugin for vim
  * [tbastos/vim-lua](https://github.com/tbastos/vim-lua) : Improved Lua 5.3 syntax and indentation support for Vim
  * [tomlion/vim-solidity](https://github.com/tomlion/vim-solidity) : Syntax files for Solidity
  * [vhda/verilog_systemverilog.vim](https://github.com/vhda/verilog_systemverilog.vim) : Vim Syntax Plugin for Verilog and SystemVerilog
  * [vim-python/python-syntax](https://github.com/vim-python/python-syntax) : Python syntax highlighting for Vim
  * [vim-ruby/vim-ruby](https://github.com/vim-ruby/vim-ruby) : includes syntax highlighting, indentation, omnicompletion, and various useful tools and mappings for writing ruby code
  * [wsdjeg/syntastic](https://github.com/wsdjeg/syntastic) : syntax checking plugin
## zen
  * [amix/vim-zenroom2](https://github.com/amix/vim-zenroom2) : emulates iA Writer environment
  * [folke/twilight.nvim](https://github.com/folke/twilight.nvim) : dims inactive portions of the code you're editing
  * [folke/zen-mode.nvim](https://github.com/folke/zen-mode.nvim) : Distraction-free coding for Neovim
  * [henriquehbr/ataraxis.lua](https://github.com/henriquehbr/ataraxis.lua) : absence of mental stress or anxiety, a state of serene calmness
  * [junegunn/limelight.vim](https://github.com/junegunn/limelight.vim) : Hyperfocus-writing in Vim
  * [koenverburg/peepsight.nvim](https://github.com/koenverburg/peepsight.nvim) : just focus on one function at the time
  * [pocco81/truezen.nvim](https://github.com/pocco81/truezen.nvim) : Clean and elegant distraction-free writing
  * [sunjon/shade.nvim](https://github.com/sunjon/shade.nvim) : dims your inactive windows
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
  * [pacha/vem-tabline](https://github.com/pacha/vem-tabline) : a lightweight Vim plugin to display your tabs and buffers at the top of your screen
  * [rafcamlet/tabline-framework.nvim](https://github.com/rafcamlet/tabline-framework.nvim)
  * [romgrk/barbar.nvim](https://github.com/romgrk/barbar.nvim)
  * [webdevel/tabulous](https://github.com/webdevel/tabulous) : Lightweight Vim plugin to enhance the tabline including numbered tab page labels
## color
  * [ap/vim-css-color](https://github.com/ap/vim-css-color) : preview colours in source code while editing
  * [chrisbra/colorizer](https://github.com/chrisbra/colorizer) : color colornames and codes
  * [lifepillar/vim-colortemplate](https://github.com/lifepillar/vim-colortemplate) : makes it easy to develop color schemes
  * [m00qek/baleia.nvim](https://github.com/m00qek/baleia.nvim) : Colorize text with ANSI escape sequences
  * [norcalli/nvim-base16.lua](https://github.com/norcalli/nvim-base16.lua) : Programmatic lua library for setting base16 themes in Neovim
  * [norcalli/nvim-colorizer.lua](https://github.com/norcalli/nvim-colorizer.lua) : A high-performance color highlighter for Neovim which has no external dependencies
  * [ntbbloodbath/color-converter.nvim](https://github.com/ntbbloodbath/color-converter.nvim) : Easily convert your CSS colors
  * [nvim-colortils/colortils.nvim](https://github.com/nvim-colortils/colortils.nvim) : Neovim color utils
  * [rktjmp/lush.nvim](https://github.com/rktjmp/lush.nvim) : colorscheme creation aid for Neovim
  * [tjdevries/colorbuddy.nvim](https://github.com/tjdevries/colorbuddy.nvim) : A colorscheme maker for Neovim
  * [ziontee113/color-picker.nvim](https://github.com/ziontee113/color-picker.nvim) : lets Neovim Users choose & modify colors
## statusline
  * [adelarsq/neoline.vim](https://github.com/adelarsq/neoline.vim)
  * [b0o/incline.nvim](https://github.com/b0o/incline.nvim)
  * [beauwilliams/statusline.lua](https://github.com/beauwilliams/statusline.lua)
  * [bluz71/vim-mistfly-statusline](https://github.com/bluz71/vim-mistfly-statusline) : a simple, fast and informative statusline for Vim
  * [datwaft/bubbly.nvim](https://github.com/datwaft/bubbly.nvim)
  * [doums/barow](https://github.com/doums/barow) : A minimalist statusline [archived]
  * [famiu/feline.nvim](https://github.com/famiu/feline.nvim) : A minimal, stylish and customizable statusline / winbar for Neovim written in Lua
  * [feline-nvim/feline.nvim](https://github.com/feline-nvim/feline.nvim)
  * [fmoralesc/worldslice](https://github.com/fmoralesc/worldslice) : minimalistic statusline and tabline configuration
  * [glepnir/galaxyline.nvim](https://github.com/glepnir/galaxyline.nvim) : light-weight and Super Fast statusline plugin
  * [glepnir/spaceline.vim](https://github.com/glepnir/spaceline.vim) : The best vim statusline plugin
  * [hoob3rt/lualine.nvim](https://github.com/hoob3rt/lualine.nvim) : A blazing fast and easy to configure Neovim statusline written in Lua
  * [itchyny/lightline.vim](https://github.com/itchyny/lightline.vim)
  * [konapun/vacuumline.nvim](https://github.com/konapun/vacuumline.nvim)
  * [ntbbloodbath/galaxyline.nvim](https://github.com/ntbbloodbath/galaxyline.nvim)
  * [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim)
  * [ojroques/nvim-hardline](https://github.com/ojroques/nvim-hardline)
  * [powerline/powerline](https://github.com/powerline/powerline)
  * [r1ri/suffer](https://github.com/r1ri/suffer) : simple bufferline plugin, in less the 30 lines of lua
  * [rbong/vim-crystalline](https://github.com/rbong/vim-crystalline) : the plugin lets you build your own statusline and tabline in a vanilla vim style. It also comes with a bufferline
  * [rebelot/heirline.nvim](https://github.com/rebelot/heirline.nvim)
  * [tamton-aquib/staline.nvim](https://github.com/tamton-aquib/staline.nvim)
  * [tjdevries/express_line.nvim](https://github.com/tjdevries/express_line.nvim)
  * [tpope/vim-flagship](https://github.com/tpope/vim-flagship)
  * [vim-airline/vim-airline](https://github.com/vim-airline/vim-airline)
  * [windwp/windline.nvim](https://github.com/windwp/windline.nvim)
## highlight
  * [galicarnax/vim-regex-syntax](https://github.com/galicarnax/vim-regex-syntax) : Syntax highlight for regular expressions
  * [guns/vim-clojure-highlight](https://github.com/guns/vim-clojure-highlight) : Extend builtin syntax highlighting to local, referred, and aliased vars in Clojure buffers
  * [lpinilla/vim-codepainter](https://github.com/lpinilla/vim-codepainter) : color different parts of code making the use of text properties
  * [numirias/semshi](https://github.com/numirias/semshi) : provides semantic highlighting for Python in Neovim
## colorscheme
  * [1995parham/naz.vim](https://github.com/1995parham/naz.vim)
  * [adisen99/apprentice.nvim](https://github.com/adisen99/apprentice.nvim)
  * [adisen99/codeschool.nvim](https://github.com/adisen99/codeschool.nvim)
  * [alessandroyorba/despacio](https://github.com/alessandroyorba/despacio)
  * [altercation/vim-colors-solarized](https://github.com/altercation/vim-colors-solarized)
  * [andersevenrud/nordic.nvim](https://github.com/andersevenrud/nordic.nvim)
  * [arcticicestudio/nord-vim](https://github.com/arcticicestudio/nord-vim)
  * [arthurealike/vim-j](https://github.com/arthurealike/vim-j)
  * [arzg/vim-substrata](https://github.com/arzg/vim-substrata)
  * [askfiy/catppuccin](https://github.com/askfiy/catppuccin)
  * [axvr/photon.vim](https://github.com/axvr/photon.vim)
  * [axvr/raider.vim](https://github.com/axvr/raider.vim)
  * [base16-project/base16-vim](https://github.com/base16-project/base16-vim)
  * [benwr/tuftish](https://github.com/benwr/tuftish)
  * [bkegley/gloombuddy](https://github.com/bkegley/gloombuddy)
  * [blueshirts/darcula](https://github.com/blueshirts/darcula)
  * [bluz71/vim-moonfly-colors](https://github.com/bluz71/vim-moonfly-colors)
  * [bluz71/vim-nightfly-guicolors](https://github.com/bluz71/vim-nightfly-guicolors)
  * [briones-gabriel/darcula-solid.nvim](https://github.com/briones-gabriel/darcula-solid.nvim)
  * [catppuccin/nvim](https://github.com/catppuccin/nvim)
  * [challenger-deep-theme/vim](https://github.com/challenger-deep-theme/vim)
  * [chriskempson/base16-vim](https://github.com/chriskempson/base16-vim)
  * [christianchiarulli/nvcode-color-schemes.vim](https://github.com/christianchiarulli/nvcode-color-schemes.vim)
  * [chrsm/paramount-ng.nvim](https://github.com/chrsm/paramount-ng.nvim)
  * [cpea2506/one_monokai.nvim](https://github.com/cpea2506/one_monokai.nvim)
  * [dilangmb/nightbuddy](https://github.com/dilangmb/nightbuddy)
  * [dracula/vim](https://github.com/dracula/vim)
  * [edeneast/nightfox.nvim](https://github.com/edeneast/nightfox.nvim)
  * [elianiva/gruvy.nvim](https://github.com/elianiva/gruvy.nvim)
  * [elianiva/icy.nvim](https://github.com/elianiva/icy.nvim)
  * [ellisonleao/gruvbox.nvim](https://github.com/ellisonleao/gruvbox.nvim)
  * [elvessousa/sobrio](https://github.com/elvessousa/sobrio)
  * [fenetikm/falcon](https://github.com/fenetikm/falcon)
  * [flazz/vim-colorschemes](https://github.com/flazz/vim-colorschemes)
  * [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim)
  * [frenzyexists/aquarium-vim](https://github.com/frenzyexists/aquarium-vim)
  * [ful1e5/onedark.nvim](https://github.com/ful1e5/onedark.nvim)
  * [ghifarit53/tokyonight-vim](https://github.com/ghifarit53/tokyonight-vim)
  * [glepnir/zephyr-nvim](https://github.com/glepnir/zephyr-nvim)
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
  * [maaslalani/nordbuddy](https://github.com/maaslalani/nordbuddy)
  * [mangeshrex/uwu.vim](https://github.com/mangeshrex/uwu.vim)
  * [markeganfuller/vim-journeyman](https://github.com/markeganfuller/vim-journeyman)
  * [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim)
  * [matsuuu/pinkmare](https://github.com/matsuuu/pinkmare)
  * [maxst/flatcolor](https://github.com/maxst/flatcolor)
  * [mcchrish/zenbones.nvim](https://github.com/mcchrish/zenbones.nvim)
  * [metalelf0/jellybeans-nvim](https://github.com/metalelf0/jellybeans-nvim)
  * [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next)
  * [mhinz/vim-janah](https://github.com/mhinz/vim-janah)
  * [mjlbach/onedark.nvim](https://github.com/mjlbach/onedark.nvim)
  * [mofiqul/dracula.nvim](https://github.com/mofiqul/dracula.nvim)
  * [mofiqul/vim-code-dark](https://github.com/mofiqul/vim-code-dark)
  * [mofiqul/vscode.nvim](https://github.com/mofiqul/vscode.nvim)
  * [mordechaihadad/nvim-papadark](https://github.com/mordechaihadad/nvim-papadark)
  * [morhetz/gruvbox](https://github.com/morhetz/gruvbox)
  * [nanotech/jellybeans.vim](https://github.com/nanotech/jellybeans.vim)
  * [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim)
  * [nekonako/xresources-nvim](https://github.com/nekonako/xresources-nvim)
  * [nightsense/cosmic_latte](https://github.com/nightsense/cosmic_latte)
  * [novakne/kosmikoa.nvim](https://github.com/novakne/kosmikoa.nvim)
  * [npxbr/gruvbox](https://github.com/npxbr/gruvbox)
  * [ntbbloodbath/doom-one.nvim](https://github.com/ntbbloodbath/doom-one.nvim)
  * [nxvu699134/vn-night.nvim](https://github.com/nxvu699134/vn-night.nvim)
  * [olimorris/onedark.nvim](https://github.com/olimorris/onedark.nvim)
  * [olimorris/onedarkpro.nvim](https://github.com/olimorris/onedarkpro.nvim)
  * [overcache/neosolarized](https://github.com/overcache/neosolarized)
  * [owickstrom/vim-colors-paramount](https://github.com/owickstrom/vim-colors-paramount)
  * [phha/zenburn.nvim](https://github.com/phha/zenburn.nvim)
  * [phsix/nvim-hybrid](https://github.com/phsix/nvim-hybrid)
  * [plan9-for-vimspace/acme-colors](https://github.com/plan9-for-vimspace/acme-colors)
  * [projekt0n/github-nvim-theme](https://github.com/projekt0n/github-nvim-theme)
  * [pygamer0/darc.nvim](https://github.com/pygamer0/darc.nvim)
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
  * [shatur/neovim-ayu](https://github.com/shatur/neovim-ayu)
  * [shaunsingh/moonlight.nvim](https://github.com/shaunsingh/moonlight.nvim)
  * [shaunsingh/nord.nvim](https://github.com/shaunsingh/nord.nvim)
  * [shaunsingh/seoul256.nvim](https://github.com/shaunsingh/seoul256.nvim)
  * [shaunsingh/solarized.nvim](https://github.com/shaunsingh/solarized.nvim)
  * [shrimpram/vim-stella](https://github.com/shrimpram/vim-stella)
  * [sickill/vim-monokai](https://github.com/sickill/vim-monokai)
  * [softmotions/vim-dark-frost-theme](https://github.com/softmotions/vim-dark-frost-theme)
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
  * [u03c1/outrun-vim](https://github.com/u03c1/outrun-vim)
  * [vigoux/oak](https://github.com/vigoux/oak)
  * [vim-conf-live/vimconflive2021-colorscheme](https://github.com/vim-conf-live/vimconflive2021-colorscheme)
  * [vim-scripts/mayansmoke](https://github.com/vim-scripts/mayansmoke)
  * [vim-scripts/peaksea](https://github.com/vim-scripts/peaksea)
  * [wgibbs/vim-irblack](https://github.com/wgibbs/vim-irblack)
  * [whatyouhide/vim-gotham](https://github.com/whatyouhide/vim-gotham)
  * [windwp/wind-colors](https://github.com/windwp/wind-colors)
  * [wittyjudge/gruvbox-material.nvim](https://github.com/wittyjudge/gruvbox-material.nvim)
  * [yagua/nebulous.nvim](https://github.com/yagua/nebulous.nvim)
  * [yashguptaz/calvera-dark.nvim](https://github.com/yashguptaz/calvera-dark.nvim)
  * [yong1le/darkplus.nvim](https://github.com/yong1le/darkplus.nvim)
  * [yonlu/omni.vim](https://github.com/yonlu/omni.vim)
  * [yuttie/hydrangea-vim](https://github.com/yuttie/hydrangea-vim)
## movment
  * [abecodes/tabout.nvim](https://github.com/abecodes/tabout.nvim) : tabbing out from parentheses
  * [arp242/jumpy.vim](https://github.com/arp242/jumpy.vim) : filetype-specific mappings for [[, ]], g[, and g] to jump to the next or previous section
  * [chrisbra/improvedft](https://github.com/chrisbra/improvedft) : makes `f`, `t`, `T`, `F` have the ability to jump multiple lines
  * [dahu/vim-fanfingtastic](https://github.com/dahu/vim-fanfingtastic) : multiline, case insensitive and aliasing for `f`, `t`, `T`, `F`
  * [drybalka/tree-climber.nvim](https://github.com/drybalka/tree-climber.nvim) : easy navigation around the syntax-tree produced by the treesitter that also works in comments and multi-language files [treesitter]
  * [easymotion/vim-easymotion](https://github.com/easymotion/vim-easymotion) : Jump fast to any place to the screen by preesing only up to three keys
  * [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim) : general-purpose motion plugin for Neovim
  * [ggandor/lightspeed.nvim](https://github.com/ggandor/lightspeed.nvim) : Lightspeed is a motion plugin for Neovim, with a relatively small interface and lots of innovative ideas
  * [goldfeld/vim-seek](https://github.com/goldfeld/vim-seek) : like `f` but for two characters
  * [haya14busa/is.vim](https://github.com/haya14busa/is.vim) : incremental search improved
  * [haya14busa/vim-asterisk](https://github.com/haya14busa/vim-asterisk) : provides improved * motions
  * [hrsh7th/vim-insert-point](https://github.com/hrsh7th/vim-insert-point) : cursor move on insert mode
  * [justinmk/vim-sneak](https://github.com/justinmk/vim-sneak) : Jump to any location specified by two characters
  * [mhinz/vim-lookup](https://github.com/mhinz/vim-lookup) : jumps to definitions of variables, functions, and commands as if tags were used, without needing a tags file
  * [phaazon/hop.nvim](https://github.com/phaazon/hop.nvim) : Hop is an EasyMotion-like plugin allowing you to jump anywhere in a document with as few keystrokes as possible
  * [rasukarusan/nvim-select-multi-line](https://github.com/rasukarusan/nvim-select-multi-line) : Yank lines not adjacent
  * [rhysd/clever-f.vim](https://github.com/rhysd/clever-f.vim) : extends f, F, t and T mappings for more convenience. Instead of `;`, `f` is available to repeat
  * [rlane/pounce.nvim](https://github.com/rlane/pounce.nvim) : It's based on incremental fuzzy search.
  * [svermeulen/vim-extended-ft](https://github.com/svermeulen/vim-extended-ft) : multiline, smart case, highlighting and more for `f`, `t`, `T`, `F`
  * [t9md/vim-smalls](https://github.com/t9md/vim-smalls) : Search and jump with easymotion style
  * [t9md/vim-textmanip](https://github.com/t9md/vim-textmanip) : move/duplicate blocks of text
  * [zirrostig/vim-schlepp](https://github.com/zirrostig/vim-schlepp) : allow the movement of lines (or blocks) of text around easily
## yanklist
  * [acksld/nvim-neoclip.lua](https://github.com/acksld/nvim-neoclip.lua)
  * [bfredl/nvim-miniyank](https://github.com/bfredl/nvim-miniyank)
  * [cyansprite/extract](https://github.com/cyansprite/extract)
  * [gbprod/yanky.nvim](https://github.com/gbprod/yanky.nvim)
  * [maxbrunsfeld/vim-yankstack](https://github.com/maxbrunsfeld/vim-yankstack)
  * [shougo/neoyank.vim](https://github.com/shougo/neoyank.vim) : Saves yank history
  * [svermeulen/vim-yoink](https://github.com/svermeulen/vim-yoink)
  * [yazgoo/yank-history](https://github.com/yazgoo/yank-history) : historize vim yanks and allow to search and paste from history based on FZF
## hop
  * [haya14busa/vim-easyoperator-phrase](https://github.com/haya14busa/vim-easyoperator-phrase) : provides a much simpler way to use some operator for phrase than vim-easymotion
  * [mfussenegger/nvim-ts-hint-textobject](https://github.com/mfussenegger/nvim-ts-hint-textobject) : Treesitter hint textobject
  * [osyo-manga/vim-hopping](https://github.com/osyo-manga/vim-hopping) : This is a plugin that incrementally narrows down buffer lines
  * [ripxorip/aerojump.nvim](https://github.com/ripxorip/aerojump.nvim) : Aerojump is a fuzzy-match searcher/jumper for Neovim
  * [s1n7ax/nvim-window-picker](https://github.com/s1n7ax/nvim-window-picker) : This plugins prompts the user to pick a window and returns the window id of the picked window
  * [yuki-yano/fuzzy-motion.vim](https://github.com/yuki-yano/fuzzy-motion.vim) : Jump to fuzzy match word
## textobject
  * [adriaanzon/vim-textobj-blade-directive](https://github.com/adriaanzon/vim-textobj-blade-directive) : textobject for blade directive
  * [adriaanzon/vim-textobj-matchit](https://github.com/adriaanzon/vim-textobj-matchit) : creates text objects from matchit pairs (example: `if???end`)
  * [chaoren/vim-wordmotion](https://github.com/chaoren/vim-wordmotion) : treat uppercase/lowercase words next to each other as different words
  * [coderifous/textobj-word-column.vim](https://github.com/coderifous/textobj-word-column.vim) : makes operating on columns of code conceptually simpler and reduces keystrokes
  * [d4ku/vim-pushover](https://github.com/d4ku/vim-pushover) : provides an interface to easily create mappings to push around text-objects
  * [deathlyfrantic/vim-textobj-blanklines](https://github.com/deathlyfrantic/vim-textobj-blanklines) : provides a text object for groups of empty lines
  * [gcmt/wildfire.vim](https://github.com/gcmt/wildfire.vim) : quickly select the closest text object among a group of candidates
  * [jeetsukumaran/vim-indentwise](https://github.com/jeetsukumaran/vim-indentwise) : provides for motions based on indent depths or levels
  * [julian/vim-textobj-variable-segment](https://github.com/julian/vim-textobj-variable-segment) : providing a single text object for variable segments
  * [kana/vim-textobj-entire](https://github.com/kana/vim-textobj-entire) : Text objects for entire buffers
  * [kana/vim-textobj-indent](https://github.com/kana/vim-textobj-indent) : provide text objects to select a block of lines which are similarly indented to the current line
  * [kana/vim-textobj-line](https://github.com/kana/vim-textobj-line) : select a portion of the current line
  * [kana/vim-textobj-user](https://github.com/kana/vim-textobj-user) : creat your own text objects
  * [michaeljsmith/vim-indent-object](https://github.com/michaeljsmith/vim-indent-object) : adds indentation based text objects
  * [misanthropicbit/vim-numbers](https://github.com/misanthropicbit/vim-numbers) : adds textobject to numbers
  * [nilsboy/vim-textobj-cindent](https://github.com/nilsboy/vim-textobj-cindent) : provides text objects to select a block of lines that have the same or higher indentation as the current line
  * [nvim-treesitter/nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects) : Syntax aware text-objects, select, move, swap, and peek support
  * [reedes/vim-textobj-quote](https://github.com/reedes/vim-textobj-quote) : Extending Vim to better support typographic (???curly???) quote characters
  * [rhysd/vim-textobj-anyblock](https://github.com/rhysd/vim-textobj-anyblock) : make `ib` and `ab` match all parentheses and not just brackets
  * [tkhren/vim-textobj-numeral](https://github.com/tkhren/vim-textobj-numeral) : Text objects for numbers
  * [tweekmonster/braceless.vim](https://github.com/tweekmonster/braceless.vim) : Text objects, folding, and more for Python and other indented languages
  * [wellle/targets.vim](https://github.com/wellle/targets.vim) : adds more bracket baised text objects.
## file-movment
  * [airblade/vim-rooter](https://github.com/airblade/vim-rooter) : go to projects root
  * [notjedi/nvim-rooter.lua](https://github.com/notjedi/nvim-rooter.lua) : change your working directory to the project root
  * [nyngwang/neoroot.lua](https://github.com/nyngwang/neoroot.lua) : toggle between own defined root and cwd of file
  * [theprimeagen/harpoon](https://github.com/theprimeagen/harpoon) : mark files and more
## file
  * [chrsm/impulse.nvim](https://github.com/chrsm/impulse.nvim) : a neovim plugin for viewing Notion.so pages
  * [dokwork/vim-hp](https://github.com/dokwork/vim-hp) : Helps to write a help
  * [donraphaco/neotex](https://github.com/donraphaco/neotex) : compiles latex files asynchronously while edditing [archived]
  * [dpelle/vim-languagetool](https://github.com/dpelle/vim-languagetool) : This plugin integrates the LanguageTool grammar checker into Vim
  * [jghauser/follow-md-links.nvim](https://github.com/jghauser/follow-md-links.nvim) : allows you to follow markdown links by pressing enter when the cursor is positioned on a link
  * [luchermitte/lh-cpp](https://github.com/luchermitte/lh-cpp) : heterogeneous suite of helpers for C and C++ programming
  * [mtth/scratch.vim](https://github.com/mtth/scratch.vim) : Unobtrusive scratch window
  * [mzlogin/vim-markdown-toc](https://github.com/mzlogin/vim-markdown-toc) : generate table of contents for Markdown files
  * [previm/previm](https://github.com/previm/previm) : Vim plugin for preview
  * [reedes/vim-wordy](https://github.com/reedes/vim-wordy) : Uncover usage problems in your writing
  * [rhysd/vim-grammarous](https://github.com/rhysd/vim-grammarous) : a powerful grammar checker for Vim
  * [stevearc/gkeep.nvim](https://github.com/stevearc/gkeep.nvim) : Neovim integration for Google Keep, built using gkeepapi
  * [tobys/pdv](https://github.com/tobys/pdv) : your tool of choice for generating PHP doc blocks
  * [vim-scripts/scratch.vim](https://github.com/vim-scripts/scratch.vim) : create a temporary scratch buffer to store and edit text that will be discarded
  * [weirongxu/plantuml-previewer.vim](https://github.com/weirongxu/plantuml-previewer.vim) : Vim/NeoVim plugin for preview PlantUML
## note
  * [boson-joe/yanp](https://github.com/boson-joe/yanp) : Yes another notetaking plugin which supports recurring topics structure and customisable syntax
  * [dobrovolsky/kb-notes.nvim](https://github.com/dobrovolsky/kb-notes.nvim) : Yet another note management system for neovim
  * [fmoralesc/vim-pad](https://github.com/fmoralesc/vim-pad) : quick notetaking plugin for vim
  * [furkanzmc/zettelkasten.nvim](https://github.com/furkanzmc/zettelkasten.nvim) : Vim philosophy oriented Zettelkasten note taking plugin
  * [goerz/jupytext.vim](https://github.com/goerz/jupytext.vim) : editing Jupyter notebook (ipynb) files through jupytext
  * [jbyuki/nabla.nvim](https://github.com/jbyuki/nabla.nvim) : Take your scentific notes in Neovim
  * [lervag/wiki.vim](https://github.com/lervag/wiki.vim) : This is for writing and maintaining a personal wiki
  * [linden-project/linny.vim](https://github.com/linden-project/linny.vim) : Personal wiki and document database
  * [luk400/vim-jukit](https://github.com/luk400/vim-jukit) : REPL plugin and Jupyter-Notebook alternative for Vim
  * [mickael-menu/zk-nvim](https://github.com/mickael-menu/zk-nvim) : Neovim extension for the zk plain text note-taking assistant
  * [oberblastmeister/neuron.nvim](https://github.com/oberblastmeister/neuron.nvim) : Make neovim the best note taking application with neuron
  * [renerocksai/telekasten.nvim](https://github.com/renerocksai/telekasten.nvim) : A Neovim plugin for working with a text-based, markdown zettelkasten / wiki and mixing it with a journal, based on telescope.nvim
  * [rexagod/samwise.nvim](https://github.com/rexagod/samwise.nvim) : line-wise note-taking plugin for neovim
  * [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki) : VimWiki is a personal wiki for Vim
  * [xolox/vim-notes](https://github.com/xolox/vim-notes) : Easy note taking in Vim
## spell
  * [iamcco/coc-spell-checker](https://github.com/iamcco/coc-spell-checker) : Spelling Checker for vim
  * [inkarkat/vim-spellcheck](https://github.com/inkarkat/vim-spellcheck) : This plugin populates the |quickfix|-list with all spelling errors found in a buffer to give you that overview
  * [kamykn/spelunker.vim](https://github.com/kamykn/spelunker.vim) : improves Vim's spell checking function
  * [reedes/vim-lexical](https://github.com/reedes/vim-lexical) : extend vims spellchecker
## markdown-langueges
  * [axvr/org.vim](https://github.com/axvr/org.vim) : Org mode and Outline mode syntax highlighting for Vim
  * [gabrielelana/vim-markdown](https://github.com/gabrielelana/vim-markdown) : complete environment to create Markdown files with a syntax highlight that doesn't suck
  * [h2ero/vim-markdown-wiki](https://github.com/h2ero/vim-markdown-wiki) : markdown wiki pulgin for vim
  * [jakewvincent/mkdnflow.nvim](https://github.com/jakewvincent/mkdnflow.nvim) : make it easy to navigate and manipulate markdown notebooks
  * [jceb/vim-orgmode](https://github.com/jceb/vim-orgmode) : Text outlining and task management for Vim based on Emacs??? Org-Mode
  * [jghauser/auto-pandoc.nvim](https://github.com/jghauser/auto-pandoc.nvim) : This plugin allows you to easily convert your markdown files using pandoc
  * [ranjithshegde/orgwiki.nvim](https://github.com/ranjithshegde/orgwiki.nvim) : implements a subset of features from the popular vimwiki plugin for org filetype
## preview
  * [davidgranstrom/nvim-markdown-preview](https://github.com/davidgranstrom/nvim-markdown-preview) : Markdown preview in the browser using pandoc and live-server
  * [euclio/vim-markdown-composer](https://github.com/euclio/vim-markdown-composer) : adds asynchronous Markdown preview
  * [frabjous/knap](https://github.com/frabjous/knap) : live preview LaTeX or markdown (or even just HTML)
  * [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim) : Preview markdown on your modern browser with synchronised scrolling and flexible configuration
  * [junegunn/vim-xmark](https://github.com/junegunn/vim-xmark) : Markdown preview on OS X
## todo
  * [arnarg/todotxt.nvim](https://github.com/arnarg/todotxt.nvim) : view and add tasks stored in a todo.txt format
  * [aserebryakov/vim-todo-lists](https://github.com/aserebryakov/vim-todo-lists) : TODO lists management
  * [dhruvasagar/vim-dotoo](https://github.com/dhruvasagar/vim-dotoo) : awesome task manager & clocker inspired by org-mode
  * [folke/todo-comments.nvim](https://github.com/folke/todo-comments.nvim) : highlight and search for todo comments like TODO, HACK, BUG
  * [wsdjeg/vim-todo](https://github.com/wsdjeg/vim-todo) : Better TODO manager plugin for neovim/vim
## gui
  * [akiyosi/goneovim](https://github.com/akiyosi/goneovim) : Neovim GUI written in Go
  * [beeender/glrnvim](https://github.com/beeender/glrnvim) : really fast & stable neovim GUI could be accelated by GPU
  * [daa84/neovim-gtk](https://github.com/daa84/neovim-gtk) : GTK ui for neovim written in rust using gtk-rs bindings, with ligatures support
  * [dzhou121/gonvim](https://github.com/dzhou121/gonvim) : Neovim GUI written in Golang [archived]
  * [equalsraf/neovim-qt](https://github.com/equalsraf/neovim-qt)
  * [kethku/neovide](https://github.com/kethku/neovide) : This is a simple graphical user interface for Neovim
  * [qvacua/vimr](https://github.com/qvacua/vimr) : Neovim GUI for macOS
  * [rmichelsen/nvy](https://github.com/rmichelsen/nvy) : minimal Neovim client for Windows written in C++
  * [rohit-px2/nvui](https://github.com/rohit-px2/nvui) : nvim gui written in cpp
  * [smolck/uivonim](https://github.com/smolck/uivonim) : fork of Veonim, written in Electron with WebGL GPU rendering and multithreading
  * [yatli/fvim](https://github.com/yatli/fvim) : Cross platform Neovim front-end UI, built with F# + Avalonia
## sidebar
  * [lambdalisue/fern.vim](https://github.com/lambdalisue/fern.vim) : is a general purpose asynchronous tree viewer written in pure Vim script
  * [preservim/tagbar](https://github.com/preservim/tagbar) : a class outline viewer for Vim
  * [sidebar-nvim/sidebar.nvim](https://github.com/sidebar-nvim/sidebar.nvim) : A generic and modular lua sidebar inspired by lualine
## other
  * [907th/vim-auto-save](https://github.com/907th/vim-auto-save) : automatically saves changes to disk without having to use `:w` [no maintain]
  * [amopel/vim-log-print](https://github.com/amopel/vim-log-print) : Like a commenter plugin, but for log/print statements
  * [andrewradev/linediff.vim](https://github.com/andrewradev/linediff.vim) : provides a simple command, `:Linediff`,which is used to diff two separate blocks of text
  * [andrewradev/sideways.vim](https://github.com/andrewradev/sideways.vim) : move the item under the cursor left or right
  * [andythigpen/nvim-coverage](https://github.com/andythigpen/nvim-coverage) : Displays coverage information in the sign column or in a pop-up window
  * [antoinemadec/fixcursorhold.nvim](https://github.com/antoinemadec/fixcursorhold.nvim) : fix neovim CursorHold and CursorHoldI AND decouple updatetime from CursorHold and CursorHoldI
  * [anuvyklack/help-vsplit.nvim](https://github.com/anuvyklack/help-vsplit.nvim) : open the help screen smartly
  * [ap/vim-templates](https://github.com/ap/vim-templates) : This is a Vim plugin for providing filetype-dependent templates for new files, using a simple but effective mechanism
  * [arp242/batchy.vim](https://github.com/arp242/batchy.vim) : perform batch operations on files
  * [arthurxavierx/vim-caser](https://github.com/arthurxavierx/vim-caser) : Easily change word casing with motions, text objects or visual mode
  * [askfiy/nvim-picgo](https://github.com/askfiy/nvim-picgo) : a picture uploading tool based on Lua language
  * [axieax/urlview.nvim](https://github.com/axieax/urlview.nvim) : a Neovim plugin which displays links from a variety of contexts
  * [beeender/comrade](https://github.com/beeender/comrade) : Brings JetBrains/IntelliJ IDEs magic to Neovim with minimal setup
  * [bfredl/nvim-ipy](https://github.com/bfredl/nvim-ipy) : Jupyter front-end for Neovim
  * [bkoropoff/bex.nvim](https://github.com/bkoropoff/bex.nvim) : Lua to Ex bridge library
  * [brglng/vim-im-select](https://github.com/brglng/vim-im-select) : Improve Vim/Neovim experience with input methods
  * [brookhong/cscope.vim](https://github.com/brookhong/cscope.vim) : smart cscope helper for vim
  * [cappyzawa/trim.nvim](https://github.com/cappyzawa/trim.nvim) : trailing whitespace and lines
  * [cdelledonne/vim-cmake](https://github.com/cdelledonne/vim-cmake) : building CMake projects inside of vim, with a nice visual feedback
  * [chrisbra/nrrwrgn](https://github.com/chrisbra/nrrwrgn) : focus on a selected region while making the rest inaccessible
  * [chrisbra/unicode.vim](https://github.com/chrisbra/unicode.vim) : handling unicode and digraphs characters
  * [clojure-vim/acid.nvim](https://github.com/clojure-vim/acid.nvim) : clojure development
  * [clojure-vim/jazz.nvim](https://github.com/clojure-vim/jazz.nvim) : Acid + Impromptu = Jazz
  * [cometsong/commentframe.vim](https://github.com/cometsong/commentframe.vim) : generate fancy-looking comments/section dividers with centered titles and append them at the current cursor position
  * [dahu/vimple](https://github.com/dahu/vimple) : provides a few maps and commands to make the casual vimmer???s life a little easier
  * [danymat/neogen](https://github.com/danymat/neogen) : Your Annotation Toolkit
  * [davidgranstrom/osc.nvim](https://github.com/davidgranstrom/osc.nvim) : Open Sound Control (OSC) library for Neovim
  * [davidgranstrom/scnvim](https://github.com/davidgranstrom/scnvim) : Neovim frontend for SuperCollider
  * [derekwyatt/vim-scala](https://github.com/derekwyatt/vim-scala) : This is a "bundle" for Vim that builds off of the initial Scala plugin
  * [dhruvasagar/vim-table-mode](https://github.com/dhruvasagar/vim-table-mode) : awesome automatic table creator & formatter
  * [dosimple/workspace.vim](https://github.com/dosimple/workspace.vim) : make it easier to manage large number of buffers by keeping them grouped separately in workspaces
  * [dpzmick/neovim-hackernews](https://github.com/dpzmick/neovim-hackernews) : Hacker News in neovim
  * [duggiefresh/vim-easydir](https://github.com/duggiefresh/vim-easydir) : simple way to create, edit and save files and directories
  * [echasnovski/mini.nvim](https://github.com/echasnovski/mini.nvim) : Collection of minimal, independent, and fast Lua modules dedicated to improve Neovim experience
  * [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim) : This is an EditorConfig plugin for Vim
  * [ekickx/clipboard-image.nvim](https://github.com/ekickx/clipboard-image.nvim) : copy images and paste url/path
  * [ellisonleao/nvim-plugin-template](https://github.com/ellisonleao/nvim-plugin-template) : A template repository for Neovim plugins
  * [esensar/nvim-dev-container](https://github.com/esensar/nvim-dev-container) : provide functionality similar to VSCode's remote container development plugin
  * [filipdutescu/renamer.nvim](https://github.com/filipdutescu/renamer.nvim) : Visual-Studio-Code-like renaming UI
  * [furkanzmc/options.nvim](https://github.com/furkanzmc/options.nvim) : A small library to create custom options for your plugins or your configuration
  * [gaborvecsei/cryptoprice.nvim](https://github.com/gaborvecsei/cryptoprice.nvim) : There are a million ways to check the price of your favourite coins, let nvim be one of them
  * [glacambre/firenvim](https://github.com/glacambre/firenvim) : Turn your browser?? into a Neovim client
  * [glts/vim-magnum](https://github.com/glts/vim-magnum) : big integer library for Vim plugins written entirely in Vim script
  * [gpanders/editorconfig.nvim](https://github.com/gpanders/editorconfig.nvim) : EditorConfig plugin for Neovim written in (NOT Lua) Fennel
  * [h-hg/fcitx.nvim](https://github.com/h-hg/fcitx.nvim) : switch and restore fcitx state for each buffer
  * [habamax/vim-evalvim](https://github.com/habamax/vim-evalvim) : Run vimscript from anywhere in vim and save output to `*` (clipboard) register
  * [hardenedapple/vsh](https://github.com/hardenedapple/vsh) : Run shell commands in a modifiable buffer
  * [heavenshell/vim-pydocstring](https://github.com/heavenshell/vim-pydocstring) : a generator for Python docstrings and is capable of automatically
  * [hkupty/iron.nvim](https://github.com/hkupty/iron.nvim) : Interactive Repls Over Neovim
  * [groctel/jobsplit.nvim](https://gitlab.com/groctel/jobsplit.nvim) : Open your jobs in an asynchronous horizontal split
  * [huawenyu/vimgdb](https://github.com/huawenyu/vimgdb) : implement GDB front-end for c/c++ gdb base on Neovim + Tmux
  * [hupfdule/refactorvim](https://github.com/hupfdule/refactorvim) : Vim plugin for refactoring vimscript plugins
  * [hyiltiz/vim-plugins-profile](https://github.com/hyiltiz/vim-plugins-profile) : a profiler for your vim plugins
  * [jakergrossman/tagurl.vim](https://github.com/jakergrossman/tagurl.vim) : Copy the URL for a help tag on vimhelp.org or neovim.io to the clipboard
  * [jameshiew/nvim-magic](https://github.com/jameshiew/nvim-magic) : pluggable framework for integrating AI code assistance into Neovim
  * [jbyuki/venn.nvim](https://github.com/jbyuki/venn.nvim) : Draw ASCII diagrams in Neovim
  * [jghauser/kitty-runner.nvim](https://github.com/jghauser/kitty-runner.nvim) : easily send lines from the current buffer to another kitty terminal
  * [jghauser/mkdir.nvim](https://github.com/jghauser/mkdir.nvim) : automatically creates missing directories on saving a file
  * [jmcantrell/vim-virtualenv](https://github.com/jmcantrell/vim-virtualenv) : make it possible to run `:python` with virtual environments
  * [jmcomets/vim-pony](https://github.com/jmcomets/vim-pony) : working with Django projects in Vim
  * [johmsalas/text-case.nvim](https://github.com/johmsalas/text-case.nvim) : An all in one plugin for converting text case in Neovim
  * [julienr/vim-cellmode](https://github.com/julienr/vim-cellmode) : enables MATLAB-style cell mode execution for python scripts in vim, assuming an ipython interpreter running in screen (or tmux)
  * [junegunn/vim-emoji](https://github.com/junegunn/vim-emoji) : Emoji in Vim
  * [junegunn/vim-pseudocl](https://github.com/junegunn/vim-pseudocl) : implements a command-line interface that mimics the native Vim command-line
  * [justinmk/vim-gtfo](https://github.com/justinmk/vim-gtfo) : Opens the file manager or terminal at the directory of the current file
  * [kana/vim-operator-user](https://github.com/kana/vim-operator-user) : Define your own operator easily
  * [kdheepak/panvimdoc](https://github.com/kdheepak/panvimdoc) : Decrease friction when writing documentation for your plugins
  * [kezhenxu94/vim-mysql-plugin](https://github.com/kezhenxu94/vim-mysql-plugin) : A highly customizable MySQL VIM plugin
  * [killthemule/nvimpam](https://github.com/killthemule/nvimpam) : neovim rpc plugin for pamcrash files
  * [kkharji/sqlite.lua](https://github.com/kkharji/sqlite.lua) : SQLite/LuaJIT binding and a highly opinionated wrapper for storing, retrieving, caching, and persisting SQLite databases
  * [klen/nvim-config-local](https://github.com/klen/nvim-config-local) : Secure load local config files
  * [klen/nvim-test](https://github.com/klen/nvim-test) : Test Runner for neovim
  * [kristijanhusak/vim-carbon-now-sh](https://github.com/kristijanhusak/vim-carbon-now-sh) : vim implementation plugin for opening selected content in https://carbon.now.sh
  * [kristijanhusak/vim-dadbod-ui](https://github.com/kristijanhusak/vim-dadbod-ui) : Simple UI for vim-dadbod
  * [lambdalisue/lista.nvim](https://github.com/lambdalisue/lista.nvim) : filter content lines and jump to where you want
  * [lambdalisue/neovim-prompt](https://github.com/lambdalisue/neovim-prompt) : A customizable command-line prompt module for Neovim/Vim
  * [lilydjwg/fcitx.vim](https://github.com/lilydjwg/fcitx.vim) : Keep and restore fcitx state for each buffer separately when leaving/re-entering insert mode or search mode
  * [luchermitte/vimfold4c](https://github.com/luchermitte/vimfold4c) : Reactive vim fold plugin for C & C++
  * [m-demare/attempt.nvim](https://github.com/m-demare/attempt.nvim) : Manage your temporary buffers
  * [m00qek/plugin-template.nvim](https://github.com/m00qek/plugin-template.nvim) : A template to create Neovim plugins written in Lua
  * [macthecadillac/vimdo](https://github.com/macthecadillac/vimdo) : execute external commands asynchronously
  * [marcweber/vim-addon-mw-utils](https://github.com/marcweber/vim-addon-mw-utils) : various utils such as caching interpreted contents of files or advanced glob like things
  * [mcauley-penney/tidy.nvim](https://github.com/mcauley-penney/tidy.nvim) : An autocommand that removes all trailing spaces/empty lines
  * [meznaric/conmenu](https://github.com/meznaric/conmenu) : Powerful but minimal context menu for neovim
  * [mg979/tasks.vim](https://github.com/mg979/tasks.vim) : manage and run global and project-local tasks
  * [mg979/vim-visual-multi](https://github.com/mg979/vim-visual-multi) : create multiple visual regions and edit them (basically multiple cursor)
  * [mhinz/vim-rfc](https://github.com/mhinz/vim-rfc) : lists all existing RFCs and opens the selected one in a new buffer
  * [michaelb/sniprun](https://github.com/michaelb/sniprun) : code runner plugin for neovim written in rust and lua
  * [milisims/nvim-luaref](https://github.com/milisims/nvim-luaref) : This 'plugin' simply adds a reference for builtin lua functions
  * [miversen33/import.nvim](https://github.com/miversen33/import.nvim) : A safe require replacement with niceties
  * [miversen33/netman.nvim](https://github.com/miversen33/netman.nvim) : Network Resource Manager
  * [mordechaihadad/bob](https://github.com/mordechaihadad/bob) : easy way to install and switch versions of nvim
  * [nanotee/luv-vimdocs](https://github.com/nanotee/luv-vimdocs) : The luv docs in vimdoc format
  * [nanotee/nvim-if-lua-compat](https://github.com/nanotee/nvim-if-lua-compat) : An `if_lua` compatibility layer for Neovim
  * [nanotee/zoxide.vim](https://github.com/nanotee/zoxide.vim) : Vim wrapper for zoxide
  * [ncm2/float-preview.nvim](https://github.com/ncm2/float-preview.nvim) : Completion preview window based on neovim's floating window
  * [nkakouros-original/numbers.nvim](https://github.com/nkakouros-original/numbers.nvim) : Disables relative line numbers when they don't make sense, e.g. when entering insert mode
  * [noahfrederick/vim-composer](https://github.com/noahfrederick/vim-composer) : Vim support for Composer PHP projects
  * [noscript/taberian.vim](https://github.com/noscript/taberian.vim) : Clickable tabs per VIM window
  * [notomo/cmdbuf.nvim](https://github.com/notomo/cmdbuf.nvim) : provides command-line window functions by normal buffer and window
  * [ntbbloodbath/cheovim](https://github.com/ntbbloodbath/cheovim) : Neovim configuration switcher written in Lua
  * [ntbbloodbath/nvenv](https://github.com/ntbbloodbath/nvenv) : lightweight and blazing fast Neovim version manager
  * [ntbbloodbath/rest.nvim](https://github.com/ntbbloodbath/rest.nvim) : fast Neovim http client written in Lua
  * [nvim-lua/popup.nvim](https://github.com/nvim-lua/popup.nvim) : An implementation of the Popup API from vim in Neovim
  * [nvim-treesitter/nvim-tree-docs](https://github.com/nvim-treesitter/nvim-tree-docs) : Highly configurable documentation generator using treesitter
  * [nyngwang/neozoom.lua](https://github.com/nyngwang/neozoom.lua) : TL;DR: Using floating window instead of vim-tab to simulate "zoom-in"
  * [paulocesar/neovim-db](https://github.com/paulocesar/neovim-db) : Database plugin for neovim
  * [petobens/poet-v](https://github.com/petobens/poet-v) : detects and activates virtual environments in your python poetry or pipenv project
  * [pianocomposer321/project-templates.nvim](https://github.com/pianocomposer321/project-templates.nvim) : create project templates
  * [pixelneo/vim-python-docstring](https://github.com/pixelneo/vim-python-docstring) : easily create python docstring
  * [pocco81/autosave.nvim](https://github.com/pocco81/autosave.nvim) : saving your work before the world collapses or you type :qa!
  * [prabirshrestha/quickpick.vim](https://github.com/prabirshrestha/quickpick.vim) : A UI for Vim to let the user pick an item from a list similar to CtrlP
  * [prettier/vim-prettier](https://github.com/prettier/vim-prettier) : wrapper for prettier, pre-configured with custom default prettier settings
  * [raghur/vim-ghost](https://github.com/raghur/vim-ghost) : Edit browser textarea content in Vim
  * [ray-x/guihua.lua](https://github.com/ray-x/guihua.lua) : library for nvim plugins
  * [rbong/vim-buffest](https://github.com/rbong/vim-buffest) : Easily edit vim registers/macros and lists as buffers
  * [rbtnn/vim-ambiwidth](https://github.com/rbtnn/vim-ambiwidth) : auto set `'ambiwidth'` (i guess, the doc is in Japanese)
  * [rcarriga/nvim-dap-ui](https://github.com/rcarriga/nvim-dap-ui) : A UI for nvim-dap
  * [rgroli/other.nvim](https://github.com/rgroli/other.nvim) : you can open other/related files for the currently active buffer
  * [rhysd/conflict-marker.vim](https://github.com/rhysd/conflict-marker.vim) : Highlight, jump and resolve conflict markers quickly
  * [rktjmp/fwatch.nvim](https://github.com/rktjmp/fwatch.nvim) : watch files or directories for changes and then run vim commands or lua functions
  * [rktjmp/paperplanes.nvim](https://github.com/rktjmp/paperplanes.nvim) : Post selections or buffers to online paste bins.
  * [rliang/termedit.nvim](https://github.com/rliang/termedit.nvim) : Sets the Neovim host instance as `$EDITOR`
  * [romainl/vim-devdocs](https://github.com/romainl/vim-devdocs) : Look up keywords on https://devdocs.io
  * [roxma/nvim-yarp](https://github.com/roxma/nvim-yarp) : Yet Another Remote Plugin Framework for Neovim
  * [roxma/vim-hug-neovim-rpc](https://github.com/roxma/vim-hug-neovim-rpc) : trying to build a compatibility layer for neovim rpc client working on vim8
  * [rraks/pyro](https://github.com/rraks/pyro) : neovim interface to write simple list manipulating python snippets
  * [rrethy/vim-indexor](https://github.com/rrethy/vim-indexor) : adding indices to a list of items
  * [rrethy/vim-tranquille](https://github.com/rrethy/vim-tranquille) : searching without moving the cursor
  * [saecki/crates.nvim](https://github.com/saecki/crates.nvim) : neovim plugin that helps managing crates.io dependencies
  * [samjwill/nvim-unception](https://github.com/samjwill/nvim-unception) : leverages Neovim's native client-serverfeature to make opening files from within Neovim's terminal emulator without experiencing weird behavior easier and completely automatic
  * [sanhajio/synonyms.vim](https://github.com/sanhajio/synonyms.vim) : allows you to show synonyms in a vim split
  * [severin-lemaignan/vim-minimap](https://github.com/severin-lemaignan/vim-minimap) : a vim minimap
  * [sgur/vim-editorconfig](https://github.com/sgur/vim-editorconfig) : Yet another Vim plugin for EditorConfig
  * [shadmansaleh/irc.nvim](https://github.com/shadmansaleh/irc.nvim) : Irc client for neovim
  * [shohi/neva](https://github.com/shohi/neva) : Neovim version manager [archived]
  * [shougo/neoinclude.vim](https://github.com/shougo/neoinclude.vim) : Include completion framework for neocomplete/deoplete/ncm
  * [shougo/vimproc](https://github.com/shougo/vimproc) : a great asynchronous execution library for Vim
  * [shougo/vimproc.vim](https://github.com/shougo/vimproc.vim) : a great asynchronous execution library for Vim
  * [simonefranza/nvim-conv](https://github.com/simonefranza/nvim-conv) : simple converter that allows you to convert
  * [skywind3000/asyncrun.vim](https://github.com/skywind3000/asyncrun.vim) : async run shell commands in qf window
  * [skywind3000/asynctasks.vim](https://github.com/skywind3000/asynctasks.vim) : modern task system
  * [skywind3000/quickmenu.vim](https://github.com/skywind3000/quickmenu.vim) : open up a `quickmenu` with often used commands
  * [skywind3000/vim-auto-popmenu](https://github.com/skywind3000/vim-auto-popmenu) : automatically open autocomplete menu
  * [skywind3000/vim-dict](https://github.com/skywind3000/vim-dict) : Automatically add dictionary files to current buffer according to the filetype
  * [skywind3000/vim-rt-format](https://github.com/skywind3000/vim-rt-format) : Format current line immediately in INSERT mode as soon as you press ENTER
  * [slashmili/alchemist.vim](https://github.com/slashmili/alchemist.vim) : This plugin uses ElixirSense to give inside information about your elixir project in vim
  * [strboul/urlview.vim](https://github.com/strboul/urlview.vim) : List and open URLs easily
  * [sudormrfbin/cheatsheet.nvim](https://github.com/sudormrfbin/cheatsheet.nvim) : A searchable cheatsheet for neovim
  * [tastyep/structlog.nvim](https://github.com/tastyep/structlog.nvim) : Structured Logging for nvim, using Lua
  * [tenfyzhong/tagbar-makefile.vim](https://github.com/tenfyzhong/tagbar-makefile.vim) : makefile for tagbar [archived]
  * [theprimeagen/refactoring.nvim](https://github.com/theprimeagen/refactoring.nvim) : refactor code
  * [thezeroalpha/vim-visualrun](https://github.com/thezeroalpha/vim-visualrun) : select some lines and run them as a Vim command
  * [thibthib18/mongo-nvim](https://github.com/thibthib18/mongo-nvim) : MongoDB Integration in Neovim
  * [thibthib18/ros-nvim](https://github.com/thibthib18/ros-nvim) : ROS in Neovim
  * [thirtythreeforty/lessspace.vim](https://github.com/thirtythreeforty/lessspace.vim) : strip the trailing whitespace from the file you are editing
  * [timeyyy/orchestra.nvim](https://github.com/timeyyy/orchestra.nvim) : lets you bind sound effects to different actions
  * [tpope/vim-apathy](https://github.com/tpope/vim-apathy) : sets the five path searching options for file types I don't care about enough to bother with creating a proper plugin
  * [tpope/vim-bundler](https://github.com/tpope/vim-bundler) : a lightweight bag of Vim goodies for Bundler
  * [tpope/vim-dadbod](https://github.com/tpope/vim-dadbod) : Vim plugin for interacting with databases
  * [tpope/vim-fireplace](https://github.com/tpope/vim-fireplace) : There's a REPL in Fireplace, but you probably wouldn't have noticed if I hadn't told you
  * [tpope/vim-pathogen](https://github.com/tpope/vim-pathogen) : Manage your `runtimepath` with ease
  * [tpope/vim-scriptease](https://github.com/tpope/vim-scriptease) : a Vim plugin for making Vim plugins
  * [tweekmonster/helpful.vim](https://github.com/tweekmonster/helpful.vim) : A plugin for plugin developers to get the version of Vim and Neovim that introduced or removed features
  * [tweekmonster/startuptime.vim](https://github.com/tweekmonster/startuptime.vim) : breaks down the output of `--startuptime`
  * [tyru/open-browser-github.vim](https://github.com/tyru/open-browser-github.vim) : Opens GitHub URL of current file, etc.
  * [tyru/open-browser-unicode.vim](https://github.com/tyru/open-browser-unicode.vim) : Opens Unicode character information
  * [tyru/open-browser.vim](https://github.com/tyru/open-browser.vim) : Open URI with your favorite browser from your most favorite editor
  * [udayvir-singh/hibiscus.nvim](https://github.com/udayvir-singh/hibiscus.nvim) : Highly opinionated macros to elegantly write your neovim config
  * [udayvir-singh/tangerine.nvim](https://github.com/udayvir-singh/tangerine.nvim) : painless way to add fennel to your config
  * [vim-jp/vital.vim](https://github.com/vim-jp/vital.vim) : A comprehensive Vim utility functions for Vim plugins
  * [vim-scripts/a.vim](https://github.com/vim-scripts/a.vim) : commands to swtich between source files and header files
  * [vim-scripts/cyclecolor](https://github.com/vim-scripts/cyclecolor) : cycle through (almost) all available colorschemes
  * [vim-scripts/taglist.vim](https://github.com/vim-scripts/taglist.vim) : provides an overview of the structure of source code files
  * [voldikss/vim-browser-search](https://github.com/voldikss/vim-browser-search) : perform a quick web search for the text selected
  * [voldikss/vim-translator](https://github.com/voldikss/vim-translator) : tranlate stuff
  * [vuki656/package-info.nvim](https://github.com/vuki656/package-info.nvim) : All the `npm`/`yarn`/`pnpm` commands I don't want to type
  * [vv-vim/vv](https://github.com/vv-vim/vv) : Neovim client for macOS
  * [wakatime/vim-wakatime](https://github.com/wakatime/vim-wakatime) : open source Vim plugin for metrics, insights, and time tracking automatically generated from your programming activity
  * [weilbith/nvim-code-action-menu](https://github.com/weilbith/nvim-code-action-menu) : provides a handy pop-up menu for code actions
  * [wyattjsmith1/weather.nvim](https://github.com/wyattjsmith1/weather.nvim) : A simple plugin to display weather in nvim
  * [xiyaowong/link-visitor.nvim](https://github.com/xiyaowong/link-visitor.nvim) : Let me help you open the links
  * [xolox/vim-lua-ftplugin](https://github.com/xolox/vim-lua-ftplugin) : Lua file type plug-in for Vim
  * [yegappan/mru](https://github.com/yegappan/mru) : provides an easy access to a list of recently opened/edited files
  * [zenbro/mirror.vim](https://github.com/zenbro/mirror.vim) : make it quick to do remote actions for each environment of project you working with
  * [ziontee113/icon-picker.nvim](https://github.com/ziontee113/icon-picker.nvim) : helps you pick ???????????? Font Characters, Symbols ??, Nerd Font Icons ??? & Emojis ???
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
  * [klen/python-mode](https://github.com/klen/python-mode) : a Python IDE for Vim
  * [ldelossa/litee.nvim](https://github.com/ldelossa/litee.nvim) : a library for building "IDE-lite" experiences in Neovim
  * [lunarvim/lunarvim](https://github.com/lunarvim/lunarvim)
  * [ntbbloodbath/doom-nvim](https://github.com/ntbbloodbath/doom-nvim)
  * [nvchad/nvchad](https://github.com/nvchad/nvchad) : neovim config written in lua aiming to provide a base configuration with very beautiful UI and blazing fast startuptime
  * [nvoid-lua/nvoid](https://github.com/nvoid-lua/nvoid)
  * [rafaeldelboni/nvim-fennel-lsp-conjure-as-clojure-ide](https://github.com/rafaeldelboni/nvim-fennel-lsp-conjure-as-clojure-ide) : Basic config to transform your NVIM in a powerful Clojure IDE using fennel, clojure-lsp and conjure
  * [shaeinst/roshnivim](https://github.com/shaeinst/roshnivim)
  * [shaunsingh/nyoom.nvim](https://github.com/shaunsingh/nyoom.nvim)
  * [siduck76/nvchad](https://github.com/siduck76/nvchad)
  * [spacevim/spacevim](https://github.com/spacevim/spacevim)
  * [vi-tality/neovitality](https://github.com/vi-tality/neovitality)
  * [wklken/k-vim](https://github.com/wklken/k-vim) : Just a Better Vim Config. Keep it Simple.
## tag
  * [jsfaint/gen_tags.vim](https://github.com/jsfaint/gen_tags.vim) : Async plugin for Vim to ease the use of ctags/gtags
  * [skywind3000/gutentags_plus](https://github.com/skywind3000/gutentags_plus) : will update gtags database in background automatically
  * [t9md/vim-quickhl](https://github.com/t9md/vim-quickhl) : highlight word and tags
  * [weilbith/nvim-floating-tag-preview](https://github.com/weilbith/nvim-floating-tag-preview) : easily preview tags in a floating window
## remote-colab
  * [floobits/floobits-neovim](https://github.com/floobits/floobits-neovim) : Real-time collaborative editing
  * [fredkschott/covim](https://github.com/fredkschott/covim) : Collaborative Editing for Vim
  * [jbyuki/instant.nvim](https://github.com/jbyuki/instant.nvim) : instant.nvim is a collaborative editing plugin for Neovim written in Lua with no dependencies
## indent
  * [darazaki/indent-o-matic](https://github.com/darazaki/indent-o-matic) : Dumb automatic fast indentation detection for Neovim written in Lua
  * [glepnir/indent-guides.nvim](https://github.com/glepnir/indent-guides.nvim) : async render indent guides
  * [nathanaelkane/vim-indent-guides](https://github.com/nathanaelkane/vim-indent-guides) : visually displaying indent levels in Vim [not maintain]
  * [vim-scripts/fortran.vim](https://github.com/vim-scripts/fortran.vim) : adds additional indentation rules
  * [zsugabubus/crazy8.nvim](https://github.com/zsugabubus/crazy8.nvim) : NeoVim plugin that automagically configures 'tabstop', 'shiftwidth', 'softtabstop' and 'expandtab'
## buffers
  * [asheq/close-buffers.vim](https://github.com/asheq/close-buffers.vim) : quickly close (bdelete) several buffers at once
  * [caenrique/swap-buffers.nvim](https://github.com/caenrique/swap-buffers.nvim) : swap buffers easily between split windows without changing the window layout
  * [codcodog/simplebuffer.vim](https://github.com/codcodog/simplebuffer.vim) : switching and deleting buffers easily
  * [el-iot/buffer-tree](https://github.com/el-iot/buffer-tree) : rendering your buffer-list as an ascii-tree
  * [el-iot/buffer-tree-explorer](https://github.com/el-iot/buffer-tree-explorer) : exploring vim-buffers, rendered as an ascii-tree
  * [elihunter173/dirbuf.nvim](https://github.com/elihunter173/dirbuf.nvim) : directory buffer
  * [famiu/bufdelete.nvim](https://github.com/famiu/bufdelete.nvim) : allow you to delete a buffer without messing up your window layout
  * [ghillb/cybu.nvim](https://github.com/ghillb/cybu.nvim) : notification window, that shows the buffer in focus and its neighbors or list of buffers is ordered by last used
  * [kazhala/close-buffers.nvim](https://github.com/kazhala/close-buffers.nvim) : Lua port of [asheq/close-buffers](https://github.com/asheq/close-buffers) with several feature extensions
  * [kwkarlwang/bufjump.nvim](https://github.com/kwkarlwang/bufjump.nvim) : jump to previous buffer in jump list
  * [kwkarlwang/bufresize.nvim](https://github.com/kwkarlwang/bufresize.nvim) : keep your buffers width and height in proportion when the terminal window is resized
  * [matbme/jabs.nvim](https://github.com/matbme/jabs.nvim) : Just Another Buffer Switcher
  * [nyngwang/neononame.lua](https://github.com/nyngwang/neononame.lua) : Layout preserving buffer deletion in Lua
  * [tklepzig/vim-buffer-navigator](https://github.com/tklepzig/vim-buffer-navigator) : Display buffers as tree in a separate window
## detectindent
  * [ciaranm/detectindent](https://github.com/ciaranm/detectindent) : automatically detecting indent settings
  * [conormcd/matchindent.vim](https://github.com/conormcd/matchindent.vim) : scans through a file when it's opened and attempts to guess which style of indentation is being used
  * [ldx/vim-indentfinder](https://github.com/ldx/vim-indentfinder) : vim plugin for automatically detecting indentation
  * [nmac427/guess-indent.nvim](https://github.com/nmac427/guess-indent.nvim) : Blazing fast indentation style detection for Neovim written in Lua
  * [raimondi/yaifa](https://github.com/raimondi/yaifa) : try to detect the kind of indentation used in your file and set the indenting options to the appropriate values
  * [timakro/vim-yadi](https://github.com/timakro/vim-yadi) : Yet Another Detect Indent
  * [tpope/vim-sleuth](https://github.com/tpope/vim-sleuth) : automatically adjusts `'shiftwidth'` and `'expandtab'` heuristically based on the current file
## asyncrun
  * [ledesmablt/vim-run](https://github.com/ledesmablt/vim-run) : Run, view, and manage UNIX shell commands with ease
## windows
  * [beauwilliams/focus.nvim](https://github.com/beauwilliams/focus.nvim) : Splits/Window Management Enhancements for Neovim
  * [blueyed/vim-diminactive](https://github.com/blueyed/vim-diminactive) : dim inactive windows
  * [declancm/windex.nvim](https://github.com/declancm/windex.nvim) : neovim plugin for cleeean neovim window (and tmux pane) functions
  * [yorickpeterse/nvim-window](https://gitlab.com/yorickpeterse/nvim-window) : quickly switching between windows
  * [luukvbaal/stabilize.nvim](https://github.com/luukvbaal/stabilize.nvim) : stabilize buffer content on window open/close events
  * [mattboehm/vim-accordion](https://github.com/mattboehm/vim-accordion) : set the maximum number of splits you want to see, and shrinks the rest to be one column wide
  * [mrjones2014/smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim) : Smart, directional Neovim split resizing and navigation
  * [sindrets/winshift.nvim](https://github.com/sindrets/winshift.nvim) : Rearrange your windows with ease
  * [smithbm2316/centerpad.nvim](https://github.com/smithbm2316/centerpad.nvim) : Center your single lonely buffer easily
  * [szw/vim-maximizer](https://github.com/szw/vim-maximizer) : Maximizes and restores the current window
  * [t9md/vim-choosewin](https://github.com/t9md/vim-choosewin) : enables you to choose a window interactively
  * [wellle/visual-split.vim](https://github.com/wellle/visual-split.vim) : Vim plugin to control splits with visual selections or text objects
  * [wesq3/vim-windowswap](https://github.com/wesq3/vim-windowswap) : Swap windows without ruining your layout
## folds
  * [anuvyklack/pretty-fold.nvim](https://github.com/anuvyklack/pretty-fold.nvim) : Folded region preview and Framework for easy foldtext customization
  * [jghauser/fold-cycle.nvim](https://github.com/jghauser/fold-cycle.nvim) : allows you to cycle folds open or closed
  * [kaile256/vim-foldpeek](https://github.com/kaile256/vim-foldpeek) : peek at folds
  * [kevinhwang91/nvim-ufo](https://github.com/kevinhwang91/nvim-ufo) : make Neovim's fold look modern and keep high performance
  * [konfekt/fastfold](https://github.com/konfekt/fastfold) : only update folds whene you need to, thous improving speed
  * [lambdalisue/readablefold.vim](https://github.com/lambdalisue/readablefold.vim) : improve `foldtext` for better looks
  * [leafcage/foldcc.vim](https://github.com/leafcage/foldcc.vim) : Provides a function to display the fold text `'foldtext'` in a nice way
  * [pseewald/vim-anyfold](https://github.com/pseewald/vim-anyfold) : Generic folding mechanism and motion based on indentation
  * [tmhedberg/simpylfold](https://github.com/tmhedberg/simpylfold) : simple, correct folding for Python
## mouse
  * [notomo/gesture.nvim](https://github.com/notomo/gesture.nvim) : is a mouse gesture plugin for Neovim
## quickfix
  * [bfrg/vim-qf-preview](https://github.com/bfrg/vim-qf-preview) : For the quickfix and location list window to quickly preview the file with the quickfix item under the cursor in a popup window
  * [gabrielpoca/replacer.nvim](https://github.com/gabrielpoca/replacer.nvim) : makes a quickfix window editable, allowing changes to both the content of a file as well as its path
  * [yorickpeterse/nvim-pqf](https://gitlab.com/yorickpeterse/nvim-pqf) : Pretty Quickfix windows for NeoVim
  * [joshmcguigan/estream](https://github.com/joshmcguigan/estream) : help you unlock the power of the quickfix window without dealing with the pain of Vim's `errorformat`
  * [kevinhwang91/nvim-bqf](https://github.com/kevinhwang91/nvim-bqf) : makes Neovim's quickfix window better
  * [nyngwang/neowell.lua](https://github.com/nyngwang/neowell.lua) : commands for quickfix window
  * [romainl/vim-qf](https://github.com/romainl/vim-qf) : is a growing collection of settings, commands and mappings put together to make working with the location list/window and the quickfix list/window smoother
  * [stefandtw/quickfix-reflector.vim](https://github.com/stefandtw/quickfix-reflector.vim) : edit direcly inside the quickfix window
  * [stevearc/qf_helper.nvim](https://github.com/stevearc/qf_helper.nvim) : A collection of improvements for neovim quickfix
  * [yssl/qfenter](https://github.com/yssl/qfenter) : allows you to open items from Vim's quickfix or location list wherever you wish
## chat
  * [throughnothing/vimchat](https://github.com/throughnothing/vimchat) : do instant messaging from within the vim text editor
  * [vim-chat/vim-chat](https://github.com/vim-chat/vim-chat) : chat in neovim and vim8
  * [wsdjeg/vim-chat](https://github.com/wsdjeg/vim-chat) : The chatting client for vim
## comment
  * [b3nj5m1n/kommentary](https://github.com/b3nj5m1n/kommentary) : Neovim plugin to comment text in and out, written in lua
  * [gennaro-tedesco/nvim-commaround](https://github.com/gennaro-tedesco/nvim-commaround) : toggle comments on and off
  * [glepnir/prodoc.nvim](https://github.com/glepnir/prodoc.nvim) : comment and annotation plugin using coroutine
  * [ludopinelli/comment-box.nvim](https://github.com/ludopinelli/comment-box.nvim) : giving you easy boxes and lines the way you want them to be
  * [numtostr/comment.nvim](https://github.com/numtostr/comment.nvim) : Smart and Powerful commenting plugin for neovim
  * [preservim/nerdcommenter](https://github.com/preservim/nerdcommenter) : Comment functions so powerful???no comment necessary
  * [suy/vim-context-commentstring](https://github.com/suy/vim-context-commentstring) : automatically set the 'commentstring' and 'comments' Vim options in file types which contain more than one syntax
  * [tomtom/tcomment_vim](https://github.com/tomtom/tcomment_vim) : provides easy to use, file-type sensible comments for Vim
  * [tpope/vim-commentary](https://github.com/tpope/vim-commentary) : Comment stuff out
  * [tyru/caw.vim](https://github.com/tyru/caw.vim) : Comment plugin: Operator/Dot-repeatable/300+ filetypes
  * [winston0410/commented.nvim](https://github.com/winston0410/commented.nvim) : A commenting plugin written in Lua that actually works
## key
  * [anuvyklack/nvim-keymap-amend](https://github.com/anuvyklack/nvim-keymap-amend) : amend the exisintg keybinding in Neovim
  * [christoomey/vim-sort-motion](https://github.com/christoomey/vim-sort-motion) : provides the ability to sort in Vim using text objects and motions
  * [christoomey/vim-system-copy](https://github.com/christoomey/vim-system-copy) : copying / pasting text to the os specific clipboard
  * [conradirwin/vim-bracketed-paste](https://github.com/conradirwin/vim-bracketed-paste) : enables transparent pasting (i.e. no more `:set paste!`)
  * [drzel/vim-split-line](https://github.com/drzel/vim-split-line) : easily split lines
  * [egzvor/vimproviser](https://github.com/egzvor/vimproviser) : quick remapping of two of your most convenient keys to actions that are most important for you right now
  * [gbprod/cutlass.nvim](https://github.com/gbprod/cutlass.nvim) : overrides the delete operations to actually just delete and not affect the current yank
  * [gukz/ftft.nvim](https://github.com/gukz/ftft.nvim) : same with as native f|t|F|T but with useful highlights
  * [guns/vim-sexp](https://github.com/guns/vim-sexp) : brings the Vim philosophy of precision editing to S-expressions
  * [gwatcha/reaper-keys](https://github.com/gwatcha/reaper-keys) : an extension for the REAPER DAW, that provides a new action mapping system based on key sequences instead of key chords
  * [hrsh7th/vim-seak](https://github.com/hrsh7th/vim-seak) : enhances the `/` and `?`
  * [hrsh7th/vim-searchx](https://github.com/hrsh7th/vim-searchx) : extend search motions
  * [inkarkat/vim-enhancedjumps](https://github.com/inkarkat/vim-enhancedjumps) : This plugin enhances the built-in `CTRL-I`/`CTRL-O` jump commands
  * [inkarkat/vim-mark](https://github.com/inkarkat/vim-mark) : adds mappings and a :Mark command to highlight several words in different colors simultaneously
  * [ironhouzi/starlite-nvim](https://github.com/ironhouzi/starlite-nvim) : Expedient and simple text highlighting using built in Neovim commands: `*`, `g*`, `#`, `g#`
  * [ironhouzi/vim-stim](https://github.com/ironhouzi/vim-stim) : aims to improve the built in star-command
  * [junegunn/vim-peekaboo](https://github.com/junegunn/vim-peekaboo) : extends `"` and `@` in normal mode and `<CTRL-R>` in insert mode so you can see the contents of the registers
  * [kylechui/nvim-surround](https://github.com/kylechui/nvim-surround) : Surround selections, stylishly
  * [lambdalisue/pinkyless.vim](https://github.com/lambdalisue/pinkyless.vim) : Rest your pinkies by using this plugin
  * [linty-org/key-menu.nvim](https://github.com/linty-org/key-menu.nvim) : which-key like plugin with a different style menu
  * [luchermitte/lh-brackets](https://github.com/luchermitte/lh-brackets) : provides various commands and functions to help design smart and advanced mappings dedicated to text insertion
  * [lyuts/vim-rtags](https://github.com/lyuts/vim-rtags) : Vim bindings for rtags
  * [marklcrns/vim-smartq](https://github.com/marklcrns/vim-smartq) : Master key for quitting vim buffers
  * [matze/vim-move](https://github.com/matze/vim-move) : Vim plugin that moves lines and selections in a more visual manner
  * [michamos/vim-bepo](https://github.com/michamos/vim-bepo) : une prise en charge de la disposition de clavier b??po (translate: integration b??po keyboard layout)
  * [ojroques/vim-oscyank](https://github.com/ojroques/vim-oscyank) : A plugin to copy text to the system clipboard from anywhere using the ANSI OSC52 sequence
  * [rhysd/vim-operator-surround](https://github.com/rhysd/vim-operator-surround) : provides Vim operator mappings to deal with surrounds
  * [ryvnf/readline.vim](https://github.com/ryvnf/readline.vim) : a library used for implementing line editing across many command-line tools
  * [stsewd/gx-extended.vim](https://github.com/stsewd/gx-extended.vim) : Extend `gx` to use it beyond just URLs
  * [takac/vim-hardtime](https://github.com/takac/vim-hardtime) : helps you break that annoying habit vimmers have of scrolling up and down the page using `jjjjj` and `kkkkk`
  * [terryma/vim-expand-region](https://github.com/terryma/vim-expand-region) : allows you to visually select increasingly larger regions of text using the same key combination
  * [thyrum/vim-stabs](https://github.com/thyrum/vim-stabs) : This script allows you to use your normal tab settings for the beginning of the line, and have tabs expanded as spaces anywhere else
  * [tommcdo/vim-express](https://github.com/tommcdo/vim-express) : Define your own operators that apply either a VimL expression or a substitution to any motion or text object
  * [tpope/vim-sexp-mappings-for-regular-people](https://github.com/tpope/vim-sexp-mappings-for-regular-people) : adds better default mappings to [guns/vim-sexp](https://github.com/guns/vim-sexp)
  * [tpope/vim-unimpaired](https://github.com/tpope/vim-unimpaired) : adds complementary pairs of mappings (like `:bnext`/`bprevious`)
  * [triglav/vim-visual-increment](https://github.com/triglav/vim-visual-increment) : adds the ability to do increasing and decreasing  ofnumber or letter sequences on multiple lines via visual mode
  * [ur4ltz/surround.nvim](https://github.com/ur4ltz/surround.nvim) : surround text using sandwich or surround style
  * [waylonwalker/telegraph.nvim](https://github.com/waylonwalker/telegraph.nvim) : provides a way to send command conveniently and bind them to hotkeys
  * [wsdjeg/vim-fetch](https://github.com/wsdjeg/vim-fetch) : process line and column jump specifications in file paths as found in stack traces and similar output
  * [yuttie/comfortable-motion.vim](https://github.com/yuttie/comfortable-motion.vim) : physics-based smooth scrolling
## toggle
  * [andrewradev/switch.vim](https://github.com/andrewradev/switch.vim) : swich segments of text with predefined replacements
  * [rmagatti/alternate-toggler](https://github.com/rmagatti/alternate-toggler) : a very small plugin for toggling alternate "boolean" values
  * [saifulapm/chartoggle.nvim](https://github.com/saifulapm/chartoggle.nvim) : toggle keys end of line
  * [tpope/vim-speeddating](https://github.com/tpope/vim-speeddating) : make it possible to use `<C-a>` to increase dates
  * [zef/vim-cycle](https://github.com/zef/vim-cycle) : toggle between pairs or lists of related words
## aligner
  * [godlygeek/tabular](https://github.com/godlygeek/tabular) : makek aligning text easy while also having complex setups
  * [junegunn/vim-easy-align](https://github.com/junegunn/vim-easy-align) : A simple, easy-to-use Vim alignment plugin
  * [tommcdo/vim-lion](https://github.com/tommcdo/vim-lion) : a tool for aligning text by some character
  * [vim-scripts/align](https://github.com/vim-scripts/align) : align statements on their equal signs, make comment boxes, align comments, align declarations, etc.
## auto-pairs
  * [jiangmiao/auto-pairs](https://github.com/jiangmiao/auto-pairs) : Insert or delete brackets, parens, quotes in pair
  * [kana/vim-smartinput](https://github.com/kana/vim-smartinput) : Provide smart input assistant
  * [raimondi/delimitmate](https://github.com/raimondi/delimitmate) : automatic closing of quotes, parenthesis, brackets, etc
  * [rrethy/nvim-treesitter-endwise](https://github.com/rrethy/nvim-treesitter-endwise) : wisely add "end" in ruby, Lua, Vimscript, etc
  * [rstacruz/vim-closer](https://github.com/rstacruz/vim-closer) : Closes brackets
  * [shougo/neopairs.vim](https://github.com/shougo/neopairs.vim) : Auto insert pairs when complete done
  * [tenfyzhong/completeparameter.vim](https://github.com/tenfyzhong/completeparameter.vim) : complete function's parameters after complete a function
  * [tmsvg/pear-tree](https://github.com/tmsvg/pear-tree) : A painless, powerful Vim auto-pair plugin
  * [townk/vim-autoclose](https://github.com/townk/vim-autoclose) : auto complete parentheses [archived]
  * [vim-scripts/delimitmate.vim](https://github.com/vim-scripts/delimitmate.vim) : automatic closing of quotes, parenthesis, brackets
  * [zsaberlv0/completeparameter_generic.vim](https://github.com/zsaberlv0/completeparameter_generic.vim) : generic verion of CompleteParameter.vim
## fennel
  * [rktjmp/hotpot.nvim](https://github.com/rktjmp/hotpot.nvim) : Seamless Fennel inside Neovim
## language
  * [akinsho/flutter-tools.nvim](https://github.com/akinsho/flutter-tools.nvim) : Build flutter and dart applications in neovim using the native LSP
  * [aonemd/fmt.vim](https://github.com/aonemd/fmt.vim) : delegates the auto-formatting to a formatter
  * [arnaud-lb/vim-php-namespace](https://github.com/arnaud-lb/vim-php-namespace) : a vim plugin for inserting "use" statements automatically
  * [arp242/runbuf.vim](https://github.com/arp242/runbuf.vim) : makes it easy to run the contents of a buffer
  * [b0o/schemastore.nvim](https://github.com/b0o/schemastore.nvim) : Neovim Lua plugin providing access to the SchemaStore catalog
  * [chiel92/vim-autoformat](https://github.com/chiel92/vim-autoformat) : Format code with one button press (or automatically on save).
  * [crusj/hierarchy-tree-go.nvim](https://github.com/crusj/hierarchy-tree-go.nvim) : Hierarchy ui tree for go
  * [crusj/structrue-go.nvim](https://github.com/crusj/structrue-go.nvim) : A more intuitive display of the symbol structure of golang files
  * [dag/vim-fish](https://github.com/dag/vim-fish) : support for editing fish scripts
  * [dahu/asif](https://github.com/dahu/asif) : uns a list of commands against a block of text (a list of lines) in a scratch buffer of a given filetype
  * [devjoe/vim-codequery](https://github.com/devjoe/vim-codequery) : Search source code gracefully, Manage your database easily and Know your code more instantly
  * [ethanjwright/toolwindow.nvim](https://github.com/ethanjwright/toolwindow.nvim) : Easy management of a toolwindow
  * [gleitz/howdoi](https://github.com/gleitz/howdoi) : Instant coding answers via the command line
  * [jaawerth/fennel-nvim](https://github.com/jaawerth/fennel-nvim) : adding native fennel support to nvim by utilizing neovim's native Lua support
  * [jakewvincent/texmagic.nvim](https://github.com/jakewvincent/texmagic.nvim) : TEXMagic is a very simple Neovimplugin that facilitates LaTeX build engine selection via magic comments
  * [jbyuki/carrot.nvim](https://github.com/jbyuki/carrot.nvim) : Markdown evaluator for Neovim Lua code blocks
  * [jeetsukumaran/vim-pythonsense](https://github.com/jeetsukumaran/vim-pythonsense) : provides text objects and motions for Python classes, methods, functions, and doc strings
  * [jpalardy/vim-slime](https://github.com/jpalardy/vim-slime) : type text in a file, send it to a live REPL,
  * [jsborjesson/vim-uppercase-sql](https://github.com/jsborjesson/vim-uppercase-sql) : auto uppercase sql keywords
  * [junegunn/vim-cfr](https://github.com/junegunn/vim-cfr) : Decompile Java class files using CFR
  * [kovisoft/paredit](https://github.com/kovisoft/paredit) : Structured Editing of Lisp S-expressions
  * [max397574/lua-dev.nvim](https://github.com/max397574/lua-dev.nvim) : Dev setup for init.lua and plugin development
  * [mhartington/nvim-typescript](https://github.com/mhartington/nvim-typescript) : nvim language service plugin for typescript
  * [mhinz/vim-crates](https://github.com/mhinz/vim-crates) : When maintaining Rust projects, this plugin helps with updating the dependencies in `Cargo.toml` files
  * [mhinz/vim-mix-format](https://github.com/mhinz/vim-mix-format) : makes it easy to run elixirs `mix format` asynchronously
  * [moll/vim-node](https://github.com/moll/vim-node) : Tools to make Vim superb for developing with Node.js
  * [nfischer/vim-rainbows](https://github.com/nfischer/vim-rainbows) : Vim runtime files for my own language, Rainbows
  * [nvim-treesitter/nvim-treesitter-refactor](https://github.com/nvim-treesitter/nvim-treesitter-refactor) : Refactor modules for nvim-treesitter [treesitter]
  * [olexsmir/gopher.nvim](https://github.com/olexsmir/gopher.nvim) : Minimalistic plugin for Go development in Neovim written in Lua
  * [olical/aniseed](https://github.com/olical/aniseed) : bridges the gap between Fennel and Neovim
  * [pappasam/vim-filetype-formatter](https://github.com/pappasam/vim-filetype-formatter) : simple, cross language Vim code formatter plugin supporting both range and full-file formatting
  * [pkazmier/java_getset.vim](https://github.com/pkazmier/java_getset.vim) : file type plugin for the creation of Java getters and setters
  * [sbdchd/neoformat](https://github.com/sbdchd/neoformat) : vim plugin for formatting code
  * [scalameta/nvim-metals](https://github.com/scalameta/nvim-metals) : provide a better experience while using Metals
  * [sheerun/vim-polyglot](https://github.com/sheerun/vim-polyglot) : A collection of language packs for Vim
  * [shinglyu/vim-codespell](https://github.com/shinglyu/vim-codespell) : checking the spelling for source code
  * [simrat39/rust-tools.nvim](https://github.com/simrat39/rust-tools.nvim) : Extra rust tools for writing applications in neovim using the native lsp
  * [stephpy/vim-php-cs-fixer](https://github.com/stephpy/vim-php-cs-fixer) : will execute the `php-cs-fixercommand` on the directory or file
  * [sukima/xmledit](https://github.com/sukima/xmledit) : a file type plugin to help edit XML
  * [ternjs/tern_for_vim](https://github.com/ternjs/tern_for_vim) : provides Tern-based JavaScript editing support
  * [tpope/vim-endwise](https://github.com/tpope/vim-endwise) : helps to end certain structures automatically, like adding `end` after `if`,`while`... in lua.
  * [tpope/vim-rails](https://github.com/tpope/vim-rails) : Vim plugin for editing Ruby on Rails applications
  * [tpope/vim-salve](https://github.com/tpope/vim-salve) : Static Vim support for Leiningen, Boot, and the Clojure CLI
  * [tweekmonster/impsort.vim](https://github.com/tweekmonster/impsort.vim) : sorting and highlighting Python imports
  * [vim-denops/denops.vim](https://github.com/vim-denops/denops.vim) : An ecosystem of Vim/Neovim which allows developers to write plugins in Deno
  * [vimjas/vim-python-pep8-indent](https://github.com/vimjas/vim-python-pep8-indent) : modifies vim???s indentation behavior to comply with PEP8 and my aesthetic preferences
  * [yioneko/nvim-yati](https://github.com/yioneko/nvim-yati) : Yet another tree-sitter indent plugin for Neovim
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
  * [madskjeldgaard/reaper-nvim](https://github.com/madskjeldgaard/reaper-nvim) : controlling the Reaper DAW
  * [neovim/go-client](https://github.com/neovim/go-client) : Neovim/go-client is a Neovim client and plugin host for Go
  * [racer-rust/vim-racer](https://github.com/racer-rust/vim-racer) : allows vim to use Racer for Rust code completion and navigation
  * [rust-lang/rust.vim](https://github.com/rust-lang/rust.vim) : Vim plugin that provides Rust file detection, syntax highlighting, formatting, Syntastic integration, and more
  * [sakhnik/nvim-gdb](https://github.com/sakhnik/nvim-gdb) : Gdb, LLDB, pdb/pdb++ and BASHDB integration with NeoVim
  * [stsewd/sphinx.nvim](https://github.com/stsewd/sphinx.nvim) : Sphinx integrations for Neovim
  * [svermeulen/nvim-moonmaker](https://github.com/svermeulen/nvim-moonmaker) : adds support for writing moonscript plugins
## lsp
  * [ahmedkhalf/lsp-rooter.nvim](https://github.com/ahmedkhalf/lsp-rooter.nvim) : change the current working directory to the project's root directory[archived]
  * [alexaandru/nvim-lspupdate](https://github.com/alexaandru/nvim-lspupdate) : Updates installed (or auto installs if missing) LSP servers, that are already configured in your init.vim
  * [amrbashir/nvim-docs-view](https://github.com/amrbashir/nvim-docs-view) : neovim plugin to display lsp hover documentation in a side panel
  * [anott03/nvim-lspinstall](https://github.com/anott03/nvim-lspinstall) : the plugin makes it really easy to install language servers for nvims built in lsp
  * [artur-shaik/jc.nvim](https://github.com/artur-shaik/jc.nvim) : jc LSP
  * [autozimu/languageclient-neovim](https://github.com/autozimu/languageclient-neovim) : LSP support
  * [folke/lsp-colors.nvim](https://github.com/folke/lsp-colors.nvim) : Automatically creates missing LSP diagnostics highlight groups for color schemes that don't yet support the Neovim 0.5 builtin lsp client
  * [folke/trouble.nvim](https://github.com/folke/trouble.nvim) : A pretty list for showing diagnostics, references, telescope results, quickfix and location lists to help you solve all the trouble your code is causing
  * [glepnir/lspsaga.nvim](https://github.com/glepnir/lspsaga.nvim) : A light-weight lsp plugin based on neovim's built-in lsp with a highly performant UI
  * [hrsh7th/vim-lamp](https://github.com/hrsh7th/vim-lamp) : Language Server Protocol client for Vim
  * [j-hui/fidget.nvim](https://github.com/j-hui/fidget.nvim) : Standalone UI for nvim-lsp progress
  * [jbyuki/one-small-step-for-vimkind](https://github.com/jbyuki/one-small-step-for-vimkind) : an adapter for the Neovim lua language
  * [jose-elias-alvarez/null-ls.nvim](https://github.com/jose-elias-alvarez/null-ls.nvim) : Use Neovim as a language server to inject LSP diagnostics, code actions, and more via Lua
  * [junnplus/nvim-lsp-setup](https://github.com/junnplus/nvim-lsp-setup) : simple wrapper for nvim-lspconfig and nvim-lsp-installer to easily setup LSP servers
  * [kkharji/lspsaga.nvim](https://github.com/kkharji/lspsaga.nvim) : light-weight lsp plugin based on neovim built-in lsp with highly a performant UI
  * [kosayoda/nvim-lightbulb](https://github.com/kosayoda/nvim-lightbulb) : VSCode bulb for neovim's built-in LSP
  * [liuchengxu/vista.vim](https://github.com/liuchengxu/vista.vim) : View and search LSP symbols, tags
  * [lukas-reineke/lsp-format.nvim](https://github.com/lukas-reineke/lsp-format.nvim) : a wrapper around Neovims native LSP formatting
  * [mfussenegger/nvim-jdtls](https://github.com/mfussenegger/nvim-jdtls) : Extensions for the built-in Language Server Protocol support in Neovim (>= 0.6.0) for eclipse.jdt.ls
  * [nanotee/nvim-lsp-basics](https://github.com/nanotee/nvim-lsp-basics) : The shiny new built-in LSP client
  * [natebosch/vim-lsc](https://github.com/natebosch/vim-lsc) : Adds language-aware tooling to vim by communicating with a language server following the language server protocol
  * [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) : Configs for the Nvim LSP client
  * [nvim-lua/lsp_extensions.nvim](https://github.com/nvim-lua/lsp_extensions.nvim) : various lsp extensions [archived]
  * [onsails/diaglist.nvim](https://github.com/onsails/diaglist.nvim) : Live-updating Neovim LSP diagnostics in quickfix and loclist
  * [onsails/lspkind-nvim](https://github.com/onsails/lspkind-nvim) : tiny plugin adds vscode-like pictograms to neovim built-in lsp
  * [onsails/lspkind.nvim](https://github.com/onsails/lspkind.nvim) : adds vscode-like pictograms to neovim built-in lsp
  * [prabirshrestha/vim-lsp](https://github.com/prabirshrestha/vim-lsp) : Async Language Server Protocol plugin for vim8 and neovim
  * [ray-x/lsp_signature.nvim](https://github.com/ray-x/lsp_signature.nvim) : Show function signature when you type
  * [ray-x/navigator.lua](https://github.com/ray-x/navigator.lua) : lsp navigation and highlighting and more
  * [rishabhrd/nvim-lsputils](https://github.com/rishabhrd/nvim-lsputils) : focuses on making nvim LSP actions highly user friendly
  * [rmagatti/goto-preview](https://github.com/rmagatti/goto-preview) : previewing native LSP's goto definition calls in floating windows
  * [smjonas/inc-rename.nvim](https://github.com/smjonas/inc-rename.nvim) : provides a command for LSP renaming with immediate visual feedback
  * [tamago324/nlsp-settings.nvim](https://github.com/tamago324/nlsp-settings.nvim) : configure Neovim LSP using json/yaml files like coc-settings.json
  * [wbthomason/lsp-status.nvim](https://github.com/wbthomason/lsp-status.nvim) : generating statusline components from the built-in LSP client
  * [weilbith/nvim-lsp-smag](https://github.com/weilbith/nvim-lsp-smag) : allows to seamlessly integrate the language server protocol into NeoVim
  * [williamboman/nvim-lsp-installer](https://github.com/williamboman/nvim-lsp-installer) : allow you to manage LSP servers
## lint
  * [mfussenegger/nvim-lint](https://github.com/mfussenegger/nvim-lint) : An asynchronous linter plugin for Neovim
  * [nvie/vim-flake8](https://github.com/nvie/vim-flake8) : runs the currently open file through Flake8, a static syntax and style checker for Python source code
  * [vim-syntastic/syntastic](https://github.com/vim-syntastic/syntastic) : Syntastic is a syntax checking plugin for Vim [no maintain]
  * [w0rp/ale](https://github.com/w0rp/ale) : ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax checking and semantic errors)
## debug
  * [dbgx/lldb.nvim](https://github.com/dbgx/lldb.nvim) : provides LLDB debugger integration for Neovim [no maintain]
  * [mfussenegger/nvim-dap](https://github.com/mfussenegger/nvim-dap) : Debug Adapter Protocol client implementation for Neovim
  * [pocco81/dap-buddy.nvim](https://github.com/pocco81/dap-buddy.nvim) : Dap Buddy allows you to manage debuggers provided by nvim-dap
  * [puremourning/vimspector](https://github.com/puremourning/vimspector) : The plugin is a capable Vim graphical debugger for multiple languages
  * [sidorares/node-vim-debugger](https://github.com/sidorares/node-vim-debugger) : Node.js debugger client and vim driver
  * [tweekmonster/exception.vim](https://github.com/tweekmonster/exception.vim) : tracing exceptions thrown by VimL scripts
  * [vim-vdebug/vdebug](https://github.com/vim-vdebug/vdebug) : a new, fast, powerful debugger client for Vim
## autocomplete
  * [ackyshake/vimcompletesme](https://github.com/ackyshake/vimcompletesme) : super simple, super minimal, super light-weight tab-completion plugin
  * [ajh17/vimcompletesme](https://github.com/ajh17/vimcompletesme)
  * [github/copilot.vim](https://github.com/github/copilot.vim) : Vim plugin for GitHub Copilot
  * [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp) : A completion engine plugin for neovim written in Lua
  * [hrsh7th/nvim-compe](https://github.com/hrsh7th/nvim-compe) : Auto completion plugin for nvim [archived]
  * [inkarkat/vim-patterncomplete](https://github.com/inkarkat/vim-patterncomplete) : offers completions that either use the last search pattern or query for a regular expression
  * [jimmyhuang454/easycompleteyou](https://github.com/jimmyhuang454/easycompleteyou) : Easily complete you "Keep It Simple, Stupid."
  * [kristijanhusak/vim-dadbod-completion](https://github.com/kristijanhusak/vim-dadbod-completion) : Database auto completion powered by vim-dadbod
  * [lifepillar/vim-mucomplete](https://github.com/lifepillar/vim-mucomplete) : minimalist autocompletion plugin for Vim
  * [maralla/completor.vim](https://github.com/maralla/completor.vim)
  * [mfussenegger/nvim-lsp-compl](https://github.com/mfussenegger/nvim-lsp-compl) : A fast and asynchronous auto-completion plugin for Neovim >= 0.7.0, focused on LSP
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
  * [vigoux/complementree.nvim](https://github.com/vigoux/complementree.nvim)
  * [ycm-core/youcompleteme](https://github.com/ycm-core/youcompleteme)
## test
  * [hkupty/runes.nvim](https://github.com/hkupty/runes.nvim) : Lua test framework for neovim plugins
  * [janko-m/vim-test](https://github.com/janko-m/vim-test) : A Vim wrapper for running tests on different granularities
  * [nvim-neotest/neotest](https://github.com/nvim-neotest/neotest) : A framework for interacting with tests within NeoVim
  * [p00f/cphelper.nvim](https://github.com/p00f/cphelper.nvim) : automating tasks in competitive programming like downloading test cases, compiling and testing
  * [rcarriga/vim-ultest](https://github.com/rcarriga/vim-ultest) : The ultimate testing plugin for NeoVim
  * [thinca/vim-themis](https://github.com/thinca/vim-themis) : testing framework for Vim script
  * [xeluxee/competitest.nvim](https://github.com/xeluxee/competitest.nvim) : a testcase manager and checker
## snippets
  * [dcampos/nvim-snippy](https://github.com/dcampos/nvim-snippy) : A snippets plugin for Neovim 0.5.0+ written in Lua
  * [drmingdrmer/xptemplate](https://github.com/drmingdrmer/xptemplate) : Code snippets engine for Vim, And snippets library
  * [ellisonleao/carbon-now.nvim](https://github.com/ellisonleao/carbon-now.nvim) : Create beautiful code snippets directly from your neovim terminal
  * [garbas/vim-snipmate](https://github.com/garbas/vim-snipmate) : provide support for textual snippets, similar to TextMate or other Vim plugins like UltiSnips
  * [hrsh7th/vim-vsnip](https://github.com/hrsh7th/vim-vsnip) : VSCode(LSP)'s snippet feature in vim
  * [jorengarenar/minisnip](https://github.com/jorengarenar/minisnip) : miniSnipis lightweight and minimal snippet plugin written in Vim Script
  * [l3mon4d3/luasnip](https://github.com/l3mon4d3/luasnip) : snippet engine written in lua
  * [molleweide/luasnip-snippets.nvim](https://github.com/molleweide/luasnip-snippets.nvim) : community driven library of LuaSnipsnipets
  * [norcalli/snippets.nvim](https://github.com/norcalli/snippets.nvim) : snippets nvim
  * [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets) : Snippets collection for a set of different programming languages
  * [shougo/neosnippet-snippets](https://github.com/shougo/neosnippet-snippets) : The standard snippets repository for neosnippet
  * [shougo/neosnippet.vim](https://github.com/shougo/neosnippet.vim) : The Neosnippet plug-In adds snippet support to Vim
  * [sirver/ultisnips](https://github.com/sirver/ultisnips) : is the ultimate solution for snippets
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
  * [acksld/nvim-anywise-reg.lua](https://github.com/acksld/nvim-anywise-reg.lua)
  * [acksld/nvim-pytrize.lua](https://github.com/acksld/nvim-pytrize.lua)
  * [ahmedkhalf/jupyter-nvim](https://github.com/ahmedkhalf/jupyter-nvim)
  * [aklt/plantuml-syntax](https://github.com/aklt/plantuml-syntax)
  * [aldantas/vim-povray](https://github.com/aldantas/vim-povray)
  * [alfredodeza/coveragepy.vim](https://github.com/alfredodeza/coveragepy.vim)
  * [amadeus/vim-convert-color-to](https://github.com/amadeus/vim-convert-color-to)
  * [ameertaweel/todo.nvim](https://github.com/ameertaweel/todo.nvim)
  * [amirrezaask/actions.nvim](https://github.com/amirrezaask/actions.nvim)
  * [andersevenrud/compe-tmux](https://github.com/andersevenrud/compe-tmux)
  * [andweeb/presence.nvim](https://github.com/andweeb/presence.nvim)
  * [anihm136/importmagic.nvim](https://github.com/anihm136/importmagic.nvim)
  * [ap/vim-readdir](https://github.com/ap/vim-readdir)
  * [ap/vim-you-keep-using-that-word](https://github.com/ap/vim-you-keep-using-that-word)
  * [arkav/lualine-lsp-progress](https://github.com/arkav/lualine-lsp-progress)
  * [artempyanykh/marksman](https://github.com/artempyanykh/marksman)
  * [asheq/close-buffers](https://github.com/asheq/close-buffers)
  * [asins/vim-dict](https://github.com/asins/vim-dict)
  * [asvetliakov/vscode-neovim](https://github.com/asvetliakov/vscode-neovim)
  * [babab/vim-magickey](https://github.com/babab/vim-magickey)
  * [beloglazov/vim-online-thesaurus](https://github.com/beloglazov/vim-online-thesaurus)
  * [bkad/camelcasemotion](https://github.com/bkad/camelcasemotion)
  * [bobrown101/git_blame.nvim](https://github.com/bobrown101/git_blame.nvim)
  * [booperlv/cyclecolo.lua](https://github.com/booperlv/cyclecolo.lua)
  * [braxtons12/blame_line.nvim](https://github.com/braxtons12/blame_line.nvim)
  * [brenopacheco/vim-hydra](https://github.com/brenopacheco/vim-hydra)
  * [bronson/vim-trailing-whitespace](https://github.com/bronson/vim-trailing-whitespace)
  * [bronson/vim-visual-star-search](https://github.com/bronson/vim-visual-star-search)
  * [callmekohei/deoplete-fsharp](https://github.com/callmekohei/deoplete-fsharp)
  * [camspiers/lens.vim](https://github.com/camspiers/lens.vim)
  * [chaitanyabsprip/present.nvim](https://github.com/chaitanyabsprip/present.nvim)
  * [chentau/marks.nvim](https://github.com/chentau/marks.nvim)
  * [chfritz/atom-sane-indentation](https://github.com/chfritz/atom-sane-indentation)
  * [chimay/wheel](https://github.com/chimay/wheel)
  * [chrisbra/vim-diff-enhanced](https://github.com/chrisbra/vim-diff-enhanced)
  * [christoomey/vim-conflicted](https://github.com/christoomey/vim-conflicted)
  * [christoomey/vim-tmux-runner](https://github.com/christoomey/vim-tmux-runner)
  * [code-biscuits/nvim-biscuits](https://github.com/code-biscuits/nvim-biscuits)
  * [cohama/agit.vim](https://github.com/cohama/agit.vim)
  * [cohama/lexima.vim](https://github.com/cohama/lexima.vim)
  * [crag666/code_runner.nvim](https://github.com/crag666/code_runner.nvim)
  * [ctrlpvim/ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim)
  * [cuducos/yaml.nvim](https://github.com/cuducos/yaml.nvim)
  * [davidhalter/jedi-vim](https://github.com/davidhalter/jedi-vim)
  * [dccsillag/magma-nvim](https://github.com/dccsillag/magma-nvim)
  * [declancm/cinnamon.nvim](https://github.com/declancm/cinnamon.nvim)
  * [delphinus/auto-cursorline.nvim](https://github.com/delphinus/auto-cursorline.nvim)
  * [dense-analysis/ale](https://github.com/dense-analysis/ale)
  * [deoplete-plugins/deoplete-clang](https://github.com/deoplete-plugins/deoplete-clang)
  * [deoplete-plugins/deoplete-dictionary](https://github.com/deoplete-plugins/deoplete-dictionary)
  * [deoplete-plugins/deoplete-jedi](https://github.com/deoplete-plugins/deoplete-jedi)
  * [deoplete-plugins/deoplete-lsp](https://github.com/deoplete-plugins/deoplete-lsp)
  * [dm1try/git_fastfix](https://github.com/dm1try/git_fastfix)
  * [dm1try/golden_size](https://github.com/dm1try/golden_size)
  * [dradtke/vim-dap](https://github.com/dradtke/vim-dap)
  * [drmikehenry/vim-fixkey](https://github.com/drmikehenry/vim-fixkey)
  * [dstein64/vim-startuptime](https://github.com/dstein64/vim-startuptime)
  * [easonml-editor/vim-reason-plus](https://github.com/easonml-editor/vim-reason-plus)
  * [echuraev/translate-shell.vim](https://github.com/echuraev/translate-shell.vim)
  * [edluffy/hologram.nvim](https://github.com/edluffy/hologram.nvim)
  * [edolphin-ydf/goimpl.nvim](https://github.com/edolphin-ydf/goimpl.nvim)
  * [ellisonleao/glow.nvim](https://github.com/ellisonleao/glow.nvim)
  * [eluum/vim-autopair](https://github.com/eluum/vim-autopair)
  * [erietz/vim-terminator](https://github.com/erietz/vim-terminator)
  * [erryma/vim-expand-region](https://github.com/erryma/vim-expand-region)
  * [ervandew/supertab](https://github.com/ervandew/supertab)
  * [ethanjwright/vs-tasks.nvim](https://github.com/ethanjwright/vs-tasks.nvim)
  * [everduin94/nvim-quick-switcher](https://github.com/everduin94/nvim-quick-switcher)
  * [f-person/git-blame.nvim](https://github.com/f-person/git-blame.nvim)
  * [farmergreg/vim-lastplace](https://github.com/farmergreg/vim-lastplace)
  * [fedepujol/move.nvim](https://github.com/fedepujol/move.nvim)
  * [ferrine/md-img-paste.vim](https://github.com/ferrine/md-img-paste.vim)
  * [fhill2/floating.nvim](https://github.com/fhill2/floating.nvim)
  * [flowtype/vim-flow](https://github.com/flowtype/vim-flow)
  * [fmoralesc/nlanguagetool.nvim](https://github.com/fmoralesc/nlanguagetool.nvim)
  * [folke/lua-dev.nvim](https://github.com/folke/lua-dev.nvim)
  * [folke/persistence.nvim](https://github.com/folke/persistence.nvim)
  * [foosoft/vim-argwrap](https://github.com/foosoft/vim-argwrap)
  * [frazrepo/vim-rainbow](https://github.com/frazrepo/vim-rainbow)
  * [furkanzmc/firvish.nvim](https://github.com/furkanzmc/firvish.nvim)
  * [furkanzmc/sekme.nvim](https://github.com/furkanzmc/sekme.nvim)
  * [gaborvecsei/memento.nvim](https://github.com/gaborvecsei/memento.nvim)
  * [gbprod/phpactor.nvim](https://github.com/gbprod/phpactor.nvim)
  * [gennaro-tedesco/nvim-jqx](https://github.com/gennaro-tedesco/nvim-jqx)
  * [google/vim-jsonnet](https://github.com/google/vim-jsonnet)
  * [google/vim-maktaba](https://github.com/google/vim-maktaba)
  * [groenewege/vim-less](https://github.com/groenewege/vim-less)
  * [gruvbox-community/gruvbox](https://github.com/gruvbox-community/gruvbox)
  * [gu-fan/riv.vim](https://github.com/gu-fan/riv.vim)
  * [haifengkao/insertleftbracket.nvim](https://github.com/haifengkao/insertleftbracket.nvim)
  * [hanschen/vim-ipython-cell](https://github.com/hanschen/vim-ipython-cell)
  * [harrisoncramer/jump-tag](https://github.com/harrisoncramer/jump-tag)
  * [hauleth/usnip.vim](https://github.com/hauleth/usnip.vim)
  * [haya14busa/incsearch-easymotion.vim](https://github.com/haya14busa/incsearch-easymotion.vim)
  * [haya14busa/vim-auto-programming](https://github.com/haya14busa/vim-auto-programming)
  * [haya14busa/vim-easyoperator-line](https://github.com/haya14busa/vim-easyoperator-line)
  * [henriquehbr/nvim-startup.lua](https://github.com/henriquehbr/nvim-startup.lua)
  * [honza/dockerfile.vim](https://github.com/honza/dockerfile.vim)
  * [honza/vim-snippets](https://github.com/honza/vim-snippets)
  * [hood/popui.nvim](https://github.com/hood/popui.nvim)
  * [hoschi/yode-nvim](https://github.com/hoschi/yode-nvim)
  * [hrsh7th/vim-eft](https://github.com/hrsh7th/vim-eft)
  * [hrsh7th/vim-feeling-move](https://github.com/hrsh7th/vim-feeling-move)
  * [hrsh7th/vim-foolish-move](https://github.com/hrsh7th/vim-foolish-move)
  * [idanarye/vim-merginal](https://github.com/idanarye/vim-merginal)
  * [instant-markdown/vim-instant-markdown](https://github.com/instant-markdown/vim-instant-markdown)
  * [ipod825/igit.nvim](https://github.com/ipod825/igit.nvim)
  * [ipod825/vim-netranger](https://github.com/ipod825/vim-netranger)
  * [iron-e/nvim-libmodal](https://github.com/iron-e/nvim-libmodal)
  * [is0n/fm-nvim](https://github.com/is0n/fm-nvim)
  * [is0n/jaq-nvim](https://github.com/is0n/jaq-nvim)
  * [itmecho/bufterm.nvim](https://github.com/itmecho/bufterm.nvim)
  * [ixru/nvim-markdown](https://github.com/ixru/nvim-markdown)
  * [jakemason/ouroboros](https://github.com/jakemason/ouroboros)
  * [jalvesaq/vimcmdline](https://github.com/jalvesaq/vimcmdline)
  * [jamessan/vim-gnupg](https://github.com/jamessan/vim-gnupg)
  * [jdonaldson/vaxe](https://github.com/jdonaldson/vaxe)
  * [jeaye/color_coded](https://github.com/jeaye/color_coded)
  * [jedi2610/nvim-rooter.lua](https://github.com/jedi2610/nvim-rooter.lua)
  * [jedrzejboczar/toggletasks.nvim](https://github.com/jedrzejboczar/toggletasks.nvim)
  * [jenterkin/vim-autosource](https://github.com/jenterkin/vim-autosource)
  * [jodosha/vim-godebug](https://github.com/jodosha/vim-godebug)
  * [jorengarenar/vim-mvvis](https://github.com/jorengarenar/vim-mvvis)
  * [jorengarenar/vim-sbnr](https://github.com/jorengarenar/vim-sbnr)
  * [jorengarenar/vim-sql-upper](https://github.com/jorengarenar/vim-sql-upper)
  * [jose-elias-alvarez/nvim-lsp-ts-utils](https://github.com/jose-elias-alvarez/nvim-lsp-ts-utils)
  * [jrasmusbm/vim-peculiar](https://github.com/jrasmusbm/vim-peculiar)
  * [junegunn/fzf.vim](https://github.com/junegunn/fzf.vim)
  * [junegunn/goyo.vim](https://github.com/junegunn/goyo.vim)
  * [junegunn/vader.vim](https://github.com/junegunn/vader.vim)
  * [junegunn/vim-after-object](https://github.com/junegunn/vim-after-object)
  * [junegunn/vim-carbon-now-sh](https://github.com/junegunn/vim-carbon-now-sh)
  * [junegunn/vim-oblique](https://github.com/junegunn/vim-oblique)
  * [junegunn/vim-plug](https://github.com/junegunn/vim-plug)
  * [junegunn/vim-slash](https://github.com/junegunn/vim-slash)
  * [jupyter-vim/jupyter-vim](https://github.com/jupyter-vim/jupyter-vim)
  * [justinmk/vim-dirvish](https://github.com/justinmk/vim-dirvish)
  * [kalekundert/vim-coiled-snake](https://github.com/kalekundert/vim-coiled-snake)
  * [kchmck/vim-coffee-script](https://github.com/kchmck/vim-coffee-script)
  * [kdav5758/truezen.nvim](https://github.com/kdav5758/truezen.nvim)
  * [kevinhwang91/promise-async](https://github.com/kevinhwang91/promise-async)
  * [kien/ctrlp.vim](https://github.com/kien/ctrlp.vim)
  * [kkoomen/vim-doge](https://github.com/kkoomen/vim-doge)
  * [konfekt/foldtext](https://github.com/konfekt/foldtext)
  * [kristijanhusak/orgmode.nvim](https://github.com/kristijanhusak/orgmode.nvim)
  * [kyazdani42/nvim-web-devicons](https://github.com/kyazdani42/nvim-web-devicons)
  * [lambdalisue/battery.vim](https://github.com/lambdalisue/battery.vim)
  * [lambdalisue/gina.vim](https://github.com/lambdalisue/gina.vim)
  * [lambdalisue/suda.vim](https://github.com/lambdalisue/suda.vim)
  * [ldelossa/calltree.nvim](https://github.com/ldelossa/calltree.nvim)
  * [lervag/vimtex](https://github.com/lervag/vimtex)
  * [lfilho/cosco.vim](https://github.com/lfilho/cosco.vim)
  * [lfv89/vim-interestingwords](https://github.com/lfv89/vim-interestingwords)
  * [lhkipp/nvim-locationist](https://github.com/lhkipp/nvim-locationist)
  * [lighttiger2505/deoplete-vim-lsp](https://github.com/lighttiger2505/deoplete-vim-lsp)
  * [liuchengxu/eleline.vim](https://github.com/liuchengxu/eleline.vim)
  * [loricandre/oneterm](https://github.com/loricandre/oneterm)
  * [ludovicchabant/vim-gutentags](https://github.com/ludovicchabant/vim-gutentags)
  * [lukelbd/vim-tabline](https://github.com/lukelbd/vim-tabline)
  * [lunarvim/colorschemes](https://github.com/lunarvim/colorschemes)
  * [lunarvim/darkplus.nvim](https://github.com/lunarvim/darkplus.nvim)
  * [lunarvim/lualine.nvim](https://github.com/lunarvim/lualine.nvim)
  * [m-demare/hlargs.nvim](https://github.com/m-demare/hlargs.nvim)
  * [machakann/vim-sandwich](https://github.com/machakann/vim-sandwich)
  * [markonm/traces.vim](https://github.com/markonm/traces.vim)
  * [mhartington/formatter.nvim](https://github.com/mhartington/formatter.nvim)
  * [mhinz/vim-sayonara](https://github.com/mhinz/vim-sayonara)
  * [micmine/jumpwire.nvim](https://github.com/micmine/jumpwire.nvim)
  * [mileszs/ack.vim](https://github.com/mileszs/ack.vim)
  * [milisims/tree-sitter-org](https://github.com/milisims/tree-sitter-org)
  * [millermedeiros/vim-esformatter](https://github.com/millermedeiros/vim-esformatter)
  * [mjbrownie/vim-htmldjango_omnicomplete](https://github.com/mjbrownie/vim-htmldjango_omnicomplete)
  * [mjlbach/try.nvim](https://github.com/mjlbach/try.nvim)
  * [mrjones2014/dash.nvim](https://github.com/mrjones2014/dash.nvim)
  * [mxw/vim-jsx](https://github.com/mxw/vim-jsx)
  * [nanotee/sqls.nvim](https://github.com/nanotee/sqls.nvim)
  * [narajaon/onestatus](https://github.com/narajaon/onestatus)
  * [natdm/bswap](https://github.com/natdm/bswap)
  * [nathanalderson/yang.vim](https://github.com/nathanalderson/yang.vim)
  * [nathom/tmux.nvim](https://github.com/nathom/tmux.nvim)
  * [neomake/neomake](https://github.com/neomake/neomake)
  * [noib3/nvim-oxi](https://github.com/noib3/nvim-oxi)
  * [norcalli/nvim_utils](https://github.com/norcalli/nvim_utils)
  * [numtostr/bufonly.nvim](https://github.com/numtostr/bufonly.nvim)
  * [numtostr/fterm.nvim](https://github.com/numtostr/fterm.nvim)
  * [nvim-treesitter/module-template](https://github.com/nvim-treesitter/module-template)
  * [nvim-treesitter/nvim-treesitter-context](https://github.com/nvim-treesitter/nvim-treesitter-context)
  * [oberblastmeister/termwrapper.nvim](https://github.com/oberblastmeister/termwrapper.nvim)
  * [ojroques/nvim-bufbar](https://github.com/ojroques/nvim-bufbar)
  * [ojroques/vim-scrollstatus](https://github.com/ojroques/vim-scrollstatus)
  * [olical/conjure](https://github.com/olical/conjure)
  * [olical/vim-enmasse](https://github.com/olical/vim-enmasse)
  * [orlp/vim-bunlink](https://github.com/orlp/vim-bunlink)
  * [osyo-manga/vim-jplus](https://github.com/osyo-manga/vim-jplus)
  * [osyo-manga/vim-over](https://github.com/osyo-manga/vim-over)
  * [osyo-manga/vim-precious](https://github.com/osyo-manga/vim-precious)
  * [othree/es.next.syntax.vim](https://github.com/othree/es.next.syntax.vim)
  * [othree/html5.vim](https://github.com/othree/html5.vim)
  * [othree/javascript-libraries-syntax.vim](https://github.com/othree/javascript-libraries-syntax.vim)
  * [pangloss/vim-javascript](https://github.com/pangloss/vim-javascript)
  * [pboettch/vim-cmake-syntax](https://github.com/pboettch/vim-cmake-syntax)
  * [pechorin/any-jump.vim](https://github.com/pechorin/any-jump.vim)
  * [peterrincker/vim-argumentative](https://github.com/peterrincker/vim-argumentative)
  * [pgdouyon/vim-accio](https://github.com/pgdouyon/vim-accio)
  * [philrunninger/nerdtree-visual-selection](https://github.com/philrunninger/nerdtree-visual-selection)
  * [pianocomposer321/yabs.nvim](https://github.com/pianocomposer321/yabs.nvim)
  * [pocco81/dapinstall.nvim](https://github.com/pocco81/dapinstall.nvim)
  * [preservim/vim-markdown](https://github.com/preservim/vim-markdown)
  * [preservim/vim-pencil](https://github.com/preservim/vim-pencil)
  * [pwntester/codeql.nvim](https://github.com/pwntester/codeql.nvim)
  * [qpkorr/vim-bufkill](https://github.com/qpkorr/vim-bufkill)
  * [qpkorr/vim-renamer](https://github.com/qpkorr/vim-renamer)
  * [quintik/snip](https://github.com/quintik/snip)
  * [rafaelsq/nvim-goc.lua](https://github.com/rafaelsq/nvim-goc.lua)
  * [rafcamlet/nvim-luapad](https://github.com/rafcamlet/nvim-luapad)
  * [raimondi/vimregstyle](https://github.com/raimondi/vimregstyle)
  * [ray-x/go.nvim](https://github.com/ray-x/go.nvim)
  * [rbtnn/vim-coloredit](https://github.com/rbtnn/vim-coloredit)
  * [rbtnn/vim-gloaded](https://github.com/rbtnn/vim-gloaded)
  * [rbtnn/vim-pkgsync](https://github.com/rbtnn/vim-pkgsync)
  * [rbtnn/vim-textobj-string](https://github.com/rbtnn/vim-textobj-string)
  * [rbtnn/vim-textobj-verbatimstring](https://github.com/rbtnn/vim-textobj-verbatimstring)
  * [rbtnn/vim-textobj-vimfunctionname](https://github.com/rbtnn/vim-textobj-vimfunctionname)
  * [rbtnn/vim-vimscript_indentexpr](https://github.com/rbtnn/vim-vimscript_indentexpr)
  * [rbtnn/vim-vimscript_lasterror](https://github.com/rbtnn/vim-vimscript_lasterror)
  * [rbtnn/vim-vimscript_tagfunc](https://github.com/rbtnn/vim-vimscript_tagfunc)
  * [rbtnn/vim-winsbar](https://github.com/rbtnn/vim-winsbar)
  * [rescript-lang/vim-rescript](https://github.com/rescript-lang/vim-rescript)
  * [rmagatti/session-lens](https://github.com/rmagatti/session-lens)
  * [rockerboo/awesome-neovim](https://github.com/rockerboo/awesome-neovim)
  * [romainl/vim-qlist](https://github.com/romainl/vim-qlist)
  * [romainl/vim-quicklist](https://github.com/romainl/vim-quicklist)
  * [romgrk/nvim-treesitter-context](https://github.com/romgrk/nvim-treesitter-context)
  * [romgrk/searchreplace.vim](https://github.com/romgrk/searchreplace.vim)
  * [ron89/thesaurus_query.vim](https://github.com/ron89/thesaurus_query.vim)
  * [roosta/fzf-folds.vim](https://github.com/roosta/fzf-folds.vim)
  * [roxma/vim-tmux-clipboard](https://github.com/roxma/vim-tmux-clipboard)
  * [rrethy/nvim-align](https://github.com/rrethy/nvim-align)
  * [rrethy/nvim-animator](https://github.com/rrethy/nvim-animator)
  * [rrethy/nvim-carom](https://github.com/rrethy/nvim-carom)
  * [rrethy/nvim-hotline](https://github.com/rrethy/nvim-hotline)
  * [rrethy/nvim-sourcerer](https://github.com/rrethy/nvim-sourcerer)
  * [rrethy/vim-hexokinase](https://github.com/rrethy/vim-hexokinase)
  * [rrethy/vim-impiared](https://github.com/rrethy/vim-impiared)
  * [rrethy/vim-lacklustertab](https://github.com/rrethy/vim-lacklustertab)
  * [rrethy/vim-spotlight](https://github.com/rrethy/vim-spotlight)
  * [ruifm/gitlinker.nvim](https://github.com/ruifm/gitlinker.nvim)
  * [runiq/telescope-trouble.nvim](https://github.com/runiq/telescope-trouble.nvim)
  * [s1n7ax/nvim-comment-frame](https://github.com/s1n7ax/nvim-comment-frame)
  * [s1n7ax/nvim-search-and-replace](https://github.com/s1n7ax/nvim-search-and-replace)
  * [scrooloose/vim-slumlord](https://github.com/scrooloose/vim-slumlord)
  * [shougo/context_filetype.vim](https://github.com/shougo/context_filetype.vim)
  * [shougo/neocomplete.vim](https://github.com/shougo/neocomplete.vim)
  * [shougo/neomru.vim](https://github.com/shougo/neomru.vim)
  * [shougo/tabpagebuffer.vim](https://github.com/shougo/tabpagebuffer.vim)
  * [sickill/vim-pasta](https://github.com/sickill/vim-pasta)
  * [sidofc/mkdx](https://github.com/sidofc/mkdx)
  * [sitiom/nvim-numbertoggle](https://github.com/sitiom/nvim-numbertoggle)
  * [sjl/clam.vim](https://github.com/sjl/clam.vim)
  * [sjl/vitality.vim](https://github.com/sjl/vitality.vim)
  * [slim-template/vim-slim](https://github.com/slim-template/vim-slim)
  * [smjonas/snippet-converter.nvim](https://github.com/smjonas/snippet-converter.nvim)
  * [softinio/scaladex.nvim](https://github.com/softinio/scaladex.nvim)
  * [someone-stole-my-name/yaml-companion.nvim](https://github.com/someone-stole-my-name/yaml-companion.nvim)
  * [spacevim/gtags.vim](https://github.com/spacevim/gtags.vim)
  * [stanangeloff/php.vim](https://github.com/stanangeloff/php.vim)
  * [stevearc/aerial.nvim](https://github.com/stevearc/aerial.nvim)
  * [stevearc/stickybuf.nvim](https://github.com/stevearc/stickybuf.nvim)
  * [sunjon/stylish.nvim](https://github.com/sunjon/stylish.nvim)
  * [svermeulen/vim-easyclip](https://github.com/svermeulen/vim-easyclip)
  * [szw/vim-ctrlspace](https://github.com/szw/vim-ctrlspace)
  * [szymonmaszke/vimpyter](https://github.com/szymonmaszke/vimpyter)
  * [t9md/vim-ruby-xmpfilter](https://github.com/t9md/vim-ruby-xmpfilter)
  * [tamago324/leaderf-neosnippet](https://github.com/tamago324/leaderf-neosnippet)
  * [tamago324/lir.nvim](https://github.com/tamago324/lir.nvim)
  * [tami5/sqlite.lua](https://github.com/tami5/sqlite.lua)
  * [teal-language/vim-teal](https://github.com/teal-language/vim-teal)
  * [tenfyzhong/tagbar-proto.vim](https://github.com/tenfyzhong/tagbar-proto.vim)
  * [terrortylor/nvim-comment](https://github.com/terrortylor/nvim-comment)
  * [thehamsta/module-template](https://github.com/thehamsta/module-template)
  * [themercorp/themer.lua](https://github.com/themercorp/themer.lua)
  * [theprimeagen/git-worktree.nvim](https://github.com/theprimeagen/git-worktree.nvim)
  * [theprimeagen/vim-apm](https://github.com/theprimeagen/vim-apm)
  * [tjdevries/colorbuddy.vim](https://github.com/tjdevries/colorbuddy.vim)
  * [tjdevries/nlua.nvim](https://github.com/tjdevries/nlua.nvim)
  * [tomtom/tlib_vim](https://github.com/tomtom/tlib_vim)
  * [toniz4/vim-stt](https://github.com/toniz4/vim-stt)
  * [tpope/vim-dispatch](https://github.com/tpope/vim-dispatch)
  * [tpope/vim-liquid](https://github.com/tpope/vim-liquid)
  * [tpope/vim-obsession](https://github.com/tpope/vim-obsession)
  * [tpope/vim-rake](https://github.com/tpope/vim-rake)
  * [tpope/vim-tbone](https://github.com/tpope/vim-tbone)
  * [tpope/vim-vinegar](https://github.com/tpope/vim-vinegar)
  * [tracyone/neomake-multiprocess](https://github.com/tracyone/neomake-multiprocess)
  * [troydm/easytree.vim](https://github.com/troydm/easytree.vim)
  * [tveskag/nvim-blame-line](https://github.com/tveskag/nvim-blame-line)
  * [tweekmonster/django-plus.vim](https://github.com/tweekmonster/django-plus.vim)
  * [tweekmonster/gofmt.vim](https://github.com/tweekmonster/gofmt.vim)
  * [tweekmonster/hl-goimport.vim](https://github.com/tweekmonster/hl-goimport.vim)
  * [tyru/capture.vim](https://github.com/tyru/capture.vim)
  * [uga-rosa/translate.nvim](https://github.com/uga-rosa/translate.nvim)
  * [unblevable/quick-scope](https://github.com/unblevable/quick-scope)
  * [untitled-ai/jupyter_ascending](https://github.com/untitled-ai/jupyter_ascending)
  * [uplus/deoplete-solargraph](https://github.com/uplus/deoplete-solargraph)
  * [vhakulinen/gnvim](https://github.com/vhakulinen/gnvim)
  * [vim-pandoc/vim-pandoc](https://github.com/vim-pandoc/vim-pandoc)
  * [vim-scripts/autocomplpop](https://github.com/vim-scripts/autocomplpop)
  * [vim-scripts/grep.vim](https://github.com/vim-scripts/grep.vim)
  * [vim-scripts/improved-paragraph-motion](https://github.com/vim-scripts/improved-paragraph-motion)
  * [vim-scripts/java_getset.vim](https://github.com/vim-scripts/java_getset.vim)
  * [vim-scripts/replacewithregister](https://github.com/vim-scripts/replacewithregister)
  * [vim-scripts/tagbar](https://github.com/vim-scripts/tagbar)
  * [vim-test/vim-test](https://github.com/vim-test/vim-test)
  * [vimpostor/vim-tpipeline](https://github.com/vimpostor/vim-tpipeline)
  * [vonheikemen/searchbox.nvim](https://github.com/vonheikemen/searchbox.nvim)
  * [vonr/align.nvim](https://github.com/vonr/align.nvim)
  * [vundlevim/vundle.vim](https://github.com/vundlevim/vundle.vim)
  * [wbthomason/buildit.nvim](https://github.com/wbthomason/buildit.nvim)
  * [weilbith/nvim-lsp-bacomp](https://github.com/weilbith/nvim-lsp-bacomp)
  * [weirongxu/coc-explorer](https://github.com/weirongxu/coc-explorer)
  * [will133/vim-dirdiff](https://github.com/will133/vim-dirdiff)
  * [wincent/command-t](https://github.com/wincent/command-t)
  * [wincent/pinnacle](https://github.com/wincent/pinnacle)
  * [windwp/nvim-projectconfig](https://github.com/windwp/nvim-projectconfig)
  * [windwp/nvim-spectre](https://github.com/windwp/nvim-spectre)
  * [windwp/nvim-ts-closetag](https://github.com/windwp/nvim-ts-closetag)
  * [winston0410/cmd-parser.nvim](https://github.com/winston0410/cmd-parser.nvim)
  * [wsdjeg/javaunit.vim](https://github.com/wsdjeg/javaunit.vim)
  * [wsdjeg/vim-assembly](https://github.com/wsdjeg/vim-assembly)
  * [wsdjeg/vim-autohotkey](https://github.com/wsdjeg/vim-autohotkey)
  * [xiyaowong/accelerated-jk.nvim](https://github.com/xiyaowong/accelerated-jk.nvim)
  * [xiyaowong/nvim-transparent](https://github.com/xiyaowong/nvim-transparent)
  * [xolox/vim-misc](https://github.com/xolox/vim-misc)
  * [xuyuanp/scrollbar.nvim](https://github.com/xuyuanp/scrollbar.nvim)
  * [yehuohan/popc](https://github.com/yehuohan/popc)
  * [ygm2/rooter.nvim](https://github.com/ygm2/rooter.nvim)
  * [yqlbu/neovim-server](https://github.com/yqlbu/neovim-server)
  * [yuki-yano/zero.nvim](https://github.com/yuki-yano/zero.nvim)
  * [zegervdv/nrpattern.nvim](https://github.com/zegervdv/nrpattern.nvim)

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