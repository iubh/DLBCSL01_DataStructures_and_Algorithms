# Code Coverage

## Algorithms, Data-Structures and Programming Languages
## 2023-02-21 Paul Libbrecht CC-BY

--- 

## Code is the house

* Readability is key
* Conciseness useful
	* but not too much! (e.g. [regexp](https://spin.atomicobject.com/2018/02/21/regular-expressions/))
* Code size matters... e.g. [nginx about http3](https://www.nginx.com/blog/our-roadmap-quic-http-3-support-nginx/)
* Conclusion: Keep it small, tidy, and well understood

- - -

## Dead code

* Code that is never used
	* costs delivery
	* costs understanding
	* may instruct wrongly
	* is not tested
* Solution: code coverage

---

## Code coverage
* Run a tool with a special flag
	* ... that marks "zones" as run or not
	* (lines, functions, blocks...)
* Available for all platforms
* Assumes you can use "all potentially used functions"
* Gives a percentage
* What to do with flagged code??

- - -

## Tools
* Coverage.py
* IntelliJ's

- - - -
## Coverage information: generalized

* Industrialize code crash reports or coverage
	* automated reporting
* => Know the places where it crashes
* Actual usage potentially more informative
	* But only if you can be "overarching"
	* E.g. no special usage is prevented
* e.g. use web-analytics with feature usage

