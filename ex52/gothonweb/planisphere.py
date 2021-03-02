class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Центральный коридор",
"""
Готоны с планеты Перкаль 25 захватили ваш корабль и уничтожили всю команду. 
Ты - единственный, кто остался в живых. Тебе нужно выкрасть нейтронную бомбу 
в оружейной лаборатории, заложить ее в топливном отсеке и покинуть корабль в 
спасательной капсуле прежде, чем он взорвется.

Ты бежишь по центральному коридору в оружейную лабораторию, когда перед тобой 
появляется готон с красной чешуйчатой кожей, гнилыми зубами и в костюме клоуна. 
Он с ненавистью смотрит на тебя и, перегородив дорогу в лабораторию, вытаскивает 
бластер, чтобы отправить тебя к праотцам.
""")


laser_weapon_armory = Room("Оружейная лаборатория",
"""
К счастью, ты знаком с культурой готонов и знаешь, что может их рассмешить. Ты 
рассказываешь бородатый анекдот: Неоколонии, изоморфно релятивные к мyльтиполосным 
гиперболическим параболоидам, теоретически катаральны. Готон замирает, старается 
сдержать смех, а затем начинает безудержно хохотать. Пока он смеется, ты достаешь 
бластер и стреляешь готону в голову. Он падает, а ты перепрыгиваешь его и бежишь 
в оружейную лабораторию.

Ты вбегаешь в оружейную лабораторию и начинаешь обыскивать комнату, спрятались ли 
тут другие готоны.  Стоит мертвая тишина. Ты бежишь в дальний угол комнаты и 
находишь нейтронную бомбу в защитном контейнере. На лицевой стороне контейнера 
расположена панель с кнопками и тебе надо ввести правильный код, чтобы достать 
бомбу. Если ты 10 раз введешь неправильный код, контейнер заблокируется и ты не 
сможешь достать бомбу. Учти, что код состоит из 3 цифр.
""")


the_bridge = Room("Топливный отсек",
"""
Контейнер открывается со щелчком и выпускает сизый газ. Ты вытаскиваешь нейтронную 
бомбу и бежишь в топливный отсек, чтобы установить бомбу в нужном месте, 
активировать ее и успеть смотаться с корабля.

Ты вбегаешь в топливный отсек с нейтронной бомбой и видишь пятерых готонов, 
безуспешно пытающихся управлять кораблем. Один уродливее другого и все в клоунских 
костюмах, как и готон, убитый тобой. Они не достают оружие, так как видят бомбу 
в твоих руках и не хотят, чтобы ты взорвал ее. Преимущество явно на твоей 
стороне.
""")


escape_pod = Room("Спасательная капсула",
"""
Ты указываешь бластером на бомбу в своих руках. Готоны поднимают лапы вверх и в 
страхе потеют. Ты осторожно, не отворачиваясь, подходишь к двери и аккуратно 
устанавливаешь бомбу, держа готонов на мушке. Ты запрыгиваешь в шлюз и закрываешь 
ее ударом по кнопке, а затем бластером расплавляешь замок, чтобы готоны не смогли 
открыть дверь. Теперь тебе нужно залезть в спасательную капсулу и удрать с корабля 
к чертям собачьим.

Ты мчишься по отсеку со спасательными капсулами. Похоже, готонов на корабле больше 
нет, потому что никто тебе не мешает. Некоторые из капсул могут быть повреждены и 
взорвутся во время полета. Всего капсул пять и у тебя нет времени, чтобы 
осматривать каждую из них на отсутствие повреждений. Задумавшись на секунду, 
ты решаешь сесть в капсулу под номером...
Капсулу под каким номером ты выбираешь?"
""")


the_end_winner = Room("Конец",
"""
Ты запрыгиваешь в капсулу номер 2 и нажимаешь кнопку отстыковки. Капсула вылетает 
в космическое пространство, а затем отправляется к планете неподалеку. Ты смотришь 
в иллюминатор и видишь, как ваш корабль взрывается. Его осколки повреждают 
топливный отсек корабля готонов и тот тоже разлетается в клочья. Победа за вами!
""")


the_end_loser = Room("Конец",
"""
Ты запрыгиваешь в капсулу со случайным номером и нажимаешь кнопку отстыковки. 
Капсула вылетает в космическое пространство, а затем взрывается с яркой вспышкой, 
разбрасывая осколки. Ты умираешь.
"""
)

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "Вы мерты.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    Здесь есть потенциальная проблема безопасности.
    Кто может задать имя? Может ли это негативно повлиять на переменную?
    """
    return globals().get(name)

def name_room(room):
    """
    Аналогичная проблема безопасности по поводу сцены?
    Можете предложить лучшее решение вместо глобального поиска?
    """
    for key, value in globals().items():
        if value == room:
            return key
