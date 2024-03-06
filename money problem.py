from itertools import permutations
def string_to_number(string, mapping):
    return int("".join(mapping[c] for c in string))
def is_mapping_possible(arr, s):
    unique_chars = set("".join(arr) + s)
    for perm in permutations("0123456789", len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if sum(string_to_number(word, mapping) for word in arr) == string_to_number(s, mapping):
            return True
    return False
if __name__ == "__main__":
    arr = ["SEND", "MONEY"]
    s = "MONEY"
    if is_mapping_possible(arr, s):
        print("Yes")
    else:
        print("No")
