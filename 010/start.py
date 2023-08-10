# Functions with Outputs

# def my_function():
#     result = 3 * 2
#     return result


# output = my_function()

# print(output)

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return formated_f_name + " " + formated_l_name

formated_string = format_name(input("What is your first name?"), input("What is your last name?"))

print(formated_string)
