try:
    raise Exception('spam', 'eggs')
except Exception as err:
    print(err)
