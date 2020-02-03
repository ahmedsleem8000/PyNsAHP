import math
class Ivns :

    def __init__(self, tl, tu, il, iu, fl, fu):

        self.tl= tl
        self.tu=tu
        self.il=il
        self.iu=iu
        self.fl=fl
        self.fu=fu


    def IsEmpty (self):
        if self.tl==0 and self.tu==0 and self.fl==0 and self.fu==0 and self.il==1 and self.iu==1 :
            return True
        else:
            return False

    def ivnsRound(self):
        self.tl=round(self.tl,2)
        self.tu=round(self.tu,2)
        self.fl=round(self.fl,2)
        self.fu=round(self.fu,2)
        self.il=round(self.il,2)
        self.iu=round(self.iu,2)


    def IsEqualTo (self,b):
        if self.tl==b.tl and self.tu==b.tu and self.fl==b.fl and self.fu==b.fu and self.il==b.il and self.iu==b.iu :
            return True
        else:
            return False

    def IsSubsetOf (self,b):
        if self.tl<=b.tl and self.tu<=b.tu and self.fl>=b.fl and self.fu>=b.fu and self.il>=b.il and self.iu>=b.iu :
            return True
        else:
            return False

    def Complement(self):
        b=Ivns(float(self.fl),float(self.fu), 1.0 -  float(self.iu) ,1.0 - float(self.il),float(self.tl),float(self.tu))
        #b=Ivns(self.fl,self.fu,  self.iu, self.il,self.tl,self.tu)

        return b

    def IvnsText(self):
        text= "<[" + str(self.tl) + "," + str(self.tu) + "],[" + str(self.il) +"," + str(self.iu) + "],["
        text= text + str(self.fl) + "," + str(self.fu) + "]>"
        #str= self.tl + self.tu + self.il + self.iu +  self.fl +  self.fu
        return text

    def Union(self,a,b):
        c = Ivns(0, 0, 0, 0, 0, 0, )
        c.tl = max(float(a.tl), float(b.tl))
        c.tu = max(float(a.tu), float(b.tu))
        c.il = min(float(a.il), float(b.il))
        c.iu = min(float(a.iu), float(b.iu))
        c.fl = min(float(a.fl), float(b.fl))
        c.fu = min(float(a.fu), float(b.fu))

        return c

    def Intersect(self, a,b):
        c= Ivns(0,0,0,0,0,0,)
        c.tl = min(float(a.tl), float(b.tl))
        c.tu = min(float(a.tu), float(b.tu))
        c.il = max(float(a.il), float(b.il))
        c.iu = max(float(a.iu), float(b.iu))
        c.fl = max(float(a.fl), float(b.fl))
        c.fu = max(float(a.fu), float(b.fu))

        return c

    def Difference(self, a,b):
        c = Ivns(0,0,0,0,0,0)

        c.tl = min(float(a.tl), float(b.fl))
        c.tu = min(float(a.tu), float(b.fu))
        c.il = max(float(a.il), 1 - float(b.iu))
        c.iu = max(float(a.iu), 1 - float(b.il))
        c.fl = max(float(a.fl), float(b.tl))
        c.fu = max(float(a.fu), float(b.tu))
        c.ivnsRound()
        return c

    def Addition(self,a, b):
        c = Ivns(0,0,0,0,0,0)

        c.tl = float(a.tl) + float(b.tl) - float(a.tl) * float(b.tl);
        c.tu = float(a.tu) + float(b.tu) - float(a.tu) * float(b.tu);
        c.il = float(a.il) * float(b.il);
        c.iu = float(a.iu) * float(b.iu);
        c.fl = float(a.fl) * float(b.fl);
        c.fu = float(a.fu) * float(b.fu);
        c.ivnsRound()
        c.minimize()
        return c

    def Product(self, a,b):
        c = Ivns(0,0,0,0,0,0)

        c.tl = float(a.tl) * float(b.tl);
        c.tu = float(a.tu )* float(b.tu);
        c.il = float(a.il )+ float(b.il) - float(a.il) * float(b.il);
        c.iu = float(a.iu) + float(b.iu) - float(a.iu) * float(b.iu);
        c.fl = float(a.fl )+ float(b.fl) - float(a.fl) * float(b.fl);
        c.fu = float(a.fu) + float(b.fu )- float(a.fu) * float(b.fu);
        c.ivnsRound()
        c.minimize()
        return c

    def Division(self, a,b):
        c = Ivns(0,0,0,0,0,0)
        if b.tl ==0 or b.tu==0 or b.il==1 or b.iu==1 or b.fl==1 or b.fu==1 :
            return 0


        else :
            c.tl = float(a.tl) / float(b.tl);
            c.tu = float(a.tu) / float(b.tu);
            c.il = (float(a.il) - float(b.il)) / (1 - float(b.il));
            c.iu = (float(a.iu) - float(b.iu)) / (1 - float(b.iu));
            c.fl = (float(a.fl) - float(b.fl)) / (1 - float(b.fl));
            c.fu = (float(a.fu) - float(b.fu)) / (1 - float(b.fu));
            c.ivnsRound()
            c.minimize()
            return c

    def DifferenceK(self,a, b):
        c = Ivns(0,0,0,0,0,0)

        c.tl = float(a.tl) - float(b.fu)
        c.tu = float(a.tu) - float(b.fl)
        c.il = max(float(a.il), float(b.il))
        c.iu = max(float(a.iu), float(b.iu))
        c.fl = float(a.fl) - float(b.tu)
        c.fu = float(a.fu) - float(b.tl)
        c.ivnsRound()

        return c


    def minimize(self):

        self.tl=min(self.tl,1)
        self.tu=min(self.tu,1)
        self.il=min(self.il,1)
        self.iu=min(self.iu,1)
        self.fl=min(self.fl,1)
        self.fu=min(self.fu,1)
        return self


    def ProductScalar(self,x):
        b=Ivns(float(self.tl) * x,float(self.tu) * x,float(self.il) * x,float(self.iu) * x,float(self.fl) * x,float(self.fu) * x)
        b.ivnsRound()
        b=b.minimize()
        return b

    def DivisionScalar(self,x):
        b=Ivns(float(self.tl) / x,float(self.tu) / x,float(self.il) / x,float(self.iu) / x,float(self.fl) / x,float(self.fu) / x)
        b.ivnsRound()
        b=b.minimize()
        return b

    def Power(self,x):
        c= Ivns(0,0,0,0,0,0)
        c.tl = float(self.tl) ** x
        c.tu = float(self.tu) ** x
        c.il = float(self.il) ** x
        c.iu = float(self.iu) ** x
        c.fl = float(self.fl) ** x
        c.fu = float(self.fu) ** x
        c.ivnsRound()
        c.minimize()
        return c

    def Ridvan(self):
        return (float(self.tl) + float(self.tu) + 4 - float(self.il) - float(self.iu) - float(self.fl) - float(self.fu)) / 6

    def Karasan(self):
        return ((float(self.tl) + float(self.tu) - float(self.fl) - float(self.fu) + 2) / 6) * (2 - float(self.il) - float(self.iu))

    def Nancy(self):
        return (4 + (float(self.tl) + float(self.tu) - 2 * float(self.il) - 2 * float(self.iu)  - float(self.fl) - float(self.fu)) * (4- float(self.tl) + float(self.tu) - float(self.fl) - float(self.fu))) / 8

    def onediff(self,x):
        one = Ivns(1, 1, 0, 0, 0, 0)
        return x.Difference(one, x)

    def linear(self, x, xmax, beneficial):
        result = xmax.Division(x, xmax)
        if isinstance(result, int) and result == 0:
            return 0
        else:
            if beneficial:
                return result
            else:

                return result.onediff(result)

    def linearMaxMin(self, x, xmax, xmin, beneficial):
        ivns = Ivns(0, 0, 0, 0, 0, 0)
        MaxMinDiff = ivns.Difference(xmax, xmin)
        if beneficial:
            overPart = ivns.Difference(x, xmin)
        else:
            overPart = ivns.Difference(xmax, x)

        return ivns.Division(overPart, MaxMinDiff)

    def linearSum(self, x, sumj,  beneficial):
        ivns = Ivns(0, 0, 0, 0, 0, 0)
        result=None
        if beneficial:
            return ivns.Division(x, sumj)
        else:
            result = ivns.Division( ivns.Division(Ivns(1,1,0,0,0,0),x),sumj)

            return result.onediff(result)


    def linearVector(self, x, sumj,  beneficial):
        ivns = Ivns(0, 0, 0, 0, 0, 0)
        result= None
        result = ivns.Division(x, sumj)
        if beneficial:
            return  result
        else:

            return result.onediff(result)

    def linearEnhanced(self, x,maxj,minj, sumMaxDiffx,sumXdiffMin,  beneficial):
        ivns = Ivns(0, 0, 0, 0, 0, 0)
        result=None
        overPart=None

        if beneficial:
            overPart= ivns.Difference(maxj,x)

            result= ivns.Division(overPart, sumMaxDiffx)

        else:
            overPart= ivns.Difference(x,minj)

            result = ivns.Division( overPart,sumXdiffMin)

        return result.onediff(result)

    def getScore(self):
        return round((float(self.tl)+float(self.tu))/2+ 2.0 -  (float(self.il)+float(self.iu))/2 -  (float(self.fl)+float(self.fu))/2 ,2)

    def deNeutrosophic(self,x):

        return  ((float(x.tl) + float(x.tu))/2 ) +(1-  ((float(x.il) + float(x.iu))/2) * float(x.iu) ) - ((float(x.fl) + float(x.fu)) / 2)* (1- float(x.fu))
