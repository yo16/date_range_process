
from date_range_process import dates_subtract


def sample():
    ret = dates_subtract(
        [{'from': '2023/1/1', 'to': '2023/5/30'}],
        [{'from': '2023/3/10', 'to': '2023/6/10'}]
    )
    
    # [{'from': '2023/01/01', 'to': '2023/03/09'}]
    print(ret)


if __name__=='__main__':
    sample()

