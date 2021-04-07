import re


table1 = [
    ["04-08-19","62%|+7 794 178-4474", None, "Чебасак, С.Ч.","Чебасак, С.Ч."],
    ["02-12-10","53%|+7 940 788-0991", None, "Фодин, Т.Б.", "Фодин, Т.Б."],
    ["01-03-18","20%|+7 508 113-6990", None, "Гесберг, С.Ф.", "Гесберг, С.Ф."]
    ]

table2 = [
    ["04-01-13","63%|+7 228 083-4659",None,"Дачекко, Т.Г.","Дачекко, Т.Г."],
    ["04-04-05","6%|+7 858 730-1491",None,"Фечолук, И.К.","Фечолук, И.К."],
    ["04-10-08","50%|+7 023 769-1249", None,"Туруцак, А.М.","Туруцак, А.М."],
    ["02-12-13","30%|+7 890 348-5298",None,"Рокянц, Н.Т.","Рокянц, Н.Т."]
]


# функция для задания
def f23(table):
    inRowCheck(table)
    separateRow(table)
    renameElements(table)
    sort(table)
    table = transposition(table)
    table = deleteDuplicates(table)
    # for line in table:
    #     print(line)
    return(table)

# функция удаления повторяющихся строк
def deleteDuplicates(table):
    new_table = []
    for line in table:
        if line not in new_table:
            new_table.append(line)
    return new_table

# функция для транспонирования таблицы
def transposition(table):
    new_table = []
    for _ in range(len(table[0])):
        new_table.append([])
    for line in table:
        for i in range(len(line)):
            new_table[i].append(line[i])
    return new_table


# функция для организации сортировки таблицы по 2-ому элементу строки
def keyFunc(line):
   return line[1]

# функция сортировки
def sort(table):
    table.sort(key=keyFunc)

# функция приведения элементов к нужному формату
def renameElements(table):
    for line in table:
        for cell in  range(len(line)):
            # регулярное выражение для даты
            match = re.fullmatch(r'\d{2}-\d{2}-\d{2}',line[cell])
            if match:
                line[cell] = match[0][-2:]+"/"+match[0][3:5]+"/"+match[0][0:2]
            # регулярное выражение для номера телефона
            match = re.fullmatch(r'\+\d\s\d{3}\s\d{3}-\d{4}',line[cell])
            if match:
                line[cell] = match[0][:-2]+'-'+match[0][-2:]
            # регулярное выражение для имени
            match = re.fullmatch(r'\w+,\s\w\.\w\.',line[cell])
            if match:
                line[cell] = match[0].replace(',','')[:-2]
            #  регулярное выражение для процентов
            match = re.fullmatch(r'\d+%',line[cell])
            if match:
                line[cell] = ('%.2f' % (int(match[0][:-1])/100))
    
                

# функция разделения 2-ого столбца по |
def separateRow(table):
    for line in table:
        string = line[1].split("|")
        line.append(string[0])
        line[1]=string[1]


# функция удаления пустого столбца
def inRowCheck(table):
    nonePosition = table[0].index(None)
    inLine = True
    for line in table:
        if line[nonePosition] != None:
            inLine = False
    if inLine:
        for line in table:
            del line[nonePosition]



# if __name__ =='__main__':
    # f23(table1)
    # f23(table2)