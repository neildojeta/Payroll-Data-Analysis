#include <iostream>
using namespace std;

// Recursive function to solve Towers of Hanoi
void towersOfHanoi(int n, char source, char target, char auxiliary) {
    if (n == 1) {
        // Base case: move the smallest ring directly
        cout << "Move ring 1 from " << source << " to " << target << endl;
        return;
    }
    // Step 1: Move n-1 rings from source to auxiliary
    towersOfHanoi(n - 1, source, auxiliary, target);
    
    // Step 2: Move the nth ring from source to target
    cout << "Move ring " << n << " from " << source << " to " << target << endl;
    
    // Step 3: Move n-1 rings from auxiliary to target
    towersOfHanoi(n - 1, auxiliary, target, source);
}

int main() {
    int n = 3; // Number of rings
    // Call the function with source 'A', target 'C', and auxiliary 'B'
    towersOfHanoi(n, 'A', 'C', 'B');
    return 0;
}

