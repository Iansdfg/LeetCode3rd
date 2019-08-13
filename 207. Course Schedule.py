class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for _ in range(numCourses)]
        courses_preres = {x:[] for x in range(numCourses)}
        
        for i,j in prerequisites:
            indegree[i]+=1
            courses_preres[j].append(i)
            
        # print(indegree, courses_preres)
            
        queue = collections.deque()
        for key in courses_preres:
            if indegree[key] == 0:
                queue.append(key)
                
        # print(queue)
                
        count = 0
        while queue:
            curr_course = queue.popleft()
            count += 1
            for prere in courses_preres[curr_course]:
                indegree[prere] -= 1
                if indegree[prere] == 0:
                    queue.append(prere)
                    
        return count == numCourses
    
    
        
         
