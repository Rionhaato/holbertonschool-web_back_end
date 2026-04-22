#!/usr/bin/env python3
"""Implement basic pagination over the baby names dataset."""

import csv
from typing import List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Serve paginated rows from the CSV dataset."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with empty dataset caches."""
        self.__dataset: List[List[str]] = []

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset without the header row."""
        if not self.__dataset:
            with open(self.DATA_FILE, mode="r", encoding="utf-8") as file:
                dataset = csv.reader(file)
                next(dataset)
                self.__dataset = [row for row in dataset]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return the rows for a given page and page size."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
