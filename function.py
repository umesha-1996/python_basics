def greet():
    print("hello")

greet()

def print_name(name):
    print(name)

print_name("uma")

def print_full_name(firstname, lastname = "ravihari"):
    print(firstname + " " + lastname)

print_full_name("umesha")
print_full_name("channa", "sandaruwan")


def get_sum(no_one, no_two):
    return no_one + no_two

summation = get_sum(5,5)
print(summation)

def greet(name, age):
    print(f"Name : {name}, Agee : {age}")

greet(age=29, name="umesha")


def add(*args):
    return sum(args)

result = add(1, 2, 3, 4)
print(result)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

