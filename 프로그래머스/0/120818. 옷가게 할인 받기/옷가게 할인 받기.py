def solution(price):
    if price >= 500000:
        return int(price*(80/100))
    elif price >= 300000:
        return int(price*(90/100))
    elif price>=100000:
        return int(price*(95/100))
    else:
        return int(price) 
    
# def solution(price):
#     discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#     for discount_price, discount_rate in discount_rates.items():
#         if price >= discount_price:
#             return int(price * discount_rate)