from typing import List
import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Available servers, kept in sorted order
        available = list(range(k))
        
        # (finish_time, server_id)
        busy = []
        
        # Number of requests handled by each server
        count = [0] * k
        
        for i in range(len(arrival)):
            
            # Step 1: Free all servers that have completed their work
            while busy and busy[0][0] <= arrival[i]:
                _, server = heapq.heappop(busy)
                bisect.insort(available, server)
            
            # Step 2: If no server is available, drop the request
            if not available:
                continue
            
            # Preferred server
            preferred = i % k
            
            # Find the first available server >= preferred
            index = bisect.bisect_left(available, preferred)
            
            # If no server is found, wrap around to the first server
            if index == len(available):
                index = 0
            
            # Assign the request
            server = available.pop(index)
            count[server] += 1
            
            # Mark server as busy until this time
            finish_time = arrival[i] + load[i]
            heapq.heappush(busy, (finish_time, server))
        
        # Find the maximum number of requests handled
        maximum = max(count)
        
        # Return all servers with the maximum count
        return [i for i in range(k) if count[i] == maximum]