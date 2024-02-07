# 内置类型[](https://docs.python.org/zh-cn/3/library/stdtypes.html#built-in-types)

[内置类型 — Python 3.12.1 文档](https://docs.python.org/zh-cn/3/library/stdtypes.html)

以下部分描述了解释器中内置的标准类型。

主要内置类型有数字、序列、映射、类、实例和异常。

有些多项集类是可变的。 它们用于添加、移除或重排其成员的方法将原地执行，并不返回特定的项，绝对不会返回多项集实例自身而是返回 `None`。

有些操作受多种对象类型的支持；特别地，实际上所有对象都可以比较是否相等、检测逻辑值，以及转换为字符串（使用 [`repr()`](https://docs.python.org/zh-cn/3/library/functions.html#repr "repr") 函数或略有差异的 [`str()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str "str") 函数）。 后一个函数是在对象由 [`print()`](https://docs.python.org/zh-cn/3/library/functions.html#print "print") 函数输出时被隐式地调用的。

## 逻辑值检测[](https://docs.python.org/zh-cn/3/library/stdtypes.html#truth-value-testing)

任何对象都可以进行逻辑值的检测，以便在 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 或 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 作为条件或是作为下文所述布尔运算的操作数来使用。

在默认情况下，一个对象会被视为具有真值，除非其所属的类定义了在对象上调用时返回 `False` 的 [`__bool__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__bool__ "object.__bool__") 方法或者返回零的 [`__len__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__len__ "object.__len__") 方法。 [[1]](https://docs.python.org/zh-cn/3/library/stdtypes.html#id12) 以下基本完整地列出了具有假值的内置对象：

- 被定义为假值的常量: `None` 和 `False`
- 任何数值类型的零: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
- 空的序列和多项集: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

产生布尔值结果的运算和内置函数总是返回 `0` 或 `False` 作为假值，`1` 或 `True` 作为真值，除非另行说明。 （重要例外：布尔运算 `or` 和 `and` 总是返回其中一个操作数。）

## 布尔运算 --- `and`, `or`, `not`[](https://docs.python.org/zh-cn/3/library/stdtypes.html#boolean-operations-and-or-not)

这些属于布尔运算，按优先级升序排列:

| 运算      | 结果：                                     | 备注 |
| --------- | ------------------------------------------ | ---- |
| `x or y`  | 如果 _x_ 为真值，则 _x_，否则 _y_          | (1)  |
| `x and y` | if _x_ is false, then _x_, else _y_        | (2)  |
| `not x`   | if _x_ is false, then `True`, else `False` | (3)  |

注释：

1. 这是个短路运算符，因此只有在第一个参数为假值时才会对第二个参数求值。
2. 这是个短路运算符，因此只有在第一个参数为真值时才会对第二个参数求值。
3. `not` 的优先级比非布尔运算符低，因此 `not a == b` 会被解读为 `not (a == b)` 而 `a == not b` 会引发语法错误。

## 比较运算[](https://docs.python.org/zh-cn/3/library/stdtypes.html#comparisons)

在 Python 中有八种比较运算符。 它们的优先级相同（比布尔运算的优先级高）。 比较运算可以任意串连；例如，`x < y <= z` 等价于 `x < y and y <= z`，前者的不同之处在于 _y_ 只被求值一次（但在两种情况下当 `x < y` 结果为假值时 _z_ 都不会被求值）。

此表格汇总了比较运算:

| 运算     | 含意           |
| -------- | -------------- |
| `<`      | 严格小于       |
| `<=`     | 小于或等于     |
| `>`      | 严格大于       |
| `>=`     | 大于或等于     |
| `==`     | 等于           |
| `!=`     | 不等于         |
| `is`     | 对象标识       |
| `is not` | 否定的对象标识 |

除不同的数字类型外，不同类型的对象不能进行相等比较。`==` 运算符总有定义，但对于某些对象类型（例如，类对象），它等于 [`is`](https://docs.python.org/zh-cn/3/reference/expressions.html#is) 。其他 `<`、`<=`、`>` 和 `>=` 运算符仅在有意义的地方定义。例如，当参与比较的参数之一为复数时，它们会抛出 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError "TypeError") 异常。

具有不同标识的类的实例比较结果通常为不相等，除非类定义了 [`__eq__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__eq__ "object.__eq__") 方法。

一个类的实例不能与相同类的其他实例或其他类型的对象进行排序，除非定义该类定义了足够多的方法，包括 [`__lt__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__lt__ "object.__lt__"), [`__le__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__le__ "object.__le__"), [`__gt__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__gt__ "object.__gt__") 以及 [`__ge__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__ge__ "object.__ge__") (而如果你想实现常规意义上的比较操作，通常只要有 [`__lt__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__lt__ "object.__lt__") 和 [`__eq__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__eq__ "object.__eq__") 就可以了)。

[`is`](https://docs.python.org/zh-cn/3/reference/expressions.html#is) 和 [`is not`](https://docs.python.org/zh-cn/3/reference/expressions.html#is-not) 运算符无法自定义；并且它们可以被应用于任意两个对象而不会引发异常。

还有两种具有相同语法优先级的运算 [`in`](https://docs.python.org/zh-cn/3/reference/expressions.html#in) 和 [`not in`](https://docs.python.org/zh-cn/3/reference/expressions.html#not-in)，它们被 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable) 或实现了 [`__contains__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__contains__ "object.__contains__") 方法的类型所支持。

## 数字类型 --- [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int"), [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float "float"), [`complex`](https://docs.python.org/zh-cn/3/library/functions.html#complex "complex")[](https://docs.python.org/zh-cn/3/library/stdtypes.html#numeric-types-int-float-complex)

存在三种不同的数字类型: _整数_, _浮点数_ 和 _复数_。 此外，布尔值属于整数的子类型。 整数具有无限的精度。 浮点数通常使用 C 中的 double 来实现；有关你的程序运行所在机器上浮点数的精度和内部表示法可在 [`sys.float_info`](https://docs.python.org/zh-cn/3/library/sys.html#sys.float_info "sys.float_info") 中查看。 复数包含实部和虚部，分别以一个浮点数表示。 要从一个复数 _z_ 中提取这两个部分，可使用 `z.real` 和 `z.imag`。 （标准库包含附加的数字类型，如表示有理数的 [`fractions.Fraction`](https://docs.python.org/zh-cn/3/library/fractions.html#fractions.Fraction "fractions.Fraction") 以及以用户定制精度表示浮点数的 [`decimal.Decimal`](https://docs.python.org/zh-cn/3/library/decimal.html#decimal.Decimal "decimal.Decimal")。）

数字是由数字字面值或内置函数与运算符的结果来创建的。 不带修饰的整数字面值（包括十六进制、八进制和二进制数）会生成整数。 包含小数点或幂运算符的数字字面值会生成浮点数。 在数字字面值末尾加上 `'j'` 或 `'J'` 会生成虚数（实部为零的复数），你可以将其与整数或浮点数相加来得到具有实部和虚部的复数。

Python 完全支持混合运算：当一个二元算术运算符的操作数有不同数值类型时，"较窄"类型的操作数会拓宽到另一个操作数的类型，其中整数比浮点数窄，浮点数比复数窄。不同类型的数字之间的比较，同比较这些数字的精确值一样。[[2]](https://docs.python.org/zh-cn/3/library/stdtypes.html#id13)

构造函数 [`int()`](https://docs.python.org/zh-cn/3/library/functions.html#int "int")、 [`float()`](https://docs.python.org/zh-cn/3/library/functions.html#float "float") 和 [`complex()`](https://docs.python.org/zh-cn/3/library/functions.html#complex "complex") 可以用来构造特定类型的数字。

所有数字类型（复数除外）都支持下列运算（有关运算优先级，请参阅：[运算符优先级](https://docs.python.org/zh-cn/3/reference/expressions.html#operator-summary)）:

| 运算              | 结果：                                                | 备注   | 完整文档                                                                                |
| ----------------- | ----------------------------------------------------- | ------ | --------------------------------------------------------------------------------------- |
| `x + y`           | _x_ 和 _y_ 的和                                       |        |                                                                                         |
| `x - y`           | _x_ 和 _y_ 的差                                       |        |                                                                                         |
| `x * y`           | _x_ 和 _y_ 的乘积                                     |        |                                                                                         |
| `x / y`           | _x_ 和 _y_ 的商                                       |        |                                                                                         |
| `x // y`          | _x_ 和 _y_ 的商数                                     | (1)(2) |                                                                                         |
| `x % y`           | `x / y` 的余数                                        | (2)    |                                                                                         |
| `-x`              | _x_ 取反                                              |        |                                                                                         |
| `+x`              | _x_ 不变                                              |        |                                                                                         |
| `abs(x)`          | _x_ 的绝对值或大小                                    |        | [`abs()`](https://docs.python.org/zh-cn/3/library/functions.html#abs "abs")             |
| `int(x)`          | 将 _x_ 转换为整数                                     | (3)(6) | [`int()`](https://docs.python.org/zh-cn/3/library/functions.html#int "int")             |
| `float(x)`        | 将 _x_ 转换为浮点数                                   | (4)(6) | [`float()`](https://docs.python.org/zh-cn/3/library/functions.html#float "float")       |
| `complex(re, im)` | 一个带有实部 _re_ 和虚部 _im_ 的复数。_im_ 默认为 0。 | (6)    | [`complex()`](https://docs.python.org/zh-cn/3/library/functions.html#complex "complex") |
| `c.conjugate()`   | 复数 _c_ 的共轭                                       |        |                                                                                         |
| `divmod(x, y)`    | `(x // y, x % y)`                                     | (2)    | [`divmod()`](https://docs.python.org/zh-cn/3/library/functions.html#divmod "divmod")    |
| `pow(x, y)`       | _x_ 的 _y_ 次幂                                       | (5)    | [`pow()`](https://docs.python.org/zh-cn/3/library/functions.html#pow "pow")             |
| `x ** y`          | _x_ 的 _y_ 次幂                                       | (5)    |                                                                                         |

注释：

1. 也称为整数除法。 对于 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int") 类型的操作数，结果的类型为 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int")。 对于 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float "float") 类型的操作数，结果的类型为 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float "float")。 总的说来，结果是一个整数，但结果的类型不一定为 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int")。 结果总是向负无穷的方向舍入: `1//2` 为`0`，`(-1)//2` 为 `-1`，`1//(-2)` 为 `-1`，`(-1)//(-2)` 为 `0`。
2. 不可用于复数。 而应在适当条件下使用 [`abs()`](https://docs.python.org/zh-cn/3/library/functions.html#abs "abs") 转换为浮点数。
3. 从 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float "float") 转换为 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int") 将会执行截断，丢弃掉小数部分。 请参阅 [`math.floor()`](https://docs.python.org/zh-cn/3/library/math.html#math.floor "math.floor") 和 [`math.ceil()`](https://docs.python.org/zh-cn/3/library/math.html#math.ceil "math.ceil") 函数了解替代的转换方式。
4. float 也接受字符串 "nan" 和附带可选前缀 "+" 或 "-" 的 "inf" 分别表示非数字 (NaN) 以及正或负无穷。
5. Python 将 `pow(0, 0)` 和 `0 ** 0` 定义为 `1`，这是编程语言的普遍做法。
6. 接受的数字字面值包括数码 `0` 到 `9` 或任何等效的 Unicode 字符（具有 `Nd` 特征属性的代码点）。

   请参阅 [Unicode 标准](https://unicode.org/Public/UNIDATA/extracted/DerivedNumericType.txt) 了解具有 `Nd` 特征属性的码位完整列表。

所有 [`numbers.Real`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Real "numbers.Real") 类型 ([`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int") 和 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float "float")) 还包括下列运算:

| 运算                                                                                         | 结果：                                                                                                               |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [`math.trunc(x)`](https://docs.python.org/zh-cn/3/library/math.html#math.trunc "math.trunc") | _x_ 截断为 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral "numbers.Integral")    |
| [`round(x[, n])`](https://docs.python.org/zh-cn/3/library/functions.html#round "round")      | _x_ 舍入到 _n_ 位小数，半数值会舍入到偶数。 如果省略 _n_，则默认为 0。                                               |
| [`math.floor(x)`](https://docs.python.org/zh-cn/3/library/math.html#math.floor "math.floor") | <= _x_ 的最大 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral "numbers.Integral") |
| [`math.ceil(x)`](https://docs.python.org/zh-cn/3/library/math.html#math.ceil "math.ceil")    | >= _x_ 的最小 [`Integral`](https://docs.python.org/zh-cn/3/library/numbers.html#numbers.Integral "numbers.Integral") |

有关更多的数字运算请参阅 [`math`](https://docs.python.org/zh-cn/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).") 和 [`cmath`](https://docs.python.org/zh-cn/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") 模块。

### 整数类型的按位运算[](https://docs.python.org/zh-cn/3/library/stdtypes.html#bitwise-operations-on-integer-types)

> [位操作 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E4%BD%8D%E6%93%8D%E4%BD%9C)

按位运算只对整数有意义。 计算按位运算的结果，就相当于使用无穷多个二进制符号位对二的补码执行操作。

二进制按位运算的优先级全都低于数字运算，但又高于比较运算；一元运算 `~` 具有与其他一元算术运算 (`+` and `-`) 相同的优先级。

此表格是以优先级升序排序的按位运算列表:

| 运算     | 结果：                 | 备注   |
| -------- | ---------------------- | ------ |
| <code>x \| y</code> | _x_ 和 _y_ 按位 _或_   | (4)    |
| `x ^ y`  | _x_ 和 _y_ 按位 _异或_ | (4)    |
| `x & y`  | _x_ 和 _y_ 按位 _与_   | (4)    |
| `x << n` | _x_ 左移 _n_ 位        | (1)(2) |
| `x >> n` | _x_ 右移 _n_ 位        | (1)(3) |
| `~x`     | _x_ 逐位取反           |        |

注释：

1. 负的移位数是非法的，会导致引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError")。
2. 左移 _n_ 位等价于乘以 `pow(2, n)` 。
3. 右移 _n_ 位等价于除以 `pow(2, n)` ，作向下取整除法。
4. 使用带有至少一个额外符号扩展位的有限个二进制补码表示（有效位宽度为 `1 + max(x.bit_length(), y.bit_length())` 或以上）执行这些计算就足以获得相当于有无数个符号位时的同样结果。

---

## 布尔类型 - [`bool`](https://docs.python.org/zh-cn/3/library/functions.html#bool "bool")[](https://docs.python.org/zh-cn/3/library/stdtypes.html#boolean-type-bool)

代表真值的布尔对象。 [`bool`](https://docs.python.org/zh-cn/3/library/functions.html#bool "bool") 类型只有两个常量实例: `True` 和 `False`。

内置函数 [`bool()`](https://docs.python.org/zh-cn/3/library/functions.html#bool "bool") 可将任意值转换为布尔值，如果该值可以被解读为逻辑值的话（参见上面的 [逻辑值检测](https://docs.python.org/zh-cn/3/library/stdtypes.html#truth) 小节）。

对于逻辑运算，请使用 [布尔运算符](https://docs.python.org/zh-cn/3/library/stdtypes.html#boolean) `and`, `or` 和 `not`。 当于两个布尔值应用按位运算符 `&`, `|`, `^` 时，它们将返回一个等价于逻辑运算 "与", "或", "异或" 的布尔值。 但是，更推荐使用逻辑运算符 `and`, `or` 和 `!=` 而不是 `&`, `|` 和 `^`。

自 3.12 版本弃用: 按位取反运算符 `~` 已被弃用并将在 Python 3.14 中引发异常。

[`bool`](https://docs.python.org/zh-cn/3/library/functions.html#bool "bool") 是 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int "int") 的子类 (参见 [数字类型 --- int, float, complex](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesnumeric))。 在许多数字场景下，`False` 和 `True` 的行为分别与整数 0 和 1 类似。 但是，不建议这样使用；请使用 [`int()`](https://docs.python.org/zh-cn/3/library/functions.html#int "int") 显式地执行转换。

---

## 序列类型 --- [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list "list"), [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple "tuple"), [`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range "range")[](https://docs.python.org/zh-cn/3/library/stdtypes.html#sequence-types-list-tuple-range)

有三种基本序列类型：list, tuple 和 range 对象。 为处理 [二进制数据](https://docs.python.org/zh-cn/3/library/stdtypes.html#binaryseq) 和 [文本字符串](https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq) 而特别定制的附加序列类型会在专门的小节中描述。

### 通用序列操作[](https://docs.python.org/zh-cn/3/library/stdtypes.html#common-sequence-operations)

大多数序列类型，包括可变类型和不可变类型都支持下表中的操作。 [`collections.abc.Sequence`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") ABC 被提供用来更容易地在自定义序列类型上正确地实现这些操作。

此表按优先级升序列出了序列操作。 在表格中，_s_ 和 _t_ 是具有相同类型的序列，_n_, _i_, _j_ 和 _k_ 是整数而 _x_ 是任何满足 _s_ 所规定的类型和值限制的任意对象。

`in` 和 `not in` 操作具有与比较操作相同的优先级。 `+` (拼接) 和 `*` (重复) 操作具有与对应数值运算相同的优先级。 [[3]](https://docs.python.org/zh-cn/3/library/stdtypes.html#id14)

|运算|结果：|备注|
|---|---|---|
|`x in s`|如果 _s_ 中的某项等于 _x_ 则结果为 `True`，否则为 `False`|(1)|
|`x not in s`|如果 _s_ 中的某项等于 _x_ 则结果为 `False`，否则为 `True`|(1)|
|`s + t`|_s_ 与 _t_ 相拼接|(6)(7)|
|`s * n` 或 `n * s`|相当于 _s_ 与自身进行 _n_ 次拼接|(2)(7)|
|`s[i]`|_s_ 的第 _i_ 项，起始为 0|(3)|
|`s[i:j]`|_s_ 从 _i_ 到 _j_ 的切片|(3)(4)|
|`s[i:j:k]`|_s_ 从 _i_ 到 _j_ 步长为 _k_ 的切片|(3)(5)|
|`len(s)`|_s_ 的长度||
|`min(s)`|_s_ 的最小项||
|`max(s)`|_s_ 的最大项||
|`s.index(x[, i[, j]])`|_x_ 在 _s_ 中首次出现项的索引号（索引号在 _i_ 或其后且在 _j_ 之前）|(8)|
|`s.count(x)`|_x_ 在 _s_ 中出现的总次数||

相同类型的序列也支持比较。 特别地，tuple 和 list 的比较是通过比较对应元素的字典顺序。 这意味着想要比较结果相等，则每个元素比较结果都必须相等，并且两个序列长度必须相同。 （完整细节请参阅语言参考的 [比较运算](https://docs.python.org/zh-cn/3/reference/expressions.html#comparisons) 部分。）

可变序列的正向和逆向迭代器使用一个索引来访问值。 即使底层序列被改变该索引也将持续向前（或向后）步进。 迭代器只有在遇到 [`IndexError`](https://docs.python.org/zh-cn/3/library/exceptions.html#IndexError "IndexError") 或 a [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration "StopIteration") 时才会终结（或是当索引降至零以下）。

### 不可变序列类型[](https://docs.python.org/zh-cn/3/library/stdtypes.html#immutable-sequence-types)

不可变序列类型普遍实现而可变序列类型未实现的唯一操作就是对 [`hash()`](https://docs.python.org/zh-cn/3/library/functions.html#hash "hash") 内置函数的支持。

这种支持允许不可变类型，例如 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple "tuple") 实例被用作 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict "dict") 键，以及存储在 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set "set") 和 [`frozenset`](https://docs.python.org/zh-cn/3/library/stdtypes.html#frozenset "frozenset") 实例中。

尝试对包含有不可哈希值的不可变序列进行哈希运算将会导致 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError "TypeError")。

### 可变序列类型[](https://docs.python.org/zh-cn/3/library/stdtypes.html#mutable-sequence-types)

以下表格中的操作是在可变序列类型上定义的。 [`collections.abc.MutableSequence`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") ABC 被提供用来更容易地在自定义序列类型上正确实现这些操作。

表格中的 _s_ 是可变序列类型的实例，_t_ 是任意可迭代对象，而 _x_ 是符合对 _s_ 所规定类型与值限制的任何对象 (例如，[`bytearray`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytearray "bytearray") 仅接受满足 `0 <= x <= 255` 值限制的整数)。

|运算|结果：|备注|
|---|---|---|
|`s[i] = x`|将 _s_ 的第 _i_ 项替换为 _x_||
|`s[i:j] = t`|将 _s_ 从 _i_ 到 _j_ 的切片替换为可迭代对象 _t_ 的内容||
|`del s[i:j]`|等同于 `s[i:j] = []`||
|`s[i:j:k] = t`|将 `s[i:j:k]` 的元素替换为 _t_ 的元素|(1)|
|`del s[i:j:k]`|从列表中移除 `s[i:j:k]` 的元素||
|`s.append(x)`|将 _x_ 添加到序列的末尾 (等同于 `s[len(s):len(s)] = [x]`)||
|`s.clear()`|从 _s_ 中移除所有项 (等同于 `del s[:]`)|(5)|
|`s.copy()`|创建 _s_ 的浅拷贝 (等同于 `s[:]`)|(5)|
|`s.extend(t)` 或 `s += t`|用 _t_ 的内容扩展 _s_ (基本上等同于 `s[len(s):len(s)] = t`)||
|`s *= n`|使用 _s_ 的内容重复 _n_ 次来对其进行更新|(6)|
|`s.insert(i, x)`|在由 _i_ 给出的索引位置将 _x_ 插入 _s_ (等同于 `s[i:i] = [x]`)||
|`s.pop()` 或 `s.pop(i)`|提取在 _i_ 位置上的项，并将其从 _s_ 中移除|(2)|
|`s.remove(x)`|删除 _s_ 中第一个 `s[i]` 等于 _x_ 的项目。|(3)|
|`s.reverse()`|就地将列表中的元素逆序。|(4)|

注释：

1. _t_ 必须与它所替换的切片具有相同的长度。
2. 可选参数 _i_ 默认为 `-1`，因此在默认情况下会移除并返回最后一项。
3. 当在 _s_ 中找不到 _x_ 时 `remove()` 操作会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError")。
4. 当反转大尺寸序列时 `reverse()` 方法会原地修改该序列以保证空间经济性。 为提醒用户此操作是通过间接影响进行的，它并不会返回反转后的序列。
5. 包括 `clear()` 和 `copy()` 是为了与不支持切片操作的可变容器 (例如 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict "dict") 和 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set "set")) 的接口保持一致。 `copy()` 不是 [`collections.abc.MutableSequence`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") ABC 的一部分，但大多数具体的可变序列类都提供了它。

    在 3.3 版本加入: `clear()` 和 `copy()` 方法。

6. _n_ 值为一个整数，或是一个实现了 [`__index__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__index__ "object.__index__") 的对象。 _n_ 值为零或负数将清空序列。 序列中的项不会被拷贝；它们会被多次引用，正如 [通用序列操作](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-common) 中有关 `s * n` 的说明。

### 列表[](https://docs.python.org/zh-cn/3/library/stdtypes.html#lists)

列表是可变序列，通常用于存放同类项目的集合（其中精确的相似程度将根据应用而变化）。

_class_ list(\[_iterable_\])[](https://docs.python.org/zh-cn/3/library/stdtypes.html#list "Link to this definition")

可以用多种方式构建列表：

- 使用一对方括号来表示空列表: `[]`
- 使用方括号，其中的项以逗号分隔: `[a]`, `[a, b, c]`
- 使用列表推导式: `[x for x in iterable]`
- 使用类型的构造器: `list()` 或 `list(iterable)`

构造器将构造一个列表，其中的项与 _iterable_ 中的项具有相同的的值与顺序。 _iterable_ 可以是序列、支持迭代的容器或其它可迭代对象。 如果 _iterable_ 已经是一个列表，将创建并返回其副本，类似于 `iterable[:]`。 例如，`list('abc')` 返回 `['a', 'b', 'c']` 而 `list( (1, 2, 3) )` 返回 `[1, 2, 3]`。 如果没有给出参数，构造器将创建一个空列表 `[]`。

其它许多操作也会产生列表，包括 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted "sorted") 内置函数。

列表实现了所有 [一般](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-common) 和 [可变](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-mutable) 序列的操作。 列表还额外提供了以下方法：

#### sort(_*_, _key=None_, _reverse=False_)[](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort "Link to this definition")

此方法会对列表进行原地排序，只使用 `<` 来进行各项间比较。 异常不会被屏蔽 —— 如果有任何比较操作失败，整个排序操作将失败（而列表可能会处于被部分修改的状态）。

[`sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort "list.sort") 接受两个仅限以关键字形式传入的参数 ([仅限关键字参数](https://docs.python.org/zh-cn/3/glossary.html#keyword-only-parameter)):

_key_ 指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如 `key=str.lower`)。 对应于列表中每一项的键会被计算一次，然后在整个排序过程中使用。 默认值 `None` 表示直接对列表项排序而不计算一个单独的键值。

可以使用 [`functools.cmp_to_key()`](https://docs.python.org/zh-cn/3/library/functools.html#functools.cmp_to_key "functools.cmp_to_key") 将 2.x 风格的 _cmp_ 函数转换为 _key_ 函数。

_reverse_ 为一个布尔值。 如果设为 `True`，则每个列表元素将按反向顺序比较进行排序。

当顺序大尺寸序列时此方法会原地修改该序列以保证空间经济性。 为提醒用户此操作是通过间接影响进行的，它并不会返回排序后的序列（请使用 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted "sorted") 显示地请求一个新的已排序列表实例）。

[`sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort "list.sort") 方法确保是稳定的。 如果一个排序确保不会改变比较结果相等的元素的相对顺序就称其为稳定的 --- 这有利于进行多重排序（例如先按部门、再接薪级排序）。

有关排序示例和简要排序教程，请参阅 [排序指南](https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto) 。

**CPython 实现细节：** 在一个列表被排序期间，尝试改变甚至进行检测也会造成未定义的影响。 Python 的 C 实现会在排序期间将列表显示为空，如果发现列表在排序期间被改变将会引发 [`ValueError`](https://docs.python.org/zh-cn/3/library/exceptions.html#ValueError "ValueError")。

### 元组[](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuples)

元组是不可变序列，通常用于储存异构数据的多项集（例如由 [`enumerate()`](https://docs.python.org/zh-cn/3/library/functions.html#enumerate "enumerate") 内置函数所产生的二元组）。 元组也被用于需要同构数据的不可变序列的情况（例如允许存储到 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set "set") 或 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict "dict") 的实例）。

_class_ tuple([_iterable_])[](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple "Link to this definition")

可以用多种方式构建元组：

- 使用一对圆括号来表示空元组: `()`
- 使用一个后缀的逗号来表示单元组: `a,` 或 `(a,)`
- 使用以逗号分隔的多个项: `a, b, c` or `(a, b, c)`
- 使用内置的 [`tuple()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple "tuple"): `tuple()` 或 `tuple(iterable)`

构造器将构造一个元组，其中的项与 _iterable_ 中的项具有相同的值与顺序。 _iterable_ 可以是序列、支持迭代的容器或其他可迭代对象。 如果 _iterable_ 已经是一个元组，会不加改变地将其返回。 例如，`tuple('abc')` 返回 `('a', 'b', 'c')` 而 `tuple( [1, 2, 3] )` 返回 `(1, 2, 3)`。 如果没有给出参数，构造器将创建一个空元组 `()`。

请注意决定生成元组的其实是逗号而不是圆括号。 圆括号只是可选的，生成空元组或需要避免语法歧义的情况除外。 例如，`f(a, b, c)` 是在调用函数时附带三个参数，而 `f((a, b, c))` 则是在调用函数时附带一个三元组。

元组实现了所有 [一般](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq-common) 序列的操作。

对于通过名称访问相比通过索引访问更清晰的异构数据多项集，[`collections.namedtuple()`](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple "collections.namedtuple") 可能是比简单元组对象更为合适的选择。

### range 对象[](https://docs.python.org/zh-cn/3/library/stdtypes.html#ranges)

[`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range "range") 类型表示不可变的数字序列，通常用于在 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环中循环指定的次数。

---

## 文本序列类型 --- [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str "str")[](https://docs.python.org/zh-cn/3/library/stdtypes.html#text-sequence-type-str)

在 Python 中处理文本数据是使用 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str "str") 对象，也称为 _字符串_。 字符串是由 Unicode 码位构成的不可变 [序列](https://docs.python.org/zh-cn/3/library/stdtypes.html#typesseq)。 字符串字面值有多种不同的写法：

- 单引号: `'允许包含有 "双" 引号'`
- 双引号: `"允许嵌入 '单' 引号"`
- 三重引号: `'''三重单引号'''`, `"""三重双引号"""`

使用三重引号的字符串可以跨越多行 —— 其中所有的空白字符都将包含在该字符串字面值中。

作为单一表达式组成部分，之间只由空格分隔的多个字符串字面值会被隐式地转换为单个字符串字面值。 也就是说，`("spam " "eggs") == "spam eggs"`。

请参阅 [字符串与字节串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#strings) 了解有关各种字符串字面值形式的更多信息，包括所支持的 [转义序列](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#escape-sequences)，以及禁用大多数转义序列处理的 `r` ("raw") 前缀。

字符串也可以通过使用 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str "str") 构造器从其他对象创建。

由于不存在单独的“字符”类型，对字符串做索引操作将产生一个长度为 1 的字符串。 也就是说，对于一个非空字符串 _s_, `s[0] == s[0:1]`。

不存在可变的字符串类型，但是 [`str.join()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.join "str.join") 或 [`io.StringIO`](https://docs.python.org/zh-cn/3/library/io.html#io.StringIO "io.StringIO") 可以被被用来根据多个片段高效率地构建字符串。

### 2.4.1.1. 转义序列[](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#escape-sequences)

如未标注 `'r'` 或 `'R'` 前缀，字符串和字节串字面值中，转义序列以类似 C 标准的规则进行解释。可用的转义序列如下：

|转义序列|含意|备注|
|---|---|---|
|`\`<newline>|忽略反斜杠与换行符|(1)|
|`\\`|反斜杠（`\`）||
|`\'`|单引号（`'`）||
|`\"`|双引号（`"`）||
|`\a`|ASCII 响铃（BEL）||
|`\b`|ASCII 退格符（BS）||
|`\f`|ASCII 换页符（FF）||
|`\n`|ASCII 换行符（LF）||
|`\r`|ASCII 回车符（CR）||
|`\t`|ASCII 水平制表符（TAB）||
|`\v`|ASCII 垂直制表符（VT）||
|<code>\\_ooo_</code>|八进制数 _ooo_ 字符|(2,4)|
|<code>\x_hh_</code>|十六进制数 _hh_ 字符|(3,4)|

字符串字面值专用的转义序列：

|转义序列|含意|备注|
|---|---|---|
|<code>\N{_name_}` |Unicode 数据库中名为 _name_ 的字符|(5)|
|<code>\u_xxxx_</code>|16 位十六进制数 _xxxx_ 码位的字符|(6)|
|<code>\U_xxxxxxxx_</code>|32 位 16 进制数 _xxxxxxxx_ 码位的字符|(7)|

---

## 运算符优先级[](https://docs.python.org/zh-cn/3/reference/expressions.html#operator-precedence)

下表对 Python 中运算符的优先顺序进行了总结，从最高优先级（最先绑定）到最低优先级（最后绑定）。 相同单元格内的运算符具有相同优先级。 除非语法显式地指明，否则运算符均为双目运算符。 相同单元格内的运算符从左至右组合的（只有幂运算符是从右至左组合的）。

请注意比较、成员检测和标识号检测均为相同优先级，并具有如 [比较运算](https://docs.python.org/zh-cn/3/reference/expressions.html#comparisons) 一节所描述的从左至右串连特性。

|运算符|描述|
|---|---|
|`(expressions...)`,<br><br>`[expressions...]`, `{key: value...}`, `{expressions...}`|绑定或加圆括号的表达式，列表显示，字典显示，集合显示|
|`x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute`|抽取，切片，调用，属性引用|
|[`await x`](https://docs.python.org/zh-cn/3/reference/expressions.html#await)|await 表达式|
|`**`|乘方 [[5]](https://docs.python.org/zh-cn/3/reference/expressions.html#id21)|
|`+x`, `-x`, `~x`|正，负，按位非 NOT|
|`*`, `@`, `/`, `//`, `%`|乘，矩阵乘，除，整除，取余 [[6]](https://docs.python.org/zh-cn/3/reference/expressions.html#id22)|
|`+`, `-`|加和减|
|`<<`, `>>`|移位|
|`&`|按位与 AND|
|`^`|按位异或 XOR|
|<code>\|</code>|按位或 OR|
|[`in`](https://docs.python.org/zh-cn/3/reference/expressions.html#in), [`not in`](https://docs.python.org/zh-cn/3/reference/expressions.html#not-in), [`is`](https://docs.python.org/zh-cn/3/reference/expressions.html#is), [`is not`](https://docs.python.org/zh-cn/3/reference/expressions.html#is-not), `<`, `<=`, `>`, `>=`, `!=`, `==`|比较运算，包括成员检测和标识号检测|
|[`not x`](https://docs.python.org/zh-cn/3/reference/expressions.html#not)|布尔逻辑非 NOT|
|[`and`](https://docs.python.org/zh-cn/3/reference/expressions.html#and)|布尔逻辑与 AND|
|[`or`](https://docs.python.org/zh-cn/3/reference/expressions.html#or)|布尔逻辑或 OR|
|[`if`](https://docs.python.org/zh-cn/3/reference/expressions.html#if-expr) -- `else`|条件表达式|
|[`lambda`](https://docs.python.org/zh-cn/3/reference/expressions.html#lambda)|lambda 表达式|
|`:=`|赋值表达式|

备注

[[1](https://docs.python.org/zh-cn/3/reference/expressions.html#id9)]

虽然 `abs(x%y) < abs(y)` 在数学中必为真，但对于浮点数而言，由于舍入的存在，其在数值上未必为真。 例如，假设在某个平台上的 Python 浮点数为一个 IEEE 754 双精度数值，为了使 `-1e-100 % 1e100` 具有与 `1e100` 相同的正负性，计算结果将是 `-1e-100 + 1e100`，这在数值上正好等于 `1e100`。 函数 [`math.fmod()`](https://docs.python.org/zh-cn/3/library/math.html#math.fmod "math.fmod") 返回的结果则会具有与第一个参数相同的正负性，因此在这种情况下将返回 `-1e-100`。 何种方式更适宜取决于具体的应用。

[[2](https://docs.python.org/zh-cn/3/reference/expressions.html#id10)]

如果 x 恰好非常接近于 y 的整数倍，则由于舍入的存在 `x//y` 可能会比 `(x-x%y)//y` 大。 在这种情况下，Python 会返回后一个结果，以便保持令 `divmod(x,y)[0] * y + x % y` 尽量接近 `x`.

[[3](https://docs.python.org/zh-cn/3/reference/expressions.html#id12)]

Unicode 标准明确区分 _码位_ (例如 U+0041) 和 _抽象字符_ (例如 "大写拉丁字母 A")。 虽然 Unicode 中的大多数抽象字符都只用一个码位来代表，但也存在一些抽象字符可使用由多个码位组成的序列来表示。 例如，抽象字符 "带有下加符的大写拉丁字母 C" 可以用 U+00C7 码位上的单个 _预设字符_ 来表示，也可以用一个 U+0043 码位上的 _基础字符_ (大写拉丁字母 C) 加上一个 U+0327 码位上的 _组合字符_ (组合下加符) 组成的序列来表示。

对于字符串，比较运算符会按 Unicode 码位级别进行比较。 这可能会违反人类的直觉。 例如，`"\u00C7" == "\u0043\u0327"` 为 `False`，虽然两个字符串都代表同一个抽象字符 "带有下加符的大写拉丁字母 C"。

要按抽象字符级别（即对人类来说更直观的方式）对字符串进行比较，应使用 [`unicodedata.normalize()`](https://docs.python.org/zh-cn/3/library/unicodedata.html#unicodedata.normalize "unicodedata.normalize")。

[[4](https://docs.python.org/zh-cn/3/reference/expressions.html#id13)]

由于存在自动垃圾收集、空闲列表以及描述器的动态特性，你可能会注意到在特定情况下使用 [`is`](https://docs.python.org/zh-cn/3/reference/expressions.html#is) 运算符会出现看似不正常的行为，例如涉及到实例方法或常量之间的比较时就是如此。 更多信息请查看有关它们的文档。

[[5](https://docs.python.org/zh-cn/3/reference/expressions.html#id15)]

幂运算符 `**` 绑定的紧密程度低于在其右侧的算术或按位一元运算符，也就是说 `2**-1` 为 `0.5`。

[[6](https://docs.python.org/zh-cn/3/reference/expressions.html#id16)]

`%` 运算符也被用于字符串格式化；在此场合下会使用同样的优先级。
