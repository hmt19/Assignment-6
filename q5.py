
def sort_items(items):
    items = items.split('-')
    items.sort()
    return '-'.join(items)

print(sort_items("green-red-yellow-black-white"))
