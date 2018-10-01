from itertools import *
from operator import *
import sys
def main():

	card = get_card()

	solve(card)
	
	

def get_card():
	nums = input("plz input 4 numbers: ").split(chr(32))
	card = [] 
	for i in nums:
		if i == chr(32):
			pass
		else:
			try:
				card.append(int(i))
			except:
				pass	
	return list(card)

def solve(ln):
	
	ops = [mul,add,sub,truediv]

	for i in permutations(ln):
	
		for j in product(ops,repeat=3):
			cur_num = 0
			card = list(i)
			
			cur_num += list(j)[0](card.pop(0),card.pop(0))

			card.insert(0,cur_num)


			cur_num =  list(j)[1](card.pop(0),card.pop(0))

			(card).insert(0,cur_num)
			
			cur_num = list(j)[2](card.pop(0),card.pop(0))

			

			if cur_num == 24:
				print("we have found the number", cur_num, i ,j)
				break

		break
				

if __name__ == "__main__":
	print(main())

