from itertools import product
contact_list = []
keys_repersentation_text_dict = { 
'2': ['a', 'b', 'c'],
'3': ['d', 'e', 'f'],
'4': ['g', 'h', 'i'],
'5': ['j', 'k', 'l'],
'6': ['m', 'n', 'o'],
'7': ['p', 'q', 'r', 's'],
'8': ['t', 'u', 'v'],
'9': ['w', 'x', 'y', 'z']
}

def create_string(result, string_touple):
    for i in string_touple:
        if type(i) == str:
            result += i
        else:
            result = create_string(result, i)
    return result

def find_releted_string(number):
    number_string = str(number)
    result_arr = None
    for digit in number_string:
        if not result_arr:
            result_arr = keys_repersentation_text_dict[digit]
            continue
        result_arr = product(result_arr, keys_repersentation_text_dict[digit])
    result_str_arr = [] 
    for item in result_arr:
        string = ""
        result_str_arr.append(create_string(string, item))
    return result_str_arr

print(find_releted_string(72343))
    
