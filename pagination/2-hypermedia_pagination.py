#!/usr/bin/env python3
"""Implement hypermedia pagination over the baby names dataset."""

import csv
import math
from typing import Dict, List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Serve paginated rows and hypermedia metadata from the dataset."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server with an empty cached dataset."""
        self.__dataset: List[List[str]] = []

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset without its header row."""
        if not self.__dataset:
            with open(self.DATA_FILE, mode="r", encoding="utf-8") as file:
                dataset = csv.reader(file)
                next(dataset)
                self.__dataset = [row for row in dataset]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return the rows for the requested page."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary containing page data and hypermedia fields."""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
