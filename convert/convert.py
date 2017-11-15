from itertools import groupby
from operator import itemgetter

def get_list(input):
    """
    Input list of ranges and return sequential list.
    """
    if type(input) != list:
        raise IndexError("type is not list()")
    elif len([i for i in input if type(i) is int]) != 0:
        raise IndexError("list contains int()")
    else:
        xranges = [(lambda l: xrange(l[0], l[-1] + 1))
                   (map(int, r.split('-'))) for r in input]
        return sorted(list(set([y for x in xranges for y in x])))

def get_ranges(input):
    """
    Input list of numbers and return sequential ranges.
    """
    seq_number_result = list()
    input = sorted([int(n) for n in input])
    
    for k, g in groupby(enumerate(input), lambda (i, x): i - x):
        seq_num = map(itemgetter(1), g)
        if len(seq_num) > 1:
            seq_number_result.append("%s-%s" % (seq_num[0], seq_num[-1]))
        else:
            seq_number_result.append(str(seq_num[0]))
    return seq_number_result

def to_table(pre_text,delim=" |",output=True):
    """
    Generates a padded table.
    Args:
        pre_text: a list of lists
        delim : the delimiter used between elements
        output : output type

    Returns:
        padded table or converted list of lists
    """
    colwidth = list()
    templist = list()
    for y in range(len(pre_text[0])):
        templist.append([])
        for x in range(len(pre_text)):
            templist[y].append(pre_text[x][y])
    for y in range(len(templist)):
        max = 0
        for a in templist[y][:]:
            if len(a) > max:
                max = len(a)
        colwidth.append(max)
    for y in pre_text[:]:
        for x in range(len(colwidth)):
            y[x] = y[x].ljust(colwidth[x]) + delim
    if output:
        for z in range(len(pre_text)):
            print "".join(pre_text[z])
        return True 
    return pre_text
