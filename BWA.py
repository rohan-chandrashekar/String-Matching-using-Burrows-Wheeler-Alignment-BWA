#DNA Substring Matching - Burrows-Wheeler Algorithm

class BWA:
	def __init__(self, reference):
		rotation_list, rotation_list_reverse, suffix_array, bwt = [list() for i in range(4)]
		C, Occ, Occ_reverse = [dict() for i in range(3)]
		alphabet = set()
		reverse_reference = reference[::-1]
		
		reference = reference.lower()
		for char in reference:
			alphabet.add(char)
		
		for char in alphabet:
			C[char] = 0
			Occ[char] = list()
			Occ_reverse[char] = list()
	
		reference = "%s$" % reference
		reverse_reference = "%s$" % reverse_reference

		for i in range(len(reference)):
			new_rotation = "%s%s" % (reference[i:],reference[0:i])
			struct = Suffix(new_rotation,i)
			rotation_list.append(struct)
			
			new_rotation_reverse = "%s%s" % (reverse_reference[i:],reverse_reference[0:i])
			struct_rev = Suffix(new_rotation_reverse,i)
			rotation_list_reverse.append(struct_rev)
		
			if reference[i]!='$':
				for char in alphabet:
					if reference[i] < char:
						C[char] = C[char] + 1	
		
		rotation_list.sort(key=textKey)
		rotation_list_reverse.sort(key=textKey)

		for i in rotation_list:
			suffix_array.append(i.pos)
			bwt.append(i.text[-1:])
		
			for char in alphabet:
				if len(Occ[char]) == 0:
					prev = 0
				else:
					prev = Occ[char][-1]
				if i.text[-1:] == char:
					Occ[char].append(prev+1)
				else:
					Occ[char].append(prev)				
					
		self.SA = suffix_array
		self.BWT = bwt
		self.C = C
		self.Occ = Occ
		self.Occ_reverse = Occ_reverse
		self.n = len(reference)
		self.D = list()
		self.alphabet = alphabet

	def find_match(self,query,num_differences):
		if num_differences == 0:
			return self.exact_match(query)

	def exact_match(self, query):
		query = query.lower()
		i = 0
		j = self.n - 1
		
		for x in range(len(query)):
			newChar = query[-x-1]
			newI = self.C[newChar] + self.OCC(newChar,i-1) + 1
			newJ = self.C[newChar] + self.OCC(newChar,j)
			i = newI
			j = newJ
		matches = self.SA[i:j+1]
		return matches

	def OCC(self,char,index,reverse=False):
		if index < 0:
			return 0
		else:
			if reverse:
				return self.Occ_reverse[char][index]
			else:
				return self.Occ[char][index]

class Suffix:
	def __init__(self, text, position):
		self.text = text
		self.pos = position

def textKey( a ): return a.text

show_data_structures = True 
difference_threshold = 0


reference = """atgcgtaatgccgtcgatcgta"""
query = "gta"

if __name__ == "__main__":
	data = BWA(reference)
	print ("\n\nReference:", reference)
	print ("Query:", query)
	if show_data_structures:
		print ("\nSA		BWT")
		print ("--		---")
		for i in range(len(data.SA)):
			print (data.SA[i] ,"\t\t", data.BWT[i])
		print ("\nC(a) = the number of characters 'a' in the Reference that are lexographically smaller than 'a'")
		print (data.C)
		print ("\nOcc(a,i) is the number of occurances of the character 'a' in BWT[0,i]")
		print (data.Occ)
	print ("\nSearching for", query, "with max difference threshold of", difference_threshold)
	matches = data.find_match(query,difference_threshold)
	print (len(matches), "match(es) at position(s):", matches, "\n\n")