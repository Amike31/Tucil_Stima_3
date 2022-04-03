customers = []
customers.append((2, "Harry")) #no sort needed here because 1 item. 
customers.append((3, "Charles"))
# customers.sort(reverse=True) 
# #Need to sort to maintain order
# customers.append((1, "Riya"))
# customers.sort(reverse=True) 
# #Need to sort to maintain order
# customers.append((4, "Stacy"))
# customers.sort(reverse=True)
for i in customers:
     print(i)

# # For the purpose of this example, let's use SimpleNamespace.
# from types import SimpleNamespace

# # SimpleNamespace allows us to set arbitrary attributes.
# # It is an explicit, handy replacement for "class X: pass".
# ns = SimpleNamespace()

# # Define a function to operate on an object's attribute.
# def square(instance):
#      instance.n *= instance.n

# ns.n = 4
# square(ns)
# print(ns.n)