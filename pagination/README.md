# Pagination

This project covers common pagination patterns for backend datasets in
Python. It includes basic index-range helpers, page/page-size pagination,
hypermedia pagination metadata, and deletion-resilient pagination.

## Learning Objectives

- Paginate a dataset with `page` and `page_size`
- Return pagination metadata with hypermedia fields
- Build deletion-resilient pagination logic

## Requirements

- Python `3.9` on Ubuntu 20.04 LTS
- All Python files start with `#!/usr/bin/env python3`
- All files end with a new line
- Code follows `pycodestyle` version `2.5.*`
- All modules, classes, and functions include real documentation
- All functions are fully type-annotated

## Files

- `0-simple_helper_function.py`: Return start and end indexes for a page
- `1-simple_pagination.py`: Basic `Server` class with page-based pagination
- `2-hypermedia_pagination.py`: Pagination with hypermedia metadata
- `3-hypermedia_del_pagination.py`: Deletion-resilient pagination
- `Popular_Baby_Names.csv`: Source dataset used by the server classes

## Dataset

Place `Popular_Baby_Names.csv` in this directory. The project code expects
the CSV file to be located next to the Python modules.
