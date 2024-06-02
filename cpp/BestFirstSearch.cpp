#include <map>
#include <set>
#include <queue>
#include "graph.h"
using namespace std;

typedef pair<int, int> pi;

void add_cost(map<int, int> &cost_map, const int value, const int cost) {
    cost_map[value] = cost;
}

map<int, int> BestFirstSearch(int start, int goal, map<int, vector<int>>graph, map<int, int>cost_map) {
    priority_queue<pi, vector<pi>, greater<pi>> pq;
    set<int> visited;
    map<int, int> parent;
    bool found = false;

    pq.push(make_pair(cost_map[start], start));
    parent[start] = -1;

    while (!pq.empty() && !found) {
        int v = pq.top().second;
        pq.pop();

        cout << v << "->{";
        for (int i=0;i<graph[v].size();i++) {
            int n = graph[v][i];
            if (visited.find(n) == visited.end()) {
                pq.push(make_pair(cost_map[n], n));
                parent[n] = v;
                visited.insert(v);
                if (v == goal) {
                    found = true;
                    break;
                }
            }
            cout << n << ", ";
        }
        cout << "\b\b}" << endl;
    }
    return parent;
}

int main() {
    Graph graph = Graph();
    map<int, int> cost_map;
    graph.add(0, 2);
    graph.add(0, 1);
    graph.add(1, 3);
    graph.add(1, 4);
    graph.add(2, 5);
    graph.add(3, 5);

    const int start = 0;
    const int goal = 5;

    add_cost(cost_map, 0, 2);
    add_cost(cost_map, 1, 2);
    add_cost(cost_map, 2, 1);
    add_cost(cost_map, 3, 1);
    add_cost(cost_map, 4, 1);
    add_cost(cost_map, 5, 0);

    /*
    for (auto pair:cost_map) {
        cout << pair.first << ":" << pair.second << endl;
    }
    */
    map<int, int> parent = BestFirstSearch(start, goal, graph.graph, cost_map);

    cout << "PARENTS: " << endl;
    for (const auto pair:parent) {
        cout << pair.first << " --> " << pair.second << endl;
    }
}

/*
 *      0
 *     / \
 *    1   2
 *   / \   \
 *  3   4  |
 *   \     |
 *    5-----
 *
 * */
