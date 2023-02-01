# All Sorts of Lists

## Algorithms, Data-Structures and Programming Languages
## 2023-01-10 Paul Libbrecht CC-BY

--- 

## From the outside: ADT Abstract Data Types

* A **list** is a sequence of objects
	* often of a given super-class (e.g. all are numbers, employees)
	* It has a size
	* One can access each element by index
	* One can add, set or remove at any index
	* One can iterate through it

- - -

## Special Lists: Arrays

* The objects' (pointers) are at contiguous RAM positions
* Thus: easy to jump a big number forward
* Allocation is single shot given a size: Reserve the block
* Get at an index: Complexity O(1)
* Insert/Remove at an index: Complexity at worst O(n)
* ... do draw how this works!

---

## Special Lists: Linked Lists

- Objects are in "buckets"
- Each bucket is linked to the next bucket
- Even more special: Doubly-linked List
	- Makes sense when you walk both direction
- Allocation for each bucket (one value, one pointer)
- Insert/remove when having a cursor: O(1)
- Get the cursor at some position (e.g. to insert/remove/get): O(n)
- e.g. https://visualgo.net/en/list

- - -
## Complexity of Operations

* Linked-List: Avoid "random" accesses:
	* but super for iterating and often add/remove
* Arrays: Avoid add/remove
	* but super for iterating and random access
* Important to envision when calculating complexity
	* e.g. Java's LinkedList's `get(n)` is of complexity `n`
* All in all only a problem when `n` becomes big
* Swapping? Never a real problem


- - -

## Why is it a problem to allocate big arrays?

* Contiguous memory allocation
	* ... needs to find space in the memory
	* heap management may have difficulties if requested size becomes big
* E.g. try a new array of size 3000000000 (3 billion) integers
	* it can work
	* ... it can fail
	* Do you really need that big?

- - -

## How to have enormous lists?

* Flexible storage is required
	* part in RAM, part on disk
	* disk SSD? Probably quite good at random
	* disk moving head: better not move randomly
* Virtuelle Lists?
* Databases are optimized for this
* ... and allow data to be selected by queries
* (and sort well ;-) )

* In principle you could implement a flexible storage model
	* you'd end up doing datatbases

- - -
