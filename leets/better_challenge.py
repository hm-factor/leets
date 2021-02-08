# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# def solution(S, K):
#     if K < 0 or K > 500:
#         return -1

#     days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
#     idx = (days.index(S) + K) % 7
#     return days[idx]

# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")


# def solution(S):
#     out = 201
#     small = 0
#     big = 0

#     while small <= big and big < len(S):
#         # progress big if the newest char has its opposite in the whole string
#         # set small to big if the newest char doesnt have its opposite in string
#         char = S[big]
#         sub = S[small:big+1]
#         if char.lower() in S and char.upper() in S:
#             if validate(sub) and len(sub) > 0:
#                 out = min(len(sub), out)
#             big += 1
#         else:
#             big += 1
#             small = big

#     if out == 201:
#         return -1
#     else:
#         return out


# def validate(string):
#     for i in string:
#         if i.lower() not in string or i.upper() not in string:
#             return False

#     return True

def operation(start, int1, int2):
    if start == 0:
        return max(int1, int2)
    else:
        return max(int1*-1, int2)

def solution3(N):
    # write your code in Python 3.6
    out = -8000
    str_N = str(N)
    length = len(str_N)
    start = 0
    if N < 0:
        start = 1

    for i in range(start, length):
        new_int = int(str_N[start:i] + "5" + str_N[i:])
        out = operation(start, new_int, out)

    return out

print(solution3(590))
