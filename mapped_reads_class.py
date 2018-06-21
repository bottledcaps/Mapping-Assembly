class mapped_read():
	def __init__(self, seq, ref_loc, length):
		self.seq = seq
		self.ref_loc = ref_loc
		self.length = length

class read():
	def __init__(self, seqid, seq, qual):
		self.seq = seq
		self.seqid = seqid
		self.qual = qual
		