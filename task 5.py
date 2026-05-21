specialties = ['Бізнес та управління персоналом', 'Економіко-математичне моделювання',
               'Економічна теорія, менеджмент і адміністрування', 'Маркетинг, інновації та регіональний розвиток']

print("Original:")
print(specialties)

count_of = len(specialties)
print("len:")
print(count_of)

position = specialties.index('Економіко-математичне моделювання')
print("index:")
print(position)

specialties.append('Міжнародна економіка')
print("append:")
print(specialties)

specialties.insert(0, 'Облік, аналіз і аудит')
print("insert:")
print(specialties)

extra = ['Фінанси і кредит']
specialties.extend(extra)
print("extend:")
print(specialties)

del specialties[0]
print("del:")
print(specialties)

specialties.remove('Міжнародна економіка')
print("remove:")
print(specialties)

deleted = specialties.pop()
print("pop:")
print(deleted)
print(specialties)

is_here = 'Економіко-математичне моделювання' in specialties
print("in:")
print(is_here)

is_not_here = 'Сварщик' not in specialties
print("not in:")
print(is_not_here)

how_many_times = specialties.count('Маркетинг, інновації та регіональний розвиток')
print("count:")
print(how_many_times)

slice_of = specialties[0:2]
print("slice:")
print(slice_of)

sorted_list = sorted(specialties)
print("sorted:")
print(specialties)

specialties.sort()
print("sort:")
print(specialties)

specialties.reverse()
print("reverse:")
print(specialties)