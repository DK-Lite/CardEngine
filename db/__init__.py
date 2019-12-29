from .picka_db import PickaDB


def create_insert_query(table, result):
    header = []
    value = ''
    for k,v in result.items():
        header.append('`{}`'.format(k))
        if isinstance(v, str):
            value += "'{}',".format(v)
        else:
            value += str(v) + ','

    return '''insert into {} ({}) values({})'''.format(table, ','.join(header), value[:-1])
