class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited=set(forbidden)
        queue=[(0,0,True)]
        max_val=max([x]+forbidden) +a+b
        while queue:
            pos,steps,back=queue.pop(0)
            if pos==x:
                return steps
            
            if pos-b not in visited and back and pos-b>0:
                queue.append((pos-b,steps+1,not back))
                visited.add(pos-b)
            if pos+a not in visited  and pos+a<=max_val:
                queue.append((pos+a,steps+1,True))
                visited.add(pos+a)
        return -1