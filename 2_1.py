test_list_1 = [22, 33.2, complex(2, 3), 'строка', [66, 'text'], ('a', 'bb'), {23, True, 'строка'}]
for el in test_list_1:
    print (type(el))
test_list_2 = [frozenset('abrakadabra'), True, None, {"key_1": 500, 2: 400, "key_3": True, 4: None}, b'text']
for el in test_list_2:
    print (type(el))