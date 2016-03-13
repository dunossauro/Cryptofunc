from string import ascii_uppercase as alphabet

func = lambda l: alphabet[(alphabet.find(l.upper()) + 13) % 26]

assert "".join(map(func, "RQHNEQB")) == "EDUARDO"
assert "".join(map(func, "EDUARDO")) == "RQHNEQB"
