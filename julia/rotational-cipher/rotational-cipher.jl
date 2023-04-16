# This function rotates a character by n
# If c is a letter, it rotates it by n
# If c is not a letter, it returns it unchanged
function rotate(n::Int, c::Char)
    if c in 'a':'z'
        'a' + (c - 'a' + n) % 26
    elseif c in 'A':'Z'
        'A' + (c - 'A' + n) % 26
    else
        c
    end
end

function rotate(n::Int, str::AbstractString)
    map(c -> rotate(n, c), str)
end

function rotate(n::Int, c::Char)
    if c in 'a':'z'
        'a' + (c - 'a' + n) % 26
    elseif c in 'A':'Z'
        'A' + (c - 'A' + n) % 26
    else
        c
    end
end