import copy

def is_numeric(value):
    if isinstance(value,str):
        return value.isnumeric()

def normalize_order(orders: dict) -> dict | None:

    if not bool(orders):
        #if the whole dictionary was empty , None will be returned
        return None

    else: 
        #if it was not empty, it will be validated
        for order in orders.values():
            
            if order["order_timestamp"] is None or order["order_timestamp"] == "" :
                order["order_timestamp"] = ""

            elif not is_numeric(order["order_timestamp"]) :
                #the invalidity here is considered if there is any thing than numbers 
                #so by using a function we are checking the validation of each timestamp
                order["order_timestamp"] = "INVALID-TIMESTAMP"

            else:
                if  len(order["order_timestamp"]) == 16: 
                    #if the len of order_timestamp is 10, the format is based on seconds so by default we assumed it's second
                    # and if it's 16, the format is microsecond and we converted it by dividing by 1000000
                    order["order_timestamp"] = str(int(order["order_timestamp"]) // 1_000_000)
                    
        return orders

    
#here because we didn't have sample data , we used this with different issues as examples to check for each timestamp value
orders = {
    "1": {"order_name": "Cream", "order_timestamp": "1777118400000000"},
    "2": {"order_name": "snack", "order_timestamp": "1777118500"},
    "3": {"order_name": "book", "order_timestamp": ""},
    "4": {"order_name": "shoes", "order_timestamp": "17771187cc0000000"},
    "5": {"order_name": "shoes", "order_timestamp": None}
}
copyOrders = copy.deepcopy(orders) #to prevent changing main data we create a copy of it 


# print("BEFORE calling normalize_order()") #because copy of main data is being sent so the result of Before and After is equivalent
# print(orders)
# BEFORE calling normalize_order()
# {'1': {'order_name': 'Cream', 'order_timestamp': '1777118400000000'}, '2': {'order_name': 'snack', 'order_timestamp': '1777118500'}, '3': {'order_name': 'book', 'order_timestamp': ''}, '4': {'order_name': 'shoes', 'order_timestamp': '17771187cc0000000'}}

converted_orders = normalize_order(copyOrders) #calling the normalize_order() to change the copied dictionary

if converted_orders is None:
    print("The dictionary is Empty")
else:
    for key, value in converted_orders.items(): 
        print(f"{key} : {value}")

# print("AFTER calling normalize_order()") #because copy of main data is being sent so the result of Before and After is equivalent
# print(orders)
# AFTER calling normalize_order()
# {'1': {'order_name': 'Cream', 'order_timestamp': '1777118400000000'}, '2': {'order_name': 'snack', 'order_timestamp': '1777118500'}, '3': {'order_name': 'book', 'order_timestamp': ''}, '4': {'order_name': 'shoes', 'order_timestamp': '17771187cc0000000'}}
