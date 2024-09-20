from solutions.CHK import checkout_solution


class TestCheckout:
	def test_simple(self):
		assert checkout_solution.checkout(['A', 'A']) == 100
	
	def test_ignore(self):
		assert checkout_solution.checkout(['F']) == -1
	
	def test_complex(self):
		assert checkout_solution.checkout(['A', 'A', 'A', 'A', 'B', 'D']) == 225
	
	def test_complex2(self):
		assert checkout_solution.checkout(['A'] * 9 + ['B', 'D']) == 200 + 130 + 50 + 30 + 15
	
	# def test_complex3(self):
	#     assert checkout_solution.checkout(['A']*9+['B', 'D']+['E', 'E']) == 200+130+50+80+15
	#
	# def test_complex4(self):
	#     assert checkout_solution.checkout(['A']*9+['B', 'B', 'D']+['E', 'E']) == 200+130+50+80+15+22.5
	#
	# def test_complex5(self):
	#     assert checkout_solution.checkout(['A']*9+['B', 'B', 'B', 'D']+['E', 'E', 'E']) == 200+130+50+120+15+50
	
	def test_complex6(self):
		assert checkout_solution.checkout(['E', 'E', 'E']) == 120
	
	def test_complex7(self):
		assert checkout_solution.checkout(["A", "A", "B", "B", "E", "E", "C", "C", "D", "D"]) == 280
	
	def test_complex8(self):
		assert checkout_solution.checkout(["CCADDEEBBA"]) == 280
		
	def test_complex9(self):
		assert checkout_solution.checkout(["AAAAAEEBAAABB"]) == 455

# - {"method": "checkout", "params": ["ABCDEABCDE"], "id": "CHK_R2_038"}, expected: 280, got: 272
# - {"method": "checkout", "params": ["CCADDEEBBA"], "id": "CHK_R2_039"}, expected: 280, got: 272
# - {"method": "checkout", "params": ["AAAAAEEBAAABB"], "id": "CHK_R2_040"}, expected: 455, got: 460


