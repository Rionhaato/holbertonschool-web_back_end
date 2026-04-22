#!/usr/bin/env python3
"""Provide a helper function for computing pagination indexes."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return the start and end indexes for the requested page."""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
