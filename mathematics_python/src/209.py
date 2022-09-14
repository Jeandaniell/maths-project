#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## 209poll
## File description:
## 209poll
##

L=int
K=exit
J=len
B=print
from sys import argv as A,stdout as F
from math import sqrt as D
class C(Exception):
	def __init__(A,message,errors='BadArgumentError'):super().__init__(message);A.errors=errors
class G:
	def __init__(A,pSize,sSize,p):
		E='You must pass a probability between 0 and 100';D=sSize;B=pSize
		if B<0 or D<0:raise C(E)
		if 0<p>100:raise C(E)
		A.pSize=B;A.sSize=D;A.probability=p
	def computeValue(A):A.variance=A.probability*(100-A.probability)/10000/A.sSize*((A.pSize-A.sSize)/(A.pSize-1));A.confidence95=1.96*D(A.variance)*2/2*100;A.confidence99=2.58*D(A.variance)*2/2*100
	def printValue(A):B('population size:\t\t{}'.format(A.pSize));B('sample size:\t\t\t{}'.format(A.sSize));B('voting intentions:\t\t{:.2f}%'.format(A.probability));B('variance:\t\t\t{:.6f}'.format(A.variance));B('95% confidence interval:\t[{:.2f}% ; {:.2f}%]'.format(0 if A.probability-A.confidence95<0 else A.probability-A.confidence95,100 if A.probability+A.confidence95>100 else A.probability+A.confidence95));B('99% confidence interval:\t[{:.2f}% ; {:.2f}%]'.format(0 if A.probability-A.confidence99<0 else A.probability-A.confidence99,100 if A.probability+A.confidence99>100 else A.probability+A.confidence99))
def H():B('USAGE\n\t./209poll pSize sSize p\n\nDESCRIPTION\n\tpSize\tsize of the population\n\tsSize\tsize of the sample (supposed to be representative)\n\tp\tpercentage of voting intentions for a specific candidate')
def I():
	if J(A)==2:
		if A[1]=='-h':H();K(0)
	if J(A)is not 4:raise C('You must pass 3 valid arguments')
	B=G(L(A[1]),L(A[2]),float(A[3]));B.computeValue();B.printValue()
if __name__=='__main__':
	try:I()
	except BaseException as E:F.write(str(type(E).__name__)+': {}\n'.format(E));K(84)
