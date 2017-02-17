def to_rna(dna):
    result_dict = {
            'C': 'G',
            'G': 'C',
            'A': 'U',
            'T': 'A'
            }
    def dict_lookup(letter):
        return result_dict[letter]
    return ''.join(map(dict_lookup, dna))
