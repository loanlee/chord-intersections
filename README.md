# Count Intersections

This Python script calculates the number of intersections between chords on a circle based on the given radians and identifiers.

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
