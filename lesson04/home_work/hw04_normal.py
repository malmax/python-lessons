# -*- coding: utf-8 -*-
"""Малахов Максим."""
import re
import os, random

# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в
# верхнем регистре. Т.е. из строки "mtMmEZUOmcq" нужно получить
# ['mt', 'm', 'mcq'] Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# вариант 1
print(re.findall(r'([a-z0-9]+)', line))

# вариант 2
upperChrs = list(map(chr, range(ord('A'), ord('Z')+1)))
line1 = line
for c in upperChrs:
    line1 = line1.replace(c, ' ')
# убираем двойные пробелы
while(~line1.find('  ')):
    line1 = line1.replace('  ', ' ')
print(line1.split(' '))


# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в
# нижнем регистре слева и два символа в верхнем регистре справа. Решить задачу
# двумя способами: с помощью re и без. Т.е. из строки "sGAMkgAYEOmHBSQs" нужно
# получить ['GAM', 'EO']

line2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

print(re.findall(r'[a-z]{2}([A-Z]+)[a-z0-9]*[A-Z]{2}', line2))
# без re не знаю как

# Задача-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла
# )произвольными целыми числами, в результате в файле должно быть 2500-значное
#  произвольное число. Найдите и выведите самую длинную последовательность
#  одинаковых цифр в вышезаполненном файле.
fileName = os.path.join('lesson04', 'home_work', 'data.txt')
data = ''

with open(fileName, 'w') as f:
    f.write(''.join([str(random.randint(0, 9)) for _ in range(2500)]))

with open(fileName, 'r') as f:
    data = f.read()

data = re.findall(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)', data)
print(max([int(n) for n in data]))
