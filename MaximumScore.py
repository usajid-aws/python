'''
     .-"""-.
>---/ _   _ \--->
    ](_' `_)[
    `-. x ,-' 
      |~~~|
      `---'
..............................................
..............................................
@author----->Usama.S

Simple python program to get highest score
from 5 students using node class
..............................................
..............................................
                                               '''

#Class node will store student object
#each student will have a name, ID, and a score


class Node(object):

	def __init__(self, id, name, score ):
		self.id = id
		self.name = name
		self.score = score
	 	self.next = None

#get name id and score from user
#store each 'student' in node
#loop to get 5 students
#if score is greater, update student node
#if equal score exists, continue 

def main():
	i=0
	return_Node = Node 
	for i in range (1,6):
		print("taking info for student %i" %i)
		s_name = raw_input("Please enter student name: ")
		s_id = int(input("Please enter stdent id: "))
		s_score = float(input("Please enter student score: ")) 
        student_Node = Node (s_id, s_name, s_score)
        if student_Node.score>i:
        	i = student_Node.score
        	return_Node = student_Node
        	
        else:
        	print("") 
        	       
    	print("")
	print("Student name: %s" %return_Node.name)
    	print("Student id:  %i" %return_Node.id)
    	print("Student score: %d" %return_Node.score)


main()


