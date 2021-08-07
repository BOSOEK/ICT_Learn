import json

def display_json():
    with open(
        "example/monsters.json", 
        encoding="UTF-8"
    ) as f:
        content_json = json.load(f) 
        print(content_json)

if __name__ == "__main__":
    # display_json()
    with open(
        "example/monsters.json", 
        encoding="UTF-8"
    ) as f:
        content_json = json.load(f)
        for each_monster in content_json:
            print("안녕하세요! ", each_monster["monsterName"])
