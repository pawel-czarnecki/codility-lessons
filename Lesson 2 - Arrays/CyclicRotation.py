'''
A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element
is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times;
that is, each element of A will be shifted to the right by K indexes.

Write a function:

    def solution(A, K)

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

Assume that:

    - N and K are integers within the range [0..100];
    - each element of array A is an integer within the range [−1,000..1,000].
'''

'''
    Analysis URL: https://codility.com/demo/results/training7S2XJ9-N5S/
    Correctness:  100%
    Performance:  not assessed
    Task score:	  100%
'''

def solution(A, K):
    if len(A) == 0:
        return A
    
    return A[len(A) - (K % len(A)):] + A[:len(A) - (K % len(A))]
