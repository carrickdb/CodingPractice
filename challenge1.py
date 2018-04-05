s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
S = "G FMNC WMS BGBLR RPYLQJYRC GR ZW FYLB. RFYRQ UFYR AMKNSRCPQ YPC DMP. BMGLE GR GL ZW FYLB GQ GLCDDGAGCLR YLB RFYR'Q UFW RFGQ RCVR GQ QM JMLE. SQGLE QRPGLE.KYICRPYLQ() GQ PCAMKKCLBCB. LMU YNNJW ML RFC SPJ."

strings = ["G", "GR", "ZW", "GL", "GQ", "QM"]

new_s = ""

url = "MAP"
count = {}

sub = {'G': 'i', 'Q': 's', 'M': 'o', 'R': 't', 'L': 'n', 'B': 'd', 'Y': 'a', 'U': 'w', 'E': 'g', 'F': 'h', 'W': 'y', 'J': 'l', 'P': 'r',\
       'C': 'e', 'N': 'p', 'S': 'u', 'Z': 'b', 'D': 'f', 'A': 'c', 'K': 'm', 'V': 'x'}

# for s in strings:
#     for char in s:
#         if char in sub:
#             print(sub[char], end='')
#         else:
#             print(char, end='')
#     print()

for char in url:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
    if char in sub:
        new_s += sub[char]
    else:
        new_s += char

print(new_s)
# print(count)



# q: t, s
# g: i, a
# gr: is, it, if, in, am, at, as, an
# gl:
# gq: is
# ml
# qm:
# zw:
#
# wms
# ypc
# dmp
# ylb
# lmu
# rfc
# spj