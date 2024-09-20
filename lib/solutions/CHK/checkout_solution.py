from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	def calculate_price(quantity, pricing_rules):
		res = 0
		for rule in pricing_rules:
			bundle_size, bundle_price = rule
			res += (quantity // bundle_size) * bundle_price
			quantity %= bundle_size
		return res
	
	price_table = {
		'A': lambda quantity: calculate_price(quantity, [(5, 200), (3, 130), (1, 50)]),
		'B': lambda quantity: (quantity % 2) * 30 + (quantity // 2) * 45,
		'C': lambda quantity: quantity * 20,
		'D': lambda quantity: quantity * 15,
		'E': lambda quantity: quantity * 40,
		'F': lambda quantity: quantity * 10,
		'G': lambda quantity: quantity * 20,
		'H': lambda quantity: calculate_price(quantity, [(10, 80), (5, 45), (1, 10)]),
		'I': lambda quantity: quantity * 35,
		'J': lambda quantity: quantity * 60,
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
			price += price_table['B'](currB - freeB)
	if skus_cnt.get('F', 0) > 2:
		currF = skus_cnt['F']
		price -= price_table['F']((currF - 1) // 2)
	
	return int(price)






