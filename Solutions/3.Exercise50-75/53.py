# Question: Print out the last name of the second employee.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}


d['employees'][1]['lastName'] = "Smooth"
print(d['employees'][1]['lastName'])


# print(d[0][1][1]) this doesn't work