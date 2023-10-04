#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, m;
    std::cin >> n >> m;
    int last = 30000;
    std::vector<int> path_distance(n, last);
    std::vector<std::vector<int>> edge_lists;

    path_distance[0] = 0;

    for (int i = 0; i < m; i++) {
        int n1, n2, w;
        std::cin >> n1 >> n2 >> w;
        edge_lists.push_back({n1, n2, w});
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            int n1, n2, w;
            n1 = edge_lists[j][0];
            n2 = edge_lists[j][1];
            w = edge_lists[j][2];
            path_distance[n2 - 1] = std::min(path_distance[n1 - 1] + w, path_distance[n2 - 1]);
        }
    }

    for (int dist : path_distance) {
        std::cout << dist << ' ';
    }
    std::cout << std::endl;

    return 0;
}
