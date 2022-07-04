import pickle 
class Clubs:
    def __init__(self,club_name,club_couch,club_wins,club_money)->None:
        self.club_name=club_name
        self.club_couch=club_couch
        self.club_wins=club_wins
        self.club_money=club_money
    def __str__(self):
        return str([self.club_name,self.club_couch,self.club_wins,self.club_money])

    def list_clubs(self):
        return [self.club_name,self.club_couch,self.club_wins,self.club_money]
print('Вас приветствует программа"Hockey Clubs"! ver: beta 0.0.1')
mas = [
    Clubs("Авангард", "Хартли Боб","4","1,4 миллиарда рублей"),
    Clubs("ЦСКА","Федоров Сергей","5","2,172 млрд рублей"),
    Clubs("Тампа-Бэй Лайтнинг","Купер Джон","900","89 млрд долларов"),
    Clubs("Вашингтон Кэпиталз","Лавиолетт Питер","0","725 млн долларов"),
    Clubs("Торонто Мейпл Лифс","Киф Шелдон","5","1 млрд долларов")
]
v=-1
while True:
    print('1 - Вывод всех клубов')
    print('2 - Вывод клубов, побеждавших в чемпионате хотя бы раз')
    print('3 - Сортировка клубов по фамилии тренера')
    print('4 - Добавление нового клуба')
    print('5 - Удаление клуба с указанным названием')
    print('6 - Запись списка всех клубов в файл')
    print('7 - Считывание списка клубов из файла')
    print('0 - Выход из программы')
    print('Ваш выбор: ',end='' )
    v=int(input())
    print()
    if v==1:
        for names in mas:
            print("Клуб:",names.club_name,"Тренер:",names.club_couch,"Кол-во побед в чемпионате:",names.club_wins,"Бюджет клуба:",names.club_money)
            print()
    if v==2:
        for points in mas:
            if int(points.club_wins)>0:
                print(points.club_name)
        print()
    if v==3:
        mas.sort(key=lambda x: x.club_couch)
        print('Клубы успешно отсортированы!')
        for names in mas:
            print("Клуб:",names.club_name,"Тренер:",names.club_couch,"Кол-во побед в чемпионате:",names.club_wins,"Бюджет клуба:",names.club_money)
        print()
    if v==4:
        if len(mas)<5:
            print("Название клуба:")
            clubname=input()
            print("Фамилия имя тренера(Для корректной работы программы стоит указывать именно в данном порядке):")
            clubcouch=input()
            print("Кол-во побед в чемпионате:")
            clubwins=input()
            print("Бюджет клуба:")
            clubmoney=input()
            mas.append(Clubs(clubname,clubcouch,clubwins,clubmoney))
            print("Ваш клуб был успешно добавлен!")
            print()
        elif len(mas)==5:
            print("К сожалению, больше в нас не лезет(Вы ввели слишком много клубов)")
            print()
    if v==5:
        print("Введите название клуба, который хотите удалить:")
        delclub=str(input())
        for delete in mas:
            if delclub==delete.club_name:
                mas.remove(delete)
        print("Клуб был успешно удален!")
        print()
    if v == 6:
        f = open('clubs.bin', 'wb')
        pickle.dump(mas, f)
        f.close()
        print('Клубы успешно записаны!.')
        print()
    if v==7:
        with open('clubs.bin', 'rb') as fileclub:
            mas_new=pickle.load(fileclub)
            
            for names in mas_new:
                print("Клуб:",names.club_name,"Тренер:",names.club_couch,"Кол-во побед в чемпионате:",names.club_wins,"Бюджет клуба:",names.club_money)
                print()
    if v==0:
        print('Всего хорошего! Спасибо, что воспользовались программой "Hockey Clubs"! ver: beta 0.0.1 ')
        break
        