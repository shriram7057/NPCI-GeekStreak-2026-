#User function Template for python3
class Solution:
    def minCost(self, houses):
      # code here
      n=len(houses)
      
      minDist = [10**18] * n
      used =[False] * n
      
      minDist[0] = 0
      total = 0
      
      for _ in range(n):
          u =- 1
          for i in range(n):
              if not used[i] and (u == -1 or minDist[i] < minDist[u]):
                  u = i
          used[u] = True
          total += minDist[u]
          
          x1, y1 = houses[u]
          for v in range(n):
              if not used[v]:
                  x2, y2 =houses[v]
                  dist = abs(x1 - x2) + abs(y1 - y2)
                  if dist < minDist[v]:
                      minDist[v] = dist
      return total
                  
                  