from typing import List, Dict, TypeVar

T = TypeVar('T', float, str)

def count_intersections(inputs: List[List[T]]) -> int:
    """
    Calculate the number of intersections between chords on a circle.

    Args:
        inputs (List[List[T]]): A list of lists, first list[float] 
        containing radians and second list[str] containing identifiers.

    Returns:
        int: The number of intersections between chords on the circle.
    """
    chord_radian_dict: Dict[int, List[float]] = {}
    for radian_value, chord_vertex in zip(inputs[0], inputs[1]):
        chord_number = int(chord_vertex[-1])
        if chord_number in chord_radian_dict:
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
            if (chord1[0] < chord2[0] < chord1[1] < chord2[1]) or (chord2[0] < chord1[0] < chord2[1] < chord1[1]):
                num_intersections += 1

    return num_intersections


def main() -> None:
    """
    Main function to execute the count_intersections function.

    Prompts the user to enter the list of radians and identifiers,
    calculates the number of intersections between chords on a circle,
    and prints the result.

    Returns:
        None
    """
    radians_str = input("Enter list of radians separated by spaces: ")
    radians = [float(r) for r in radians_str.split()]
    identifiers_str = input("Enter list of identifiers separated by spaces: ")
    identifiers = identifiers_str.split()
    inputs = [radians, identifiers]
    num_intersections = count_intersections(inputs)
    print("Number of intersections:", num_intersections)


if __name__ == "__main__":
    main()
