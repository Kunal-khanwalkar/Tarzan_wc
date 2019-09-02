#!/usr/bin/env python3

import numpy as np

########################### Functions ###############################################################

def find_new(lst):
	high = -1
	new = np.matrix([0,0,0])
	for i in range(0,lst.shape[0]):
		if(high<lst[i,0] or high==lst[i,0]):
			high = lst[i,0]

	for i in range(0,lst.shape[0]):
		if(lst[i,0]==high):
			new = np.concatenate((new,lst[i]),axis=0)

	new = np.delete(new,0,axis=0)
	return new

def heuristic(x,y,g0,g1):
	h_val = abs(x-g0)+abs(y-g1)
	return h_val

def find_min(mat):
	low = 100000
	new_low = np.matrix([ [0,0,0] ])
	for i in range(0,len(mat)):
		if(low>=mat[i,0]):
			low=mat[i,0]
	for i in range(0,mat.shape[0]):
		if(mat[i,0]==low):
			yy = mat[i,:]
			yy = yy.reshape((1,3))
			new_low = np.concatenate((new_low,yy),axis=0)
	new_low = np.delete(new_low,0,axis=0)
	return new_low

def move(new,hist):
	global g_value,cost,up,down,left,right,work_grid,inc
	inc = inc+1
	for i in range(0,len(new)):
		work_grid[new[i,1],new[i,2]]= 2
		f_prob = np.array([ [0,0,0] ])

		for j in range(0,len(diirection)):
			x = new[i,1]+diirection[j,0]
			y = new[i,2]+diirection[j,1]
			if(x>=0 and x<=grid.shape[0]-1 and y>=0 and y<=grid.shape[1]-1):
				if(work_grid[x,y]==0):
					f_prob = np.concatenate((f_prob,[[ g_value+1+h_func[x,y] ,x,y ]]),axis=0)
		f_prob = np.delete(f_prob,0,axis=0)
		f_min = find_min(f_prob)

		for j in range(0,f_min.shape[0]):
			hist = np.append( hist,[ [ new[i,0]+1 ,f_min[j,1], f_min[j,2]] ],axis=0 )
			g_value = hist[len(hist)-1,0]
			work_grid[ hist[len(hist)-1,1] , hist[len(hist)-1,2] ] = 2
			exp[ hist[len(hist)-1,1] , hist[len(hist)-1,2] ]=inc
	return hist

########################### Initiating Variables #######################################################
# grid = np.array([[0,1,0,0,0,1],
# 				   [0,1,1,0,0,0],
# 				   [0,1,0,0,0,0],
# 				   [0,1,0,0,1,0],
# 				   [0,0,0,0,0,0]])
grid = np.array([ [0,0,1,0,0,0],
				  [0,0,1,0,0,0],
				  [0,0,1,0,0,0],
				  [0,0,0,0,1,0],
				  [0,0,1,1,1,0],
				  [0,0,0,0,1,0] ])

start = np.array([[0,0]])
goal = np.array([[grid.shape[0]-1,grid.shape[1]-1]])

global g_value,cost,work_grid,inc,exp,path,direction_name,star,coor,diirection,h_func
g_value = 0
cost = 1 
inc = 0 
star= False

diirection = np.array([[-1,0],
				  [1,0],
				  [0,-1],
				  [0,1]])

direction_name = np.array(['v','^','>','<'])

open_list = np.array([ [g_value,start[0,0],start[0,1]] ])

work_grid = np.copy(grid)

exp = np.ones((grid.shape[0],grid.shape[1]))
exp = exp*(-1)
exp[start[0,0],start[0,1]] = 0

path = np.array([[' ' for row in range(grid.shape[1])] for col in range(grid.shape[0])])
path[ goal[0,0],goal[0,1] ] = ('*')

h_func = np.copy(grid)
for i in range(0,len(h_func)):
	for j in range(0,h_func.shape[1]):
		h_func[i,j] = heuristic(i,j,goal[0,0],goal[0,1])
print(h_func)

history = np.matrix([g_value,start[0,0],start[0,1]])

########################### Main Loop To Find Goal ################################################################
while True:
	exit = 0
	max_g = find_new(history)
	history = move(max_g,history)
	max_g0 = find_new(history)
	for i in range(0,len(max_g0)):
		if(max_g0[i,1]==goal[0,0] and max_g0[i,2]==goal[0,1]):
			print('Mandir yahin banwaenge.')
			exit = 1
	if(exit==1):
		coor = np.array([[goal[0,0],goal[0,1]]])
		print(find_new(history))
		print(history)
		print(work_grid)
		print(grid)
		print(exp)
		break 
	if(max_g[0,1]==max_g0[0,1] and max_g[0,2]==max_g0[0,2]):
		coor = np.matrix(history[len(history)-1,1:])
		path[coor[0,0],coor[0,1]]='#'
		print(history)
		print(work_grid)
		print(grid)
		print(exp)
		print(coor)
		print('Randi hai yeh')
		break

while star==False:
	for i in range(0,len(diirection)):
		x = coor[0,0]+diirection[i,0]
		y = coor[0,1]+diirection[i,1]

		if(x>=0 and x<=grid.shape[0]-1 and y>=0 and y<=grid.shape[1]-1):
			if(exp[x,y]==g_value-1):
				coor = coor+diirection[i,:]
				g_value = g_value-1
				if(i==0):
					path[x,y]=direction_name[0]
				elif(i==1):
					path[x,y]=direction_name[1]
				elif(i==2):
					path[x,y]=direction_name[2]
				else:
					path[x,y]=direction_name[3]
		if(x==start[0,0] and y==start[0,1]):
			print(path)
			star = True