#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Loan2Value mortgage calculator

inputs: priceband1, priceband2, deposit, loan2val, term(months), interest(apr), fee

usage: python L2V.py 100000 500000 40000 80 12 2.5 1000

AS
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

inp = sys.argv[1:]

# Calculate loan to value ratio
if len(inp) > 2:	
	tot   = np.arange(int(inp[0]),int(inp[1])+1)
	dep   = int(inp[2])
	thrsh = int(inp[3])
	loan  = tot - dep
	rat   = (loan/tot)*100

	fig = plt.figure()
	plt.plot(tot,rat,color='red')
	
	# find the closest point to requested ratio & add line
	i   = np.abs(thrsh-rat).argmin()
	plt.axhline(y=rat[i], xmin=0, xmax=1, hold=None)
	plt.show()
	buf = "The closest home value for your ratio = %d\n" % (tot[i])
	print(buf)

# check for fee
if len(inp) < 7:
	fee = 0
else:
	fee = int(inp[6])

# calculate repayments as required
if len(inp) > 5:
	term = int(inp[4])
	apr  = float(inp[5])
	
	theloan = tot[i] - dep
	adjloan = theloan + (theloan*(apr*.01)) + fee
	buf = "Total mortgage = %d\n" % (adjloan)
	print(buf)
	
	repay   = adjloan / (term*12)
	buf = "Total repayments should be around %d per month\n" % (repay)
	print(buf)

	

