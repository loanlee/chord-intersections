# Count Intersections

This Python script calculates the number of intersections between chords on a circle based on the given radians and identifiers.

## Algorithm Explanation

1. **Input Processing**:
   - The script takes a list of radians and a list of identifiers as input
   - The radians and identifiers are processed into a dictionary where the keys represent chord numbers and the values are lists of radian values
   - Each list of radian values has 2 floats, corresponding to the start and end points of the chords
   - Each list is then sorted - this fixes the smaller item in the list to be the starting points

2. **Chord Intersection Calculation**:
   - The algorithm iterates through the list of chords and compares each chord with the remaining chords
   - For each pair of chords, it checks if their respective radian values form an intersection on the circle
   - For any two chords, there are two orientations that yield an intersection. Going clockwise, if the points are in the order
      -  s1 < s2 < e1 < e2 i.e. e1 is between s2 and e2
      -  s2 < s1 < e2 < e1 i.e. e2 is between s1 and e1
   - Since all starting and ending points are unique, checking for strict inequalties is enough
   - If an intersection is found, the intersection counter is incremented

3. **Output**:
   - The script returns the total number of intersections between chords on the circle.

## Time Complexity

The time complexity of the provided Python code can be broken down as follows:

- **Input Processing**: 
  - Iterating through the input lists to create a dictionary: O(n), where n is the length of the input lists.

- **Chord Intersection Calculation**:

  - Nested loop to check for intersections: O(n^2), where n is the number of items in the list.

Overall, the worst case time complexity of the code is O(n^2), where n is the length of the input lists.

## Requirements

- Python 3.x

## Usage

1. Clone the Repository:
   
    ```bash
    git clone https://github.com/loanlee/chord-intersections.git
    ```

2. Navigave to the directory containing `count_intersections.py` file


3. Run the script by entering the following command:

    ```bash
    python count_intersections.py
    ```

4. Follow the prompts to enter the two parallel list of radians and identifiers.

5. After entering the input, the script will display the number of intersections between the chords on the circle.

## Example

Suppose you want to calculate the number of intersections between chords with the following radians and identifiers:

- Radians: (0.9, 1.3, 1.7, 2.92)
- Identifiers: ('s1', 'e1', 's2', 'e2')

You would run the script as follows:

```bash
python count_intersections.py
```

Then, enter the radians separated by spaces when prompted:

```
Enter list of radians separated by spaces: 0.9 1.3 1.7 2.92
```

Next, enter the identifiers separated by spaces when prompted:

```
Enter list of identifiers separated by spaces: s1 e1 s2 e2
```

After entering the input, the script will display the number of intersections between the chords on the circle:

```
Number of intersections: 0
```
