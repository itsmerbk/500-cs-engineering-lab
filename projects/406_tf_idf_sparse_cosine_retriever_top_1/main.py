from collections import Counter
import math

def tfidf_search(docs, query, k=1):
    toks = [d.lower().split() for d in docs]; N = len(docs)
    df = Counter(t for doc in toks for t in set(doc))
    def vec(words):
        tf = Counter(words)
        return {w: (c / len(words)) * math.log((N + 1) / (df[w] + 1)) for w, c in tf.items() if w in df}
    qv = vec(query.lower().split())
    scored = sorted(range(N), key=lambda i: sum(qv.get(w, 0)*val for w, val in vec(toks[i]).items()), reverse=True)
    return scored[:k]

if __name__ == "__main__":
    corpus = ["distributed raft consensus", "sql query optimizer", "neural network backprop", "lsm tree storage", "tcp packet routing"]
    assert tfidf_search(corpus, "raft distributed")[0] == 0
