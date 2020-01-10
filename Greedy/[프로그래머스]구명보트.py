def solution(people, limit):
    answer = 0;
    
    people.sort(); // 먼저, 사람의 몸무게를 정렬한다.
    // 이후 가장 가벼운 사람과 무거운 사람을 기준으로 찾아나간다.
    i = 0;
    j = len(people) - 1; 
    
    while i <= j : 
        answer += 1; // 가장 무거운 사람이 포함됨으로, 우선 구명보트가 하나 추가로 포함되어야 한다. 
        if int(people[i]) + int(people[j]) <= limit : // limit보다 작다면, 해당 사람은 앞서 추간 구명보트에 태운다.
            i += 1;
        j -= 1;

    return answer ;
