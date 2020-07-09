# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for skill_tree in skill_trees : 
        list = []
        
        for skill_name in skill_tree :
            if skill_name in skill : # 선행조건이 존재하는 스킬만 남김
                list.append(skill_name)
        
        for i in range(len(list)) :
            if list[i] != skill[i] : 
                # 만약 스킬들의 순서가 다르다면 선행 조건을 만족하지 못한 경우
                answer -= 1
                break
            
    return answer