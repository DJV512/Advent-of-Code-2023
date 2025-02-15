#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import numpy as np
from collections import defaultdict
import heapq

RESET = "\033[0m"         # Resets all styles
BLACK = "\033[30;1m"      # Black text
RED = "\033[31;1m"        # Red text
GREEN = "\033[32;1m"      # Green text
YELLOW = "\033[33;1m"     # Yellow text
BLUE = "\033[34;1m"       # Blue text
MAGENTGA = "\033[35;1m"   # Magenta text
CYAN = "\033[36;1m"       # Cyan text
WHITE = "\033[37;1m"      # White text

BOLD = "\033[1m"          # Bold text
UNDERLINE = "\033[4m"     # Underlined text

def main():
    start_time = time.time()

    data, large_x, large_y, large_z = parse_data()
    parse_time = time.time()

    answer1, supporting, supported_by, fallen_arrangement = part1(data, large_x, large_y, large_z)
    part1_time = time.time()
    answer2 = part2(data, supporting, supported_by, fallen_arrangement)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time)} ms")
    print("---------------------------------------------------")


def parse_data():
    bricks = {}
    
    with open(FILENAME, "r") as f:
        data = f.readlines()

    large_x = 0
    large_y = 0
    large_z = 0
    for i, brick in enumerate(data):
        side1, side2 = brick.strip().split("~")
        x_1, y_1, z_1 = side1.split(",")
        x_2, y_2, z_2 = side2.split(",")
        differences = (int(x_2)-int(x_1), int(y_2)-int(y_1), int(z_2)-int(z_1))
        if differences[0] != 0:
            direction = 0
            distance = differences[0] + 1
        elif differences[1] != 0:
            direction = 1
            distance = differences[1] + 1
        elif differences[2] != 0:
            direction = 2
            distance = differences[2] + 1
        else:
            direction = 3
            distance = 1

        bricks[i+1] = ((int(x_1), int(y_1), int(z_1)-1), direction, distance)
        if int(x_2) > large_x:
            large_x = int(x_2) 
        if int(y_2) > large_y:
            large_y = int(y_2) 
        if int(z_2) > large_z:
            large_z = int(z_2) 

    return bricks, large_x, large_y, large_z


def part1(data, large_x, large_y, large_z):

    # Make initial array based on the snapshot
    space = np.zeros((large_x+1, large_y+1, large_z), dtype=int)
    for brick in data:
        start_location = data[brick][0]
        direction = data[brick][1]
        distance = data[brick][2]
        space[start_location[0]][start_location[1]][start_location[2]] = brick
        if direction == 3:
            continue
        for i in range(1, distance):
            if direction == 0:
                space[start_location[0]+i][start_location[1]][start_location[2]] = brick
            elif direction == 1:
                space[start_location[0]][start_location[1]+i][start_location[2]] = brick
            elif direction == 2:
                space[start_location[0]][start_location[1]][start_location[2]+i] = brick
    

    # Make the bricks fall, from bottom to top, stopping when they hit another brick
    done = False
    while not done:
        done = True
        checked = set()
        for z in range(1, large_z):
            for x in range(large_x+1):
                for y in range(large_y+1):
                    if space[x,y,z] != 0:
                        brick = space[x,y,z]
                        if brick not in checked:
                            checked.add(brick)
                            direction = data[brick][1]
                            distance = data[brick][2]
                            fall = True
                            if direction == 0:
                                for i in range(0, distance):
                                    if space[x+i, y, z-1] != 0:
                                        fall = False
                                        break
                                if fall:
                                    for i in range(0, distance):
                                        space[x+i,y,z-1] = space[x+i,y,z]
                                        space[x+i,y,z] = 0
                                    done = False

                            elif direction == 1:
                                for i in range(0, distance):
                                    if space[x, y+i, z-1] != 0:
                                        fall = False
                                        break
                                if fall:
                                    for i in range(0, distance):
                                        space[x,y+i,z-1] = space[x,y+i,z]
                                        space[x,y+i,z] = 0
                                    done = False

                            elif direction == 2 or direction == 3:
                                if space[x, y, z-1] == 0:
                                    for i in range(0, distance):
                                        space[x,y,z+i-1] = space[x,y,z+i]
                                        space[x,y,z+i] = 0
                                    done = False

    # Make a map of how the bricks look after falling
    fallen_arrangement = {}
    for brick in data:
        fallen_arrangement[brick] = np.argwhere(space == brick)

    # Determine which bricks are supporting, or are being supported by, other bricks
    supporting = defaultdict(set)
    supported_by = defaultdict(set)
    for brick in fallen_arrangement:
        for location in fallen_arrangement[brick]:
            if space[location[0], location[1], location[2]+1] != 0 and space[location[0], location[1], location[2]+1] != brick:
                supporting[brick].add(int(space[location[0], location[1], location[2]+1]))
            if space[location[0], location[1], location[2]-1] != 0 and space[location[0], location[1], location[2]-1] != brick:
                supported_by[brick].add(int(space[location[0], location[1], location[2]-1]))

    # Determine which bricks can be disintegrated without other bricks falling 
    disintegratable = set()
    cant_disintegrate = set()
    for brick in data:
        if brick not in supporting:
            disintegratable.add(brick)
    for brick in data:
        if len(supported_by[brick]) == 1:
            for value in supported_by[brick]:
                cant_disintegrate.add(value)
                disintegratable.discard(value)
        else:
            for value in supported_by[brick]:
                if value not in cant_disintegrate:
                    disintegratable.add(value)
        
    return(len(disintegratable), supporting, supported_by, fallen_arrangement)

