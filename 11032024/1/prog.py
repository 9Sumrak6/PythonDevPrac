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


    def do_up(self, args):
        self.y = (self.y - 1) % 10
        self.encounter(self.x, self.y)


    def do_down(self, args):
        self.y = (self.y + 1) % 10
        self.encounter(self.x, self.y)


    def do_right(self, args):
        self.x = (self.x + 1) % 10
        self.encounter(self.x, self.y)


    def do_left(self, args):
        self.x = (self.x - 1) % 10
        self.encounter(self.x, self.y)


    def do_addmon(self, args):
        args = shlex.split(args)

        if len(args) != 8:
            print("Invalid arguments")
            return

        name = args[0]

        if name not in self.allowed_list and name not in self.user_list:
            print("Invalid arguments")
            return

        hello = ''
        hp = 0
        m_x, m_y = 0, 0

        i = 1
        while i < 8:
            if args[i] == 'hello':
                hello = args[i+1]
            elif args[i] == 'hp':
                try:
                    hp = int(args[i+1])
                except Exception:
                    break

                if hp <= 0:
                    break
            elif args[i] == 'coords':
                try:
                    m_x = int(args[i+1])
                    m_y = int(args[i+2])
                except Exception:
                    break

                if m_x < 0 or m_x > 9 or m_y < 0 or m_y > 9:
                    break

                i += 1
            else:
                print("Invalid arguments")
                break
            i += 2

        if i < 8:
            return

        if self.field[m_y][m_x] == 0:
            print(f'Added monster to ({m_x}, {m_y}) saying {hello}')
        else:
            print(f'Replaced the old monster')

        self.field[m_y][m_x] = {'hello':hello, 'hp': hp, 'name': name}


    def do_EOF(self, args):
        return True


if __name__ == "__main__":
    print("<<< Welcome to Python-MUD 0.1 >>>")

    Mud().cmdloop()    
