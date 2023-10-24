'''
ascii table:
              64  @
33  !         65  A         97  a
34  "         66  B         98  b
35  #         67  C         99  c
              68  D        100  d
37  %         69  E        101  e
38  &         70  F        102  f
39  '         71  G        103  g
40  (         72  H        104  h
41  )         73  I        105  i
42  *         74  J        106  j
43  +         75  K        107  k
44  ,         76  L        108  l
45  -         77  M        109  m
46  .         78  N        110  n
47  /         79  O        111  o
48  0         80  P        112  p
49  1         81  Q        113  q
50  2         82  R        114  r
51  3         83  S        115  s
52  4         84  T        116  t
53  5         85  U        117  u
54  6         86  V        118  v
55  7         87  W        119  w
56  8         88  X        120  x
57  9         89  Y        121  y
58  :         90  Z        122  z
59  ;
60  <
61  =
62  >
63  ?         95  _
'''
# 85 tag
import random
from termcolor import cprint

random_text = '''!;#$%&()*+,-./:;<=>?@[]^_{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'''


def input_integer(text):
    while True:
        try:
            value = int(input(text).strip())
        except ValueError:
            cprint('\nYou can only use whole numbers!\n', color='red', force_color=True)
            continue
        return value


def random_password(length):
    password = []
    for i in range(length):
        password.append(random_text[random.randint(0, len(random_text) - 1)])
    return password


print(''.join(random_password(input_integer('How long do you want your password to be? '))))
