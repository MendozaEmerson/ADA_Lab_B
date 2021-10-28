
# Emerson Danny Mendoza Hilasaca
# 4. What is the time complexity in terms of O()?
# O(n * m)
# n: La primera iteracion O(n)
# m: La iteracion dentro de la primera iteracion O(m)
"fgh" "abcdefghi"
def find_needle(needle, haystack)
    needle_index = 0
    haystack_index = 0
    
    while haystack_index < haystack.length
        if needle[needle_index] == haystack[haystack_index]
            found_needle = true
            while needle_index < needle.length:
                if needle[needle_index] != haystack[haystack_index + needle_index]
                    found_needle = false
                break
            end
            needle_index += 1
            end
        return true if found_needle
        needle_index = 0
        end
        haystack_index += 1
    end
    return false
end

# La complejidad se debe a la iteracion que se presenta de valores distintos uno contenido en otro.