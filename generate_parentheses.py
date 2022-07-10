from typing import List

def  generate_parentheses_version_one(n: int) -> List[str]:
    
    current_stack = []
    response = []

    def backtrack(open_N: int, closed_N: int):
        print(current_stack)
        if open_N == closed_N == n:
            ## we are done, went throught combinations
            response.append("".join(current_stack))
        
        if open_N < n:
            ## we can add an open parenthese 
            current_stack.append("(")
            ## call again and continue 
            ## increment open_N count 
            backtrack(open_N=open_N+1, closed_N=closed_N) 
            current_stack.pop()
        if closed_N < open_N:
            ## append closed parentheses 
            current_stack.append(")")
            backtrack(open_N=open_N, closed_N=closed_N+1)
            current_stack.pop()
    
    backtrack(0, 0)
    return response



def generate_parentheses_version_two(n: int) -> List[str]:
    response: List[str] = []

    def backtrack(list: List[str], current_str: str, open_N: int, closed_N: int, max: int):
        if len(current_str) == max * 2:
            return response.append(current_str)
        if open_N < max:
            next_str: str = current_str + "("; next_open_N: int = open_N + 1
            backtrack(response, current_str=next_str, open_N=next_open_N, closed_N=closed_N, max=max)
        if closed_N < open_N:
            next_str: str = current_str + ")"; next_closed_N: int  = closed_N + 1
            backtrack(response, current_str=next_str, open_N=open_N, closed_N=next_closed_N, max=max)

    backtrack(list=response, current_str="", open_N=0, closed_N=0, max=n)
    return response


print(generate_parentheses_version_two(2))