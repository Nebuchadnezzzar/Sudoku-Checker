# Sudoku-Checker

**A tiny program validating a traditional 9x9 Sudoku.**

Sudoku requires that every row, column and 3x3 square contain all digits from 1 to 9. As no duplicates are allowed, no rows, columns or regions can be identical. The program accepts Python matrix, a list with 9 lists consisting of 9 elements, as an input, for example:

```python
filled_sudoku = 
[[1, 3, 2, 5, 7, 9, 4, 6, 8],
[4, 9, 8, 2, 6, 1, 3, 7, 5], 
[7, 5, 6, 3, 8, 4, 2, 1, 9],
[6, 4, 3, 1, 5, 8, 7, 9, 2],
[5, 2, 1, 7, 9, 3, 8, 4, 6],
[9, 8, 7, 4, 2, 6, 5, 3, 1],
[2, 1, 4, 9, 3, 5, 6, 8, 7],
[3, 6, 5, 8, 1, 7, 9, 2, 4],
[8, 7, 9, 6, 4, 2, 1, 5, 3]]
```
