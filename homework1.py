"""
Задача 1
Креирајте 2 листи.
1. По колку елементи има секоја од листите?
2. Во првата листа додадете го 2 пати истиот елемент.
3. Избришете ги дупликатите од првата листа. Како изгледа сега листата?
4. На првата листа додадете и ја втората. Колку елементи имаме сега?
5. Сортирајте ја новата листа. Како изгледа сега?

Задача 2
Дадена е листата: my_list = [5, 10, 15, 20, 25]
1. Кој е вториот елемент во листата?
2. Додадете елемент со вредност 30 на крајот.
3. Додадете елемент со вредност 0 на почетокот.
4. Сортирајте ја листата од најголем до најмал.
5. Извадете подлиста од 2риот елемент до крај.

Задача 3
1. Креирајте листа која ќе има 10 елементи.
2. Направете функција која на влез ќе прима 2 броја. Направете ги следниве проверки:
    1. Дали првиот број е помал од вториот. Доколку не е испринтајте внесовте грешка броеви. 
    2. Дали броевите се позитивни цели броеви. Доколку не се испринтајте внесовте негативни броеви. 
    3. Дали вториот број е помал од должината на листата. Доколку не е испринтајте внесете помал број. 
3. Користејќи ги овие 2 броја, креирајте подлиста која ќе почнува со првиот индекс, а ќе завршува со последниот.
4. Проверете дали во подлистата го имаме бројот 6. 

Задача 4
Даден е речникот: grades = {'Ангела': 90, 'Бојан': 85, 'Васил': 95, 'Гордан': 80, 'Даниела': 100}
1. Колку поени има Ангела?
2. Во пресметувањето на поени, се увидело дека имаме грешка кај Гордан. Сменете ги неговите поени во 75.
3. Додадете нов ученик Никола со 92 поени.
4. Бојан се отпишал, па избришете ги информациите за него.
5. Колку ученици имаме и како се викаат?
6. Извадете ги сите поени кои ги освоиле студентите.

Задача 5
Даден е речникот:
book_dict = {
    'Mystery': ['The Girl with the Dragon Tattoo', 'Gone Girl', 'The Da Vinci Code'],
    'Romance': ['The Notebook', 'Pride and Prejudice', 'The Fault in Our Stars'],
    'Science Fiction': ['The Hunger Games', 'Ender\'s Game', 'Dune'],
    'Fantasy': ['The Lord of the Rings', 'Harry Potter and the Philosopher\'s Stone', 'A Game of Thrones'],
    'Classics': ['To Kill a Mockingbird', 'The Catcher in the Rye', 'Wuthering Heights']
}
1. Додадете ја книгата The Silence of the Lambs во жанрот Mystery.
2. Избришете ја книгата Enders Game.
3. Кои се сите жанрови за кои имаме информации?
4. Колку книги имаме во жанрот Fantasy?
5. Проверете дали ја имаме книгата The Lord of the Rings во Fantasy.

Напишете го кодот и како коментар одговорете ги прашањата.
Решенијата генерирани со ChatGPT нема да се валидни како решена домашна.
"""
# Задача 1
# Креирајте 2 листи.
# 1. По колку елементи има секоја од листите?
lista1 = [1, 5, 3, 20, 13, 24, 3, 23]
print(lista1)
lista2 = [2, 4, 7, 18, 72, 31]
print(lista2)
print('lista1 ima elementi:', len(lista1))
print('lista2 ima elementi:', len(lista2))
# 2. Во првата листа додадете го 2 пати истиот елемент.
lista1.extend([100]*2)
print(lista1)
# 3. Избришете ги дупликатите од првата листа. Како изгледа сега листата?
lista1=set(lista1)
print(lista1)
# 4. На првата листа додадете и ја втората. Колку елементи имаме сега?
lista1.update(lista2)
print(lista1)
# 5. Сортирајте ја новата листа. Како изгледа сега?
lista = sorted(lista1)
print('Lista po sortiranje', lista)

# Задача 2
# Дадена е листата: my_list = [5, 10, 15, 20, 25]
# 1. Кој е вториот елемент во листата?
my_list = [5, 10, 15, 20, 25]
print('Vtoriot element e:', lista[1])
# 2. Додадете елемент со вредност 30 на крајот.
my_list.append(30)
print(my_list)
# 3. Додадете елемент со вредност 0 на почетокот.
my_list.insert(0, 0)
print(my_list)
# 4. Сортирајте ја листата од најголем до најмал.
my_list.reverse()
print(my_list)
# 5. Извадете подлиста од 2риот елемент до крај.
my_new_list=my_list[1:]
print(my_new_list)

