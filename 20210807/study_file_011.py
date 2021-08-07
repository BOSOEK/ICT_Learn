import csv

def write_to_csv_list():
    with open("product.csv", "w", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "분류", "상품명", "수량", "가격"])
        writer.writerow([41, "가구", "의자", 10, 100])
        writer.writerow([20, "식품", "라면", 20, 1500])
        writer.writerow([13, "가전제품", "TV", 30, 100000])

def write_to_csv_dictionary():
    with open("product.csv", "w", encoding="UTF-8") as file:
        headers = ["ID", "분류", "상품명", "수량", "가격"]
        writer = csv.DictWriter(file, fieldnames = headers)
        writer.writeheader()

        item = {
            "ID" : 41,
            "분류" : "가구",
            "상품명" : "의자",
            "수량" : 39,
            "가격" : 30
        }
        writer.writerow(item)

        items = [{
            "ID" : 41,
            "분류" : "가구",
            "상품명" : "의자",
            "수량" : 39,
            "가격" : 30
        },
        {
            "ID" : 41,
            "분류" : "가구",
            "상품명" : "의자",
            "수량" : 39,
            "가격" : 30
        }]
        writer.writerows(items)

if __name__ == "__main__":
    write_to_csv_list()
    write_to_csv_dictionary()