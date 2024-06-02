#include <iostream>
#include <vector>
#include <map>
using namespace std;

typedef unsigned int pint;
class Graph {
    public:
        map <int, vector<int>> graph;

        void add (pint a, pint b) {
            graph[a].push_back(b);
            graph[b].push_back(a);
        }

        void print() {
            for (auto pair: graph) {
                cout << pair.first << " -> {";
                vector <int> list = pair.second;
                for (pint i=0;i<list.size()-1;i++) {
                    cout << list[i] << ", ";
                }
                cout << list.back() << "}" << endl;
            }
        }
};


