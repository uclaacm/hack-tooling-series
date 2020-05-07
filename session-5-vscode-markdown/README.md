# Hack Tooling Series - VS Code and Markdown

**Date**: May 7, 2020\
**Location**: Zoom\
**Teachers**: Kristie Lim owo

## Resources

**Slides**

- [Slides](https://tinyurl.com/tooling-5)

**ACM Membership Attendance Portal**

- [Portal](https://members.uclaacm.com/login)

**Resources**

- [VS Code](https://code.visualstudio.com/download)
- [VS Code Themes](https://vscodethemes.com/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Table of Contents

- <a href="#markdown">Introduction to Markdown</a>
- <a href="#vscode">VS Code Tips and Extensions</a>

## <div id="markdown">Introduction to Markdown</div>

Markdown is a markup language designed to be readable. A markup language is just text that is annotated with different kinds of formatting, for example marking certain text in italics. It's common to see software projects come with a README, which usually describes the project and how to run it. At ACM Hack, we use Markdown to write notes for our workshops! You can also use variations of Markdown in Slack and Facebook Messenger:
<img src="images/slack.png" alt="Slack">
<img src="images/messenger.png" alt="Messenger">

Markdown syntax is converted to HTML by a Markdown processor which can then be viewed in a browser for nice formatting. Viewing the Markdown file in Github also automatically shows with formatting and VS Code can show a preview as well.
<img src="images/wikipedia.png" alt="Side by side of markdown syntax, HTML, and final view">

Let's write some Markdown! Create a new file on VS Code (File > New File or Ctrl/Cmd N). Then save it as a `.md` file. To view the preview, press Ctrl/Cmd Shift-P to open the command palette. Then search "Markdown: Open Preview to the Side" and hit enter.

Check out [Adam Pritchard's Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for everything that we'll be going over.

A few things that we were not mentioned in the cheatsheet:

### New lines

Paragraphs can be separated by two new lines.

If you want to have a new line but in the same paragraph, you have to end the line with either a backslash or two spaces.

```md
This will show
up on the same line

This will show \
up on two separate lines

This will show (two spaces to the right)  
up on two separate lines
```

This will show
up on the same line

This will show \
up on two separate lines

This will show (there are two spaces to the right)  
up on two separate lines

### img tags

I prefer using an HTML img tag instead of the Markdown style images since you have better control over the size of the image.

```
<img src="https://d.newsweek.com/en/full/1571628/baby-yoda.png" height="10">
```

<img src="https://d.newsweek.com/en/full/1571628/baby-yoda.png" alt="smol baby yoda" height="50">

## <div id="vscode">VS Code Tips and Extensions</div>

### Built-in Terminal

VS Code has a built-in terminal so you don't have to switch between your text editor and a terminal! To open the terminal, select "Terminal" > "New Terminal" from the top tab. Alternatively, use the shortcut Ctrl `\
The backtick is located above tab.

### Git Integration

Remember how last week we learned how to add, commit, and push files using git? VS Code also has tools to help you manage git projects. Click the source control tab on the left toolbar (looks like three dots connected by squiggles) in a git project.If you click on a file, you can see all the unstaged changes you've made. It's kind of like `git status` and `git diff` but a lot prettier. Note that this is not VS Code magic. VS Code just takes the information from git and presents it in a nice way.

<img src="images/unstaged.png" alt="VS Code unstaged changes">

I like to review all the changes I've made before committing. Once you know which changes you'd like to commit, you can click the plus sign on the file to stage the changes, either by individual file or altogether. This is the same as `git add`.

Lastly you can write a commit message and hit Ctrl/Cmd Enter to commit the changes.

VS Code also really helps when dealing with merge conflicts. Let's say there was a change that was pushed to Github dealing with a line that I have also changed on my local computer but have not pushed.

### Extensions
