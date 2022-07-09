def append(list1, list2):
    "`append` (*given two lists, add all items in the second list to the end of the first list*)"
    return list1 + list2


def concat(lists):
    "`concatenate` (*given a series of lists, combine all items in all lists into one flattened list*)"
    return [el for lst in lists for el in lst]


def filter(function, list):
    "`filter` (*given a predicate and a list, return the list of all items for which `predicate(item)` is True*)"
    return [el for el in list if function(el)]


def length(list):
    "`length` (*given a list, return the total number of items within it*)"
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    "`map` (*given a function and a list, return the list of the results of applying `function(item)` on all items*)"
    return [function(el) for el in list]


def foldl(function, list, initial):
    "`foldl` (*given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left using `function(accumulator, item)`*)"
    accumulator = initial
    for el in list:
        accumulator = function(accumulator, el)
    return accumulator


def foldr(function, list, initial):
    "`foldr` (*given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right using `function(item, accumulator)`*)"
    accumulator = initial
    for el in list[::-1]:
        accumulator = function(el, accumulator)
    return accumulator


def reverse(list):
    "`reverse` (*given a list, return a list with all the original items, but in reversed order*)"
    return list[::-1]
