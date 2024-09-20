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
		'B': lambda quantity: calculate_price(quantity, [(2, 45), (1, 30)]),
		'C': lambda quantity: calculate_price(quantity, [(1, 20)]),
		'D': lambda quantity: calculate_price(quantity, [(1, 15)]),
		'E': lambda quantity: calculate_price(quantity, [(1, 40)]),
		'F': lambda quantity: calculate_price(quantity, [(1, 10)]),
		'G': lambda quantity: calculate_price(quantity, [(1, 20)]),
		'H': lambda quantity: calculate_price(quantity, [(10, 80), (5, 45), (1, 10)]),
		'I': lambda quantity: calculate_price(quantity, [(1, 35)]),
		'J': lambda quantity: calculate_price(quantity, [(1, 60)]),
		'K': lambda quantity: calculate_price(quantity, [(2, 150), (1, 80)]),
		'L': lambda quantity: calculate_price(quantity, [(1, 90)]),
		'M': lambda quantity: calculate_price(quantity, [(1, 15)]),
		'N': lambda quantity: calculate_price(quantity, [(1, 40)]),
		'O': lambda quantity: calculate_price(quantity, [(1, 10)]),
		'P': lambda quantity: calculate_price(quantity, [(5, 200),(1, 50)]),
		'Q': lambda quantity: calculate_price(quantity, [(3, 80),(1, 30)]),
		'R': lambda quantity: calculate_price(quantity, [(1, 50)]),
	}
	def cal_diff(sku1, sku2, sku1_bundle, skus_cnt):
		price = 0
		if skus_cnt.get(sku1, 0) >= sku1_bundle:
			freeSKU2 = skus_cnt[sku1] // sku1_bundle
			currSKU2 = skus_cnt.get(sku2, 0)
			if currSKU2 > 0:
				price -= price_table['B'](currSKU2)
				price += price_table['B'](currSKU2 - freeSKU2)
		return price
	promotable = {
		'E': lambda sku_q: cal_diff('E', 'B', 2, sku_q)
	}
	if any([item not in price_table.keys() for item in skus]):
		return -1
	
	skus_cnt = Counter(skus)
	
	price = 0
	
	for item, quantity in skus_cnt.items():
		price += price_table[item](quantity)
		if item in promotable:
			price += promotable[item](skus_cnt)

	if skus_cnt.get('F', 0) > 2:
		currF = skus_cnt['F']
		price -= price_table['F']((currF - 1) // 2)
	if skus_cnt.get('R', 0) >= 3:
		freeQ = skus_cnt['R'] // 3
		currQ = skus_cnt.get('Q', 0)
		if currQ > 0:
			price -= price_table['B'](currQ)
			price += price_table['B'](currQ - freeQ)
	return int(price)

