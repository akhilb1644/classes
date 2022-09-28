"""
The purpose of this program is to be a simulation of school using python, but it also is to look at a possible use of
access modifiers. Most of the access modifier related code will be present in the oop.py, and here, the result of that
will be shown through this program's output.
"""

from oop import *

nabiyev = Student("Rahmon","Nabiyev",28106,5,10)
nabiyev.go_to_school() # Scroll to the bottom for more info
"""
Should output:
Rahmon attended class 0x9430a.
Rahmon attended class 0x66923.
Rahmon attended class 0x649e1.
Rahmon attended class 0x8c5fc.
Rahmon attended class 0x2f273.
"""
#Note that numbers will be different because the code generates random hexadecimal numbers.
print("") # Just for a new line when output is printed
rahmon = Senior("Emomali","Rahmon",76598,8)
rahmon.go_to_school() # Scroll to the bottom for more info
"""
Should output:
Emomali attended class 0xcd41d.
Emomali attended class 0x2efdd.
Emomali attended class 0xc80c1.
Emomali attended class 0x96aef.
Emomali attended class 0xa4d68.
Emomali attended class 0xe1c98.
Emomali attended class 0xcaea7.
Emomali attended class 0x11748.
"""
# Note that numbers will be different because code generates random hexadecimal numbers.
print("")
rahmon.apply_for_colleges("Purdue","Duke","Harvard","Iowa State","MIT")
"""
Emomali, you have applied for the following colleges:
 - Purdue
 - Duke
 - Harvard
 - Iowa State
 - MIT
"""
print("")
samani = Junior("Ismoil","Somoni",52305,4)
samani.go_to_school() # Scroll to the bottom for more info
"""
Should output:
Ismoil attended class 0xb3f78.
Ismoil attended class 0xfdabe.
Ismoil attended class 0x990a7.
Ismoil attended class 0xad4ce.
"""
# Note that numbers will be different because code generates random hexadecimal numbers.
print("")
samani.completeSAT(4)
"""
Should output:
Ismoil, you got a 1600 on the SAT
"""

"""
Any function that says: go_to_school

There is a function that is called inside it, but it is a protected function. This means with regular syntax, it is
inaccessible outside of the original and derived classes, like here. This is why in this simulation of school, one
can't go to one class but go to another. You either attend all of the classes, or none of them. This is why this school
is skipper proof in case anyone dares to skip this school.
"""