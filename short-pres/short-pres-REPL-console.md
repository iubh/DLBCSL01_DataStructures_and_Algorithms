# Programme Interactively: the Console!

## Algorithms, Data-Structures and Programming Languages
## 2023-04-13 Paul Libbrecht CC-BY

--- 

## Inspiration

- ... a person answering requests
- ... a machine does what it is _ordered to_
- computers that have no screen but a printer (e.g. [here](https://commons.wikimedia.org/wiki/File:Ken_Thompson_(sitting)_and_Dennis_Ritchie_at_PDP-11_(2876612463).jpg))
- LISP machines
- basic idea: input something, get an answer
- frame: notion of **session**, more refined than a pair sender/executor

- - -

## The REPL console
* Read Evaluate Print Loop:
	* read an input from the user
	* evaluate this input
	* print result
* the input is parsed into an instruction
	* ... in a programming language
	* possibly continued (e.g. a bracket needs closing)
* the instruction is evaluated in a programming environment (variables, files, processes, ...): local or global
* the result is rendered to string (or...), tries to be readable

- - -

## Classic examples
* Terminals
	* (also accessed over SSH)
	* Runs a Shell: an execution environment (e.g. bash, zsh, tcsh, cmd...)
* shells in programming languages
	* e.g. in nodejs, python, prolog: just type the command
	* e.g. hooked to a web-page (JS console)
	* e.g. hooked to a debugger
	* e.g. in extra shell environments (e.g. jshell, beanshell...)
	* e.g. notebooks interface (jupyter, ...)
* demo
- - - 

## REPL enrichments
* Autocompletion
	* e.g. using tab
	* uses the environment (variables, files, processes... can be enriched)
* Syntax coloring
* System-messaging...
* Interface to the external world
	* e.g. drag-and-drop
	* e.g. text search
* History
	* a list of all previous commands
	* try ctrl-R
- - -
## REPL seen as indirect
* Commands in REPL take time to input
	* correct syntax needed
	* finding all the right parameters is complex
	* this is an advantage: it's a mini-programme!
* Elementary operations easier done with graphic means
	* "direct manipulation" is easier
* Consider sculpting a command as a direct manipulation
	* use auto-completion to verify
	* keep trying
---

## Demoes

* Interactive
* Enriched
* Debugging