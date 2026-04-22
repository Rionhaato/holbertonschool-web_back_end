#!/usr/bin/env python3
"""Update the topics for school documents in MongoDB."""


def update_topics(mongo_collection, name, topics):
    """Replace the topics list for all documents matching the school name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
