from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render_to_response
from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponse
from ivns.models import InputForm
from ivns.models import InputNormForm
from ivns.models import InputAHPForm
from ivns.models import InputSimiForm


from ivns.compute import compute
from ivns.IvnM import IvnM

from ivns.ivns import Ivns
from ivns.normal import norm

def similarity(request):
    form = InputSimiForm(request.POST or None)
    context = {'form': form, }

    if request.method == 'POST':
        if 'Euclidian' in request.POST:
            form = InputSimiForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.num1
                textB = form.num2
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrixA.EuclidianDistance(listA,listB)
                resultlabel='Euclidian Distance'
                form = InputSimiForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'simi' in request.POST:
                    form = InputSimiForm(request.POST)
                    if form.is_valid():
                        form = form.save(commit=False)
                        textA = form.num1
                        textB = form.num2
                        matrixA = IvnM(textA)
                        matrixB = IvnM(textB)
                        matrix = IvnM(textA)
                        listA = matrixA.Create()
                        listB = matrixB.Create()
                        result = matrixA.similarity(listA, listB)
                        resultlabel = 'Similarity Measure'
                        form = InputSimiForm()
                        context = {'form': form,
                                   'result': result,
                                   'resultlabel': resultlabel,
                                   }
    else:
        form = InputSimiForm(request.POST or None)



    return render(request, 'similarty.html', context)

def ahp(request):

    form = InputAHPForm(request.POST or None)
    context = {'form': form, }
    if request.method == 'POST':
        if 'AHP' in request.POST:
            form = InputAHPForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                text=form.matrix
                matrixA = IvnM(text)
                listA = matrixA.Create()
                #aaa= Ivns(.1,.5,.3,.4,.2,.5)
                #bbb= Ivns(.4,.5,.2,.3,.1,.3)
                sumCols = matrixA.matrixGetColSum(listA)
                updatedMatrix = matrixA.AHPgetmatrixDivSum(listA, sumCols)
                CriteriaWeight = matrixA.matrixGetCriteriaWeight(updatedMatrix)
                matrixTimesWeight = matrixA.AHPproductWeight(listA, CriteriaWeight)
                CrSumWeight = matrixA.AHPCrSumWeight(matrixTimesWeight)
                CSWdivW = matrixA.AHP_CSWdivW(CrSumWeight, CriteriaWeight)
                #lambdaMax = matrixA.DivScalar(CSWdivW, len(CSWdivW))
                deNutrosophicValue = matrixA.deNuutrosophicMatrix(matrixTimesWeight)
                deNutrosophicSum = matrixA.deNuutrosophicSum(deNutrosophicValue)
                lambdaMax = matrixA.lambdamax(deNutrosophicSum,CriteriaWeight)
                result =  matrixA.ArrayToText(matrixA.matrixGetColSum(listA))
                result2 = matrixA.ToText(updatedMatrix)
                result3 = matrixA.ArrayToText(CriteriaWeight)
                result4 = matrixA.ToText(matrixTimesWeight)
                result5 = matrixA.printFloatMatrix(deNutrosophicValue)

                #result5 = deNutrosophicValue
                result6= matrixA.ToText(listA)
                #result5 = matrixA.ArrayToText(CrSumWeight)
                result6 = deNutrosophicSum
                result7 = lambdaMax

                #result= matrixA.ToText(matrixA.getMatrixScore(listA))
                #result = (matrixA.getmax(listA,1)).IvnsText()
                #aaa=       ( aaa.Division(aaa,bbb))
                #result= aaa.IvnsText()
                resultlabel='AHP '

                form = InputAHPForm()
                context = {'form': form,
                           'result': result,
                           'result2': result2,
                           'result3': result3,
                           'result4': result4,
                           'result5': result5,
                           'result6': result6,
                           'result7': result7,
                           'resultlabel': resultlabel,
                           }
    else:
        form = InputAHPForm(request.POST or None)



    return render(request, 'ahp.html', context)


