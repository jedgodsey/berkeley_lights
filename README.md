# BERKELEY LIGHTS TAKE-HOME PROJECT

## Part 1
I've created a class "Interval" to produce range objects for pen indices. Viewable in solution.py

## Part 2
I've created a function "parse_input" that parses and validates pen range entries. Viewable in solution.py

## Part 3
I've created a function "interval_synth" to reduce overlapping pen numbers and intervals to the most efficient objects.  Viewable in solution.py

## Part 3b
The function runs in O(n^2) time as the list of page entries must be looped over and then the entries themselves must be looped over with regular expressions to produce range objects. Space complexity is O(n)

## Unit Tests
I've created a series of unit tests "TestCases" to ensure proper function. Viewable in solution.py
