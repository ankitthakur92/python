def binary_search(numbers, query):
    hi = len(numbers) - 1
    lo = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if numbers[mid] == query:
            return mid
        elif numbers[mid] > query:
            lo = mid + 1
        elif numbers[mid] < query:
            hi = mid - 1
    return -1

test = {
    'input':{
        'numbers':[9,7,5,3,2,1],
        'query':5
    },
    'output':2
}

test1 = {
    'input':{
        'numbers':[9,7,5,3,2,1],
        'query':7
    },
    'output':0
}

tests = []
tests.append(test)
tests.append(test1)

print('start')


for test in tests:
    if binary_search(**test['input']) == test['output']:
        print("True")
    elif binary_search(**test['input']) != test['output']:
        print("False")
print('end') 