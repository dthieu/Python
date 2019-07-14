import unittest as ut


"""
Support function
"""
def ArrToStr(arr):
	my_str = ""
	for i in range(len(arr)):
		my_str = my_str + str(arr[i])
	return my_str

#========================================================================


"""
Convert decimal number to n 
n = 2  => Dec to Binary
n = 16 => Dec to Hexa
"""
def DecToN(num, n):
	result = []
	HEX    = { 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F" }
	N      = num
	while (N != 0):
		modulo = N % n
		if n == 16 and modulo >= 10:
			modulo = HEX[modulo]
		result.append(modulo)
		N = int(N / n)
	return result[::-1] # Revert array

"""
	Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

	Example

    For n = 9, the output should be
    isSumOfConsecutive2(n) = 2.

    There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

    For n = 8, the output should be
    isSumOfConsecutive2(n) = 0.

    There are no ways to represent n = 8.
"""
def isSumOfConsecutive(n):
	return 2

"""
ex: 1 2 3 4
  -   4 2 5
  => 4 < 5 => take 1 => 14 - 5 = 9 => 4
  => 3 - 2 (+1)
"""
def SubtractByHand(a, b):
	pass



#========================================================================
"""
Test function
"""
# n = 11
# print("My result: DEC2HEX(", n, ") = ", ArrToStr(DecToN(n, 16)))
# print("PC result: DEC2HEX(", n, ") = ", hex(n))
# print("My result: DEC2BIN(", n, ") = ", ArrToStr(DecToN(n, 2)))
# print("PC result: DEC2BIN(", n, ") = ", bin(n))

class testFunction(ut.TestCase):


	def test_isSumOfConsecutive2(self):
		assertEqual(isSumOfConsecutive(9), 2)
		# assertEqual(isSumOfConsecutive(8), 0)
		# assertEqual(isSumOfConsecutive(15), 3)
		# assertEqual(isSumOfConsecutive(24), 1)
		# assertEqual(isSumOfConsecutive(13), 1)

# Run all test
# if __name__ == "__main__":
# 	ut.main(verbosity=2)

# n = 10
# ss = "{0:0>"+str(n)+"}"
# s = ss.format("123")


def directionOfReading(num):
    # align by 0 (equal len arr)
    # convert all to string
    # init result arr
    # loop len each number and join by "" => append to arr
    fm 	= lambda s, n : s.format(str(n))
    f   = "{0:0>"+str(len(num))+"}"
    arr = [fm(f, n) for n in num]

    r   = [int(''.join([arr[i][j] for i in range(len(num))])) for j in range(len(num))]
    


# num = [12, 345, 67, 5]
# directionOfReading(num)	

arr = ["code", "eodc", "deco", "frame", "framer"]

def funWithAnagrams(arr):
	check = lambda s1, s2 : all([i in s2 and len(s1)==len(s2) for i in s1])
	
	r_idx = []
	j = 0
	for i in range(len(arr)):
		for j in range(1, len(arr)):
			if (check(arr[i], arr[j])) and (i not in r_idx) :
				r_idx.append(i)
				

	return sorted([arr[i] for i in r_idx])

# print(funWithAnagrams(arr)) 
"""
6 - 16 char
leter, num,1 "-"
start by letter not end with "-"
"""
import re
def validate(s):
	pat = "^[a-zA-Z][0-9](?=.{6,16}$)[-]{1}$"
	if re.match(pat, s) != None and not s.endswith("-"):
		return True
	return False

#str = "Alibaba93-pac"
#print(validate(str))
class DocumentStore(object):
	"""docstring for DocumentStore"""
	def __init__( capacity):
		_capacity = capacity
		_documents = []

	@property
	def capacity(self):
		return _capacity

	@property
	def documents(self):
		return _documents

	def add_document( document):
		if (len(_documents) >= _capacity):
			raise Exception("Document store is full")
		_documents.append(document)
	
	def __repr__(self):
		return "Document store: " + str(len(_documents)) + "/" + str(_capacity)
	
# document_store = DocumentStore(2)
# document_store.add_document("document")
# document_store.add_document("abc")


# print(document_store)

from collections import namedtuple

def merge(*records):
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """ 
    a1 = records[0]
    a2 = records[1]

    Patient = namedtuple("Patient", sorted(a1._fields + a2._fields))
    return Patient(*(a1+a2))

    
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972')
                                   
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(hair_color = 'Black', eye_color = 'Blue')
  
# print(merge(personal_details, complexion))
def nth_most_rare(elements, n):
	s = set(elements)
	result = {k : 0 for k in s}

	sl = sorted(elements)
	i = 0
	while i < len(elements):
		result[sl[i]] += 1
		i += 1
	return sorted(result)[n-1]

# print(nth_most_rare([5,4,3,2,1,5,4,3,2,5,4,3,5,4,5], 3))
def differentValuesInMultiplicationTable2(n, m):
    return len({*[i * j for i in range(1,n+1) for j in range(1,m+1)]})

# print(differentValuesInMultiplicationTable2(2, 3))

from random import randint
import numpy as np
MINE = 100

def genMines(rows, cols, mines):
	result = [[0 for i in range(rows)] for j in range(cols)]
	# Generate mines
	arr_mines = []
	while len(arr_mines) != mines:
		x = randint(0, rows-1)
		y = randint(0, cols-1)
		if [x, y] not in arr_mines:
			arr_mines.append([x, y])
	# Add mines into board
	for x, y in arr_mines:
		result[x][y] = MINE

	# Add numbers around the mines
	getNeighbour = lambda x, y: [[x-1,y-1],	[x-1, y], [x-1, y+1],
								 [x, y+1], [x+1, y+1], [x+1, y],
								 [x+1, y-1], [x, y-1]]
	
	get_num_of_mine = lambda a, x, y: sum([1 for i, j in getNeighbour(x, y) if a[i][j] == MINE])

	tmp_r = np.pad(result, pad_width=1, mode='constant', constant_values=0)
	
	# Save padding position
	padd = [[0, y] for y in range(cols+2)]
	for y in range(cols+2):
		padd.append([rows+1, y])
	for x in range(rows+2):
		padd.append([x, 0])
		padd.append([x, cols+1])

	# Calc number of mines around the mines
	for x, y in arr_mines:
		arr_nei = getNeighbour(x, y)
		# Because we add padding => we need to map pos from original to padding by plus 1
		for i, j in arr_nei:
			if (tmp_r[i+1][j+1] == 0) and ([i+1, j+1] not in padd) and (tmp_r[i+1][j+1] != MINE):
				tmp_r[i+1][j+1] = get_num_of_mine(tmp_r, i+1, j+1)
	print (tmp_r)
		
	ret = []
	for e in tmp_r[1:-1]:
		ret.append(e[1:cols+1].tolist())
	return ret


print (genMines(9,9,20))


# róc rách róc rách chú lùn đang câu cá
# lá rơi lá rơi bạch tuyết đang nằm bơi

