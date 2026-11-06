from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        # Sort logs by time
        logs.sort(key=lambda log: log[1])
        
        # Keep original query positions
        sorted_queries = sorted(
            [(time, index) for index, time in enumerate(queries)]
        )
        
        count = defaultdict(int)
        active_servers = 0
        
        left = 0
        right = 0
        answer = [0] * len(queries)
        
        for query_time, index in sorted_queries:
            
            # Add all logs with time <= query_time
            while right < len(logs) and logs[right][1] <= query_time:
                server = logs[right][0]
                
                if count[server] == 0:
                    active_servers += 1
                
                count[server] += 1
                right += 1
            
            # Remove logs with time < query_time - x
            while left < right and logs[left][1] < query_time - x:
                server = logs[left][0]
                
                count[server] -= 1
                
                if count[server] == 0:
                    active_servers -= 1
                
                left += 1
            
            # Servers with no requests
            answer[index] = n - active_servers
        
        return answer