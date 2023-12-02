def solution_1():
    with open('./Day01/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    def get_first_digit(input_string):
        for char in input_string:
            if char.isdigit():
                return char
    
    return sum([int(get_first_digit(x) + get_first_digit(reversed(x))) for x in data])
        
def solution_2():
    with open('./Day01/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    def strs_to_nums(input_string):
        word_to_number_dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }
        
        new_str = ""
        for i in range(len(input_string)):
            if input_string[i: i + 3] in word_to_number_dict:
                new_str += str(word_to_number_dict[input_string[i: i + 3]])
            elif input_string[i: i + 4] in word_to_number_dict:
                new_str += str(word_to_number_dict[input_string[i: i + 4]])
            elif input_string[i: i + 5] in word_to_number_dict:
                new_str += str(word_to_number_dict[input_string[i: i + 5]])
            else:
                new_str += input_string[i]
                
        return new_str
    
    def get_first_digit(input_string):
        for char in input_string:
            if char.isdigit():
                return char
    
    return sum([int(get_first_digit(strs_to_nums(x)) + get_first_digit(reversed(strs_to_nums(x)))) for x in data])


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())