func = lambda l: alfabeto[(alfabeto.find(l.upper()) + 13) % 26]

assert "".join(map(func, "RQHNEQB")) == "EDUARDO"
assert "".join(map(func, "EDUARDO")) == "RQHNEQB"
