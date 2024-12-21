# TODO решите задачу
def task() -> float:
    data = [
        {
            "score": 2.296152645028281,
            "weight": 1
        }
    ]

    total_product = 0
    for dictionary in data:
        score = dictionary["score"]
        weight = dictionary["weight"]

        product = score * weight
        total_product += product

    return round(total_product, 3)
result = task()
print(result)






