#align to sequence then assemble 

from mapped_reads_class import *

def stri(s):
	return s[:len(s)-1]

def get_reads():
	#with open("KSS_S7_L001_R1_001.fastq", "r") as f:
	reads = []
	with open("test", "r") as f:
		for i, line in enumerate(f):
			if i%4 == 0:
				temp_seq_id = line
			elif i%4 == 1:
				temp_seq = line
			elif i%4 == 3:
				temp_qual = line
				reads.append(read(stri(temp_seq_id), stri(temp_seq), stri(temp_qual))) #these have "line ends" or whatever on them
	return reads

def align():
	reads = get_reads()
	#ref_gaps = [] 
	#indexes where the ref sequence has a gap. Retroactively insert into old ones and insert into new ones if they don't have it?? 
	#note where the dashes in the reference happen and make sure they also happen in other references? Don't know if that makes sense
	for read in reads:
		read.mapped = needleman_wunsch(ref_seq, read.seq)



align()