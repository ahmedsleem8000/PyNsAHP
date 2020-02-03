from ivns.ivns import Ivns
import copy
from math import sqrt
class IvnM:

    def __init__(self, text):

        self.text = text

    def GetRowsCount(self):

        return len(self.text.split('\n'))

    def GetColsCount(self):
        text=self.text.split('\n')

        return len(text[0].split('  '))

    def Create(self):
        matrix = []
        text=self.text.split('\n')
        for line in text:
            items = line.split('  ')
            row=[]
            for item in items:
                item =item.translate({ord(i): None for i in '<>[]'})
                item= item.translate({ord(i): None for i in ' '})
                numbers=item.split(',')
                ivns=Ivns(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5],)
                row.append(ivns)
            matrix.append(row)
        return matrix

    def ToText(self,matrix):
        strText=''
        for row in matrix:
            for item in row:
                if isinstance(item, float) or isinstance(item, int) or item== None :
                    strText = strText + str(item) + '  '
                else:

                    strText = strText + item.IvnsText() + '  '
                #strText=strText + '&&&&' + item.tl +'&&' + item.tu
            strText=strText+ '\n'
        return strText

    def ArrayToText(self,matrix):
        strText=''
        for item in matrix:
                if isinstance(item, float) or isinstance(item, int) or item== None :
                    strText = strText + str(item) + '  '
                else:

                    strText = strText + item.IvnsText() + '  '
                #strText=strText + '&&&&' + item.tl +'&&' + item.tu
        return strText

    def EmptyCheck(self,matrix):
        NoofEmpty=0
        for row in matrix:
            for item in row:
                if item.IsEmpty() :
                    NoofEmpty=NoofEmpty + 1

        return NoofEmpty

    def Complement(self,matrix):
        mat=[]
        for row in matrix:
            rows=[]
            for item in row:
                rows.append(item.Complement())
            mat.append(rows)
        return mat

    def productScalar(self,matrix,x):
        mat = []
        for row in matrix:
            rows = []
            for item in row:
                rows.append(item.ProductScalar(x))

            mat.append(rows)

        return mat

    def DivScalar(self, matrix, x):
        mat = []
        for row in matrix:
            rows = []
            for item in row:
                rows.append(item.DivisionScalar(x))

            mat.append(rows)

        return mat

    def KarasanScore(self, matrix):
        mat = []
        for row in matrix:
            rows = []
            for item in row:
                rows.append(item.Karasan())

            mat.append(rows)

        return mat

    def Intersction(self,listA,listB):

        listC =  copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j] = listA[i][j].Intersect(listA[i][j], listB[i][j])
        return listC

    def NancyScore(self, matrix):
        mat = []
        for row in matrix:
            rows = []
            for item in row:
                rows.append(item.Nancy())

            mat.append(rows)

        return mat


    def RidvanScore(self, matrix):
        mat = []
        for row in matrix:
            rows = []
            for item in row:
                rows.append(item.Ridvan())

            mat.append(rows)

        return mat

    def Power(self, matrix, x):
        mat = []
        for row in matrix:
            rows = []
            for item in row:
                rows.append(item.Power(x))

            mat.append(rows)

        return mat

    def Union(self,listA,listB):

        listC = copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j]= listA[i][j].Union(listA[i][j],listB[i][j])
        return listC

    def Addition(self,listA,listB):

        listC = copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j]= listA[i][j].Addition(listA[i][j],listB[i][j])
        return listC

    def Difference(self,listA,listB):

        listC = copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j]= listA[i][j].Difference(listA[i][j],listB[i][j])
        return listC

    def DifferenceK(self,listA,listB):

        listC = copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j]= listA[i][j].DifferenceK(listA[i][j],listB[i][j])
        return listC

    def Product(self,listA,listB):

        listC = copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j]= listA[i][j].Product(listA[i][j],listB[i][j])
        return listC

    def getMin(self,listj,col):
        minscore= 9999
        minitem = None
        for row in listj:
                if row[col].getScore()<  minscore:
                    minitem=row[col]
                    minscore=row[col].getScore()

        return minitem


    def getmax(self,listj,col):
        maxscore= -9999
        maxitem = None
        for row in listj:
                if row[col].getScore()>  maxscore:
                    maxitem=row[col]
                    maxscore=row[col].getScore()

        return maxitem

    def getSum(self,listj,col):
        sum= Ivns(0,0,1,1,1,1)
        for row in listj:
              sum= sum.Addition( sum,row[col])
        return sum



    def getSumOfMaxDiffX(self,listj,col,xmax):
        sum= Ivns(0,0,1,1,1,1)
        maxitem = None
        for row in listj:
              sum= sum.Addition( sum,sum.Difference(xmax, row[col]))
        return sum
    def getSumOfXDiffMin(self,listj,col,xmin):
        sum= Ivns(0,0,1,1,1,1)
        maxitem = None
        for row in listj:
              sum= sum.Addition( sum,sum.Difference( row[col],xmin))
        return sum

    def getSquareSum(self,listj,col):
        sum= Ivns(0,0,1,1,1,1)
        maxitem = None
        for row in listj:
              sum= sum.Addition( sum, row[col].Power(2))
        return sum

    def matrixLinear(self,matrix,bene):
        listj= IvnM('')
        result= copy.deepcopy(matrix)
        maxj= None

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                maxj = listj.getmax(matrix,j)
                result[i][j]= maxj.linear(matrix[i][j],maxj,bene)


        return result

    def matrixLinearMinMax(self,matrix,bene):
        listj= IvnM('')
        result= copy.deepcopy(matrix)
        maxj= None
        minj= None

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                maxj = listj.getmax(matrix,j)
                minj = listj.getMin(matrix,j)
                result[i][j]= maxj.linearMaxMin(matrix[i][j],maxj,maxj,bene)
        return result

    def matrixLinearSum(self,matrix,bene):
        listj= IvnM('')
        result= copy.deepcopy(matrix)
        sumj= None

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                sumj = listj.getSum(matrix,j)

                result[i][j]= sumj.linearSum(matrix[i][j],sumj,bene)
        return result

    def matrixLinearVector(self, matrix, bene):
        listj = IvnM('')
        result = copy.deepcopy(matrix)
        sumj = None

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                sumj = listj.getSquareSum(matrix, j)
                sumj= sumj.Power(0.5)
                result[i][j] = sumj.linearVector(matrix[i][j], sumj, bene)

        return result
    def matrixLinearEnhanced(self, matrix, bene):
        listj = IvnM('')
        result = copy.deepcopy(matrix)
        sumj = None

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                maxj= listj.getmax(matrix,j)
                minj= listj.getMin(matrix,j)
                sumMaxDiffX = listj.getSumOfMaxDiffX(matrix, j,maxj)
                sumXDiffMin = listj.getSumOfXDiffMin(matrix,j,minj)
                result[i][j] = sumMaxDiffX.linearEnhanced(matrix[i][j],maxj,minj,sumMaxDiffX,sumXDiffMin, bene)

        return result

    def getMatrixScore(self,listA):
        listC = copy.deepcopy(listA)
        for i in range(len(listA)):
            for j in range(len(listA[0])):
                listC[i][j]= listA[i][j].getScore()
        return listC
    def getSumDirect(self,listj,col):
        sum= Ivns(0,0,0,0,0,0)

        for row in listj:
              sum.tl =  round(sum.tl + float(row[col].tl),3)
              sum.tu =  round(sum.tu + float(row[col].tu),3)
              sum.il =  round(sum.il + float(row[col].il),3)
              sum.iu =  round(sum.iu + float(row[col].iu),3)
              sum.fl =  round(sum.fl + float(row[col].fl),3)
              sum.fu =  round(sum.fu + float(row[col].fu),3)

        return sum
    def getSumDirectForRow(self,matrix,row):
        sum= Ivns(0,0,0,0,0,0)

        for j in range(len(matrix[0])):
              sum.tl =  round(sum.tl + float(matrix[row][j].tl),3)
              sum.tu =  round(sum.tu + float(matrix[row][j].tu),3)
              sum.il =  round(sum.il + float(matrix[row][j].il),3)
              sum.iu =  round(sum.iu + float(matrix[row][j].iu),3)
              sum.fl =  round(sum.fl + float(matrix[row][j].fl),3)
              sum.fu =  round(sum.fu + float(matrix[row][j].fu),3)
        return sum

    def matrixGetColSum(self, matrix):
        listj= IvnM('')
        result= []
        sumj= None

        for i in range(1):

            for j in range(len(matrix[0])):
                sumj = listj.getSumDirect(matrix,j)

                result.append(sumj)
        return result

    def getDivDirect(self,listj,col):
         divResult= Ivns(0,0,0,0,0,0)

         divResult.tl =  round(float(listj.tl) / float(col.tl),3)
         divResult.tu =  round(float(listj.tu) / float(col.tu),3)
         divResult.il =  round(float(listj.il) / float(col.il),3)
         divResult.iu =  round(float(listj.iu) / float(col.iu),3)
         divResult.fl =  round(float(listj.fl)/ float(col.fl),3)
         divResult.fu =  round(float(listj.fu) / float(col.fu),3)

         return divResult

    def matrixGetCriteriaWeight(self, matrix):
        listj= IvnM('')
        result= []
        sumj= None
        NumOfCriteria= len(matrix)
        divideBy= Ivns(NumOfCriteria,NumOfCriteria,NumOfCriteria,NumOfCriteria,NumOfCriteria,NumOfCriteria)
        for i in range(NumOfCriteria):
            sumj = listj.getSumDirectForRow(matrix,i)
            sumj= self.getDivDirect(sumj,divideBy)
            result.append(sumj)
        return result

    def AHPgetmatrixDivSum(self, matrix,colSum):

        result= copy.deepcopy(matrix)

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                colSum[j].tl= colSum[j].tu
                colSum[j].il = colSum[j].iu
                colSum[j].fl = colSum[j].fu

                result[i][j]= self.getDivDirect(matrix[i][j],colSum[j])



        return result

    def AHPgetCriteriaWeight(self, matrix):

        result= copy.deepcopy(matrix)

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                result[i][j]= self.getDivDirect( matrix[i][j],0)



        return result

    def AHPproductWeight(self, matrix, cweight):
        result=copy.deepcopy(matrix)
        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                     result[i][j].tl = round(float(matrix[i][j].tl) * float(cweight[j].tl),3)
                     result[i][j].tu = round(float(matrix[i][j].tu) * float(cweight[j].tu),3)
                     result[i][j].il = round(float(matrix[i][j].il) * float(cweight[j].il),3)
                     result[i][j].iu = round(float(matrix[i][j].iu) * float(cweight[j].iu),3)
                     result[i][j].fl = round(float(matrix[i][j].fl) * float(cweight[j].fl),3)
                     result[i][j].fu = round(float(matrix[i][j].fu) * float(cweight[j].fu),3)


        return result

    def AHPCrSumWeight(self,matrix):
        listj = IvnM('')
        result = []
        sumj = None
        NumOfCriteria = len(matrix)

        for i in range(NumOfCriteria):
            sumj = listj.getSumDirectForRow(matrix, i)

            result.append(sumj)
        return result

    def AHP_CSWdivW(self,CSW,W):
        result=copy.deepcopy(W)

        for i in range(len(W)) :
            result[i].tl = float(CSW[i].tl) / float(W[i].tl)
            result[i].tu = float(CSW[i].tu) / float(W[i].tu)
            result[i].il = float(CSW[i].il) / float(W[i].il)
            result[i].iu = float(CSW[i].iu) / float(W[i].iu)
            result[i].fl = float(CSW[i].fl) / float(W[i].fl)
            result[i].fu = float(CSW[i].fu) / float(W[i].fu)
        return result

    def printFloatMatrix(self,matrix):
        result=''

        for row in matrix:
            for item in row:
                result=   result + str(item) + ' , '
            result= str(result) + '\n'
        return result

    def deNuutrosophicMatrix(self, matrix):
        result = copy.deepcopy(matrix)
        x = Ivns(0, 0, 0, 0, 0, 0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[i][j]= round(x.deNeutrosophic(matrix[i][j]),3)
        return result
    def deNuutrosophicSum(self,matrix):
        sum=0
        rowSum = []
        x = Ivns(0, 0, 0, 0, 0, 0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               sum = sum + matrix[i][j]
            sum= round(sum,3)
            rowSum.append(sum)
            sum=0

        return rowSum

    def lambdamax(self,arr,w):

        Rindex=[0,0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49]

        sum=0
        x = Ivns(0, 0, 0, 0, 0, 0)
        for i in range(len(arr)):
            sum = sum + float(arr[i]) / x.deNeutrosophic(w[i])

        result = sum / len(arr)
        result =result - len(arr)
        result= result / (len(arr) - 1)

        result=result/Rindex[len(arr)]
        result=round(result,4)
        return result



    def AHP(self, matrix):
        sumCols=  self.matrixGetColSum(matrix)
        updatedMatrix= self.AHPgetmatrixDivSum(matrix,sumCols)
        CriteriaWeight= self.matrixGetCriteriaWeight(updatedMatrix)
        matrixTimesWeight= self.AHPproductWeight(matrix,CriteriaWeight)
        CrSumWeight=self.AHPCrSumWeight(matrixTimesWeight)
        CSWdivW= self.AHP_CSWdivW(CrSumWeight,matrixTimesWeight)
        lambdaMax =self.DivScalar(CSWdivW,len(CSWdivW))

        listj= IvnM('')
        result= []
        sumj= None

        for i in range(1):

            for j in range(len(matrix[0])):
                sumj = listj.getSumDirect(matrix,j)

                result.append(sumj)
        return result

    def EuclidianDistance(self, n1, n2):
        result=0
        for i in range(len(n1)):
            result = result + (float(n1[i][0].tl) - float(n2[i][0].tl))**2 + (float(n1[i][0].tu) - float(n2[i][0].tu))**2 + (float(n1[i][0].il) - float(n2[i][0].il))**2 + (float(n1[i][0].iu) - float(n2[i][0].iu))**2 + (float(n1[i][0].fl) - float(n2[i][0].fl))**2 +  (float(n1[i][0].fu) - float(n2[i][0].fu))**2

        result = sqrt(result/(6 * len(n1)))
        return result

    def similarity(self, n1, n2):
        result1=0
        result2 = 0

        for i in range(len(n1)):
            result1 = result1 + min(float(n1[i][0].tl) , float(n2[i][0].tl)) + min(float(n1[i][0].tu) , float(n2[i][0].tu)) + min(float(n1[i][0].il) , float(n2[i][0].il)) + min(float(n1[i][0].iu) , float(n2[i][0].iu)) + min(float(n1[i][0].fl) , float(n2[i][0].fl)) +  min(float(n1[i][0].fu) , float(n2[i][0].fu))
            result2 = result2 + max(float(n1[i][0].tl) , float(n2[i][0].tl)) + max(float(n1[i][0].tu) , float(n2[i][0].tu)) + max(float(n1[i][0].il) , float(n2[i][0].il)) + max(float(n1[i][0].iu) , float(n2[i][0].iu)) + max(float(n1[i][0].fl) , float(n2[i][0].fl)) +  max(float(n1[i][0].fu) , float(n2[i][0].fu))

        result = result1/result2
        return result