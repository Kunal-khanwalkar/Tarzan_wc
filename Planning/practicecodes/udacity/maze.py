#!/usr/bin/env python3

import numpy as np
import math

########################## Building Functions ###############################################################

def find_new(lst):
	count = 0
	h = 0
	ind = 0
	new = np.matrix([0,0,0])
	for i in range(0,lst.shape[0]):
		if(h<lst[i,0] or h==lst[i,0]):
			h = lst[i,0]

	for i in range(0,lst.shape[0]):
		if(lst[i,0]==h):
			count = count+1
			new = np.concatenate((new,lst[i]),axis=0)
	new = np.delete(new,0,axis=0)
	return new

def move(new,hist):
	global g_value,cost,up,down,left,right,work_grid, inc
	inc = inc+1
	for i in range(0,len(new)):
		work_grid[new[i,1],new[i,2]]= 2
		for j in range(0,len(udlr)):
			x = new[i,1]+udlr[j,0]
			y = new[i,2]+udlr[j,1]
			if(x>=0 and x<=grid.shape[0]-1 and y>=0 and y<=grid.shape[1]-1):
				if(work_grid[x,y]==0):
					mov = np.matrix([[cost,udlr[j,0],udlr[j,1]]])
					hist = np.concatenate((hist,new[i,:]+mov),axis=0)
					g_value = hist[len(hist)-1,0]
					work_grid[ hist[len(hist)-1,1] , hist[len(hist)-1,2] ] = 2
					exp[ hist[len(hist)-1,1] , hist[len(hist)-1,2] ]=inc
	return(hist)

########################### Initiating Variables #######################################################
grid = np.array([[0,0,0,0,0,1],
				 [0,0,1,0,0,0],
				 [0,0,1,0,0,0],
				 [1,0,1,0,1,0],
				 [0,0,0,0,1,0]])

start = np.matrix([[0,0]])
goal = np.matrix([[4,5]])

global g_value,cost,work_grid,inc,exp,path,direc,star,coor,udlr
g_value = 0
cost = 1 
inc =0 
star=False

udlr = np.matrix([[-1,0],
				  [1,0],
				  [0,-1],
				  [0,1]])

direc = np.array(['v','^','>','<'])

open_list = np.matrix([[g_value,start[0,0],start[0,1]]])

work_grid = np.copy(grid)

exp = np.ones((grid.shape[0],grid.shape[1]))
exp = exp*(-2)
exp[start[0,0],start[0,1]] = 0

path = np.matrix([[' ' for row in range(grid.shape[1])] for col in range(grid.shape[0])])
path[ goal[0,0],goal[0,1] ] = ('*')

history = np.matrix([g_value,start[0,0],start[0,1]])

########################## Main Loop To Find Goal ################################################################
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
		coor = np.matrix([[goal[0,0],goal[0,1]]])
		print(find_new(history))
		print(history)
		print(work_grid)
		print(grid)
		print(exp)
		break 
	if(max_g[0,1]==max_g0[0,1] and max_g[0,2]==max_g0[0,2]):
		coor = np.matrix(history[len(history)-1,1:])
		path[coor[0,0],coor[0,1]]='#'
		print(grid.shape)
		print(exp)
		print(coor)
		print('Randi hai yeh')
		break

while star==False:
	for i in range(0,len(udlr)):
		x = coor[0,0]+udlr[i,0]
		y = coor[0,1]+udlr[i,1]

		if(x>=0 and x<=grid.shape[0]-1 and y>=0 and y<=grid.shape[1]-1):
			if(exp[x,y]==g_value-1):
				coor = coor+udlr[i,:]
				g_value = g_value-1
				if(i==0):
					path[x,y]=direc[0]
				elif(i==1):
					path[x,y]=direc[1]
				elif(i==2):
					path[x,y]=direc[2]
				else:
					path[x,y]=direc[3]
		if(x==start[0,0] and y==start[0,1]):
			print(path)
			star = True