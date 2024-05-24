"""Init file with common constants and functions for client and server files."""

from io import StringIO
import cowsay
from pathlib import Path

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

weapons = {'sword': 10, 'spear': 15, 'axe': 20}

prompt = ':->'

path_doc = str(Path(__file__).parent.resolve() / '../docs/build/html/index.html')
path_transl = str(Path(__file__).parent.resolve() / '../po')
