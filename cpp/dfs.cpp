#include <iostream>
#include <vector>
#include <algorithm>
#include "graph.h"

using namespace std;


// Check if num exist in vector
bool find_num(vector<pint> arr, pint num) {
    auto it = find(arr.begin(), arr.end(), num);
    if (it == arr.end()) {
        return false;
    }
    return true;
}

// return parents as vector array
vector<int> DFS(vector<vector<pint>> graph, pint start) {
    vector<pint> stack; // Stack
    vector<pint> visited; // Array of visited
    vector<int> parent; // Array of parents
    parent.resize(graph.size()); // Resize parent vector to number of vertices

    stack.push_back(start); // add start to stack
    visited.push_back(start); // add start in visited
    parent[start] = -1; // Set parent of 0 node as -1. Which means no parent
    while (!stack.empty()) {
        // Save last element of stack and remove it. Just like stack
        pint v = stack.back();
        stack.pop_back();

        cout << v << "->{";
        // Itereate over all neighbors of node "v"
        for (pint i=0;i<graph[v].size();i++) {
            pint neighbor = graph[v][i];
            if (!find_num(visited, neighbor)) {
                stack.push_back(neighbor);
                visited.push_back(neighbor);
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

    vector parents = DFS(graph.graph, 0);
    cout << "PARENTS: " << endl;
    for (pint i=0;i<parents.size();i++) {
        cout << i << " -> " << parents[i] << endl;
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
