#!/usr/bin/env python3
"""Query school documents by topic."""


def schools_by_topic(mongo_collection, topic):
    """Return all school documents whose topics include the given value."""
    return list(mongo_collection.find({"topics": topic}))
