import sys
list = [1,2,3,4,5]
it = iter(list)
print(next(it))
# iter() func listi dolaşacak
# next() functionu 

for x in it:
    print(x, end="")
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
