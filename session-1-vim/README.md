# An Introduction to Vim

_For a UCLA student who has taken CS 31 and 32._

Based on material from [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/2020/editors/)

## Installing vim

We're going to be using a version of vim called [Neovim](https://neovim.io/). Instructions to install it are [available here](https://github.com/neovim/neovim/wiki/Installing-Neovim). In general, we recommend using Chocolatey if you're on Windows, Homebrew if you're on macOS, and your default package manager if you're on Linux.

## A Brief History of Vim

Vim has a long and storied history. It stands for "Vi IMproved", where vi was another text editor. `vi` was in turn based on a text editor called `ex`, which was based on a program called `ed`, which was based on an editor called QED written by Ken Thompson at Bell Labs in 1966.

Two Bit History covers the [history of Vim](https://twobithistory.org/2018/08/05/where-vim-came-from.html) more in depth if you're interested!

## Ideas of vim

### Telling your editor what to do

Vim can be used entirely through a keyboard – a fairly radical approach from most GUI applications we're familiar with. This leads to a large learning curve at first, but promises increased efficiency, especially for common tasks.

### Modes of Editing

Vim is a modal text editor: as the name implies, Vim is in different modes when inserting/editing/selecting text.

The most common modes of Vim are:

- Normal: for moving around a file and making edits
- Insert: for inserting text
- Visual (plain, line, or block) mode: for selecting blocks of text

Keys have different meanings in different modes. For example, the `x` in insert mode will just insert a literal character ‘x’, but in normal mode, it will delete the character under the cursor, and in visual mode, it will delete the selection.

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
- `:w` save (“write”)
- `:wq` save and quit
- `:e {name of file}` open file for editing
- `:help {topic}` open help
  - e.g., `:help :w` opens help for the :w command
  - e.g., `:help w` opens help for the w movement

### Moving Around

You should spend most of your time in normal mode, using movement commands to navigate the buffer. Movements in Vim are also called “nouns”, because they refer to chunks of text.


### Selecting Text

### Editing Text

### Counts

### Text Objects

### Find and Replace

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

### Window and Tab Management

### Macros

### Marks

## Where to go after vimtutor

- https://www.moolenaar.net/habits.html
- :h
- http://vimcasts.org/
- https://sanctum.geek.nz/arabesque/vim-koans/
- https://learnvimscriptthehardway.stevelosh.com/

### Plugins

[VimAwesome](https://vimawesome.com/) is a great list of plugins.

- minpac
- ALE
- FZF
- vim-commentary
- vim-surround
- vim-fugitive
- NERDTree
- vim-gitgutter
- vim-airline







