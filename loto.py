from random import shuffle, choice, sample


class QStart(object):
    def __init__(self, meshok, k):
        self.meshok = [i + 1 for i in range(meshok)]
        self.rlist = [i for i in range(7)]
        self.k = sample(range(90), k)

    def del1(self, *args):
        ss = [self.meshok.remove(i) for i in args]
        return ss

    # def getfrommeshok(self, numm):
    #     qq = sample(range(90), k=numm)
    #     return qq

    def line(self, line):
        qq = [sorted(line[i:i + 5]) for i in range(0, len(line), 5)]
        for i in range(len(qq)):
            shuffle(self.rlist)
            for j in range(4):  # 5 цифр + 4 пустые клетки = 9 ячеек
                qq[i].insert(self.rlist[j], ' ')
        return qq

    def vid(self, vid, word):
        for i in range(len(vid)):
            for j in range(len(vid[i])):
                if len(str(vid[i][j])) == 1:
                    vid[i][j] = " " + str(vid[i][j])
                else:
                    vid[i][j] = str(vid[i][j])

        ff = [" ".join(i) for i in vid]

        first_str = "_" * ((len(ff[2]) - len(word)) // 2)
        end_str = "_" * ((len(ff[2]) - len(word)) // 2)
        if len(word) % 2 == 1:
            end_str = end_str + "_"
        vs = f'{first_str}{word}{end_str}\n'
        for i in ff:
            vs = vs + i + "\n"
        vs = vs + "-" * len(ff[2])
        return vs


while 1:
    bochonki = input("Введите количество бочонков в мешке")
    number_in_card = input("Введите количество числел  в карточке")
    if bochonki.isdigit() and number_in_card.isdigit():
        bochonki = int(bochonki)
        number_in_card = int(number_in_card)
        break
    else:
        print("Введите числа!!")
# bochonki = 90
# number_in_card = 15
qs = QStart(bochonki, number_in_card)
qs1 = QStart(bochonki, number_in_card)

line = qs.line(qs.k)  # Делаем список из которого будем удалять
line_c = qs1.line(qs1.k)  # Делаем список из которого будем удалять

lineeplayer1 = qs.vid(line, "Моя карточка")  # Формируем красивый вид
lineeplayer2 = qs1.vid(line_c, "Компьютер")  # Формируем красивый вид

flag_1 = 1


def win(vid):  # Условия победы если заканчиваются цифры
    z = 0
    for i in vid:
        if "--" in i:
            z = z + i.count("--")
    return z


def mydel(i):  # Ищем и удаляем в  Своей карточке
    foo = i.index(gg)
    i.insert(foo, "--")
    i.remove(gg)


while flag_1 == 1:

    z = win(line)
    z1 = win(line_c)
    if z == number_in_card:
        print("Победил Пользователь")
        break
    elif z1 == number_in_card:
        print("Победил компьютер")
        break

    gg = choice(qs.meshok)
    qs.del1(gg)  # Берем 1 номер из мешка и удаляем его из мешка
    gg = str(gg)
    print("\n")
    print(f"Новый бочонок: {gg} (осталось {len(qs.meshok)})")

    print(lineeplayer1)  # Показываем красивый вид
    print(lineeplayer2)

    if len(gg) == 1:
        gg = " " + gg

    q = input("Зачеркнуть цифру? (Y/N)")

    # МЫ
    for i in line:
        if str(gg) in i:
            if q == "Y":
                mydel(i)
                break
            elif q == "N":
                flag_1 = 2
    else:
        if q == "Y":
            flag_1 = 2
    # КОМП
    for i in line_c:
        if str(gg) in i:
            mydel(i)
    lineeplayer1 = qs.vid(line, "Моя карточка")  # Формируем красивый вид
    lineeplayer2 = qs1.vid(line_c, "Компьютер")  # Формируем красивый вид
