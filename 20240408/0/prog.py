import calendar
import sys


def foo():
    ans = calendar.month(int(sys.argv[1]), int(sys.argv[2])).split('\n')
    ans[0] = "..table::" + ' '.join(ans[0].split()) + "\n"

    for i in range(1, len(ans)):
        ans[i] = '    ' + ans[i]

    aans = []

    for i in range(len(ans) - 1):
        if i == 1 or i == 3:
            aans.append('    ' + '== '*6 + "==")
        aans.append(ans[i])

    aans.append('    ' + '== '*6 + "==")
    return '\n'.join(aans)


if __name__ == "__main__":
    print(foo())
