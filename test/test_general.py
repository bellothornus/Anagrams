from src.code import anagrams

def test_abba():
    assert anagrams("abba",["aabb","abcd","bbaa","dada"]) == ["aabb","bbaa"]
    assert anagrams("racer", ["crazer","carer","racar","caers","racer"]) == ["carer","racer"]