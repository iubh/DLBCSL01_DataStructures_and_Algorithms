# Scopes

## Algorithms, Data-Structures and Programming Languages
## 2023-02-01 Paul Libbrecht CC-BY
- -- 
## Frame

* Software is written in source form (text or other)
* Software is then packaged and run... 
	* but developers understand it as the source being run
* Sources are written by multiple persons and multiple teams
* Variables, methods, functions... have names
* Software of team A used by team B: great economy
	* Library sharing
	* Tuning (e.g. consultants)
	* particularly strong with open-source repositories
	* depend on each other
--- 

## Just make everything public

* This was common practice in small projects:
	* Source A can reference anything source B
	* anywhere inside, all variables are global
* Problem: people don't talk to each other about each detail
* Source B changed it's way to act
	* ... Source A becomes invalid
* Gets worse when re-use happens
* Note: this does not mean that author of source A has not access to source B
	* A matter of freedom (of _agency_: being able to act)
---

## Scopes

* For every function, method, constructor, variable, property:
	* scope: the set of places where it can be accessed (written/read/called...)
* typical:
	* `public`: Can be called from anywhere
	* `local`: only within the current source (or current function)
* for each programming language different: `module`, `package`, namespace, subclasses, ...

- - -

## The Contract? The Documentation? The Debt
* A library is made available
	* ... because it can do X/Y/Z
	* as in the spec; as advertised (the _contract_)
	* developer docs says: do so/so/so (uses the details of _the contract_)
* E.g. the contract is the abstract data type of each object (plus a little description)
* The contract is often said to be called the **API**
* The debt: What's offered should stay offered


- - - 
## Semantic Versioning

* A practice of noting versions of software releases
* three components: major.minor.fix
	* e.g. PouchDB version 7.3.1
* major: between each major versions, everything can change
* minor: between minor versions, APIs can be enriched but should stay compatible
* fix: no API changes, just bug-fixes
* Used, e.g., in NPM and Maven
* deprecation can signal things that will get old

- - - 

## Best Practices for Scoping

* Expose the least
	* use Encapsulation as much as possible
	* But don't use active defense
* When using global, make them prominently available
* Rely on automatic parsing of scopes
	* ... people get auto-complete
* Avoid ambiguities:
	* no `var` like redefinitions (the scope depends on the runtime!) or `global` annotations anywhere
	* follow one tradition (e.g. fields above from a class, or in constructor...)
* 

- - - 
## Take Away
* Software dependency can become a huge graph
	* e.g. 1000 dependencies is not rare in NodeJS projects
* Minimise accessible scope to just "what is needed"
* API-stability practice well established with semantic versioning
	* breaches have had well-known effects
* Each language organizes itself differently
	* Each repository too
* Documentation is never far in defining the scopes