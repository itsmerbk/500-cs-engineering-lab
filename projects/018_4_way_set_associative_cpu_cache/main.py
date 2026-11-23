from collections import OrderedDict

def sim_cache(trace, sets=4, ways=4):
    cache = [OrderedDict() for _ in range(sets)]
    hits = misses = 0
    for addr in trace:
        idx, tag = addr % sets, addr // sets
        if tag in cache[idx]:
            hits += 1; cache[idx].move_to_end(tag)
        else:
            misses += 1
            if len(cache[idx]) >= ways: cache[idx].popitem(last=False)
            cache[idx][tag] = True
    return hits, misses

if __name__ == "__main__":
    h, m = sim_cache([0, 0, 4, 4, 8, 0, 4, 0])
    assert h + m == 8 and h >= 2
