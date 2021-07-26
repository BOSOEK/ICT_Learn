from googlesearch import search

query = input("무엇을 검색하고 싶으신가요?")

for i in search(query, start = 0, stop=20):
    print(i)