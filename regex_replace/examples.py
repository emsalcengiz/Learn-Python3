s = 'one two one two one'

print(s.replace(' ', '-'))

print(s.replace(' ', ''))


print(s.replace('one', 'XtwoX').replace('two', 'YYY'))

print(s.replace('two', 'YYY').replace('one', 'XtwoX'))


s_lines = 'one\ntwo\nthree'
print(s_lines)

print(s_lines.replace('\n', '-'))

s_lines_multi = 'one\ntwo\r\nthree'
print(s_lines_multi)

print(s_lines_multi.replace('\r\n', '-').replace('\n', '-'))


print(repr(s_lines_multi.replace('\r\n', '-').replace('\n', '-')))


print(s_lines_multi.replace('\n', '-').replace('\r\n', '-'))


print(repr(s_lines_multi.replace('\n', '-').replace('\r\n', '-')))

print(s_lines_multi.splitlines())
# ['one', 'two', 'three']

print('-'.join(s_lines_multi.splitlines()))