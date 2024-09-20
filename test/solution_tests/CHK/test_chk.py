from solutions.CHK import checkout_solution


class TestCheckout:
    def test_simple(self):
        assert checkout_solution.checkout(['A', 'A']) == 100

    def test_ignore(self):
        assert checkout_solution.checkout(['F']) == -1
    
    def test_complex(self):
        assert checkout_solution.checkout(['A', 'A', 'A', 'A', 'B', 'D']) == 225