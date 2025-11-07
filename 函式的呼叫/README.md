# 函式的呼叫
### 引數位置呼叫

```python
>>> def menu(wine, entree, dessert):
    return {'wine': wine, 'entree':entree, 'dessert': dessert}

>>> menu('白酒', '牛排', '蛋糕')
{'wine': '白酒', 'entree': '牛排', 'dessert': '蛋糕'}

>> menu('紅酒', '雞排', '冰淇淋')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '冰淇淋'}

```

### 引數名稱呼叫

```python
#引數名稱呼叫
#可以不依照順序
>>> menu(entree='牛排', dessert='冰淇淋', wine='白酒')
{'dessert': 'bagel', 'wine': 'bordeaux', 'entree': 'beef'}
```

### 引數位置和引數名稱混合呼叫  
```
#前面一定先用引數位置,後面使用引數名稱
#使用引數名稱後,就不可以再使用引數位置

>>> menu('紅酒', dessert='蛋糕', entree='雞排')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}

```

### 指定預設參數的值

```python
>>> def menu(wine, entree, dessert='奶昔'):
	    return {'wine': wine, 'entree':entree, 'dessert': dessert}

#呼叫時,可省略有預設參數的值
>>> menu('紅酒','雞排')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '奶昔'}

#呼叫時,不省略預設的參數值
>>> menu('紅酒','雞排','蛋糕')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}

>>> menu('紅酒','雞排',dessert='蛋糕')
{'wine': '紅酒', 'entree': '雞排', 'dessert': '蛋糕'}
```

```python

>>> def buggy(arg, result=[]):
		result.append(arg)
		print(result) 
		...
>>> buggy('a')
['a']
>>> buggy('b') # expect ['b'] 
['a', 'b']

```

```python

>>> def works(arg):
		result = []
		result.append(arg)
		return result
...
>>> works('a')
['a']
>>> works('b')
['b']

```

```python

>>> def nonbuggy(arg, result=None):
		if result is None:
			result = []
		result.append(arg)
		print(result) 
...
>>> nonbuggy('a') 
['a']
>>> nonbuggy('b')
['b']

```



###  接收參數設定
1. 函數若有接收參數，執行時就必須給他參數。
2. 函數接收資料時參數若有初始值，執行時若沒有給值就會使用那些初始值。
3. 如果函數接收資料時參數沒有初始值，執行時就必須給他參數，且參 數數量必須相同。

#### 操作範例 :請動手操作，並留意輸出結果
```python
# fun5-2.py

def printinfo( name="may", age=20 ): 
	print ("Name: ", name)
	print ("Age ", age)
	print("-----------")
	return( )

printinfo(50,"miki" ) 
printinfo( ) 
printinfo("John") 
printinfo(300) 
printinfo('max',45) 
```

####  Question:請問執行後的結果哪一個是對的?(選擇題)
```python
def test2( name="may", age=20 ): 
	print (name,age)
	return( )
	
test2(200)
```

(1) 200,20  
(2) 20,200  
(3) may,20  
(4) may,200  

### 使用*參數,可接收不限數量的位置引數
大部份使用在參數的最前方

```python
>>> def print_args(*args):
		print('Positional argument tuple:', args) 
...

>>> print_args()
Positional argument tuple: ()

>>> print_args(3, 2, 1, 'wait!', 'uh...')
Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')

>>> def print_more(required1, required2, *args): 
		print('Need this one:', required1)
		print('Need this one too:', required2) 
		print('All the rest:', args)
		
>>> print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')	

Need this one: cap
Need this one too: gloves
All the rest: ('scarf', 'monocle', 'mustache wax')


```

### 使用**參數,呼叫時可使用不限數量的引數名稱
使用在最後的參數位置

```python
>>> def print_kwargs(**kwargs):
		print('Keyword arguments:', kwargs) 
...

>>> print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

Keyword arguments: {'dessert': 'macaroon', 'wine': 'merlot', 'entree': 'mutton'}

```

### 如果在呼叫函式使用*arg或 **kwarg是解開tuple或dictionary,這和定義function時使用的方式剛好相反

```python
#通過一個元組給一個函數傳遞四個參數，並且讓python將它們解開成不同的參數。
def func(a,b,c,d):
    print(a,b,c,d)

a = (1,2,3,4)
func(*a)

# 如果已經有一個元祖，在參數前加*，函數會把元祖中的元素一個一個傳到函數裏面
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)

num = (1,2,3,4)
calc(*num)


#如果已經有一個dict,在參數前面加**，函數會把dict中所有鍵值對轉換為關鍵字參數傳進去

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

extra = {'city': 'Taipei', 'job': 'Engineer'}
person('Jack', 24, **extra)
輸出：
1 2 3 4
30
name: Jack age: 24 other: {'city': 'Taipei', 'job': 'Engineer'}
```
