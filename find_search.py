from helpers.gen_helpers import line_break

def find_needle_in_haystack(needle: str, haystack: str) -> int:
    found_idx: int = - 1
    haystack_len: int = len(haystack); needle_len: int = len(needle)

    if not needle: return -1

    ## notes for classs ##
    ## think of it this way 
    ## we only have to iterate to a position in the <haystack> until IDX of haystack <= (len(haystack) - len(needle)
    ## no point iteration values which cannot 'fit' 'needle' at the end

    for i in range(haystack_len + 1 - needle_len): ## yes that looks weird, stop to explain!
        for j in range(needle_len):
            ## case if the values are not equal
            ## break and keep search further down the <haystack>
            if needle[j] != haystack[i + j]:
                break
            else:
                if j == needle_len - 1: 
                    ## we are at the end
                    ## found the first start IDX 
                    return i
    
    return found_idx ## or we can just do -1

line_break()
print("Test Haystack: {mississippi}, Needle: {sissip}" )
print("Expected output?: 3")
print("Actual output: " + str(find_needle_in_haystack("sissip", "mississippi")))
line_break()
