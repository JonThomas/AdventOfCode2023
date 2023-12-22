from fileOps import readFileRemoveLinebreaks

class LocationMapper:
    # spaceSeparatedMap example: 50 98 2       <--- 50 is the destination, 98 is the source, 2 is the length
    #                            52 50 48
    def __init__(self, name):
        self.name = name
        self._maps = []
    def _parseMap(self, spaceSeparatedMap):
        return list(map(int, spaceSeparatedMap.split(' ')))
    def AddMap(self, spaceSeparatedMap):
        self._maps.append(self._parseMap(spaceSeparatedMap))
    def mapSourceToDestination(self, source):
        for map in self._maps:
            if source >= map[1] and source <= map[1] + map[2]:
                return source + map[0] - map[1]
        return source
    def __str__(self):
        mapStr = ""
        for map in self._maps:
            mapStr += f"{self.name}: Source={map[1]}, Destination={map[0]}, Length={map[2]} \n"
        return mapStr

def parseInput(lines):
    seeds = []
    locationMappers = []
    thisMapper = None
    for line in lines:
        if line.startswith("seeds: "):
            seedString = line.split(':')[1].strip()
            for seed in seedString.split(' '):
                seeds.append(int(seed))
        elif line.strip() == "":
            if thisMapper != None:
                locationMappers.append(thisMapper)
            thisMapper = None
            continue
        elif line.strip().endswith(" map:"):
            thisMapper = LocationMapper(line.replace(" map:", "").strip())
        else:
            thisMapper.AddMap(line.strip())
    locationMappers.append(thisMapper)
    return seeds, locationMappers

seeds, maps = parseInput(readFileRemoveLinebreaks("day05input.txt"))

print(seeds)
for map in maps:
    print(map)

location = 0
for seed in seeds:
    source = seed
    for map in maps:
        source = map.mapSourceToDestination(source)

    if location == 0:
        location = source
    else: 
        location = min(source, location)

print(f"The lowest location is {location}")