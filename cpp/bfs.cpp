#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <unordered_set>
#include "graph.h"
using namespace std;


// return parents as vector array
map<int, int> DFS(map<int, vector<int>> graph, int start) {
    queue<int> q; // Stack
    unordered_set<int> visited; // Array of visited
    map<int, int> parent; // Array of parents

    q.push(start); // add start to stack
    visited.insert(start); // add start in visited
    parent[start] = -1; // Set parent of start node as -1. Which means no parent
    while (!q.empty()) {
        // Save first element of queue and remove it.
        int v = q.front();
        q.pop();

        cout << v << "->{";
        // Itereate over all neighbors of node "v"
        for (pint i=0;i<graph[v].size();i++) {
            int neighbor = graph[v][i];
            if (visited.find(neighbor) == visited.end()) {
                q.push(neighbor);
                visited.insert(neighbor);
                parent[neighbor] = v;
            }
            cout << neighbor << ", ";
        }
        cout << "\b\b}" << endl;
    }
    return parent;
}

int main() {
    Graph graph = Graph();
    graph.add(0, 1);
    graph.add(0, 2);
    graph.add(1, 3);
    graph.add(1, 4);
    graph.add(2, 5);
    graph.add(3, 5);

    map<int, int> parents = DFS(graph.graph, 0);
    cout << "PARENTS: " << endl;
    for(const auto pair : parents) {
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
