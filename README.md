# my_leetcode_journey
## Activity log: to a full-year algorithmic journey in Leetcode 
02/16 Implemented a pointer-based Segment Tree, adding one star to Segment Tree(-> ★☆☆☆☆)

--👆2023👆--

10/22 Learned Kanade's Algorithm to find the maximum subarray. And reverse it to find the minimum
10/03 Reboot. Reviewing 1~2 DP problems a day.

04/14 Solved two topological sort problems: Course Schdule I, II. Classy classical problems brought up in 6.006 recitation as well. At the end of day(almost), participated in AtCoder Beginner Contest 248. Only solved 3 problems, got stuck on the 3rd problem so long which turns out to be another basic DP problem. Gigantic failure... 

04/14 Just realized there's this build-in function `divmod(divident, divisor)` in Python. Super handy for getting every digit of an integer, by ```while n > 0:
    n, digit = divmod(n, 10)```
    
04/12 Almost finished Graph Theory Study Plan I. One lesson: use BFS || Dynamic programming 

04/05 Remember: `[iterable].forEach` in Javascript modifies the iterable inplace and RETURNS undefined 

04/04 &nbsp;&nbsp; Implement get_neighors(i, j) using JS and Python generator for BFS algorithms in 2D matrix(e.g. 01 Matrix). This should cut memory usage down for a bit 

04/03 &nbsp;&nbsp; Figure out a way to optimize space complexity from O(n) to O(1) for the '101' and '010' problem(select building) by drawing a dependency graph. And write the explanation to the problem's discussion panel 

04/02 &nbsp;&nbsp; Attend Weekly contest for the first time. Solve only 1 out of 4 

03/25 &nbsp;&nbsp; Start using Chrome Extension Leethub to automate uploading leetcode submission to Github 

## Weekly Summary
### 2022
### 10/2 - 
#### Interesting articles on DP
- https://segmentfault.com/a/1190000040132029/ (Covered examples: Climbing stairs, maximum subarray, longest increasing subsequence, edit distance)
- https://github.com/ascoders/weekly/blob/master/%E5%89%8D%E6%B2%BF%E6%8A%80%E6%9C%AF/192.%E7%B2%BE%E8%AF%BB%E3%80%8ADOM%20diff%20%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97%E3%80%8B.md (DOM diff 最长上升子序列)
### 4/5 - 4/17
Feel like getting stuck in the depths of muddy graph algorithms... After 'finishing' (quotation mark because I didn't solve the last 5 problems on my own) the Graph Theory Study Plan I, I did not seem to have improvement in my coding skills at all. All intuitions and practical muscles I acquired is limited to handling basic graph-ish problems with DFS/BFS. There are so many topics left to pick up or get a review on: A*, Shortest Path, Maximaxpaium Flow, Minimum Cut, Minimum Spanning tree... Last note, after finishing this round of Study Plan(up to around April 25th), I need to focus on preparing for coding tests from LINE and other companies, so I am deciding to shift to AtCoder for a while, maybe until June, during the period I will be doing very few leetcode problems. And instead of uploading Leetcode submissions, I will uploading those from AtCoder.

### 3/28 - 4/4 : **BFS**|**DFS**
This is a BFS and DFS week. Did over 20 problems on BFS and DFS. A significant part of the problems are based on a similar setting of a 2D 01-matrix and the definition of a water cell(0) and landcell(1). Several notes on key ideas to solve this type of problem and coding technique involved: \
 - For painting/finding a connected set of cell of the same type, *usually both BFS and DFS works*. 
 - For path finding, or shortest path in particular, just do **BFS**. It's **dummy-proof**.
 - For DFS, depending on the problem's specs, wisely pick between recusion, sometime with backtracking add-on and iterative approach with a stack.
 - For BFS, depending on the problem, either using a `queue` or `this_level` and `next_level` is more favorable. In situations where mutating the input is allowed, space complexity may be reduced by simply replacing old value in the original graph with a flag.
 - Otherwise, for both algorithms, maintaining a `seen` or `visited` set object is usually necessary to prevent the program falls into an infinite loop/recursion. 
 - `getValidNeighbors(i, j)` is needed in almost every island/matrix problem, which can be implemented by defining a generator in both Python and Javascript.

### 3/21 - 3/27 : **DP**
To consolidate inputs coming from 6.006 lectures and recitations on dynamic programming, most problems solved this week fell under the DP hood, and most of them are archived under the DP folder. I had a lot of troubles seeing the subproblems/optimal substructures, but now having coded these problems, of same pattern repeatedly, hopefully I won't forget about the black magic too quickly. 

## Analysis
#### Max Area of Island
Isn't this a slightly revised version of floodfill repeated several times?

## Concepts Checklist[^1]
## Data Structures 
### Basic
* **Array**: 

> Python: list  
> Java: ArrayList  
> C++: std::vector  

* **LinkedList**: 

> Python: list or customized  
> Java: LinkedList   
> C++: std::list

* **HashTable**: 

> Python: dict(), collections.defaultdict()   
> Java: HashMap  
> C++: std::unordered_map  

* **HashSet**

> Python: set()  
> Java: HashSet()  
> C++: std::unordered_set  

### Advanced
* **Tree**
* **Graph**
* **Stack**

> Python: list, deque  
> Java: Stack  
> C++: std::stack

* **Deque**

> Python: collections.deque()  
> Java: LinkedList, ArrayDeque  
> C++: std::deque 

* **PriorityQueue** (heap)

> Python: heapq, collections.PriorityQueue (thread safe)  
> Java: PriorityQueue  
> C++: std::priority_queue

* BinarySearchTree (map)

> Python: None (try to use [bisect](https://docs.python.org/3/library/bisect.html), but big O is different)  
> Java: TreeMap  
> C++: std::map

* BinarySearchTree (set)

> Python: None (try to use [bisect](https://docs.python.org/3/library/bisect.html)], but big O is different)  
> Java: TreeSet  
> C++: std::set

* Trie: a map of key, map pairs; 

> - `T = lambda: collections.defaultdict(T)`
> - [Implement Trie (Prefix Tree) - LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)

* UnionFind
> You can implement by yourself in an interview, here is a very concise and brilliant template (path compression has been included):
> ```py
> uf = {i:i for i in range(len(M))}
> def find(p):
>   if uf[p] != p:
>       uf[p] = find(uf[p])
>   return uf[p]
>
> def union(p1, p2):
>   a1, a2 = find(p1), find(p2)
>   uf[a2] = a1
> ```
> WARNING: this implementation has some limitation, such as you need to traverse the `uf` by calling `find` for every element with a `set` to count the number of unions, this operation is O(n) since the length of the path for every element will be no more than 2.
> 
>Time complexity for union find is a little bit tricky, the union and find operation will take log*n time. Please check this [wiki](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) to get a better understanding.

### Ultimate
* *Red-black tree*
* *KD-Tree*
* *B-tree*
★☆☆☆☆ Segment Tree

## Algorithms[^2]
### Basics
★★★☆☆ **DFS**
 
★★★☆☆ **BFS** 

★☆☆☆☆ **BackTracking**

★☆☆☆☆ **Binary Search**

★★☆☆☆ **Two pointers**

★☆☆☆☆ Fast and slow pointers 

★☆☆☆☆ (Thinking from Reverse Order)


### Advanced
★☆☆☆☆ **Topological sort**

☆☆☆☆☆ Greedy: e.g. Huffman coding

☆☆☆☆☆ Divide and Conquer

☆☆☆☆☆ UnionFind

★★★☆☆ Cycle detection in undirected graph

★★☆☆☆ Cycle detection in directed graph

☆☆☆☆☆ Find SCC in directed Graph

☆☆☆☆☆ Lowest Common Ancestor 
    * [Lowest Common Ancestor of a Binary Tree - LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)[Lowest Common Ancestor Binary Tree - YouTube](https://www.youtube.com/watch?v=13m9ZCB8gjw&list=RDCMUCZLJf_R2sWyUtXSKiKlyvAw&index=8&frags=pl%2Cwn)

★☆☆☆☆ Dijkstra: single source shortest path, O(nlogn + m )

★☆☆☆☆ Bellman-Floyd: single source with negative weights, O(mn)

☆☆☆☆☆ Floyd-Warshall: all pairs shortest path; O(n^3)

☆☆☆☆☆ Reservoir Sampling

☆☆☆☆☆ KMP [Implement strStr() - LeetCode](https://leetcode.com/problems/implement-strstr/)
☆☆☆☆☆ *Manacher*

★★☆☆☆ *Morris*


### Ultimate
☆☆☆☆☆ *Minimum Spanning Tree: Prim’s, Kruskal*

☆☆☆☆☆ *minimum s-t cut: Ford-Fulkerson*

☆☆☆☆☆ *global min cut: Karger’s, Karger Stein*

[^1]: This list is credited to xianzhez/Coding-Interview-101.
[^2]: ★☆☆☆☆ <br> Can implement a basic structure of this algorithm in classical examples/settings/scenarios <br> 
Can remember the time complexity <br> 
★★☆☆☆ <br>
Can effectively identify the possible usefulness of this algorithm given an arbitrary setting <br>
Provided with enough time, can implement the algorithm to solve a problem given such setting <br>
★★★☆☆ <br>
Can implement the algorithm reasonably fast<br>
Can explain the algorithm well by drawing illustrations and writing pseudocode<br>
Can do a correct analysis on the upperbound time & space complexity of the algorithm<br>
★★★★☆<br>
Can implement the algorithm really fast<br>
Can do a mathematically rigorous analysis of the algorithm (eg. with combinatorics/probability/induction proof/invariants etc.) and its time & space complexity<br>
★★★★★<br>
Can explain the general version of this algorithm in a logcial way (worth writing a blog on it)<br>
Know different implementational strategies and understand their pros/cons<br>
