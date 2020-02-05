
def alphabetic_permutations(characters: str):
    def generate_permutations(chars, permutation=None):
        permutation = permutation or ''
        if len(permutation) == len(chars):
            permutations.append(permutation)

        for char in chars:
            if char not in permutation:
                permutation += char
                generate_permutations(chars, permutation)
                permutation = permutation[:-1]

    permutations = list()
    generate_permutations(characters)

    return permutations


print(alphabetic_permutations('012'))  # ['012', '021', '102', '120', '201', '210']
