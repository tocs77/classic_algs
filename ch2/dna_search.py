import enum
import typing

Nucleotide: enum.IntEnum = enum.IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = typing.Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = typing.List[Codon]


gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if(i+2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]],
                        Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene)-1
    while low <= high:
        mid: int = (low+high) // 2
        if gene[mid] < key_codon:
            low = mid+1
        elif gene[mid] > key_codon:
            high = mid-1
        else:
            return True
    return False


acg: Codon = (Nucleotide['A'], Nucleotide['C'], Nucleotide['G'])
gat: Codon = (Nucleotide['G'], Nucleotide['A'], Nucleotide['T'])

my_gene: Gene = string_to_gene(gene_str)
my_sorted_gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