def norm(request):

    form = InputNormForm(request.POST or None)
    context = {'form': form, }



    if request.method == 'POST':
        if 'linear' in request.POST:
            form = InputNormForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                text=form.matrix
                matrixA = IvnM(text)
                listA = matrixA.Create()
                #aaa= Ivns(.1,.5,.3,.4,.2,.5)
                #bbb= Ivns(.4,.5,.2,.3,.1,.3)
                result = matrixA.ToText(matrixA.matrixLinear(listA,form.beneficial))
                #result= matrixA.ToText(matrixA.getMatrixScore(listA))
                #result = (matrixA.getmax(listA,1)).IvnsText()
                #aaa=       ( aaa.Division(aaa,bbb))
                #result= aaa.IvnsText()
                resultlabel='Linear Normalization '
                if form.beneficial :
                    resultlabel= resultlabel + ' (Beneficial)'
                else:
                    resultlabel = resultlabel + ' (Non-Beneficial)'
                form = InputNormForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'maxmin' in request.POST:
            form = InputNormForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                text=form.matrix
                matrixA = IvnM(text)
                listA = matrixA.Create()
                #aaa= Ivns(.1,.5,.3,.4,.2,.5)
                #bbb= Ivns(.4,.5,.2,.3,.1,.3)
                result = matrixA.ToText(matrixA.matrixLinearMinMax(listA,form.beneficial))
                #result= matrixA.ToText(matrixA.getMatrixScore(listA))
                #result = (matrixA.getmax(listA,1)).IvnsText()
                #aaa=       ( aaa.Division(aaa,bbb))
                #result= aaa.IvnsText()
                resultlabel='Linear Normalization (Max-Min)'
                if form.beneficial:
                    resultlabel = resultlabel + ' (Beneficial)'
                else:
                    resultlabel = resultlabel + ' (Non-Beneficial)'
                form = InputNormForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'sum' in request.POST:
            form = InputNormForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                text=form.matrix
                matrixA = IvnM(text)
                listA = matrixA.Create()
                result = matrixA.ToText(matrixA.matrixLinearSum(listA,form.beneficial))
                resultlabel='Linear Normalization (Sum)'
                if form.beneficial:
                    resultlabel = resultlabel + ' (Beneficial)'
                else:
                    resultlabel = resultlabel + ' (Non-Beneficial)'
                form = InputNormForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'vector' in request.POST:
            form = InputNormForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                text=form.matrix
                matrixA = IvnM(text)
                listA = matrixA.Create()
                result = matrixA.ToText(matrixA.matrixLinearVector(listA,form.beneficial))
                resultlabel='Linear Normalization (Vector)'
                if form.beneficial:
                    resultlabel = resultlabel + ' (Beneficial   )'
                else:
                    resultlabel = resultlabel + ' (Non-Beneficial)'
                form = InputNormForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'enhanced' in request.POST:
            form = InputNormForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                text=form.matrix
                matrixA = IvnM(text)
                listA = matrixA.Create()
                result = matrixA.ToText(matrixA.matrixLinearEnhanced(listA, form.beneficial))
                resultlabel='Enhanced Accuracy Normalization'
                if form.beneficial:
                    resultlabel = resultlabel + ' (Beneficial)'
                else:
                    resultlabel = resultlabel + ' (Non-Beneficial)'
                form = InputNormForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }

        else:
            form = InputNormForm(request.POST or None)
            return render(request, 'norm.html', {'form': form})

    else:
        form = InputNormForm(request.POST or None)




    return render(request, 'norm.html', context)




