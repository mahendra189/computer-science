# List of Computer Science Algorithms

def main():
    algorithms = {
        "Sorting Algorithms": [
            "Bubble Sort",
            "Insertion Sort",
            "Selection Sort",
            "Merge Sort",
            "Quick Sort",
            "Heap Sort",
            "Counting Sort",
            "Radix Sort",
            "Bucket Sort"
        ],
        "Searching Algorithms": [
            "Linear Search",
            "Binary Search",
            "Jump Search",
            "Interpolation Search",
            "Exponential Search"
        ],
        "Graph Algorithms": [
            "Depth-First Search (DFS)",
            "Breadth-First Search (BFS)",
            "Dijkstra's Algorithm",
            "Bellman-Ford Algorithm",
            "Floyd-Warshall Algorithm",
            "Kruskal's Algorithm",
            "Prim's Algorithm",
            "Topological Sort",
            "A* Search"
        ],
        "Dynamic Programming": [
            "Knapsack Problem",
            "Longest Common Subsequence (LCS)",
            "Longest Increasing Subsequence",
            "Edit Distance",
            "Matrix Chain Multiplication",
            "Rod Cutting"
        ],
        "Greedy Algorithms": [
            "Activity Selection Problem",
            "Huffman Coding",
            "Fractional Knapsack Problem",
            "Job Sequencing Problem",
            "Minimum Spanning Tree (MST) - Kruskal's and Prim's"
        ],
        "Backtracking Algorithms": [
            "N-Queens Problem",
            "Sudoku Solver",
            "Hamiltonian Path",
            "Subset Sum Problem",
            "Knapsack Problem (also falls under Dynamic Programming)"
        ],
        "Divide and Conquer Algorithms": [
            "Merge Sort",
            "Quick Sort",
            "Binary Search",
            "Strassen's Matrix Multiplication"
        ],
        "Other Algorithms": [
            "Ford-Fulkerson Method",
            "KMP String Matching Algorithm",
            "Rabin-Karp Algorithm",
            "Boyer-Moore Algorithm",
            "Sieve of Eratosthenes",
            "Tarjan's Algorithm",
            "Kosaraju's Algorithm",
            "Union-Find Algorithm",
            "Bloom Filter"
        ]
    }

    print("Computer Science Algorithms:")
    for category, algo_list in algorithms.items():
        print(f"\n{category}:")
        for algo in algo_list:
            print(f"  - {algo}")

if __name__ == '__main__':
    main()
