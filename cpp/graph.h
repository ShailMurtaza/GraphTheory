#include <vector>
using namespace std;

typedef unsigned int pint;
class Graph {
    public:
        vector<vector<pint>> graph;
        void add(pint a, pint b) {
            if (graph.size() <= a) {
                graph.resize(a + 1);
            }
            if (graph.size() <= b) {
                graph.resize(b + 1);
            }
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
};


