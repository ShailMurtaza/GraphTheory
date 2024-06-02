#include <iostream>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include "graph.h"

using namespace std;


// return parents as vector array
map<int, int> DFS(map <int, vector<int>>graph, int start) {
    stack<int> stack; // Stack
    set<int> visited; // Array of visited
    map<int, int> parent; // Array of parents

    stack.push(start); // add start to stack
    visited.insert(start); // add start in visited
    parent[start] = -1; // Set parent of 0 node as -1. Which means no parent
    while (!stack.empty()) {
        // Save last element of stack and remove it. Just like stack
        int v = stack.top();
        stack.pop();

        cout << v << "->{";
        // Itereate over all neighbors of node "v"
        for (pint i=0;i<graph[v].size();i++) {
            int neighbor = graph[v][i];
            if (visited.find(neighbor) == visited.end()) {
                stack.push(neighbor);
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

    // graph.print();
    map<int, int> parents = DFS(graph.graph, 0);
    cout << "PARENTS: " << endl;
    for (const auto pair : parents) {
        cout << pair.first << " -> " << pair.second << endl;
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
