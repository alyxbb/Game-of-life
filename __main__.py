import time

def main():
    grid = [[0] * 10 for _ in range(10)]
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][3] = 1
    grid[3][2] = 1
    grid[3][1] = 1
    print("-" * 50)
    gridprinter(grid)
    while True:
        time.sleep(1)
        neighbourgrid=countallneighbours(grid)
        grid=updateallitems(grid,neighbourgrid)
        gridprinter(grid)

def updateallitems(grid,neighbourgrid):
    for row in range(len(grid)):
        for item in range(len(grid[row])):
            currentitem=grid[row][item]
            currentneighbour=neighbourgrid[row][item]
            if currentitem>=1:
                if currentneighbour!=3:
                    if currentneighbour!=4:
                        grid[row][item] = 0
            else:
                if currentneighbour==3:
                    grid[row][item]=1
    return grid




def countallneighbours(grid):
    y=[]
    for row in range(len(grid)):
        x=[]
        for item in range(len(grid[row])):
            x.append(countneighbours(grid, row, item))
        y.append(x)
    return y


def countneighbours(grid,row,item):
    count=0
    for i in range(-1,2):
        for j in range(-1,2):

            try:
                if grid[row+i][item+j]>=1:
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
