'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

    - S is empty;
    - S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
    - S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]",
the function should return 0, as explained above.

Assume that:

    - N is an integer within the range [0..200,000];
    - string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Complexity:

    - expected worst-case time complexity is O(N);
    - expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
'''

'''
    Analysis URL: https://codility.com/demo/results/training2SQPYU-WUK/
    Correctness:  100%
    Performance:  100%
    Task score:	  100%
'''

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[self.size() - 1]

def solution(S):
    stack = Stack()
    is_correct = 1

    for i in range(len(S)):
        if S[i] in ["(", "[", "{"]:
            stack.push(S[i])
        else:
            if stack.is_empty() and i <= len(S):
                is_correct = 0
                break
            
            if (
                    stack.top() == "(" and S[i] == ")" or
                    stack.top() == "[" and S[i] == "]" or
                    stack.top() == "{" and S[i] == "}"
                ):
                stack.pop()
            else:
                is_correct = 0
                break

    if not stack.is_empty():
        is_correct = 0
        
    return is_correct
