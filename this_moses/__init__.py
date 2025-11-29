s = """Gur Mra bs Zbfrf, ol Wrfhf

V nz gur YBEQ lbhe Tbq; lbh funyy abg unir fgenatr tbqf orsber zr.
Lbh funyy abg gnxr gur anzr bs gur YBEQ lbhe Tbq va inva.
Erzrzore gb xrrc ubyl gur YBEQ’f Qnl.
Ubabe lbhe sngure naq zbgure.
Lbh funyy abg xvyy.
Lbh funyy abg pbzzvg nqhygrel.
Lbh funyy abg fgrny.
Lbh funyy abg orne snyfr jvgarff ntnvafg lbhe arvtuobe.
Lbh funyy abg pbirg lbhe arvtuobe’f jvsr.
Lbh funyy abg pbirg lbhe arvtuobe’f tbbqf."""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
