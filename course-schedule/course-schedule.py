class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph(prereqs, numCourses):
            graph = {}
            for after, before in prereqs:
                if before not in graph:
                    graph[before] = [after]
                else:
                    graph[before].append(after)
                    
            for i in range(numCourses):
                if i not in graph:
                    graph[i] = []
            return graph
        
        def dfs(G):
            # Return False if detects a backward edge
            parent = {}
            for course in course_dependencies:
                if course not in parent:
                    parent[course] = None
                    if not dfs_visit(G, course, parent): 
                        return False

            return True    

        def dfs_visit(G, v, parent):
            # Return False it there is a backedge else return True
            containeBackward = False
            for vx in G[v]:
                if vx not in parent: 
                    parent[vx] = v 
                    if not dfs_visit(G, vx, parent):  # If nodes below vx contains backward edge, return False
                        return False
                    continue
                elif parent[vx] == None: # v is a direct parent of vx, and dfs_visit() has returned from vx before 
                    parent[vx] = v

                if isBackward(parent, v, vx): # If v -> vx is a backward edge, return False
                    return False

            return True
                    
        def isBackward(parent, v, u):
            """
            Detect whether v->u is a backward edge. (i.e. whether u is an ancestor of v
            """
            while v in parent and parent[v] is not None:
                # print(f'{parent[v]} is a direct parent of {v}')
                if parent[v] == u: 
                    return True
                else:
                    # print(f'{v} = {parent[v]}')
                    v = parent[v]
            return False


        course_dependencies = build_graph(prerequisites, numCourses)
        return dfs(course_dependencies)