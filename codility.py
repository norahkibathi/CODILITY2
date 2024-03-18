##the code has presented  a list of strings called S. Our task is to find a pair of strings in this list that share a common letter at the same position. I
##the first step will be We’ll compare each pair of strings in the list
def solution(S):
    # Iterate through each pair of strings in S
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            # Iterate through each position in the strings
            for k in range(len(S[i])):
                # If the letters at the current position are equal
                if S[i][k] == S[j][k]:
                    # Return the pair and position
                    return [i, j, k]
    # If no pair with a common letter is found, return an empty array
    return []
print(solution(["abc","bca","dbe"]))  
print(solution(["zzzz","ferz","zdsr","fgtd"]))
print(solution(["gr","sd","rg"]))  
print(solution(["bdafg","ceagi"]))  