def index(request):
    s = None  # initial value of result
    rowscountA = 0
    colscountA = 0
    rowscountB = 0
    colscountB = 0
    result=''

    outputA=''
    outputB = ''
    textA=textB=''
    emptynumA=0
    emptynumB = 0
    complementA= None
    complementB = None
    productScalar=powerA=powerB=''
    divScalar=''
    divScalarB=''
    compAtext=''
    compBtext = ''
    productScalarB=''
    intersection=''
    addition=''
    product=''
    diff=''
    diffk=''
    union=''
    testA=testB=''
    resultlabel=''
    karasanA=karasanB=nancyA=nancyB=ridvanA=ridvanB=''

    form = InputForm(request.POST or None)
    context = {'form': form,}
    if request.method == 'POST':
        if 'complementA' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Complement(listA))
                resultlabel='Complement of Matrix A'
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }

        elif 'complementB' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Complement(listB))
                resultlabel='Complement of Matrix B'
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'productA' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixA.productScalar(listA,float(form.productScalar)))
                resultlabel='Product Scalar of Matrix A with ' + str(form.productScalar)
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'productB' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixB.productScalar(listB,float(form.productScalar)))
                resultlabel='Product Scalar of Matrix B with ' + str(form.productScalar)
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'powerA' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixA.Power(listA,float(form.productScalar)))
                resultlabel='Power of Matrix A with ' + str(form.productScalar)
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'powerB' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixB.Power(listB,float(form.productScalar)))
                resultlabel='Power of Matrix B with ' + str(form.productScalar)
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'karasanA' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixA.KarasanScore(listA))
                resultlabel='Karasan Score of Matrix A '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'karasanB' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixB.KarasanScore(listB))
                resultlabel='Karasan Score of Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'ridvanA' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixA.RidvanScore(listA))
                resultlabel='Ridvan Score of Matrix A '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'ridvanB' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixB.RidvanScore(listB))
                resultlabel='Ridvan Score of Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'nancyA' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixA.NancyScore(listA))
                resultlabel='Nancy Score of Matrix A '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'nancyB' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrixB.NancyScore(listB))
                resultlabel='Nancy Score of Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'intersection' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Intersction(listA, listB))
                resultlabel='Matrix A intersect Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'union' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Union(listA, listB))
                resultlabel='Matrix A Union Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'plus' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Addition(listA, listB))
                resultlabel='Matrix A + Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'diff' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Difference(listA, listB))
                resultlabel='Difference : Matrix A - Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'kdiff' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.DifferenceK(listA, listB))
                resultlabel='Karasan Difference : Matrix A - Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }
        elif 'product' in request.POST:
            form = InputForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                textA = form.A
                textB = form.B
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                result = matrix.ToText(matrix.Product(listA, listB))
                resultlabel='Difference : Matrix A - Matrix B '
                form = InputForm()
                context = {'form': form,
                           'result': result,
                           'resultlabel': resultlabel,
                           }

        elif 'output' in request.POST:
            form = InputForm(request.POST or None)
            if form.is_valid():
                form = form.save(commit=False)

                textA = form.A
                textB = form.B
                form.A=''
                form.B=''
                matrixA = IvnM(textA)
                matrixB = IvnM(textB)
                matrix = IvnM(textA)
                listA = matrixA.Create()
                listB = matrixB.Create()
                outputA = matrixA.ToText(listA)
                outputB = matrixB.ToText(listB)
                rowscountA = matrixA.GetRowsCount()
                colscountA = matrixA.GetColsCount()
                rowscountB = matrixB.GetRowsCount()
                colscountB = matrixB.GetColsCount()

                emptynumA = matrixA.EmptyCheck(listA)
                emptynumB = matrixB.EmptyCheck(listB)
                #complementA= matrixA.Complement(listA)
                #complementB= matrixB.Complement(listB)

                compAtext= matrix.ToText(matrix.Complement(listA))
                compBtext= matrix.ToText(matrix.Complement(listB))
                productScalarB= matrix.ToText(matrixB.productScalar(listB,float(form.productScalar)))

                karasanA= matrix.ToText(matrixA.KarasanScore(listA))

                karasanB = matrix.ToText(matrixB.KarasanScore(listB))
                nancyA = matrix.ToText(matrixA.NancyScore(listA))
                nancyB = matrix.ToText(matrixB.NancyScore(listB))
                ridvanA = matrix.ToText(matrixA.RidvanScore(listA))
                ridvanB = matrix.ToText(matrixB.RidvanScore(listB))

                powerA= matrix.ToText(matrixA.Power(listA,float(form.productScalar)))

                powerB= matrix.ToText(matrixB.Power(listB,float(form.productScalar)))

                productScalar= matrix.ToText(matrixA.productScalar(listA,float(form.productScalar)))
                divScalar = matrix.ToText(matrixA.DivScalar(listA, float(form.productScalar)))
                divScalarB = matrix.ToText(matrixB.DivScalar(listB, float(form.productScalar)))

                #intersection = matrix.ToText(matrix.Intersction(listA,listB))
                intersection = matrix.ToText(matrix.Intersction(listA, listB))

                union = matrix.ToText(matrix.Union(listA, listB))
                #union =  matrix.ToText(listA)
                addition = matrix.ToText(matrix.Addition(listA, listB))
                #addition = matrix.ToText(listB)
                diff = matrix.ToText(matrix.Difference(listA, listB))
                diffk = matrix.ToText(matrix.DifferenceK(listA, listB))
                product = matrix.ToText(matrix.Product(listA, listB))
                testA=matrix.ToText(listA)
                testB= matrix.ToText(listB)
                form = InputForm()
                context = {'form': form,
                           'rowscountA': '%d' % rowscountA,
                           'colscountA': '%d' % colscountA,
                           'rowscountB': '%d' % rowscountB,
                           'colscountB': '%d' % colscountB,
                           'Aoutput': textA,
                           'Boutput': textB,
                           'emptynumA': emptynumA,
                           'emptynumB': emptynumB,
                           'compAtext': compAtext,
                           'compBtext': compBtext,
                           'productScalar': productScalar,
                           'productScalarB': productScalarB,
                           'divScalarB': divScalarB,
                           'divScalar': divScalar,
                           'intersection': intersection,
                           'product': product,
                           'addition': addition,
                           'diff': diff,
                           'diffk': diffk,
                           'union': union,
                           'karasanA': karasanA,
                           'karasanB': karasanB,
                           'nancyA': nancyA,
                           'nancyB': nancyB,
                           'ridvanA': ridvanA,
                           'ridvanB': ridvanB,
                           'powerA': powerA,
                           'powerB': powerB,
                           'testA': testA,
                           'testB': testB,
                           }
            else:
                form = InputForm(request.POST or None)
                return render(request, 'index.html', {'form': form})

    else:
        form = InputForm(request.POST or None)




    return render(request, 'index.html', context)
    # return render_to_response('hw2.html',
    #                          {'form': form,
    #                           's': '%.5f' % s if isinstance(s, float) else ''
    #                           }, context_instance=RequestContext(request))

    # context = {'form': form}
    # return render(request, 'index.html', context)

# def present_output(form):
#    r = form.r
#    s = compute(r)
#    return HttpResponse('Hello, World! sin(%s)=%s' % (r, s))
