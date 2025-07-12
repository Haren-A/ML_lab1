def highest_occurring_char(matrix, m):
    
    if not matrix or not matrix[0]:
        return None, 0
    
    input_string = ''.join(matrix[0]).lower()
    
    
    char_count = {}
    for char in input_string:
        if char.isalpha():  
            char_count[char] = char_count.get(char, 0) + 1
    
    if not char_count:
        return None, 0
    
    
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return max_char, max_count


A = [['H', 'i', 'p', 'p', 'o'], ['p', 'o', 't', 'a', 'm'], ['u', 's']]
m = 3
char, count = highest_occurring_char(A, m)
print(f"Maximally occurring character is '{char}' & occurrence count is {count}")
