import sys
print(sys.version)
import pandas as pd

if( len(sys.argv)<1 ): #If the input is less then one, the code will print the input needed to be able to run the code
	print("tab_to_fasta.py")
	print("USAGE:	tab_to_fasta.py <Tab delimited .txt file from SNPCallOnly.sh>")
	exit()

try:
	SNPFile = sys.argv[1]

except Exception as e:
	print("USAGE:	tab_to_fasta.py <Tab delimited .txt file from SNPCallOnly.sh>")
	exit()

data=pd.read_csv(SNPFile, delimiter="\t", header=(0)) # Open tab delimited SNP file from SNPCallOnly.sh as panda df
data=data.replace(to_replace="/", value="", regex=True) # Remove "/" and replace with nothing
data.columns=">"+data.columns # Add header as fasta format
data.columns=data.columns.str.replace(".sort.bam", "") # Remove .sort.bam behind column name
data.drop(data.iloc[:, 0:3], axis=1, inplace=True) # Remove three first columns with chromosome [0], position [1] and reference base [2]

fasta=open("snpFile.fasta","w+") # Open a fasta file which we will write inf to

for columnName in data.columns: # Write column name and concentate all rows to a string
    fasta.write(columnName)
    fasta.write("\n")
    fasta.write(data[columnName].sum())
    fasta.write("\n")

print("OUTPUT: snpFile.fasta for input into iqtree")
