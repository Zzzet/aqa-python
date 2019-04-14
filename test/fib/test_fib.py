from src.fib.FibGenerator import FibGenerator


class TestFib:

    def test_fib_result(self):
        fib_generator = FibGenerator()
        assert fib_generator.generateFibonacci(5) == [1, 1, 2, 3, 5]

    def test_fib_positive_length(self):
        fib_generator = FibGenerator()
        assert len(fib_generator.generateFibonacci(25)) == 25

    def test_fib_zero_length(self):
        fib_generator = FibGenerator()
        assert fib_generator.generateFibonacci(0) == []

    def test_fib_negative_length(self):
        fib_generator = FibGenerator()
        assert fib_generator.generateFibonacci(-1) == []
