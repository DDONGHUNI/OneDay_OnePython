import re

# p = re.compile('[a-z]+')
# m = p.match("python")
# m2 = p.search("123 python")
# if m :
#     print('match found : ', m.group())
# else:
#     print('no match')
#
# if m2:
#     print('match found : ', m2.group())
# else:
#     print('no match')

# m = p.match("3 python")
# print(m)

# DoTALL
# p = re.compile('a.b', re.DOTALL)
# m = p.match('a\nb')
# print(m)

# re.I
# p = re.compile('[a-z]', re.I) # I = IgnoreCase 대소문자관계없이 매치
# m = p.match('python')
# print(m)
# m = p.match('Python')
# print(m)
# m = p.match('PYTHON')
# print(m)

# re.M (Multiline)
# p = re.compile("^python\s\w+", re.M)
#
# data =  """python one
# life is too short
# python two
# you need python
# python three"""
#
# a = p.match(data)
# print(a)
# print(a.group())
#
# print(p.findall(data))

# re.X (Verbose) , 이메일
# regrex = re.compile(r'''([a-zA-Z0-9.%+-]+@[a-zA-Z0-9.%+-]+(\.[a-zA-Z]{2,4}){1,2})''')
# email_regrex = re.compile(r'''(
#     [a-zA-Z0-9.%+-]+        # ID
#     @                       # @
#     [a-zA-Z0-9.%+-]+        # domain name (naver, daum 등)
#     (\.[a-zA-Z]{2,4}){1,2}  # dot-somethin (.com, .net 등)
#     )''', re.VERBOSE)
#
# test1 = "asdaca@naver.com"
# output = email_regrex.search(test1).group()
# print(output)
#
# # \ (백슬래시)처리
# p1 = re.compile('\\section')
# p2 = re.compile('\\\\section')
# p3 = re.compile(r'\\section')
#
# print(p1.match('\section'))
# print(p2.match('\section'))
# print(p3.match('\section'))