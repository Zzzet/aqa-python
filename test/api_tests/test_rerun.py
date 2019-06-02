class TestRerun:
    counter = 1

    def test_rerun(self):
        cur_counter = TestRerun.counter
        TestRerun.counter = 2
        if cur_counter == 1:
            assert False
        assert True
