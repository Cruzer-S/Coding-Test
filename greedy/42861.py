class island:
    def __init__(self, id):
        self.id = id
        self.link = dict()

    def get_distance(self, target):
        return self.link[target]

    @staticmethod
    def set_link(a, b, cost):
        a.link[b] = cost
        b.link[a] = cost

    def get_links(self):
        return self.link

    def has_link(self, island):
        return island in self.link

    @staticmethod
    def del_link(a, b):
        del a.link[b]
        del b.link[a]

    def change_link(self, b, c, cost):
        island.del_link(self, b)
        island.set_link(self, c, cost)

    def __str__(self):
        return str(self.id)

def solution(_, costs):
    answer = 0

    id_to_island = dict()
    islands = list()

    for iso1_id, iso2_id, cost in costs:
        if iso1_id not in id_to_island:
            id_to_island[iso1_id] = island(iso1_id)
        
        if iso2_id not in id_to_island:
            id_to_island[iso2_id] = island(iso2_id)

        iso1 = id_to_island[iso1_id]
        iso2 = id_to_island[iso2_id]

        islands.append(iso1)
        islands.append(iso2)
            
        island.set_link(iso1, iso2, cost)

    next_id = max(id_to_island.keys()) + 1

    while len(islands) > 1:
        iso1 = islands.pop()

        links = list(iso1.get_links())
        if (len(links) == 0):
            continue

        iso2 = links[0]
        for i in links[1:]:
            if iso1.get_distance(i) < iso1.get_distance(iso2):
                iso2 = i

        answer += iso1.get_distance(iso2)

        islands.remove(iso2)
        island.del_link(iso1, iso2)

        new_island = island(next_id)
        next_id += 1

        for iso in list(iso1.get_links()):
            cost = iso1.get_distance(iso)
            if new_island.has_link(iso):
                if new_island.get_distance(iso) < cost:
                    island.del_link(iso, iso1)
                    continue
            iso.change_link(iso1, new_island, cost)

        for iso in list(iso2.get_links()):
            cost = iso2.get_distance(iso)
            if new_island.has_link(iso):
                if new_island.get_distance(iso) < cost:
                    island.del_link(iso, iso2)
                    continue
            iso.change_link(iso2, new_island, cost)

        islands.append(new_island)

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
