FILENAME = "sample_input.txt"
# FILENAME = "input.txt"

import time
import numpy as np
from scipy.optimize import least_squares
import random
import statistics

min_intersection = 7
max_intersection = 27

# min_intersection = 200000000000000
# max_intersection = 400000000000000

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

    data, averages = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data, averages)
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
    with open(FILENAME, "r") as f:
        data = f.readlines()

    pxs = []
    pys = []
    pzs = []
    vxs = []
    vys = []
    vzs = []
    hailstones = {}
    for line in data:
        position, velocity = line.strip().split(" @ ")
        px, py, pz = position.split(", ")
        vx, vy, vz = velocity.split(", ")
        hailstones[(int(px), int(py), int(pz))] = (int(vx), int(vy), int(vz))

        pxs.append(int(px))
        pys.append(int(py))
        pzs.append(int(pz))
        vxs.append(int(vx))
        vys.append(int(vy))
        vzs.append(int(vz))

        averages = [statistics.mean(pxs), statistics.mean(pys), statistics.mean(pzs), statistics.mean(vxs), statistics.mean(vys), statistics.mean(vzs)]

    return hailstones, averages


def part1(data):
    total_intersections = 0
    checked = set()
    for hailstone_a in data:
        for hailstone_b in data:
            if hailstone_a == hailstone_b or (hailstone_b, hailstone_a) in checked:
                continue

            checked.add((hailstone_a, hailstone_b))
            px1, py1, _ = hailstone_a
            px2, py2, _ = hailstone_b
            vx1, vy1, _ = data[hailstone_a]
            vx2, vy2, _ = data[hailstone_b]

            det = vx1*vy2 - vx2*vy1

            if np.isclose(det, 0):
                continue

            delta_x = px1 - px2
            delta_y = py1 - py2
            t1 = round((delta_y * vx2 - delta_x * vy2) / det, 3)
            t2 = round((delta_y * vx1 - delta_x * vy1) / det, 3)

            if not np.isfinite(t1) or not np.isfinite(t2) or t1 <= 0 or t2 <= 0:
                continue

            final_x1 = round(px1 + t1*vx1, 3)
            final_y1 = round(py1 + t1*vy1, 3)

            if (min_intersection <= final_x1 <= max_intersection
                and min_intersection <= final_y1 <= max_intersection
            ):
                total_intersections += 1

    return total_intersections

def line_intersection(params, data):
    x0, y0, z0, a, b, c = params
    errors=[]

    for (px, py, pz), (vx, vy, vz) in data.items():
        # Set up the system for solving t_i
        A = np.array([[a - vx], [b - vy], [c - vz]])
        B = np.array([px - x0, py - y0, pz - z0])
        
        # Solve for t_i using least squares
        t_i, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
        t_i = t_i[0]  # Extract scalar value


        # Adjust the point's position using its velocity at time t_i
        adjusted_px = px + vx * t_i
        adjusted_py = py + vy * t_i
        adjusted_pz = pz + vz * t_i

        # Compute predicted position at t_i
        predicted_x = x0 + a * t_i
        predicted_y = y0 + b * t_i
        predicted_z = z0 + c * t_i
        
        # Compute error
        error = np.sqrt((adjusted_px - predicted_x) ** 2 + 
                        (adjusted_py - predicted_y) ** 2 + 
                        (adjusted_pz - predicted_z) ** 2)
        errors.append(error)

    return errors


def part2(data, averages):
    scale = 1
    initial_guess = [value/scale for value in averages]

    random_keys = random.sample(list(data.keys()), 3)

    new_data = dict()
    for random_key in random_keys:
        scaled_px = random_key[0]/scale
        scaled_py = random_key[1]/scale
        scaled_pz = random_key[2]/scale
        scaled_vx = data[random_key][0]/scale
        scaled_vy = data[random_key][1]/scale
        scaled_vz = data[random_key][2]/scale
        new_data[(scaled_px, scaled_py, scaled_pz)] = (scaled_vx, scaled_vy, scaled_vz)

    # Optimize using least squares to find the best line parameters
    result = least_squares(line_intersection, initial_guess, args=(new_data,), verbose=2, max_nfev=100000)

    # Extract optimized values
    x0, y0, z0, a, b, c = result.x

    for key in new_data:
        print(key, new_data[key])

    print()
    print(f"Initial guess: {initial_guess}")

    # Print results
    print(f"Starting point (x0, y0, z0): ({x0*scale:.2f}, {y0*scale:.2f}, {z0*scale:.2f})")
    print(f"Direction vector (a, b, c): ({a*scale:.2f}, {b*scale:.2f}, {c*scale:.2f})")


    return f"{(x0+y0+z0)*scale:.2f}"


if __name__ == "__main__":
    main()