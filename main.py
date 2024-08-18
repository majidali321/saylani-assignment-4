# q#1
movies=[]
name = input("enter your first name")
movies.append(name)
name = input("enter your first name")
movies.append(name)
name = input("enter your first name")
movies.append(name)
reverse = movies[::-1]
print(reverse)

# q3
user_list = list(map(int,input("enter your numbers").split()))

largest_num = user_list[0]

for num in user_list:
    if num > largest_num:
        largest_num = num

print(f"you num is {largest_num}")

# q4
element = input("enter your multipleelements for rotating").split()

rotate = [element[-1]] + element[:-1]
print("your rotated list  is: ",rotate)


# Q5

user_word = input("enter your words  ")
modified_word = user_word.replace(user_word,"").strip()
modified_word = " ".join(modified_word.split())
print("modified word is ")
print(modified_word)

# Q6
here we are going to make a dictionary
months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}
date = input("Enter a date in the format mm/dd/yyyy: ")
month, day, year =date.split("/")
day = str(int(day))
month_name = months[month]
print(f"{month_name} {day}, {year}")

# Q7
def capital_words(input_string):
    capital_string = input_string.title()
    return capital_string
# dendur
if __name__ == '__main__':
    user_input = input("Enter a sentence: ")
    final = capital_words(user_input)
    print("Capitalized sentence is:")
    print(final)

# q8
Function to calculate the sum of each row in a matrix
def sum_row(matrix):
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        print(f"Sum of row {i + 1} = {row_sum}")

if __name__ == '__main__':
    matrix = [
        [2, 11, 7, 12],
        [5, 2, 9, 15],
        [8, 3, 10, 42]
    ]
    for row in matrix:
        print(row)
    sum_row(matrix)

# q9
def add_matrices(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

if __name__ == '__main__':
    #  two matrices of size n x m
    matrix1 = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ]

    matrix2 = [
        [4, 4, 4],
        [5, 5, 5],
        [6, 6, 6]
    ]

    result_matrix = add_matrices(matrix1, matrix2)

    print("Resultant ")
    for row in result_matrix:
        print(row)

# Q10
def multiply_matrices(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)

    return result

if __name__ == '__main__':
    #  two matrices of size n x m
    matrix1 = [
        [1, 1, 1],
        [2, 2, 2],
        [3, 3, 3]
    ]

    matrix2 = [
        [4, 4, 4],
        [5, 5, 5],
        [6, 6, 6]
    ]

    result_matrix = multiply_matrices(matrix1, matrix2)

    print("Resultant ")
    for row in result_matrix:
        print(row)

