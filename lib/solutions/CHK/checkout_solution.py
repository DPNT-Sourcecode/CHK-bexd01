from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	price_table = {
		'A': lambda quantity: (quantity % 3) * 50 + (quantity // 3) * 130,
		'B': lambda quantity: (quantity % 2) * 30 + (quantity // 2) * 45,
		'C': lambda quantity: quantity * 20,
		'D': lambda quantity: quantity * 15
	}
	if any([item not in price_table.keys() for item in skus]):
		return -1
	
	skus_cnt = Counter(skus)
	
	price = 0
	for item, quantity in skus_cnt.items():
		price += price_table[item](quantity)
	return price

