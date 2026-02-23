1| import pkg.mod1
2| import pkg.mod2
3| from pkg.mod1 import foo
4| from pkg.mod2 import Bar as Qux
5| 
6| bar_instance = pkg.mod2.Bar()
7| foo()
8| qux_instance = Qux()
