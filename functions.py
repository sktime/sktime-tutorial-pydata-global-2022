# -*- coding: utf-8 -*-
import itertools
from typing import List, Tuple

from sklearn.base import BaseEstimator
from sktime.transformations.base import BaseTransformer


# TODO: possibly add this to sktime as a general utils function
def get_all_permutations(steps: List[Tuple[str, BaseEstimator]]) -> List[List[str]]:
    """Utils functions for Permute to get all possible transformer permutations.

    Parameters
    ----------
    steps : List[Tuple[str, BaseEstimator]]
        Steps as defined for a pipeline class.

    Returns
    -------
    List[List[str]]
        A list of lists with all possible transformer combinations.

    """
    steps_preprocess = []
    steps_postprocess = []

    names, estimators = zip(*steps)
    for name, est in zip(names, estimators):
        if isinstance(est, BaseTransformer):
            steps_preprocess.append(name)
        else:
            steps_postprocess = list(set(names) - set(steps_preprocess))
            break

    # create permutations of pre-preocessing steps
    tuples = list(itertools.permutations(steps_preprocess))
    permutations = [list(x) for x in tuples]
    permutations = [x for x in permutations if len(x) == len(set(x))]

    # append forecaster and post-processing steps to permutations
    for i in range(len(permutations)):
        permutations[i] = permutations[i] + steps_postprocess

    return permutations
