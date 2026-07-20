"""
Fishing Pool Knowledge

Loads fishing pool information used by Scout.
"""

from teo.knowledge.loader import load_json


def load_fishing_pools():
    """
    Load the fishing pool knowledge base.
    """

    return load_json("fishing_pools.json")


def get_fishing_pools():
    """
    Return every fishing pool.
    """

    return load_fishing_pools()["fishing_pools"]


def get_pool(pool_id):
    """
    Return a single fishing pool by ID.
    """

    pools = get_fishing_pools()

    for pool in pools:
        if pool["pool_id"] == pool_id:
            return pool

    return None