def is_anagram(s: str, t: str) -> bool:
    if len(s) == 0:
        return False

    if len(s) != len(t):
        return False

    def make_hashmap(some_string: str) -> dict[str, int]:
        hashmap = dict()
        for c in some_string:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] += 1
        return hashmap

    return make_hashmap(s) == make_hashmap(t)


def test_is_anagram_1():
    assert is_anagram(s='anagram', t='nagaram')


def test_is_anagram_2():
    assert not is_anagram(s='rat', t='car')
