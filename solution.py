import heapq

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

# codes here


  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options

def isH(index):
	return _[index][0] == "H"

def do(visited = {}):
	res = []
    heap = []

	for i in _.keys():
		runningMax = -1
		maxNode = None
		prevNode = i

		localVisited = visited
		localPath = [i]
		localSum = 0

		while(True):
			for j in _.keys():
				if j in visited:
					continue
				tmp = score(i, j)
				if tmp > runningMax:
					runningMax = tmp
					maxNode = j

			if runningMax <= -1:
				break
			#elif runningMax == 0:
			#	break
			else:
				localPath.append(j)
				visited.add(j)
				prevNode = j
				localSum += runningMax
				if not isH(j):
					break

		heapq.push(heap, (-localSum, localPath))


	path = heappop(heap)
	path = path[1]
	while(not isH(path[-1])):
		


