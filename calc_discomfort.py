
def calc_discomfort(vs,dt):
    # to answer the query, this inner function is used.
    def acceleration(i):
      #The array was used to generate an example of calculating the acceleration equation, which can then be printed.
        a[i] = (vs[i+1] - vs[i]) / dt
        if i <= 0:
            return a[i] ** 2
        else:
            # call the procedure again if the end of the vs array is not reached.
            return (a[i] ** 2) + acceleration(i-1)
    #this line of code calls the function for an n-1 time instance.
    discomfort = acceleration(len(vs)-2)
    print(discomfort)

#this is the data used to test the working of the function calc_discomfort
a = [0, -1, 5, 7, 9]
b = 5
calc_discomfort(a,b)