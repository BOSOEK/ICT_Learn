import json

# 파이썬의 딕셔너리 (dictionary) format은 JSON과 동일
def generate_dictionary(monster_name, title, price, scariness):
    return {
        "monster_name" : monster_name,
        "title" : title,
        "price" : price,
        "scariness" : scariness
    }

if __name__ == "__main__":
    monster_one = generate_dictionary(
        "Filo",
        "Baker by Day, Techie by Night",
        29, 3
    )
    monster_two = generate_dictionary(
        "Timber",
        "Database Expert",
        19, 2
    )
    print(type(monster_one))
    print(monster_one)
    with open("monster.json", "w", encoding="UTF-8") as file:
        json.dump([monster_one, monster_two], file)