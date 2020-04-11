# Hack Sprint Session 1: Basics of Kotlin
**Date**: April 16, 2020  
**Location**: Zoom Meeting  
**Teacher**: Timothy Rediehs

## Resources
**Slides**
* []() -- TODO

**ACM Membership Attendance Portal**
* [Portal](http://members.uclaacm.com/login)

**Other useful resources** 

[The Missing Semester of Your CS Education: Git](https://missing.csail.mit.edu/2020/version-control/#snapshots)

[Pro Git](https://git-scm.com/book/en/v2)

Type `man gittutorial` into your command line, then <key>ENTER</key>.

---
## About Version Control
## Terms You'll Learn
* **Version Control**
* **Repository**
* **Commit**
* **Branch**
* **Merge**
* **Merge Conflict**
* **Fetch**
* **Pull**

## What is Git?
In short, Git lets you and your team take "snapshots" of your code at each step of development. These "snapshots" are represented as **commits** which contain the who, what, and when of your changes. We create a sort of "timeline" of your project that looks like this:

<img src='assets/bare_graph.png' width=500>

Each circle is a commit. Each arrow points from a commit to the commit it came from (called it's **parent**). In our "timeline" which we'll call a **graph** from now on, we know a few things:

1. There are no loops/cycles in the graph if you follow the arrows
2. Commits can point to one or more other commits.

We call this setup a **Directed Acyclic Graph**.

## Why Use Version Control
### Keeping A History of Your Code
One of the many nice things about version control is that it helps you keep track of how your code has changed. This is very useful, because it allows you to:

1. Find out **what** change was made in a file
   1. This is useful for bug hunting
2. Find out **who** wrote a section of code
3. Find out **when** a change was made
4. Revert unwanted changes
5. Feel secure against accidentally deleting your work
   1. No more commenting out code just to "keep it around just in case"

### Collaborate with Others Concurrently
Nowadays, we usually code in teams. Without version control, this becomes very difficult. If two people made changes, those changes would have to be manually combined. This would be an error prone disaster. Heaven forbid they modify the same file.

## Basic Git Operations
### git init
### git add
<img src='assets/git_add.png'>

### git commit
<img src='assets/git_commit.png'>

## Branching and Merging
### git branch \<name\>
<img src='assets/git_branch.png'>

### git checkout \<branch_name\>
<img src='assets/git_checkout.png'>

### git merge \<revision\>
<img src='assets/git_merge.png'>

### git rebase
<img src='assets/git_rebase.png'>

## View Status
### git status
### git branch
### git log
### git diff
### git show

## Undo
## git commit --amend
## git reset head \<file\>
## git checkout -- \<file\>

---
## Using Git
## Starting Up
### Installing Git
TODO  
TODO  
TODO
### Creating a New Repository
Let's create a folder for our repository and then move inside it:

```
mkdir project
cd project
```

then, inside the folder, we can use the following command:

```
git init
```

`git init` – This command will create all of the data that git uses to keep track of your project. We call this a **repository**.

You should see the following in after executing `git init`:

```
Initialized empty Git repository in .git/
```

Congratulations, you're done with setup.

### Cloning an Existing Repository
Often times, we'll want to create a copy of an existing repository. You can do so with the following command:

`git clone <repository>`: This command copies a repository indicated by the `<repository>`. `<repository>` can be a path to a local folder, or even a url that points to a repository (on github for instance)!

If you want to clone a repository from git hub, you can get the URL here:

PICTURE OF GITHUB

and then use the clone command like this example (make sure to be in the directory that you want the project's folder to be inside of): 
```
git clone https://github.com/uclaacm/hack-tooling-series.git
```

## Making a First Commit
### Create a New File
Right now we have a empty repository
```
.

0 directories, 0 files
```
Let's create a new file in our project called `math.py` put the following text in it using your favorite text editor:

```python
# math.py
def add(x, y):
    return x + y
```

Our project now looks like this:
```
.
└── math.py

0 directories, 1 file
```
We are ready to add this file to our repository!

### Staging Changes
We have made a change to our project. The next step is to tell Git **which changes we want to commit**. Well... what is there? Let's try finding out by using this command:
```
git status
```
We get back:
```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	math.py

nothing added to commit but untracked files present (use "git add" to track)
```
Wow! Isn't Git so helpful? It tells us: `use "git add <file>..." to include in what will be committed`. Let's do that:
```
git add math.py
```
Now `git status` will show:
```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   math.py
```

We have set our change to be committed! Mission Accomplished.

### Committing Changes
Now, let's actually commit our staged changes:
```
git commit
```
`git commit`: this will create a **commit** with all of your **staged** changes

Git will open up a command line text editor (probably Vim) for a **commit message**. These are descriptions of the changes you made. It's Vim... so:
1. Press 'i' for insert mode
2. Type message: Adds math file
3. Press ESC, then ':wq', then ENTER to quit Vim

You should see something like this after:
```
[master (root-commit) aeb900e] Adds math file
 1 file changed, 3 insertions(+)
 create mode 100644 math.py
```
We can use check on our progress with the following:
```
git log
```
to see our one commit:
```
commit aeb900e29558464ea38f4003daeae8cc797e9b70 (HEAD -> master)
Author: Emrakul Eldrazi <eeldrazi@g.ucla.edu>
Date:   Wed Apr 8 23:20:53 2020 -0700

    Adds math file
```
Our graph looks like this... very boring:

<img src='assets/boring_graph.png' width=500>
