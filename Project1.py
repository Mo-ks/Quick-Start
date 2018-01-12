#!/usr/bin/python

from collections import defaultdict
import re, sys, random 
from Bio import SeqIO
# - - - - - H E A D E R - - - - - - - - - - - - - - - - -
'''
Objectives:
1. Read in a sequence
2. Find a specific segment of that sequence
3. Change a letter (mutation)
4. Output the sequence with the mutation

'''

# - - - - - U S E R    V A R I A B L E S - - - - - - - -

mssg = " Search and Destroy"
genFile  = 'P1.txt'
inFile   = 'P1.txt'
inFolder = '.'
site   = ""  # what the mutation is 
outFile  = "Project1-Out.txt"
GenSeqs = defaultdict(lambda: "my own unknown" )
CT        = defaultdict(lambda: 'nada')
GeneSeqs   = defaultdict(lambda: 'nada')
CX  = defaultdict(lambda: 0)
count = defaultdict(lambda: 0)
NTs    = ['a', 't', 'g', 'c']
afreq		 = defaultdict(lambda: -1.1 )
tfreq		 = defaultdict(lambda: -1.1 )
gfreq		 = defaultdict(lambda: -1.1 )
cfreq		= defaultdict(lambda: -1.1 )
seq = 'P1.txt'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - M A I N - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("\n\n", mssg, ". . . . ")

# 
# records = list(SeqIO.parse("P1.txt", "fasta"))
# print(records)  # first record

for records in SeqIO.parse ('P1.txt','fasta'):
	if 'a' in records.seq:
		print (records)

#  
#  
   
