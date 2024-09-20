from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	def calAprice(quantity):
		res = 0
		res += (quantity // 5) * 200
		res += ((quantity % 5) // 3) * 130
		res += (quantity % 5) % 3 * 50
		return res
	price_table = {
		'A': calAprice,
		'B': lambda quantity: (quantity % 2) * 30 + (quantity // 2) * 45,
		'C': lambda quantity: quantity * 20,
		'D': lambda quantity: quantity * 15,
		'E': lambda quantity: quantity * 40,
		'F': lambda quantity: quantity * 10,
	}
	if any([item not in price_table.keys() for item in skus]):
		return -1
	
	skus_cnt = Counter(skus)
	
	price = 0
	
	for item, quantity in skus_cnt.items():
		price += price_table[item](quantity)
	
	# Todo make it unifrom
	if skus_cnt.get('E', 0) >= 2:
		freeB = skus_cnt['E'] // 2
		currB = skus_cnt.get('B', 0)
		if currB > 0:
			price -= price_table['B'](currB)
			price += price_table['B'](currB-freeB)
	if skus_cnt.get('F', 0) > 2:
		price -= price_table['F'](skus_cnt.get('F', 0) %2)
	return int(price)


