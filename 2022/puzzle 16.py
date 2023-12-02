import re
from dataclasses import dataclass
import functools

@dataclass(frozen=True, order=True)
class Valve():
    id: str
    pressure: int
    tunnels: set[str]

def main():
    with open('input/puzzle 16', 'r') as f:
        data = re.findall('Valve (\S+) has flow rate=(\d+);.+[valve]s? (.+)', f.read())

    valves = {}
    for valve, rate, tunnels in data:
        valves[valve] = Valve(valve, int(rate), {x.strip() for x in tunnels.split(',')})

    # print("\n".join(str(valve) for valve in valves.values()))
    
    # The function is embedded because dictionaries are not ahshable and cant be cached
    # Cache is used for memoization :D
    @functools.cache
    def relief_pressure(opened, minutes, current_id, p2=False):
        
        if minutes <= 0 :
            if p2:
                return relief_pressure(opened, 26, 'AA')
            return 0
        
        relief = 0
        current_valve = valves[current_id]
        for valve in current_valve.tunnels:
            relief = max(relief,
                         relief_pressure(opened, minutes - 1, valve, p2))
    
        if current_id not in opened and current_valve.pressure > 0 and minutes > 0:
            opened = set(opened)
            opened.add(current_id)
            minutes -= 1
            released = minutes * current_valve.pressure
            
            for valve in current_valve.tunnels:
                relief = max(relief,
                             released + relief_pressure(frozenset(opened), minutes-1, valve, p2))
        
        return relief
    
    print(relief_pressure(frozenset(), 30, 'AA'))
    print(relief_pressure(frozenset(), 26, 'AA', p2=True))
        
main()