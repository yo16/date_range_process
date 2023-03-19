import unittest
#import datetime

from date_range_process import dates_subtract, str_to_dt


class TestSubtractPatterns(unittest.TestCase):
    def assertion_func(self, test_base, test_sub, expects):
        ret_lists = dates_subtract(
            test_base, test_sub
        )
        assert len(ret_lists) == len(expects)
        for i, dt_range in enumerate(ret_lists):
            assert str_to_dt(dt_range['from']) == str_to_dt(expects[i][0])
            assert str_to_dt(dt_range['to']) == str_to_dt(expects[i][1])

    
    def test_A_A(self):
        #print('test A-A')
        self.assertion_func(
            [{'from': '2023/1/1', 'to': '2023/5/30'}],
            [{'from': '2023/3/1', 'to': '2023/3/31'}],
            [('2023/1/1', '2023/2/28'), ('2023/4/1', '2023/5/30')]
        )


    def test_A_AB(self):
        #print('test A-AB')
        self.assertion_func(
            [{'from': '2023/1/1', 'to': '2023/5/30'}],
            [{'from': '2023/3/10', 'to': '2023/5/30'}],
            [('2023/1/1', '2023/3/9')]
        )


    def test_A_B(self):
        #print('test A-B')
        self.assertion_func(
            [{'from': '2023/1/1', 'to': '2023/5/30'}],
            [{'from': '2023/3/10', 'to': '2023/6/10'}],
            [('2023/1/1', '2023/3/9')]
        )


    def test_AB_A(self):
        #print('test AB-A')
        self.assertion_func(
            [{'from': '2023/1/1', 'to': '2023/5/31'}],
            [{'from': '2023/1/1', 'to': '2023/4/10'}],
            [('2023/4/11', '2023/5/31')]
        )


    def test_AB_AB(self):
        #print('test AB-AB')
        self.assertion_func(
            [{'from': '2023/1/1', 'to': '2023/5/31'}],
            [{'from': '2023/1/1', 'to': '2023/5/31'}],
            []
        )


    def test_AB_B(self):
        #print('test AB-B')
        self.assertion_func(
            [{'from': '2023/1/1', 'to': '2023/3/10'}],
            [{'from': '2023/1/1', 'to': '2023/5/31'}],
            []
        )


    def test_B_A(self):
        #print('test B-A')
        self.assertion_func(
            [{'from': '2023/2/1', 'to': '2023/5/10'}],
            [{'from': '2023/1/1', 'to': '2023/3/31'}],
            [('2023/4/1', '2023/5/10')]
        )


    def test_B_AB(self):
        #print('test B-AB')
        self.assertion_func(
            [{'from': '2023/2/1', 'to': '2023/5/10'}],
            [{'from': '2023/1/1', 'to': '2023/5/10'}],
            []
        )


    def test_B_B(self):
        #print('test B-B')
        self.assertion_func(
            [{'from': '2023/2/1', 'to': '2023/3/10'}],
            [{'from': '2023/1/1', 'to': '2023/5/10'}],
            []
        )


    def test_case1(self):
        #print('test case1')
        self.assertion_func(
            [
                {'from': '2023/1/1', 'to': '2023/12/31'},
            ],
            [
                {'from': '2023/2/1', 'to': '2023/3/31'},
                {'from': '2023/5/1', 'to': '2023/7/31'}
            ],
            [
                ('2023/1/1', '2023/1/31'),
                ('2023/4/1', '2023/4/30'),
                ('2023/8/1', '2023/12/31')
            ]
        )


    def test_case2(self):
        #print('test case2')
        self.assertion_func(
            [
                {'from': '2023/1/1', 'to': '2023/2/10'},
                {'from': '2023/3/1', 'to': '2023/3/10'},
                {'from': '2023/5/1', 'to': '2023/12/31'},
            ],
            [
                {'from': '2023/2/1', 'to': '2023/7/1'}
            ],
            [
                ('2023/1/1', '2023/1/31'),
                ('2023/7/2', '2023/12/31')
            ]
        )


    def test_case3(self):
        #print('test case3')
        self.assertion_func(
            [
                {'from': '2023/1/1', 'to': '2023/11/10'}
            ],
            [
                {'from': '2023/2/1', 'to': '2023/2/10'},
                {'from': '2023/4/1', 'to': '2023/4/10'},
                {'from': '2023/11/1', 'to': '2023/12/31'},
            ],
            [
                ('2023/1/1', '2023/1/31'),
                ('2023/2/11', '2023/3/31'),
                ('2023/4/11', '2023/10/31')
            ]
        )


    def test_case4(self):
        #print('test case4')
        self.assertion_func(
            [],
            [
                {'from': '2023/1/1', 'to': '2023/11/10'}
            ],
            []
        )


    def test_case5(self):
        #print('test case5')
        self.assertion_func(
            [
                {'from': '2023/1/1', 'to': '2023/11/10'}
            ],
            [],
            [
                ('2023/1/1', '2023/11/10')
            ]
        )


    def test_case6(self):
        #print('test case6')
        self.assertion_func(
            [],
            [],
            []
        )



if __name__ == '__main__':
    unittest.main()
