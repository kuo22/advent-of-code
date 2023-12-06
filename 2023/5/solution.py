import re
import math
from pathlib import Path
from collections import defaultdict

def lowest_seed_location(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')

    sources = [int(i.strip()) for i in f.readline().strip().split(':')[1].split(' ') if i]
    f.readline()
    maps = parse_maps(f)
    
    for map in maps:
        for i, source in enumerate(sources):
            dest_id = source
            for map_item in map:
                dest_start, source_start, length = map_item
                if source_start <= source <= source_start + length:
                    dest_id = dest_start + (source - source_start)
                    sources[i] = dest_id
                    break
            
            sources[i] = dest_id

    return min(sources)

def lowest_seed_location_2(file_name="input.txt"):
    file_path = Path(Path(__file__).parent.absolute(), file_name)
    f = open(file_path, 'r')

    sources = [int(i.strip()) for i in f.readline().strip().split(':')[1].split(' ') if i]
    f.readline()
    maps = parse_maps(f)
    
    lowest_dest = float('inf')


    for i in range(0, len(sources), 2):
        source = sources[i]
        source_range = sources[i + 1]
        for j in range(source, source + source_range + 1):
            prev_source = j
            for map in maps:
                for map_item in map:
                    dest_start, source_start, length = map_item
                    if source_start <= prev_source <= source_start + length:
                        prev_source = dest_start + (prev_source - source_start)
                        break 
            
            lowest_dest = min(lowest_dest, prev_source)
                

    return lowest_dest

def parse_maps(f):
    lines = f.read().splitlines()
    all_maps = []
    i = 0
    line = lines[i]
    current_map = []
    for line in lines:
        if "map:" in line:
            current_map = []
        elif not line:
            all_maps.append(current_map)
        else:
            mapping = [int(i) for i in line.strip().split()]
            current_map.append(mapping)

    all_maps.append(current_map)

    return all_maps



print("Lowest seed location:", lowest_seed_location())
#print(lowest_seed_location_2())