# Задача 3
# 1. Креирајте листа која ќе има 10 елементи.
# 2. Направете функција која на влез ќе прима 2 броја. Направете ги следниве проверки:
#  1. Дали првиот број е помал од вториот.Доколку не е испринтајте внесовте грешка броеви.
#  2.Дали броевите се позитивни цели броеви. Доколку не се испринтајте внесовте негативни броеви.
#  3. Дали вториот број е помал од должината на листата. Доколку не е испринтајте внесете помал број.
# 3. Користејќи ги овие 2 броја, креирајте подлиста која ќе почнува со првиот индекс, а ќе завршува со последниот.
# 4. Проверете дали во подлистата го имаме бројот 6.
lista = [3, 8, 12, 43, 27, 14, 89, 73, 99, 66]
print(lista)

def numbers(num1, num2):
 num1 = int(input("Vnesi broj: "))
 num2 = int(input("Vnesi broj: "))

 if num1 > num2:
  print("Vnesovte greska broevi")
 elif (num1 and num2 < 0):
  print("Vnesovte negativni broevi")
 elif num2 > len(lista):
  print("vnesete pomal broj")
  lista.extend([[num1, num2]])
  print(lista)

numbers(1, 4)
print(lista)
print()
# Задача 4
# Даден е речникот: grades = {'Ангела': 90, 'Бојан': 85, 'Васил': 95, 'Гордан': 80, 'Даниела': 100}
# 1. Колку поени има Ангела?
# 2. Во пресметувањето на поени, се увидело дека имаме грешка кај Гордан. Сменете ги неговите поени во 75.
# 3. Додадете нов ученик Никола со 92 поени.
# 4. Бојан се отпишал, па избришете ги информациите за него.
# 5. Колку ученици имаме и како се викаат?
# 6. Извадете ги сите поени кои ги освоиле студентите.
grades = {'Ангела': 90,
          'Бојан': 85,
          'Васил': 95,
          'Гордан': 80,
          'Даниела': 100}
print(grades)
print(grades.get('Ангела'))
grades.update({'Гордан':75})
print(grades)
grades['Никола']=92
print(grades)
grades.pop('Бојан')
print(grades)
students=list(grades.keys())
print(students)
broj_studenti=len(students)
print(broj_studenti)
print(list(grades.values()))
# Задача 5
# Даден е речникот:
# book_dict = {
#     'Mystery': ['The Girl with the Dragon Tattoo', 'Gone Girl', 'The Da Vinci Code'],
#     'Romance': ['The Notebook', 'Pride and Prejudice', 'The Fault in Our Stars'],
#     'Science Fiction': ['The Hunger Games', 'Ender\'s Game', 'Dune'],
#     'Fantasy': ['The Lord of the Rings', 'Harry Potter and the Philosopher\'s Stone', 'A Game of Thrones'],
#     'Classics': ['To Kill a Mockingbird', 'The Catcher in the Rye', 'Wuthering Heights']
# }
# 1. Додадете ја книгата The Silence of the Lambs во жанрот Mystery.
# 2. Избришете ја книгата Enders Game.
# 3. Кои се сите жанрови за кои имаме информации?
# 4. Колку книги имаме во жанрот Fantasy?
# 5. Проверете дали ја имаме книгата The Lord of the Rings во Fantasy.
book_dict = {
'Mystery': ['The Girl with the Dragon Tattoo', 'Gone Girl', 'The Da Vinci Code'],
'Romance': ['The Notebook', 'Pride and Prejudice', 'The Fault in Our Stars'],
'Science Fiction': ['The Hunger Games', 'Enders Game', 'Dune'],
'Fantasy': ['The Lord of the Rings', 'Harry Potter and the Philosophers Stone', 'A Game of Thrones'],
'Classics': ['To Kill a Mockingbird', 'The Catcher in the Rye', 'Weathering Heights']}
print(book_dict)
book_dict['Mystery'].append('The Silence of the Lambs')
print('Updated dict:',book_dict)
del book_dict['Science Fiction'][1]
print('dict posle brisenje:', book_dict)
zanrovi=list(book_dict.keys())
print('site zanrovi:',zanrovi)
Broj_na_Fantasy_knigi=len(book_dict['Fantasy'])
print('Broj na Fantasy knigi:',Broj_na_Fantasy_knigi)
if 'The Lord of the Rings' in book_dict['Fantasy']:print('Knigata The Lord of The Rings ja ima vo zanrot Fantasy')



