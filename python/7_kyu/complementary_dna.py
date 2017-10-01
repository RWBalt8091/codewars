def DNA_strand(dna):
    output = ''
    for char in dna:
        if char == 'A':
            output = output + 'T'
        elif char == 'T':
            output = output + 'A'
        elif char == 'C':
            output = output + 'G'
        else:
            output = output + 'C'
    return output