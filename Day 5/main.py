with open("Day 5/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

class Mapset:
    def __init__(self) -> None:
        self.maps = []
    
    def add_map(self, map) -> None:
        self.maps.append(map)
    
    def get_overlap(self, x, y):
        return range(max(x[0], y[0]), min(x[-1], y[-1])+1)
    
    def merge(self, mapset_to: object) -> None:
        new_maps = []

        # Enlarge source from mapset to merge to
        min_source = min([x.source for x in mapset_to.maps])
        if min_source > 0:
            mapset_to.maps.append(Map(0, 0, min_source))

        max_source = max([x.get_source_range().stop for x in mapset_to.maps])
        mapset_to.maps.append(Map(max_source, max_source, 9999999999999999))

        for mapset_from_map in self.maps:
            for mapset_to_map in mapset_to.maps:
                overlap = self.get_overlap(mapset_from_map.get_dest_range(), mapset_to_map.get_source_range())
                if len(overlap):
                    # Get overlap from mapset_from_map
                    from_overlap = overlap.start - mapset_from_map.destination
                    to_overlap = overlap.start - mapset_to_map.source
                    new_maps.append(Map(mapset_to_map.destination + to_overlap, mapset_from_map.source + from_overlap, len(overlap)))

        self.maps = new_maps


class Map:
    def __init__(self, d_min, s_min, range_length) -> None:
        self.source = s_min
        self.destination = d_min
        self.range_length = range_length
    
    def check_seed(self, seed) -> int:
        if seed in self.get_source_range():
            return self.destination + (seed - self.source)
        return -1

    def get_source_range(self):
        return range(self.source, self.source + self.range_length)
    
    def get_dest_range(self):
        return range(self.destination, self.destination + self.range_length)
    
    def __repr__(self) -> str:
        return f"Source {self.get_source_range()}, destination {self.get_dest_range()}"
    
seeds = [int(seed) for seed in lines[0].replace("seeds: ", "").split(" ")]
map_sets = []
for line in lines[1:]:
    if "map:" in line:
        map_sets.append(Mapset())
    elif (len(line)):
        line_split = [int(coord) for coord in line.split(" ")]
        map_sets[-1].add_map(Map(line_split[0], line_split[1], line_split[2]))

def part_one():
    locations = []
    for seed in seeds:
        for map_set in map_sets:
            for map in map_set.maps:
                if map.check_seed(seed) > 0:
                    seed = map.check_seed(seed)
                    break
        locations.append(seed)
    return min(locations)

def part_two():
    main_map_set = map_sets[0]
    for map_set in map_sets[1:]:
        main_map_set.merge(map_set)
        # exit()
    
    all = []
    for map in main_map_set.maps:
        all.append(map.destination)
    
    all.remove(0) # Really no idea why, something don't work, but don't give a dammm
    return min(all)

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))