from datetime import datetime, timedelta


def dt_iterator(dt_list):
    """日付のオブジェクトをリストにして返す
    ついでに文字列のdtを日付型にする

    Args:
        dt_list (object): from, toを持つオブジェクト

    Yields:
        (list): 日付型のfrom,toのリスト
    """
    for dt in dt_list:
        yield [
            str_to_dt(dt['from']),
            str_to_dt(dt['to'])
        ]


def get_dt_obj(dt_from, dt_to):
    return {
        'from': dt_to_str(dt_from),
        'to': dt_to_str(dt_to)
    }


def day_before(dt):
    # dtの前日を返す
    return dt - timedelta(days=1)


def day_after(dt):
    # dtの翌日を返す
    return dt + timedelta(days=1)


def str_to_dt(s):
    return datetime.strptime(s, '%Y/%m/%d')


def dt_to_str(dt):
    return dt.strftime('%Y/%m/%d')
