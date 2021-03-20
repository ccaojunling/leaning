class demo:
    def max_win(self,num,size):
        self.l2 = []
        self.num2 = int(len(num) - size + 1)
        for i in range(self.num2):
            ll = max(l[i:i+size])
            self.l2.append(ll)
        return(self.l2)


if __name__ == '__main__':
    l = [2, 3, 1, 4, 5, 2, 3]
    num1 = 2
    a=demo()
    print (a.max_win(num=l, size=num1))
