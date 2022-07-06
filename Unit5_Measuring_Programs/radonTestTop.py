from radon.visitors import ComplexityVisitor
f=open("radonTest.py","r")
v = ComplexityVisitor.from_code(f.read())
f.close()
print(v.functions)
