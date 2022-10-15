import random
den=1
sitost=15
dengi=30
zdorov=30
uspev=40
while True:
    print('Чтобы выйти из введите 5')
    while True:
        if uspev<0 or sitost<0 or dengi<0 or zdorov<0:
            break
        if uspev>=100 and dengi>=100:
            print('Вы победили')
            break
        if uspev >= 100:
            uspev=100
        if sitost>=100:
            sitost=100
        if zdorov>=100:
            zdorov=100
        if dengi>=100:
            dengi=100
        if den==1 or den==2 or den==3:
            print(f'Здоровье: {zdorov} Деньги: {dengi} Успеваемость: {uspev} Сытость: {sitost}')
            print(f'Сейчас день, выберите действие: '
f'\n1)Сходить на пары(Успеваемость: +5 Сытость: 0 - -15 Деньги: 0 - -5 Здоровье: -5 - -10)'
f'\n2)Работа(Деньги: +15 Успеваемость: -5 Сытость: -15 Здоровье -5)'
f'\n3)Закрыть долги(Успеваемость: +10 - +30 Сытость: -10 - -30 Здоровье 0 - -10)'
f'\n4)Поесть(Сытость: +20)'
f'\n5)Пойти на пробежку(Здоровье +15)')
            deistv=int(input())
            if deistv==1:
                sitost-=10
                zdorov-=5
                uspev+=5
                print(f'Здоровье: {zdorov}\nДеньги: {dengi} \nУспеваемость: {uspev} \nСытость: {sitost}')
                print('Идти на пары:\n1)Пешком\n2)Транспорт')
                pari=int(input())
                if pari==1:
                    zdorov-=5
                    sitost-=15
                elif pari==2:
                    dengi-=5
                else:
                    print('Вы нажали не ту кнопку')
                    break
            elif deistv==2:
                dengi+=15
                uspev-=5
                sitost-=15
                zdorov-=5
            elif deistv==3:
                print(f'Здоровье: {zdorov}\nДеньги: {dengi} \nУспеваемость: {uspev} \nСытость: {sitost}')
                print('Какие предметы закрывать:\n'
'1)Лёгкие(Успеваемость: +10 Сытость: -10)'
'\n2)Сложные(Успеваемость: +20 Сытость: -20)'
'\n3)Супер сложные(Успеваемость: +30 Сытость: -30)')
                zark=int(input())
                if zark==1:
                    uspev+=10
                    sitost-=10
                elif zark==2:
                    uspev+=20
                    sitost-=20
                    zdorov-=5
                elif zark==3:
                    uspev+=30
                    sitost-=30
                    zdorov-=10
                else:
                    print('Вы нажали не ту кнопку')
                    break
            elif deistv==4:
                sitost+=20
            elif deistv==5:
                zdorov+=15
            else:
                print('Вы нажали не ту кнопку')
                break
            den+=1
            if den==4:
                den=0
            elif den==0:
                print(f'Здоровье: {zdorov}\nДеньги: {dengi} \nУспеваемость: {uspev} \nСытость: {sitost}')
                print(f'Сейчас ночь, выберите действие: \n1)Спать(Здоровье: +10 Сытость: +5)'
f'\n2)Учить уроки(Успеваемость: +10 Здоровье: -5)')
                deistv=int(input())
                if deistv==1:
                    zdorov+=10
                    sitost-=5
                elif deistv==2:
                    uspev+=10
                    zdorov-=5
                else:
                    print('Вы нажали не ту кнопку')
                    continue
                den+=1
            else:
                print('Вы нажали не ту кнопку')
                break
    if uspev < 0 or sitost < 0 or dengi < 0 or zdorov < 0:
        print('Вы проиграли')
        break
    if uspev >= 100 and dengi >= 100:
        break
        print('ВЫ хотите выйти из игры?\nДа/Нет')
        x = input()
        if x=='Да':
            break
        else:
            continue
print('Игра окончена')