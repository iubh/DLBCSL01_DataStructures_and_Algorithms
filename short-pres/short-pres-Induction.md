# Induction (weak, strong, ...)

## Algorithms, Data-Structures and Programming Languages
## 2022-12-19 Paul Libbrecht CC-BY

--- 

## Algorithm Property Proofs

* An algorithm is a set of steps
	* In general to process a data-set (_the input_)
* Properties of an algorithm include:
	* Termination: it finishes (not infinite)
	* Correctness: it finishes and answers right
	* Run-time bounds: it finishes within a time in the order of O(...)
	* Run-space bounds: it finishes within a space in the order of O(...)
- - -

## Provable property
* A property of an algorithm can be proven using a proof
	* A sequence of deduction steps (if... then...)
	* Start with known facts 
	* Uses known deductions
	* To formulate a proof of the property
		* which holds with any input
* Proofs can be formalised: Using λ-calculus and ... 
	* Used in high-risks environment for the verification of softwares
	* even in Intel processor design
* Proofs are typically convincing the reader
	* ... except if becoming too complex or skip a lot
---

## Induction Proofs

* The idea: the property P is split into a sequence of properties P(i)
* P(i): for the input of "size" equal to i, the property P holds
* P(≤i): for the input of "size" up to i, the property P holds
* Induction proofs:
	* Base case: P(0) holds
	* Induction step (weak): if P(i) holds then P(i+1) holds
	* Induction step (strong): if P(≤i) holds, then P(i+1) holds
* ... this proves P(i) for any integer i
* Important everything must have a size

- - - 
## Example Induction Proof

* Simple one: P(i): Algo below finds element in the linked list
	* Problem: function `search`  with a parameter `list` and `object`
	* Algo: go through each element and compare to `object`
		* `list` empty: return `false`
		* first element in the list equal to the `object` => return `true`
		* otherwise apply search with the list truncated from the first
* Proof:
	* P(0): `list` is empty: return correctly false
	* P(1): `list` has a single element: take it and compare to `object`: returns true if it is equal to `object` or false if unequal to `object`  which is correct
	* P(i) => P(i+1): `list` has i+1 elements, `list` without first element has i elements. 
		* First element is equal to `object`? return true (correct).
		* Otherwise return the result of `list` without first element (correct because of P(i))
	* Thus, by the induction principle, P holds for any sizes

- - - 

## Induction Proofs around the World
* Many many in the coursebook and elsewhere
* Has been used informally since 1000 AD
* formalized around Pascal's times (~1600)
* Choosing weak or strong for an algo-prop proof?
	* It depends how your algo works
	* It often does not only depends on P(i)
* Is one of them a less useful candidate? no

- - - 

## Exercise proof by induction

* Name the properties explicitly by the size amount
	* explicitly use quantifiers such as ∀ and ∃
	* name runtime functions and remember f(n) = O(g(n)) is not transitive!
* Mark algorithm steps by line numbers
* Verify by debugging that you have performed steps correctly
	* with a few input