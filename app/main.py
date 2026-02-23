import pkg.mod1
import pkg.mod2
from pkg.mod1 import foo
from pkg.mod2 import Bar as Qux

bar_instance = pkg.mod2.Bar()
foo()
qux_instance = Qux()
