def invert_hash(dictionary):
    final_dictionary = {}
    
    for key, value in dictionary.items():
        final_dictionary[value] = key
        
    return final_dictionary

print(invert_hash(
    { 'a' : 1,
      'b' : 2,
      'c' : 3 }
))
