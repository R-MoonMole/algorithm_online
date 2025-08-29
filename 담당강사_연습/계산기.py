icp = {'(': 3, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # stack에 push하기 전
isp = {'(': 0, ')': 3, '*': 2, '/': 2, '+': 1, '-': 1} # stack 내부

infix = '(6+5*(2-8)/2)+6'   # 중위 표기
postfix = ''                # 후위 표기
S = []
# 중위 표기에서 token을 하나씩 읽어서 반복
    # 연산자면
        # token이 ')' 면 S에 '('가 나올때 까지 pop 해서 출력하고 '(' pop
        # 나머지는 S에 push, token보다 S 우선순위가 높은 연산자를들을 모두 S에서 pop해서 출력
        # token push

    # 피연산자면 postfix에 출력

for token in infix:
    if token in icp:
        if token == ')':
            while S and S[-1] != '(':   # while S <- 비어있는지 확인 (주어진 연산자가 이상할 경우를 대비)
                postfix += S.pop()
            S.pop()

        else:
            while S and isp[S[-1]] >= icp[token]:
                postfix += S.pop()
            S.append(token)

    else:
        postfix += token

while S:    # 빈 스택 체크
    postfix += S.pop()

print(postfix)