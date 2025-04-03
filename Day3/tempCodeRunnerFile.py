def CustomerDiscount(customers):
    eligibleCustomers = list(filter(lambda customer: customer["age"] <= 40, customers))

    def adjust_discount(customer):
        if 18 <= customer["age"] <= 25:
            discounted_price = round(customer["total_purchase"] * 0.90)
        elif 26 <= customer["age"] <= 40:
            discounted_price = round(customer["total_purchase"] * 0.95)
        else:
            return customer

        return {"name": customer["name"], "age": customer["age"], "total_purchase": discounted_price}

    selected_customers = list(map(adjust_discount, eligibleCustomers))

    no_discount_customers = list(filter(lambda customer: customer["age"] > 40, customers))
    for cust in no_discount_customers:
        print(f"{cust['name']} (Age {cust['age']}) - No Discount")

    print(selected_customers)

customers = [
    {"name": "Rogers", "age": 35, "total_purchase": 520},
    {"name": "Thor", "age": 50, "total_purchase": 350},
    {"name": "Thanos", "age": 28, "total_purchase": 610},
    {"name": "Peter", "age": 20, "total_purchase": 250}
]

CustomerDiscount(customers)