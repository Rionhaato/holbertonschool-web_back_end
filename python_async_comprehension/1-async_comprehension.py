#!/usr/bin/env python3
"""Collect values from an asynchronous generator with a comprehension."""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Return ten random floats gathered from async_generator."""
    return [value async for value in async_generator()]
