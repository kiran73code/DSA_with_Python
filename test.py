counter = {
    1:2,
    2:2,
    3:2
}

min_value_key = min(counter, key=counter.get)
print(min_value_key)