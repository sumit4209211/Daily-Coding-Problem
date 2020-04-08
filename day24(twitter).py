#Question

A classroom consists of N students, whose friendships can be represented in an adjacency list. 
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations.
In other words, this is the smallest set such that no student in the group has any friends outside this group.
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.

def bfs(dictionary,start):
	di = dictionary
	queue = [start]
	visited = []

	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.append(vertex)
			neighbours = di[vertex]
			for neighbour in neighbours:
				queue.append(neighbour)
	return visited

def connected_components(dictionary,points):
	d = []
	for i in points:
		d.append(tuple(sorted(bfs(dictionary,i))))
	return d

d = {0: [1, 2],
	 1: [0, 5],
	 2: [0],
	 3: [6],
	 4: [],
	 5: [1],
	 6: [3]} 
ar = connected_components(d,[0,1,2,3,4,5,6])
se = {}
for i in ar:
	se[i] = 0
for key in se:
	print(key)

