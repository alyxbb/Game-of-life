import time
grid=[["1"]*10]*10

def main():
    grid[4][2]
    gridprinter(grid)
    while True:
        time.sleep(10)
        for row in range(len(grid)):
            for item in range(len(grid[row])):
                countneighbours(grid,row,item)



def countneighbours(grid,row,item):
    count=0
    for i in range(-1,2):
        for j in range(-1,2):
            if not(j==0 and i==0):
                if grid[row][item]==1:
                    count+=1
                    print(count)
    return(count)



def gridprinter(grid):
    for row in grid:
        for item in row:
            print(item,end="")
        print()


if __name__ == '__main__':
    main()
