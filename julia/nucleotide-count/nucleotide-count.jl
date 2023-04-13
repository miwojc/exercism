"""
    count_nucleotides(strand)

The count of each nucleotide within `strand` as a dictionary.

Invalid strands raise a `DomainError`.

"""
function count_nucleotides(strand)
    if !all(x -> x in "ACGT", strand)
        throw(DomainError("Invalid strand"))
    end
    return Dict('A' => count(x -> x == 'A', strand),
                'C' => count(x -> x == 'C', strand),
                'G' => count(x -> x == 'G', strand),
                'T' => count(x -> x == 'T', strand))
end
