import time
grid = [[0]*10 for _ in range(10)]

def main():
    grid[4][2]=1
    grid[3][3]=1
    grid[2][2]=1
    print("-" * 50)
    gridprinter(grid)
    time.sleep(1)
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            print(countneighbours(grid,row,item),end="")
        print()



def countneighbours(grid,row,item):
    count=0
    for i in range(-1,2):
        for j in range(-1,2):
            if not(j==0 and i==0):
                try:
                    if grid[row+i][item+j]==1:
                        count+=1
                except IndexError:
                    True
    return(count)



def gridprinter(grid):
    for row in grid:
        for item in row:
            print(item,end="")
        print()
    print("-" * 50)


if __name__ == '__main__':
    main()
