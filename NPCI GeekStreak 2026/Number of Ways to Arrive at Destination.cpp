class Solution {
  public:
    int countPaths(int V, vector<vector<int>>& edges) {
        // code here
        const int MOD = 1e9 + 7;
        vector<vector<pair<int,int>>>adj(V);
        for(auto &e : edges)
        {
            int u=e[0],v=e[1],w=e[2];
            adj[u].push_back({v,w});
            adj[v].push_back({u,w});
        }
        vector<long long>dist(V,LLONG_MAX);
        vector<int>ways(V,0);
        priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<>>pq;
        dist[0]=0;
        ways[0]=1;
        pq.push({0,0});
        while(!pq.empty())
        {
            auto[d,u]=pq.top();
            pq.pop();
            if(d>dist[u])continue;
            for(auto&[v,w]:adj[u])
            {
                if(dist[v]>d+w)
                {
                    dist[v]=d+w;
                    ways[v]=ways[u];
                    pq.push({dist[v],v});
                }else if (dist[v]==d+w)
                {
                    ways[v]=(ways[v]+ways[u]) % MOD;
                }
            }
        }
        return ways[V-1];
    }
}