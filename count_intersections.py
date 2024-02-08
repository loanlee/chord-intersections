from math import pi
from typing import List, Tuple, Dict

def count_intersections(inputs: List[Tuple[float, str]]) -> int:
    chord_radian_dict: Dict[int, List[float]] = {}
    for radian_value, chord_vertex in zip(inputs[0], inputs[1]):
        chord_number = int(chord_vertex[-1])
        if chord_number in chord_radian_dict.keys():
            chord_radian_dict[chord_number].append(radian_value)
            chord_radian_dict[chord_number].sort()
        else:
            chord_radian_dict[chord_number] = []
            chord_radian_dict[chord_number].append(radian_value)
            
    chords_list = list(chord_radian_dict.values())
    num_intersections = 0
    chords_list = list(chord_radian_dict.values())
    for i, chord1 in enumerate(chords_list):
        for chord2 in chords_list[i+1:]:
            if (chord1[0] < chord2[0] < chord1[1] < chord2[1]) or  (chord2[0] < chord1[0] < chord2[1] < chord1[1]):
                num_intersections += 1
                
    return num_intersections

def main() -> None:
    radians_str = input("Enter list of radians separated by spaces: ")
    radians = [float(r) for r in radians_str.split()]
    identifiers_str = input("Enter list of identifiers separated by spaces: ")
    identifiers = identifiers_str.split()
    inputs = [radians, identifiers]
    num_intersections = count_intersections(inputs)
    print("Number of intersections:", num_intersections)
    
if __name__ == "__main__":
    main()
    