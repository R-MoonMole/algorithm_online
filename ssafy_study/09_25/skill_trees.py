skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        cnt = 0        # skill에서 지금까지 맞춘 개수
        check = 0      # 현재까지 올바른 순서로 맞춘 스킬 개수
        pass_cnt = 0   # -1이면 잘못된 스킬트리라는 뜻

        for ch in i:
            if ch in skill:          # skill에 포함된 스킬만 체크
                if ch == skill[cnt]: # 올바른 순서면
                    cnt += 1
                    check += 1
                    if cnt == len(skill):  # skill 끝까지 다 확인했으면 break
                        break
                else:                 # 순서 틀렸을 때
                    pass_cnt = -1
                    break

        if pass_cnt != -1:  # 순서를 안 어겼으면 카운트
            answer += 1

    return answer

print(solution(skill, skill_trees))