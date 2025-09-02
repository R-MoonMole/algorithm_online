'''
(6+5*(2-8)/2)
6528-*2/+
'''

stack = [0] * 10

top = -1

icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 밖에 있을 때의 우선순위 (클수록 높음)
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 안에 있을 떄의 우선순위 (클수록 높음)

infix = '(6+5*(2-8)/2)'
postfix = ''

for token in infix:
    if token not in '(+-*/)':   # 피 연산자면 후위식에 추가
        postfix += token
    elif token == ')':         # 닫는 괄호면 여는 괄호를 만날 때까지 pop
        while top > -1 and stack[top] != '(':   # top > -1을 넣는건 혹시 여는괄호가 없을수도 있으니까
            top -= 1
            postfix += stack[top+1]
        if top != -1:   # 전체 수식이 괄호로 둘러쌓이지 않은 경우에 대해서 확인하기위함
            top -= 1    # '(' 버림...
    else:               # 연산자인 경우
        if top==-1 or isp[stack[top]] < icp[token]: # 토큰의 우선순위가 더 높으면
            top += 1    # push
            stack[top] = token
        elif isp[stack[top]] >= icp[token]:         # 토큰과 우선순위가 같거나 더 높으면
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            top += 1  # push
            stack[top] = token

print(postfix)
#postfix = '6528-*2/+'

for x in postfix:
    if x not in '+-/*': # 피연산자면...
        top += 1            # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x =='+':  # op1 + op2
            top += 1                # push()
            stack[top] = op1 + op2
        elif x =='-':
            top += 1
            stack[top] = op1 - op2
        elif x =='/':
            top += 1
            stack[top] = op1 / op2
        elif x =='*':
            top += 1
            stack[top] = op1 * op2

print(stack[top])








# 이 코드는 애초에 ()로 되어있는 경우라 (가 없을 경우를 안따져도 됨
# # 위 코드는 ( 없는 경우도 체크 하는거임
#
# stack = [0]*100
# top = -1
# icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
# isp = {'(':0, '*':2, '/':2, '+':1, '-':1}
#
# fx = '(6+5*(2-8)/2)'
# susik = ''
# for x in fx:
#     if x not in '(+-*/)':   # 피연산자
#         susik += x
#     elif x == ')':      # '('까지 pop()
#         while stack[top] != '(':    # peek
#             susik += stack[top]
#             top -= 1
#         top -= 1        # '(' 버림. pop
#     else:   # '(+-*/'
#         if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
#             top += 1    # push
#             stack[top] = x
#         elif isp[stack[top]] >= icp[x]:
#             while top > -1 and isp[stack[top]] >= icp[x]:
#                 susik += stack[top]
#                 top -= 1
#             top += 1  # push
#             stack[top] = x
#
# print(susik)
#
# #susik = '6528-*2/+'
# for x in susik:
#     if x not in '+-/*': # 피연산자면...
#         top += 1            # push(x)
#         stack[top] = int(x)
#     else:
#         op2 = stack[top]  # pop()
#         top -= 1
#         op1 = stack[top]  # pop()
#         top -= 1
#         if x=='+':  # op1 + op2
#             top += 1                # push()
#             stack[top] = op1 + op2
#         elif x=='-':
#             top += 1
#             stack[top] = op1 - op2
#         elif x=='/':
#             top += 1
#             stack[top] = op1 / op2
#         elif x=='*':
#             top += 1
#             stack[top] = op1 * op2
#
# print(stack[top])