import re
from functools import reduce
from pathlib import Path
from collections import defaultdict

def find_part_numbers_sum(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    schema = [line.strip() for line in f.readlines()]
    
    f.close()
    col_length = len(schema[0])
    row_length = len(schema)

    part_areas = [[False for i in range(col_length)] for j in range(row_length)]
    symbol_pattern = "(?!\d|\.)(.)"
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    for i in range(row_length):
        line = schema[i]
        matches = re.finditer(symbol_pattern, line)

        for match in matches:
            j = int(match.start())
            for direction in directions:
                adj_i = i + direction[0]
                adj_j = j + direction[1]
                if is_valid_index(adj_i, adj_j, row_length, col_length):
                    part_areas[adj_i][adj_j] = True
    
    number_pattern = "(\d+)"
    part_number_sum = 0
    for i in range(row_length):
        line = schema[i]
        matches = re.finditer(number_pattern, line)

        for match in matches:
            number = match.group(1)
            is_part_number = False
            for j in range(match.start(), match.end()):
                if part_areas[i][j]:
                    part_number_sum += int(number)
                    break


    return part_number_sum

def find_gear_ratio_sum(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')
    
    schema = [line.strip() for line in f.readlines()]
    
    f.close()
    col_length = len(schema[0])
    row_length = len(schema)

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    
    number_pattern = "(\d+)"
    adj_to_gear = defaultdict(list)

    for i in range(row_length):
        line = schema[i]
        matches = re.finditer(number_pattern, line)

        for match in matches:
            number = match.group(1)
            gears_visited = set()
            for j in range(match.start(), match.end()):
                found_gear = False

                for direction in directions:
                    adj_i = i + direction[0]
                    adj_j = j + direction[1]

                    if is_valid_index(adj_i, adj_j, row_length, col_length):
                        if schema[adj_i][adj_j] == '*':
                            gear_location = (adj_i, adj_j)

                            if gear_location not in gears_visited:
                                gears_visited.add(gear_location)
                                adj_to_gear[(adj_i, adj_j)].append(int(number))

    gear_ratio_sum = 0

    for key in adj_to_gear:
        if len(adj_to_gear[key]) == 2:
            gear_ratio = 1

            for gear in adj_to_gear[key]:
                gear_ratio *= gear
            gear_ratio_sum += gear_ratio

    return gear_ratio_sum

def is_valid_index(i, j, row_length, col_length):
    if i < 0 or i >= row_length or j < 0 or j >= col_length:
        return False
    
    return True


print("Part number sum:", find_part_numbers_sum())
print("Gear ratio sum:", find_gear_ratio_sum())
