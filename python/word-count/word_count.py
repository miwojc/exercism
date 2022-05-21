import re
from collections import Counter, OrderedDict
from string import punctuation


class OrderedCounter(Counter, OrderedDict):
    "Counter that remembers the order elements are first seen"

    def __repr__(self):
        return f"{self.__class__.__name__}({OrderedDict(self)})"

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


def count_words(sentence):
    return dict(
        OrderedCounter(
            (
                sen.strip(punctuation)
                for sen in sentence.lower().replace(",", " ").replace("_", " ").split()
            )
        )
    )
