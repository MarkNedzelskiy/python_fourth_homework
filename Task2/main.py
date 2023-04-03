# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

garden_bed_count = int(input("Введите количество грядок: "))
garden_bed_harvest = []

for i in range(garden_bed_count):
    garden_bed_harvest.append(randint(0, 1000))

max_harvest_count = 0
max_harvest_garden_bed = 0

for i in range(len(garden_bed_harvest)):
    if i == len(garden_bed_harvest) - 1:
        if garden_bed_harvest[i-1] + garden_bed_harvest[i] + garden_bed_harvest[0] > max_harvest_count:
            max_harvest_count = garden_bed_harvest[i-1] + garden_bed_harvest[i] + garden_bed_harvest[0]
            max_harvest_garden_bed = i
    else:
        if garden_bed_harvest[i-1] + garden_bed_harvest[i] + garden_bed_harvest[i+1] > max_harvest_count:
            max_harvest_count = garden_bed_harvest[i-1] + garden_bed_harvest[i] + garden_bed_harvest[i+1]
            max_harvest_garden_bed = i

print(f"Максимальное количество ягод ({max_harvest_count}) удастся собрать на кусте под номером {max_harvest_garden_bed}")
