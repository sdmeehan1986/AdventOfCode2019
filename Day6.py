import networkx as nx

data = open('AoC_Data/day6.txt').read().splitlines()
G, aList, aSet, count = nx.DiGraph(), [], set(), 0
planetYou, planetSan = None, None

for i in data:
    planet, orbit = i.split(')')
    aList.append((planet, orbit))
    aSet.add(planet)
    aSet.add(orbit)
    if orbit == 'YOU':
        planetYou = planet
    if orbit == 'SAN':
        planetSan = planet

G.add_edges_from(aList)

for i in aSet:
    temp = nx.dfs_successors(G, i)
    for i in temp:
        count += len(temp[i])

print(f'Part one is {count}')

part2 = nx.Graph()
part2.add_edges_from(aList)
print(f'Part two is {len(nx.shortest_path(part2, planetYou, planetSan)) - 1}')
