import cowsay
import cmd
from io import StringIO
import shlex


class Mud(cmd.Cmd):
    jgsbat = cowsay.read_dot_cow(StringIO("""
    $the_cow = <<EOC;
        ,_                    _,
        ) '-._  ,_    _,  _.-' (
        )  _.-'.|\\--//|.'-._  (
         )'   .'\\/o\\/o\\/'.   `(
          ) .' . \\====/ . '. (
           )  / <<    >> \\  (
            '-._/``  ``\\_.-'
      jgs     __\\'--'//__
             (((""`  `"")))
    EOC
    """))

    prompt = ':->'

    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0

        self.field = [[0 for j in range(10)] for i in range(10)]
        
        self.allowed_list = cowsay.list_cows()
        self.user_list = {'jgsbat': self.jgsbat}

    def get_mon_args(self, args):
        args = shlex.split(args)

        default = ('', '', 0, -1, -1)
        name, hello, hp, m_x, m_y  = default

        if len(args) != 8:
            print("Invalid arguments")
            return default

        name = args[0]

        if name not in self.allowed_list and name not in self.user_list:
            print("Invalid arguments")
            return default

        i = 1
        while i < 8:
            if args[i] == 'hello':
                hello = args[i+1]
            elif args[i] == 'hp':
                try:
                    hp = int(args[i+1])
                except Exception:
                    return default

                if hp <= 0:
                    return default
            elif args[i] == 'coords':
                try:
                    m_x = int(args[i+1])
                    m_y = int(args[i+2])
                except Exception:
                    return default

                if m_x < 0 or m_x > 9 or m_y < 0 or m_y > 9:
                    return default

                i += 1
            else:
                print("Invalid arguments")
                return default
            i += 2

        if i < 8:
            return default

        return (name, hello, hp, m_x, m_y)


    def move_mon(self, name, hello, hp, m_x, m_y):
        if self.field[m_y][m_x] == 0:
            print(f'Added monster to ({m_x}, {m_y}) saying {hello}')
        else:
            print(f'Replaced the old monster')

        self.field[m_y][m_x] = {'hello':hello, 'hp': hp, 'name': name}


    def encounter(self, x, y):
        print(f'Moved to ({x}, {y})')

        if self.field[y][x] == 0:
            return

        hello = self.field[y][x]['hello']
        hp = self.field[y][x]['hp']
        name = self.field[y][x]['name']

        if name in self.allowed_list:
            print(cowsay.cowsay(hello, cow=name))
        else:
            print(cowsay.cowsay(hello, cowfile=self.user_list[name]))


    def move_up(self):
        self.y = (self.y - 1) % 10
        self.encounter(self.x, self.y)


    def move_down(self):
        self.y = (self.y + 1) % 10
        self.encounter(self.x, self.y)


    def move_right(self):
        self.x = (self.x + 1) % 10
        self.encounter(self.x, self.y)


    def move_left(self):
        self.x = (self.x - 1) % 10
        self.encounter(self.x, self.y)


    def do_up(self, args):
        self.move_up()


    def do_down(self, args):
        self.move_down()


    def do_right(self, args):
        self.move_right()


    def do_left(self, args):
        self.move_left()


    def do_addmon(self, args):
        self.move_mon(*self.get_mon_args(args))

    def do_attack(self, args):
        if self.field[self.y][self.x] == 0:
            print("No monster here")
            return

        hp = int(self.field[self.y][self.x]['hp'])
        name = self.field[self.y][self.x]['name']
        damage = 10

        if hp < 10:
            damage = hp
        hp -= damage

        print(f"Attacked {name},  damage {damage} hp")

        if hp == 0:
            print(f"{name} died")
            self.field[self.y][self.x] = 0
        else:
            print(f"{name} now has {hp}")
            self.field[self.y][self.x]['hp'] = hp

    def do_EOF(self, args):
        return True


if __name__ == "__main__":
    print("<<< Welcome to Python-MUD 0.1 >>>")

    Mud().cmdloop()    