# Python Variable Annotations

This project introduces type annotations in Python 3. It covers how to
annotate variables, function parameters, return values, higher-order
functions, and complex container types while keeping code compatible with
Python 3.9.

## Learning Objectives

- Understand type annotations in Python 3
- Use annotations to describe function signatures and variable types
- Apply duck typing with iterable and sequence-based annotations
- Validate annotated code with `mypy`

## Requirements

- All files are interpreted with Python 3.9 on Ubuntu 20.04 LTS
- Every Python file starts with `#!/usr/bin/env python3`
- All files end with a new line
- Code follows `pycodestyle` version `2.5`
- All modules, classes, and functions include real documentation
- All Python files are executable

## Files

- `0-add.py`: Typed function that returns the sum of two floats
- `1-concat.py`: Typed function that concatenates two strings
- `2-floor.py`: Typed function that returns the floor of a float
- `3-to_str.py`: Typed function that converts a float to a string
- `4-define_variables.py`: Annotated module-level variables
- `5-sum_list.py`: Typed function that sums a list of floats
- `6-sum_mixed_list.py`: Typed function that sums a mixed numeric list
- `7-to_kv.py`: Typed function that returns a string/float tuple
- `8-make_multiplier.py`: Typed function that returns a multiplier function
- `9-element_length.py`: Typed function using iterable and sequence duck typing

## Validation

You can validate style and typing with commands such as:

```bash
pycodestyle *.py
mypy *.py
```

Current local validation status:

- `pycodestyle` passes on all Python files in this project
- `mypy` reports `Success: no issues found in 10 source files`