def part2(data, supporting, supported_by, fallen_arrangement):

    # initialize a dictionary to keep track of how many bricks would fall if each
    # brick were disintegrated
    number_caused_to_fall = {}

    # go through each brick in turn and disintegrate it
    for brick in data:
        stack = []
        
        # if this brick is not supporting anything, nothing will fall if it's disintegreated
        # go to the next brick

        if brick not in supporting or not supporting[brick]:
             continue
        
        # if this brick is supporting bricks, add those bricks to the heap to check
        else:
            for value in supporting[brick]:
                heapq.heappush(stack, (fallen_arrangement[value][0][2], value))
     
        # keep popping bricks off the heap, with the bricks at the lowest z values going first
        # keep track of any bricks that would fall in a set
        falling_bricks = set()
        while stack:
            _, next_brick = heapq.heappop(stack)

            # if the brick popped off the heap is only supported by 1 brick (which would be the one that push it to the heap in the first place)
            # then it will fall. Add it to the set of falling bricks, and add every brick it's supporting to the heap
            if len(supported_by[next_brick]) == 1:
                falling_bricks.add(next_brick)
                for value in supporting[next_brick]:
                    heapq.heappush(stack, (fallen_arrangement[value][0][2], value))
                continue
            
            # if the brick popped off the heap is supported by more than one brick, it's more complicated
            # we know that at least one of those bricks supporting it would fall, but we need to go through
            # every brick supporting it and see if they are already in the falling bricks set
            if len(supported_by[next_brick]) > 1:
                fall = True
                for new_brick in supported_by[next_brick]:
                    # if even one brick supporting it is not in the falling list, then it will not fall
                    # break out of the loop, go to the next iteration of the while loop
                    # and add nothing to the heap
                    if new_brick not in falling_bricks:
                        fall = False
                        break
                # if, however, all bricks supporting it are in the falling bricks list, then
                # add it to the falling brick list, and add all blocks that IT is supporting
                # to the heap to check
                if fall:
                    falling_bricks.add(next_brick)
                    for value in supporting[next_brick]:
                        heapq.heappush(stack, (fallen_arrangement[value][0][2], value))
                    continue

        # at the conclusion of every while loop, add to a dictionary, at a key of the original
        # disintegrated brick, the number of bricks that would fall if it was disintegrated
        number_caused_to_fall[brick] = len(falling_bricks)

    # sum all the values in the dictionary to get the answer to the puzzle
    return sum(number_caused_to_fall.values())


if __name__ == "__main__":
    main()