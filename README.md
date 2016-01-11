# commontools
commontools is set of tools to help with common tasks

# installation

```
sudo pip install git+https://github.com/felix001/commontools.git
sudo pip install git+ssh://git@github.com/felix001/commontools.git
```

# convert.py

```
>>> get_ranges([1,2,3,4,5,6])
['1-6']
>>> 
>>> get_list(["1-6"])
[1, 2, 3, 4, 5, 6]
>>>
>>> >>> list_lists = ["apples", "bananas", "pears", "orange"],["123", "12453", "125454", "21332"],["1", "2", "3", "222"],["987", "654   654", "654654", "42454654"],["464", "12", "121", "12"],["12", "123", "123123", "123123123123"]>>>
>>> to_table(list_lists)
apples |bananas   |pears  |orange       |
123    |12453     |125454 |21332        |
1      |2         |3      |222          |
987    |654   654 |654654 |42454654     |
464    |12        |121    |12           |
12     |123       |123123 |123123123123 |
```
