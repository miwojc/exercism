"""
    ispangram(input)

Return `true` if `input` contains every alphabetic character (case insensitive).

"""
function ispangram(input)
    letters = Set{Char}()
    for c in input
        if isletter(c)
            push!(letters, lowercase(c))
        end
    end
    return length(letters) == 26
end

