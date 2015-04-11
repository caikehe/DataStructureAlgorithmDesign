class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        tmp = []
        i = j = 0
        while i < m and j < n:
            if A[i] >= B[j]:
                tmp.append(B[j])
                j += 1
            elif A[i] < B[j]:
                tmp.append(A[i])
                i += 1
            
        # A still left
        if i < m:
            tmp.extend(A[i:])
        if j < n:
            tmp.extend(B[j:])
        A = tmp
        print A

so = Solution()
A = [0]
m = 1
B = [1]
n = 1
so.merge(A, m, B, n)
