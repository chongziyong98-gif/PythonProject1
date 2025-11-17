#dictionary = {key:value, a:d}

person = {"name":'王大锤', "age":55, "height":168, "weight":60, "addr":'成都市武侯区科华北路62号1栋101'}
print(person)
items1 = dict(zip('ABCDE', '12345')) #use zip() to shortcut.
print(items1)
items3 = {x: x ** 2 for x in range(1, 6)}
print(f"{items3}")

print(person.get("nme",0)) #dict.get(key,value if key not found)
for key, value in person.items():
    print(f'{key}:\t{value}')

#use .update() to add/replace the key & values. Also can use dict1 |= dict2 to do the same

#exercise: input a sentence, summarize each alphabet appear times, print appear times in decending order

sentence = input("Enter a sentence: ")
appear = {}
for alphabet in sentence:
    if "A" <= alphabet <= "Z" or "a" <= alphabet <= "z":
        appear[alphabet] = appear.get(alphabet, 0) + 1
sorted_alphabet = sorted(appear, key=appear.get, reverse=True)
for key in sorted_alphabet:
    print(f"{key}: {appear[key]}")

#exercise 2: find stocks with value greater than 100, put into stock 2
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

stocks2 = {stock:value for stock,value in stocks.items() if value > 100}
print(stocks2)