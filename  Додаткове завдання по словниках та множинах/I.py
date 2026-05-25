n = int(input())

everyone_knows = set()
at_least_one_knows = set()
is_first_student = True

for i in range(n):
    languages_count = int(input())
    student_languages = set()

    for j in range(languages_count):
        lang = input()
        student_languages.add(lang)

    at_least_one_knows = at_least_one_knows | student_languages

    if is_first_student:
        everyone_knows = student_languages
        is_first_student = False
    else:
        everyone_knows = everyone_knows & student_languages

print(len(everyone_knows))
for lang in sorted(everyone_knows):
    print(lang)

print(len(at_least_one_knows))
for lang in sorted(at_least_one_knows):
    print(lang)