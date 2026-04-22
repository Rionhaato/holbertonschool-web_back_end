#!/usr/bin/env python3
"""Implement deletion-resilient hypermedia pagination."""

import csv
from typing import Dict, List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Serve deletion-resilient pages from the CSV dataset."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize dataset caches for page lookups."""
        self.__dataset: List[List[str]] = []
        self.__indexed_dataset: Dict[int, List[str]] = {}

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset without its header row."""
        if not self.__dataset:
            with open(self.DATA_FILE, mode="r", encoding="utf-8") as file:
                dataset = csv.reader(file)
                next(dataset)
                self.__dataset = [row for row in dataset]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Create an indexed dataset for deletion-resilient pagination."""
        if not self.__indexed_dataset:
            truncated_dataset = self.dataset()[:1000]
            self.__indexed_dataset = {
                index: row for index, row in enumerate(truncated_dataset)
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """Return a deletion-resilient page starting at the given index."""
        assert index is not None and isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        max_index = max(indexed_dataset)
        assert index <= max_index

        data: List[List[str]] = []
        current_index = index

        while len(data) < page_size and current_index <= max_index:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data,
        }
