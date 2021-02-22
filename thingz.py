
# make it so 7s destroy other pieces
# and 7s only spread over abcd
# and '$' makes 7s

#hows it g                                                            oin
# buy android worms
# buy lots of food 
# violin music for supermarkets - jon rose
# https://www.youtube.com/watch?v=i7j6ZKVJJAU

import os
import time
import random
from colorama import Fore, Back, Style
from copy import copy, deepcopy

'''

    Oliver Thingz. A celular automata in the vein of Conways game of life

    Dedicated to John Conway.

    Copyright (C) 2021 Adam Oliver


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

global num
num = 80
hei = 22
wid = 80


print('#')
print(Fore.RED + '%', end='') #
#print(Fore.LIGHTGREEN + '%') #
print(Fore.YELLOW + '*') #
print(Fore.GREEN + '&') #
print(Fore.BLUE + '$') #
#quit()

global grid
global grid2
grid = [[0 for i in range(wid)] for j in range(hei)] # 80 20 
grid2 = [[0 for i in range(wid)] for j in range(hei)] # 80 20 

# set all grid[x][y] to 6

county = 0
count = 0
for i in grid:
  for j in i:
    grid[county][count] = '6'
    
    count += 1
  count = 0 
  county += 1
# done

# set a few example variables (to be removed)

grid[0][1] = '1'
grid[0][2] = '2'
grid[0][3] = '3'
grid[0][4] = '4'
grid[0][9] = '5'
grid[1][7] = '6'

'''
buckets = ['6'] * num
buckets[9] = '7'
buckets[1] = '8'
buckets[2] = '9'
buckets[3] = '0'
buckets[4] = '1'
'''


# prints the grid2
def print_grid():

  grid2 = grid
  #grid2 = deepcopy(grid)

  count = 0
  for i in grid2:
    for e in i:

      if(e=='1'):print(Fore.WHITE + '#', end='' ) # end='' removes newline
      if(e=='2'):print(Fore.RED + '%', end='' ) # 
      if(e=='3'):print(Fore.YELLOW + '*', end='' ) # 
      if(e=='4'):print(Fore.GREEN + '&', end='' ) # 
      if(e=='5'):print(Fore.BLUE + '$', end='' ) # 
      if(e=='6'):print(Fore.BLUE + ' ', end='' ) # 

      if(e=='7'):print(Fore.BLUE + 'i', end='' ) # 

      if(e=='10'):print(Fore.WHITE + 'a', end='' ) # 
      if(e=='11'):print(Fore.RED + 'b', end='' ) # 
      if(e=='12'):print(Fore.YELLOW + 'c', end='' ) # 
      if(e=='13'):print(Fore.GREEN + 'd', end='' ) # 


      if(e=='a'):print(Fore.WHITE + 'a', end='' ) # 
      
      count += 1
      if(count == wid): print(''); count = 0


#print_grid()

print('')
print('')
	

# just grid
def add_a_cell():

  print('')
  print('')
  
  # change range(1) to change number of new characters
  
  for i in range(10):
    # finds a random place in the grid, adds a cell
    #print(random.randint(1,6))
    x = random.randint(0,hei-1)
    y = random.randint(0,wid-1)

    if( grid[x][y] != 6 ):
      grid[x][y] = str(random.randint(1,5))
    else:
      grid[x][y] = 6
      grid[x-1][y] = 6
      grid[x][y-1] = 6
      grid[x+1][y] = 6
      grid[x-1][y+1] = 6

      #  pass

    #wid-1
    #hei-1
    #str(random.randint(1,6))
    
# this just stops list index out of range error
def numberz_h(thenum):

  #print('[')
  #print('wid thenum')
  #print(wid)
  #print(thenum)

  if(thenum >= wid):
    return wid - 1
  else:
    return thenum
    
def numberz(thenum):

  #print('[')
  #print('hei thenum')
  #print(hei)
  #print(thenum)

  if(thenum >= hei):
    return hei - 1
  else:
    return thenum


def expand():
  
  #grid2 = grid

  global grid

  ####a
  #y = deepcopy(x)
  grid2 = deepcopy(grid)

  count = 0
  for i in grid:
    county = 0
    for j in i:
      #pass

      #print(j)

      if( j == '1' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][county-1] = '10' # up
        grid2[count][ numberz_h(county+1) ] = '10' # down
        grid2[count-1][county] = '10' # left
        grid2[ numberz(count+1) ][county] = '10' # right

        grid2[ count-1 ][county-1] = '10' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '10' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '10' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '10' # up right
        #grid[count][county] = '4'
        
      if( j == '2' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][ numberz_h(county+1) ] = '11'
        grid2[count][county-1] = '11'
        grid2[count-1][county] = '11'
        grid2[ numberz(count+1) ][county] = '11' # sometimes this goes out of the grid
        #grid[count][county] = '4'
        
        grid2[ count-1 ][county-1] = '11' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '11' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '11' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '11' # up right

        
      if( j == '3' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][county-1] = '12' # up
        grid2[count][ numberz_h(county+1) ] = '12' # down
        grid2[count-1][county] = '12' # left
        grid2[ numberz(count+1) ][county] = '12' # right

        grid2[ count-1 ][county-1] = '12' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '12' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '12' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '12' # up right
        #grid[count][county] = '4'

      if( j == '4' ): # not working
        #print(':D' + str(i))
        #print('# detected')
        #print('x and y of # is: ...' + str(county) + ' ' + str(count))
        grid2[count][county-1] = '13' # up
        grid2[count][ numberz_h(county+1) ] = '13' # down
        grid2[count-1][county] = '13' # left
        grid2[ numberz(count+1) ][county] = '13' # right

        grid2[ count-1 ][county-1] = '13' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '13' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '13' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '13' # up right
        #grid[count][county] = '4'
        
      if( j == '5' ): # here
        if( grid2[count][county-1] != '6' ):
          grid2[count][county-1] = '5' # up

        if( grid2[count][ numberz_h(county+1) ] != '6' ):
          grid2[count][ numberz_h(county+1) ] = '5' # down
        if( grid2[count-1][ county ] != '6' ):
          grid2[count-1][county] = '5' # left
        if( grid2[ numberz(count+1) ][ county ] != '6' ):
          grid2[ numberz(count+1) ][county] = '5' # right
        grid2[ count ][county] = '6'
        '''
        grid2[ count-1 ][county-1] = '13' # up left
        grid2[ numberz(count+1) ][ numberz_h(county+1) ] = '13' # down right
        grid2[ numberz(count+1) ][ county-1 ] = '13' # down left
        grid2[ count-1 ][ numberz_h(county+1) ] = '13' # up right
        '''

      county += 1
      
    count += 1





  # experiment
  count = 0
  for i in grid2:
    county = 0
    for j in i:
      if( j != grid[count][county] and ( grid[count][county] != 6 and j != 6 ) ):
        if(int(j) > 4):
          j = '1'
        else:
          j += '1'
        #grid2[count][county] %= 4
        
      county += 1
      
    count += 1






  grid = deepcopy(grid2)

#?!

  #pass

while True:

  add_a_cell()

  print_grid()

  time.sleep(0.1)#0.1

  expand()  


###
# end
#










