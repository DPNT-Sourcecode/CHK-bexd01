from solutions.CHK import checkout_solution


class TestCheckout:
    def test_simple(self):
        assert checkout_solution.checkout(['A', 'A']) == 100

    def test_ignore(self):
        assert checkout_solution.checkout(['F']) == -1
    
    def test_complex(self):
        assert checkout_solution.checkout(['A', 'A', 'A', 'A', 'B', 'D']) == 225

    def test_complex2(self):
        assert checkout_solution.checkout(['A']*9+['B', 'D']) == 200+130+50+30+15

    def test_complex3(self):
        assert checkout_solution.checkout(['A']*9+['B', 'D']+['E', 'E']) == 200+130+50+80+15


    def test_complex3(self):
        assert checkout_solution.checkout(['A']*9+['B', 'B', 'D']+['E', 'E']) == 200+130+50+80+15+22.5