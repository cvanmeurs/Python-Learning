#students = {"Alice":25, "Bob":27, "Claire":17, "Dan":21, "Emma":22}

# the following is the same as the above, but visually formatted differently for easier reading

"""students = {
	"Alice":25,
	"Bob":27, 
	"Claire":17, 
	"Dan":21, 
	"Emma":22
	}"""


# students dictionary but with value as a list

#students = {
#	"Alice":["ID0001", 25, "A"],
#	"Bob":["ID0002", 27, "B"],
#	"Claire":["ID0003", 17, "C"],
#	"Dan":["ID0004", 21, "D"],
#	"Emma":["ID0005", 22, "E"]
#}

#print(students)

#print(students["Claire"]) # prints only Claire's info
#print(students["Claire"][0]) # prints only Claire's ID# (index 0)

# each dictionary value can be another dictionary!

students = {
	"Alice":{"id":"ID0001", "age":25, "grade":"A"},
	"Bob":{"id":"ID0002", "age":27, "grade":"B"},
	"Claire":{"id":"ID0003", "age":17, "grade":"C"},
	"Dan":{"id":"ID0004", "age":21, "grade":"D"},
	"Emma":{"id":"ID0005", "age":22, "grade":"E"},
}

print(students["Dan"]["age"]) # returns Dan's age

print(students["Emma"]["id"], students["Emma"]["grade"]) # returns Emma's id# and grade

