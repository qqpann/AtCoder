# a = input()
# bc = input()
# s = input()
#
# a = int(a)
# b, c = bc.split(' ')
# b = int(b)
# c = int(c)
#
# print(a+b+c, s)

#############

n, q = input().split(" ")
n = int(n)
q = int(q)

class Markers:
    def __init__(self, lst):
        # set PLR
        # インスタンス変数。len(lst)が2以上前提。
        self.lst = lst
        self.mP = len(lst) - 1
        self.mL = 0
        self.mR = nP - 1

    def compare(a,b):
        print('?', a, b)
        result = input()

    def swap(a,b):
        self.lst[a], self.lst[b] = self.lst[b], self.lst[a]

    def sort(self):
        # LはPより大きな数に出会った時に止まる。
        # Rにぶつかっても止まらない。
        # 対象数列の右端にぶつかったら止まる。
        while self.mL < self.mP:
            if compare(self.mL, self.mP) == '>':
                #L stops.
                break
            self.mL += 1
        # RはPより小さな数に出会った時に止まる。
        # 止まったLにぶつかると止まる。
        # Lに追い越されていた場合、動かずに止まる。
        while self.mR > 0:
            if self.mL >= self.mR:
                break
            if compare(self.mR, self.mP) == '<':
                break
        # RがLにぶつかって止まった場合、その場所とPの要素を交換する。
        # Lが右端に来て止まった場合、Pをソート済みにする。
        if self.mL == self.mR:
            swap(self.mL, self.mP)
        elif self.mL == self.mP:
            pass # P is sorted.
        else:
            swap(self.mL, self.mR)

# http://stackoverflow.com/questions/16060899/alphabet-range-python
import string
alphabets = list(string.ascii_uppercase)
al = [ alphabets[:n] ]

def quickSort(lst):
    # もしリストなら処理する。文字列なら次へスキップする。
    for i in lst:
        if type(i) != list:
            continue
        if len(i) == 1:
            i = i[0]
            continue
        # リストの中について、
        # Pを決める。
        # Lを決める
        # Rを決める
        m = Markers(i)
        m.sort()
    return 0
