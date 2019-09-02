#!/usr/bin/env python3
import numpy as np

######################## Functions ##############################################
def compute_value(grid,goal,cost):
	global delta,delta_name
	print(grid)
	work_grid = np.copy(grid)
	for i in range(0,grid.shape[0]):
		for j in range(0,grid.shape[1]):
			work_grid[i,j]=99  

	path = np.array([[' ' for i in range(0,grid.shape[1]) ] for j in range(0,grid.shape[0])])

	change=True
	while (change==True):
		change=False
		for x in range(0,grid.shape[0]):
			for y in range(0,grid.shape[1]):
				if goal[0,0]==x and goal[0,1]==y:
					if work_grid[x,y]>0:
						work_grid[x,y]=0
						path[x,y]='*'
						change=True
				elif(grid[x,y]==0):
					for i in range(0,delta.shape[0]):
						x_new = x+delta[i,0]
						y_new = y+delta[i,1]
						if(x_new>=0 and x_new<grid.shape[0] and y_new>=0 and y_new<grid.shape[1]):
							if(grid[x_new,y_new]==0):
								val=work_grid[x_new,y_new]+cost
								if val<work_grid[x,y]:
									work_grid[x,y]=val
									path[x,y]=delta_name[0,i]
									change = True
	print(path)
	return work_grid
######################## Variable Initialization ################################

grid = np.array([ [0,0,1,0,0,0],
				  [0,0,1,0,0,0],
				  [0,0,1,0,0,0],
				  [0,0,1,0,1,0],
				  [0,0,1,1,1,0],
				  [0,0,0,0,1,0] ])

goal = np.matrix([[0,0]])
goal[0,0] = grid.shape[0]-1 
goal[0,1] = grid.shape[1]-1

cost = 1

global delta,delta_name,work_grid
delta = np.array([ [-1,0],
				   [0,-1],
				   [1,0],
				   [0,1], ])
delta_name = np.array([['^','<','v','>']])
start = np.array([[0,0]])
######################## Main Loop ##############################################
r = compute_value(grid,goal,1)
print(r)