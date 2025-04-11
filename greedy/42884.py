def solution(routes):
    # 1. 차량의 대수 1 이상, 10,000 이하
    # 2. routes[i][0] 에는 i 번째 차량이 고속도로에 `진입한 지점`,
    #    routes[i][1] 에는 i 번째 차량이 고속도로에서 `나간 지점`
    # 3. 차량의 진입/출 지점에 카메라가 설치되어 있어도 카메라를 만난 것으로 간주
    # 4. 진입 지점, 진출 지점은 -30,000 이상 30,000 이하

    # 5. `최소` 몇 대의 카메라를 설치해야 하는지를 반환

    # limits
    # 1 <= len(routes) <= +10,000
    # -30,000 <= routes[X][0,1] <= +30,000

    # 겹치는 지점을 파악해서 배열을 병합?

    # 1.
    # 1-------------------1
    #                 2-----------------2
    #                     3----------------3
    #                                           4---------4

    # 2.
    #                 1---2
    #                     3----------------3
    #                                           4---------4

    # 3.                 2,3
    #                                           4---------4
    # 이럼 두 대의 카메라가 필요

    # 1. 진입 지점으로 정렬하고
    # 2. n 번 차량의 출차 지점과 n + 1 번 차량의 진출 지점을 비교해서
    # 3. 겹치다면 병합하고 다음으로 진행
    # 4. 더 이상 병합이 안되는 경로의 수를 반환 (이게 바로 설치에 필요한 카메라의 수)

    routes = sorted(routes, key = lambda route: route[1])

    i = 0
    while (i < len(routes) - 1) and (len(routes) > 1):
        end = routes[i][1]
        start = routes[i + 1][0]

        if (start > end):
            i += 1
            continue

        new_route = [start, end]
        routes = routes[:i] + routes[i + 2:]

        routes.insert(i, new_route)

    return len(routes)

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
