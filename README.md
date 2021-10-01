# HackTheNorth2021

### Check out the Devpost @https://devpost.com/software/vizualdb!

## Inspiration 💭 : 
Our initial inspiration came from our traumatic past experiences with Leetcode and other online coding assessments. In particular, data structures proved far too overwhelming time and time again. We’ve spent long hours attempting to complete these questions. We learn best through visual representation, and we believe this is the case for many of our fellow programmers. As a result, we decided to create a data structure visualizing debugger, a tool that will help users in their own journey of mastering data structures.

## What it does 💁‍♂️ : 
VizualDB (short for Visual Debugger) is a command-line tool designed to aid programmers in solving data structure problems. It provides line-by-line graphical displays of the current program state. The user will call the debugger on their program, and visual cues will then be revealed on the terminal. Throughout this process, the user can easily discover how their program flows, identify incorrect data and find errors in their program. Additional features such as breakpoints enable a straightforward and user-friendly debugging process.

## How we built it 😳 : 
We first researched the debugging process in Python, and designed a control-flow process accordingly. We then analyzed the call stack and traversed through the codebase, with breakpoint functionality. Using Python Curses, we were able to design a text-based visual interface for our debugger. We developed dynamic visualization functions to process and present various data structures in a manner convenient to the user, allowing them to quickly detect algorithmic errors.

## Challenges we ran into 😳 : 
None of us had extensive experience with command-line tools, so there was a deep learning curve in our implementation. Some data structures, specifically the binary tree and linked list required a greater amount of time and effort in their design. This was due to the fact that only these two structures required traversing through individual nodes and are duplicated in the call stack.

## Accomplishments that we're proud of 💪 : 
- Challenging ourselves to explore new technologies and tools to use in our solution.
- Implementing difficult data representations such as hashmaps, linked lists, and our favourite, binary trees.
- Building a practical project that is easily usable and relevant to our careers.

## What we learned 🧠 : 
- Gained a greater understanding of various data structures including implementation and analysis.
- Learned about the functional process of debuggers, and their role in software development.
- Researched and designed our own ASCII art in the form of various shapes and objects XD.

## What's next for VizualDB 🔮 : 
- Expanding our program’s informative capabilities (more descriptions, more visual formats and patterns, etc.)
- Support more data structures such as graphs, alternate versions of trees etc.
- Improving our user interface with better and more cohesive designs. 
