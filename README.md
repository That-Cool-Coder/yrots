# Yrots

## Contents:
- [About](#about)
- [User instructions](userInstructions.md)
- [Compiling](#compiling)

## About

Yrots is an esoteric programming language which is designed to look like a story (that's where the name comes from). It has no practical purpose and is cumbersome to use. Yrots source files have the extension `.yrot`. The compiler is written in Python. Yrots code compiles into nodejs.


## Compiling

To compile yrots code, run `ymcp.py`. The command line arguments that it accepts are input file name and output file name

A basic compilation would look something like this:

```
python3 ycmp.py myYrotsSourceFile.yrot myCompiledNodeJSFile.js
```