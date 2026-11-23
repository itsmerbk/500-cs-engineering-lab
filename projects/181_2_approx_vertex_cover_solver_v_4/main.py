def approx_vertex_cover(edges):
    cover = set()
    for u, v in edges:
        if u not in cover and v not in cover:
            cover.add(u); cover.add(v)
    return cover

if __name__ == "__main__":
    e = [(i, i + 1) for i in range(4 - 1)]
    vc = approx_vertex_cover(e)
    assert all(u in vc or v in vc for u, v in e)
