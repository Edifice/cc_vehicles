Create a vehicles administratory application

There are three types of vehicles:
* cars
* trucks
* motorcycles

Every vehicle has a licence number, cars have number of seats, trucks have carrying capacity and motorcycles have accelaration.

We should count the registered vehicle number. We shoul also able to create multiply vehicles at once with giving the following formated text:

car|abc123|4
motorcycle|dce123|2.8
truck|ert568|10
car|frg258|5
truck|eas118|15


# Exercise 1 - Find by plate number
Implement a solution to retreive a vehicle by its plate number.

# Exercise 2 - Police gate
Extend the code to allow saving maximum speed for each type of vehicles.
Implement a solution, where the user can enter a plate number and speed value. (prepare for the following formats of plate numbers: xyz123, XYZ123, xyz-123, XYZ-123)
If this speed exceeds the maximum allowed speed limit of the vehicle with more then 10% , then print out "This vehicle is too fast".
