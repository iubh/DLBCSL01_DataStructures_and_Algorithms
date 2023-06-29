# Representing Graphs
## Algorithms, Data-Structures and Programming Languages
## 2023-06-29 Paul Libbrecht CC-BY

--- 

## Mathematics of Graphs

* a graph is a pair (V,E) where
	* V is a set of vertices (anything)
	* E is a set of set of two vertices
* a directed graph is a pair (V,E) where
	* V is a set of vertices (anything)
	* E is a set of pair of two vertices
* lots of research on graph theory ([springboard wikipedia](https://en.wikipedia.org/wiki/Graph_theory))
	* with hard problems such as path detection
	* or coloring

---
## IT operations on graphs

* represent in memory (storage, queries...)
* iterate
* find path
* assign coordinates ("layout")
* present on screen
---
## Representations

* incidence matrix
	* not directed
* list of edges
* something internal
* graph databases
* see the coursebook

---

## Libraries to iterate

* [graphlib](https://docs.python.org/3/library/graphlib.html) for DAGs
* ...

- - -
## Layout Algorithms

* idea: give the graph core info
	* get coordinates that you can present
	* _minimize fuss_ : e.g. crossings, overlaps...
* classic: [graphviz](https://graphviz.org/) (with [python bindings](https://pypi.org/project/graphviz/))
* many examples in browsers: found in collections such as:
	* [Plotly's scientific](https://plotly.com/javascript/scientific-charts/), [D3](https://d3js.org/) (e.g. [d3-dag](https://github.com/erikbrinkman/d3-dag))
* but careful: a graph is not a graphic (words are often confused)

---
## Shortest Path Algorithn

* Normally Dijkstra's algorithm... greedy
* e.g. [ahojukka5's Dijkstra](https://github.com/ahojukka5/dijkstra)
* in principle also doable with a graph database
	* but probably best with a "complex request"
	* see [the many pathfinding algos of neo4j](https://neo4j.com/docs/graph-data-science/current/algorithms/pathfinding/)
