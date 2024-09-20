from solutions.CHK import checkout_solution


class TestCheckout:
	def test_simple(self):
		assert checkout_solution.checkout(['A', 'A']) == 100
	
	def test_ignore(self):
		assert checkout_solution.checkout(['AP']) == -1
	
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
	
	def test_complex15(self):
		assert checkout_solution.checkout([i for i in "FFFFFFFFF"]) == 50
	
	def test_complex16(self):
		assert checkout_solution.checkout([i for i in "UUU"]) == 120
		
	def test_complex17(self):
		assert checkout_solution.checkout([i for i in "UUUU"]) == 120
		
	def test_complex18(self):
		assert checkout_solution.checkout([i for i in "UUUUUU"]) == 200
	
	def test_complex19(self):
		assert checkout_solution.checkout([i for i in "NNNMM"]) == 135
		
	def test_complex20(self):
		assert checkout_solution.checkout([i for i in "RRRRRRQQ"]) == 300
		
	def test_complex21(self):
		assert checkout_solution.checkout([i for i in "NNNM"]) == 120
		
	def test_complex22(self):
		assert checkout_solution.checkout([i for i in "RRRQRQRR"]) == 300
		
	def test_complex23(self):
		assert checkout_solution.checkout([i for i in "STX"]) == 45

	def test_complex25(self):
		assert checkout_solution.checkout([i for i in "SZXXVV"]) == 152

	def test_complex26(self):
		assert checkout_solution.checkout([i for i in "K"]) == 70

	def test_complex27(self):
		assert checkout_solution.checkout([i for i in "ABCDEFGHIJKLMNOPQRSTUVW"]) == 795

	def test_complex28(self):
		assert checkout_solution.checkout([i for i in "SSSZ"]) == 65
		
	def test_complex29(self):
		assert checkout_solution.checkout([i for i in "STXS"]) == 62



