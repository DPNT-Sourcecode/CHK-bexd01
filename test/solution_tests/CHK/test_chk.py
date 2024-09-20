from solutions.CHK import checkout_solution


class TestCheckout:
	def test_simple(self):
		assert checkout_solution.checkout(['A', 'A']) == 100
	
	def test_ignore(self):
		assert checkout_solution.checkout(['P']) == -1
	
	def test_complex(self):
		assert checkout_solution.checkout(['A', 'A', 'A', 'A', 'B', 'D']) == 225
	
	def test_complex2(self):
		assert checkout_solution.checkout(['A'] * 9 + ['B', 'D']) == 200 + 130 + 50 + 30 + 15

	def test_complex6(self):
		assert checkout_solution.checkout(['E', 'E', 'E']) == 120
	
	def test_complex7(self):
		assert checkout_solution.checkout(["A", "A", "B", "B", "E", "E", "C", "C", "D", "D"]) == 280
	
	def test_complex8(self):
		assert checkout_solution.checkout([i for i in "CCADDEEBBA"]) == 280
		
	def test_complex9(self):
		assert checkout_solution.checkout([i for i in "AAAAAEEBAAABB"]) == 455

	def test_complex10(self):
		assert checkout_solution.checkout([i for i in "FFF"]) == 20
	
	def test_complex11(self):
		assert checkout_solution.checkout([i for i in "FF"]) == 20

	def test_complex12(self):
		assert checkout_solution.checkout([i for i in "FFFF"]) == 30

	def test_complex14(self):
		assert checkout_solution.checkout([i for i in "FFFFFF"]) == 40
