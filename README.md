# my_leetcode_journey
## Activity log: to a full-year algorithmic trip in Leetcode 
04/05 Remember: `[iterable].forEach` in Javascript modifies the iterable inplace and RETURNS undefined \
04/04 &nbsp;&nbsp; Implement get_neighors(i, j) using JS and Python generator for BFS algorithms in 2D matrix(e.g. 01 Matrix). This should cut memory usage down for a bit \
04/03 &nbsp;&nbsp; Figure out a way to optimize space complexity from O(n) to O(1) for the '101' and '010' problem(select building) by drawing a dependency graph. And write the explanation to the problem's discussion panel \
04/02 &nbsp;&nbsp; Attend Weekly contest for the first time. Solve only 1 out of 4 \
03/25 &nbsp;&nbsp; Start using Chrome Extension Leethub to automate uploading leetcode submission to Github 

## Weekly Summary
### 2022

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

## TODO  
- [x] Sort solutions into folders by category
