import sys
import cmd
import readline
import time


if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")


class Sayer(cmd.Cmd):
    prompt = '~>'
    def precmd(self, line):
        time.sleep(1)
        return super().precmd(line)

    def do_bless(self, args):
        print(f"Be blessed, {args}!")

    def do_sendto(self, args):
        print(f"Go to {args}!")

    def do_EOF(self, args):
        return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fd:
            saycmd = Sayer(stdin=fd)
            saycmd.prompt = ""
            saycmd.use_rawinput = False
            saycmd.cmdloop()
    else:
        saycmd = Sayer()

        saycmd.cmdloop()
