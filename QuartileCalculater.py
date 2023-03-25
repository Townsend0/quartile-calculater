class Q1:
    
    def __init__(self, group):
        self.group = group
        self.i = self.group[0][1] - self.group[0][0]
        self.group_med_no = 0
        self.group_mod = self.group[0]
        self.sig_f = 0
        a = 0
        for b in self.group:
            a += b[2]
            b.append((b[0] + b[1]) / 2)
            b.append(b[3] * b[2])
            b.append(a)

    def mean(self):
        a = [0,0]
        for b in self.group:
            a[0] += b[4]
            a[1] += b[2]
        return round(a[0] / a[1],2)

    def mode(self):
        for a in range(len(self.group)):
            if self.group[a][2] > self.group_mod[2]:
                self.group_mod = self.group[a]
                l_mod = self.group_mod[0]
                tr1 = self.group_mod[2]
                tr2 = self.group_mod[2]
                if a != 0:
                    tr1 -= self.group[a - 1][2]
                if a != len(self.group) - 1:
                    tr2 -= self.group[a + 1][2]
        return round(l_mod + tr1 / (tr1 + tr2) * self.i, 2)

    def median(self):
        self.sig_f = self.group[len(self.group) - 1][5]
        for a in range(len(self.group)):
            if self.group[a][5] > self.sig_f/2:
                self.group_med_no = a
                l_med = self.group[a][0]
                f_med = self.group[a][2]
                f1 = self.group[a][5] - self.group[a][2]
                break
        return round(l_med + (self.sig_f / 2 - f1) / f_med * self.i, 2)
        
class Q2(Q1):

    def __init__(self, group):
        super().__init__(group)

    def quartile2(self):
        return round(Q2.median(), 2)
    
    def quartile1(self):
        l_q1 = self.group[self.group_med_no - 1][0]
        f_q1 = self.group[self.group_med_no - 1][2]
        f_1 = self.group[self.group_med_no - 1][5] - f_q1
        return round(l_q1 + (self.sig_f / 4 - f_1)/f_q1 * self.i, 2)

    def quartile3(self):
        l_q3 = self.group[self.group_med_no + 1][0]
        f_q3 = self.group[self.group_med_no + 1][2]
        f_1 = self.group[self.group_med_no + 1][5] - f_q3
        return round(l_q3 + (3 * self.sig_f / 4 - f_1) / f_q3 * self.i, 2)

Q1 = Q1([ [40,50,3], [50,60,5], [60,70,11], [70,80,22], [80,90,15], [90,100,6] ])
print("Q1. mean =",Q1.mean())
print("Q1. mode =",Q1.mode())
print("Q1. median =",Q1.median(),"\n")

Q2 = Q2([ [0,20,8], [20,40,12], [40,60,25], [60,80,15], [80,100,10] ])
Q2.quartile2()
print("Q2. Quartile1 =",Q2.quartile1())
print("Q2. Quartile2 =",Q2.quartile2())
print("Q2. Quartile3 =",Q2.quartile3())