
input_str = input("Enter a hyphen-separated sequence of words as input : ")

words_list = input_str.split("-")
sorted_words = sorted(words_list)
output_str = ""

for i in sorted_words:
    output_str += i + "-"


output_str = output_str[:-1]

print(output_str)
