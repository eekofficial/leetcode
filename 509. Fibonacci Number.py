#https://leetcode.com/problems/fibonacci-number/

#include <vector>
using namespace std;

class Solution {
public:
    int fib(int N) {
        if (N <= 1) {
            return N;
        }
        vector<int> fib_list(N + 1);
        fib_list[0] = 0;
        fib_list[1] = 1;
        for (int i = 2; i < N + 1; i++) {
            fib_list[i] = fib_list[i-2] + fib_list[i-1];
        }
        return fib_list[N];
    }
};
