import cowsay
import cmd
import readline
import shlex

from ..common import jgsbat, prompt, weapons

class Mood(cmd.Cmd):
    prompt = prompt

    def __init__(self, conn):
        super().__init__()

        self.conn = conn

        self.allowed_list = cowsay.list_cows()
        self.user_list = {'jgsbat': jgsbat}

    def do_up(self, args):
        self.conn.sendall("move 0 -1\n".encode())

    def do_down(self, args):
        self.conn.sendall("move 0 1\n".encode())

    def do_right(self, args):
        self.conn.sendall("move 1 0\n".encode())

    def do_left(self, args):
        self.conn.sendall("move -1 0\n".encode())

    def do_addmon(self, args):
        self.conn.sendall(("addmon " + args + "\n").encode())

    def do_attack(self, args):
        self.conn.sendall(("attack " + args + "\n").encode())

    def do_sayall(self, args):
        self.conn.sendall(("sayall " + args + "\n").encode())

    def complete_attack(self, text, line, begidx, endidx):
        res = shlex.split(line[:begidx], 0, 0)

        if len(res) <= 1:
            mon_list = list(self.user_list.keys()) + self.allowed_list
            return [c for c in mon_list if c.startswith(text)]
        elif res[-1] == 'with':
            return [c for c in weapons if c.startswith(text)]

    def do_EOF(self, args):
        return True


def recieve(cmd):
    while cmd.conn is not None:
        data = ""

        while len(new := cmd.conn.recv(1024)) == 1024:
            data += new.decode()

        data += new.decode()

        print(f"\n{data.strip()}\n{cmd.prompt}{readline.get_line_buffer()}", end='', flush=True)
