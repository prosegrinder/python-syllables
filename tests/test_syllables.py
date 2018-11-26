from __future__ import division
import re

import cmudict
import syllables

def test_estimate():
    EXPECTED_ACCURACY = .75
    hits = []
    misses = []

    d = cmudict.dict()
    for word in d:
        phones = d[word][0]
        cmudict_syllables = 0
        for phone in phones:
            if re.match(r"\w*[012]$", phone):
                cmudict_syllables += 1
        estimated_syllables = syllables.estimate(word)
        if cmudict_syllables == estimated_syllables:
            hits.append(word)
        else:
            misses.append(word)

    hit = len(hits)
    miss = len(misses)
    total = hit + miss
    ACCURACY = hit / total
    if (ACCURACY < EXPECTED_ACCURACY):
        raise AssertionError('syllables.estimate(): Expected accuracy of {0}, got {1}.'.format(
            EXPECTED_ACCURACY, ACCURACY))
