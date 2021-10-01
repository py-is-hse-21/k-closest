# k ближайших чисел
Задача: найти `k` чисел, ближайших к заданному значению, в *упорядоченном* массиве. Само значение может не встретиться в массиве.

Пример:
```python3
assert closest([1,4,8,10], target=2, count=3) == [1, 4, 8]
```

Решение должно иметь сложность O(log(n) + k)
