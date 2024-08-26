name = "Kinley Tobgay Lhendrup"
age = 19
height = 165
is_student = True

person_info = {
    "name": name,
    "age": 19, 
    "height": 165,
    "is_student": is_student
}
print(person_info)

person_info["favorite_color"] = "blue"
print(person_info)

try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")

