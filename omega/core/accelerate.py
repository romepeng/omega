#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Aaron-Yang [code@jieyu.ai]
Contributors:

"""
import logging
import warnings

from numba import NumbaPendingDeprecationWarning

warnings.filterwarnings("ignore", category=NumbaPendingDeprecationWarning)

logger = logging.getLogger(__name__)


def merge(left, right, by):
    """
    njit fail if one of left, right contains object, not plain type, but the loop is
    very fast, cost 0.0001 seconds
    Args:
        left:
        right:
        by:

    Returns:

    """
    i, j = 0, 0

    while j < len(right) and i < len(left):
        if right[j][by] < left[by][i]:
            j += 1
        elif right[j][by] == left[by][i]:
            left[i] = right[j]
            i += 1
            j += 1
        else:
            i += 1

    return left