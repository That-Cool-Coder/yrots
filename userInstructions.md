# Yrots user instructions

[Back to README](README.md)

This is a combination of tutorial and user reference to using yrots. If you are new to the language, it is recommended to work through this document in the order it is written.

## Prerequisites to using yrots
- Python >= 3.6, to run the compiler
- A text file editor, to write yrots code in
- A shell/command prompt window, to manage everything
- A NodeJs installation to run the compiled code

## Hello world

First, lets write a hello world program. Create an empty file called `Hello.yrot` in the same directory as the compiler and write this inside. Be sure to write the correct amount of new lines, as they are important!

```
Hello



This is the first book by this author



Chapter 1: Introduction
A tale to tell

Roger said "Hello, world!"
```

Then run `python3 ycmp.py Hello.yrot Hello.js` in a shell window. Replace `python3` with the name of your python installation.

If the compilation was successful, you should be able to see a file called `Hello.js` pop up in your current directory. Then run it using NodeJs (for example, type `nodejs Hello.js`). Then you should see the words `Hello, world!` pop up on your screen.

## Program structure

#### Title

A yrots program starts with the title. This is preferably the same as the file name, minus the extension. In the example above, the title is `Hello`. The title is followed by three blank lines. (4x \n)

#### Imports list

Next comes the imports list. Each file in the imports list gets copy-and-pasted into the top of the current one In the example above, there are no imports, so we wrote `This is the first book by this author`. For more information, scroll down to [Importing files](#importing-files).

The imports list is followed by three blank lines (4x \n)

#### Functions

The rest of the program is just made up of functions. Each function has a chapter number and a name. The value of the chapter number doesn't matter. There can be one function in each file called `Introduction`. This function is run when the program starts. Each function is seperated from the one before it by three blank lines (4x \n).

#### Lines

Each function is made up of a number of lines. Each line does one thing, such as print to the screen or read a value