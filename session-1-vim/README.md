# An Introduction to Vim

_For a UCLA student who has taken CS 31 and 32._

Based on material from [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/2020/editors/).

## Installing Neovim

We're going to be using a version of Vim called [Neovim](https://neovim.io/). Instructions to install it are [available here](https://github.com/neovim/neovim/wiki/Installing-Neovim).

### Windows

Go to [Neovim 0.4.3](https://github.com/neovim/neovim/releases/tag/v0.4.3). Click on **nvim-win64.zip** to download the file, extract it, and you're done!

> Note: If your computer runs on a 32-bit CPU (this usually applies to fairly old computers), download **nvim-win32.zip** instead.

To start Neovim, go to where you extracted the zip file, open the **bin** directory, and double click on **nvim-qt.exe**.

> Note: If an error message pops up saying that `VCRUNTIME140.dll` is missing, go to [Visual C++ Redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads), download **vc\_redist.x64.exe** (or vc\_redist.x86.exe for 32-bit CPUs) and install it.

### macOS

On macOS, we recommend installing Neovim through the [Homebrew](https://brew.sh/) package manager.

If you don't have Homebrew installed, run

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

To install Neovim, run

```
brew install neovim
```

### Linux

Neovim is available on most Linux distro package managers. The latest version is 0.4.3 (as of writing), but you really just need anything above 0.2.0 for this tutorial. Check the [Neovim install guide](https://github.com/neovim/neovim/wiki/Installing-Neovim#linux) for specific instructions on particular distros.


## A Brief History of Vim

Vim has a long and storied history. It stands for "Vi IMproved", where vi was another text editor. `vi` was in turn based on a text editor called `ex`, which was based on a program called `ed`, which was based on an editor called QED written by Ken Thompson at Bell Labs in 1966. Two Bit History covers the [history of Vim](https://twobithistory.org/2018/08/05/where-vim-came-from.html) more in depth if you're interested!

Vim is one of the most influential editors of all time; almost every other editor ([emacs](https://github.com/emacs-evil/evil), [VS Code](https://github.com/VSCodeVim/Vim), [Sublime Text](https://www.sublimetext.com/docs/3/vintage.html), [Atom](https://github.com/t9md/atom-vim-mode-plus), [IntelliJ](https://github.com/JetBrains/ideavim), etc.) has a Vim mode plugin. In 2019, it was the [5th most popular development environment](https://insights.stackoverflow.com/survey/2019#development-environments-and-tools) of the Stack Overflow community and the most popular terminal based editor.

Neovim is a fairly new addition to the world of Vi-editors. It's a fork of the Vim codebase that aims to improve the configurability and extensibility of Vim. It also provides saner and more beginner-friendly defaults, which is why we'll be using it in this tutorial! Geoff Greer covers a bit more of the motivation behind Neovim in [a blog post](https://geoff.greer.fm/2015/01/15/why-neovim-is-better-than-vim/), if you're interested.


## Ideas of vim

### Telling your editor what to do

Vim can be used entirely through a keyboard – a fairly radical approach from most GUI applications we're familiar with. This leads to a large learning curve at first, but promises increased efficiency, especially for common tasks.

### Modes of Editing

Vim is a modal text editor: as the name implies, Vim is in different modes when inserting/editing/selecting text.

The most common modes of Vim are:

- Normal: for moving around a file and making edits
- Insert: for inserting text
- Visual (plain, line, or block) mode: for selecting blocks of text

Keys have different meanings in different modes. For example, the `x` in insert mode will just insert a literal character 'x', but in normal mode, it will delete the character under the cursor, and in visual mode, it will delete the selection.

Vim shows the mode it is in in the bottom left corner of the screen. By default, it is in normal mode.

### Hackability

Vim is one of the most customizable text editors available. There's an entire [scripting language](https://en.wikipedia.org/wiki/Vim_(text_editor)#Vim_script) used to configure settings! There's also a very large plugin community that extends Vim capabilities in various ways.

## Basic Text Manipulation

### Inserting Text

Press `i` to enter insert mode. Now try typing some text! Press `<ESC>` to leave insert mode and go back into normal mode.

### Command Line

Command mode can be entered by typing `:` in normal mode. Your cursor will jump to the command line at the bottom of the screen upon pressing :. This mode has many functionalities, including opening, saving, and closing files, and quitting Vim.

Some common commands are:

- `:q` quit (close window)
- `:w` save ("write")
- `:wq` save and quit
- `:e {name of file}` open file for editing
- `:help {topic}` open help
  - e.g., `:help :w` opens help for the :w command
  - e.g., `:help w` opens help for the w movement

### Moving Around

You should spend most of your time in normal mode, using movement commands to navigate the buffer. Movements in Vim are also called "nouns", because they refer to chunks of text.

Some common commands are:

- Basic movement: `hjkl` (left, down, up, right)
- Words: `w` (next word), `b` (beginning of word), `e` (end of word)
- Lines: `0` (beginning of line), `^` (first non-blank character), `$` (end of line)
- Screen: `H` (top of screen), `M` (middle of screen), `L` (bottom of screen)
- Scroll: `Ctrl-u` (up), `Ctrl-d` (down)
- File: `gg` (beginning of file), `G` (end of file)
- Line numbers: `{number}G` (line {number})
- Misc: `%` (corresponding item)
- Find: `f{character}`, `t{character}`, `F{character}`, `T{character}`
    - find/to forward/backward {character} on the current line
    - `,` / `;` for navigating matches


### Selecting Text

You can select text in Visual Mode, which you enter by pressing `v`. From there, you can move the selection using the above nouns. 

You can also select lines of text in Visual Line mode, which is entered with `V`.

### Editing Text

Everything that you used to do with the mouse, you now do with the keyboard
using editing commands that compose with movement commands. Here's where Vim's
interface starts to look like a programming language. Vim's editing commands
are also called "verbs", because verbs act on nouns.

- `i` enter insert mode
    - but for manipulating/deleting text, want to use something more than
    backspace
- `o` / `O` insert line below / above
- `d{motion}` delete {motion}
    - e.g. `dw` is delete word, `d$` is delete to end of line, `d0` is delete
    to beginning of line
- `c{motion}` change {motion}
    - e.g. `cw` is change word
    - like `d{motion}` followed by `i`
- `x` delete character (equal do `dl`)
- `s` substitute character (equal to `xi`)
- visual mode + manipulation
    - select text, `d` to delete it or `c` to change it
- `u` to undo, `<C-r>` to redo
- `y` to copy / "yank" (some other commands like `d` also copy)
- `p` to paste

### Counts

You can combine nouns and verbs with a count, which will perform a given action
a number of times.

- `3w` move 3 words forward
- `5j` move 5 lines down
- `7dw` delete 7 words

You can start to see that this is where the real power of Vim emerges, as you can compose simple actions (e.g., "delete") into fully formed sentences (e.g., "delete these 5 words").

### Text Objects

Vim has a series of commands that can be used after a verb or in Visual Mode to select a sequence of text. These commands are called "text objects" because they describe objects of text. All text objects start with `i` or `a`, which mean "inner" or "around" respectively.

- `daw` delete a word, including whitespace
- `dap` delete a paragraph, including whitespace
- `ci(` change the contents inside the current pair of parentheses
- `ci[` change the contents inside the current pair of square brackets
- `da'` delete a single-quoted string, including the surrounding single quotes

### Find and Replace

In Vim, search is done by pressing `/` in Normal Mode. Vim searches using [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression), which we won't cover too much in this workshop, but will go more in depth in a future Hack workshop. If you're curious, here's a [good reference](https://learnbyexample.gitbooks.io/vim-reference/content/Regular_Expressions.html) for regular expressions in Vim.

- Search: `/{regex}`, `n` / `N` for navigating matches

Vim can do replacements in a file by typing `:s/old phrase/new phrase/g`. Note that it uses regular expressions here as well. The `g` at the end tells Vim to replace all instances of the phrase, not just the first on each line.

## A note on CTRL and ESC

vi was originally developed on a ADM-3A computer, which had the following layout.

Note that the Ctrl key is where the caps lock key usually is and the Escape key is right above it! Typing esc or ctrl was much more ergonomic back in the good ol' vi days than it is now. Because of this, many people remap either esc or ctrl to their caps lock key. We recommend you play around with this.

https://stevelosh.com/blog/2012/10/a-modern-space-cadet/#s13-control-escape

## vimtutor

The de facto introduction to vim is via an interactive tutorial called vimtutor. You can access it by opening Neovim:

```
nvim
```

then typing: `:Tutor`. Let's try it out!

## Advanced Features

We won't be covering these in the demo, but they're cool features to play around with as you get more comfortable with Vim!

### Window and Tab Management

Vim maintains a set of open files, called "buffers". A Vim session has a number of tabs, each of which has a number of windows (split panes). Each window shows a single buffer. Unlike other programs you are familiar with, like web browsers, there is not a 1-to-1 correspondence between buffers and windows; windows are merely views. A given buffer may be open in multiple windows, even within the same tab. This can be quite handy, for example, to view two different parts of a file at the same time.

By default, Vim opens with a single tab, which contains a single window.

`:h windows` is the reference to read more on this.

### Macros

Macros are a way to repeat common keystrokes efficiently. They're hard to describe, so you should check out [this video](http://vimcasts.org/episodes/converting-haml-to-erb-with-vim-macros/) demonstrating their power. `:h q` to find out more about macros.

### Marks

Ever wanted to switch efficiently between two sections of code you're working on? Marks are the answer! Type `m[letter]` to set a mark and `'[letter]` to jump to that mark. Check out `:h m` and `:h '` for details.

## Where to go after vimtutor

- [The language of vim](https://stackoverflow.com/a/1220118): How to grok vim.
- [Seven habits of effective text editing](https://www.moolenaar.net/habits.html): An essay by Bram Moolenaar, the creator of Vim.
- `:h`, the Vim documentation. (Online Link)
- [Vimcasts](http://vimcasts.org/): Video tutorials on Vim tricks.
- [Vimgolf](http://www.vimgolf.com/): Challenges focused on minimizing keystrokes.
- [Learn Vimscript the Hard Way](https://learnvimscriptthehardway.stevelosh.com/): A book on Vimscript.
- [Vim Koans](https://sanctum.geek.nz/arabesque/vim-koans/): Zen stories about Vim.

### Plugins

Vim is one of the most configurable editors available and has a huge ecosystem of plugins. In general, especially when you're just starting out with Vim, we recommend avoiding most plugins that make Vim more similar to editors like VS Code or Emacs. However, there are some plugins that are essential to extending Vim's functionality or building upon the core ideas of Vim. Drew Neil covers the philosophy of various plugins more in his excellent blog post, [On sharpening the saw](http://vimcasts.org/blog/2012/08/on-sharpening-the-saw/).

[VimAwesome](https://vimawesome.com/) is a great list of plugins. We'd also be remiss if we didn't mention [Tim Pope](https://github.com/tpope), a prolific Vim plugin developer who has created some of the most popular and polished plugins for Vim. Below are some of our favorites to get started.

- [minpac](https://github.com/k-takata/minpac): A modern package manager.
- [ALE](https://github.com/dense-analysis/ale): Linter/formatter integration for Vim.
- [FZF](https://github.com/junegunn/fzf): A fuzzy finder for opening files.
- [vim-commentary](https://github.com/tpope/vim-commentary): Easily comment stuff out.
- [vim-surround](https://github.com/tpope/vim-surround): Easily quote/parenthesize.
- [vim-gitgutter](https://github.com/airblade/vim-gitgutter): Git diff lines in vim.
- [NERDTree](https://github.com/preservim/nerdtree): A file system explorer for Vim.
- [vim-airline](https://github.com/vim-airline/vim-airline): Fancy status lines.
