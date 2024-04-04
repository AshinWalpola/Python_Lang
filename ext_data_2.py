import numpy as np
import matplotlib.pyplot as plt

    #open the relavent file
with open('/Users/ashinwalpola/Documents/XCode/Python/pop.txt','r') as file:
    #read the file content
    content = file.read()
    #Eval Content to Python code
pop = eval(content)

with open('/Users/ashinwalpola/Documents/XCode/Python/gdp_cap.txt','r') as file:
    #read file content
    buffer = file.read()
gdp_cap = eval(buffer)

with open('/Users/ashinwalpola/Documents/XCode/Python/life_exp.txt','r') as file:
    #read file content
    buffer = file.read()
life_exp = eval(buffer)

with open('/Users/ashinwalpola/Documents/XCode/Python/col.txt','r') as file:
    #read file content
    buffer = file.read()
col = eval(buffer)

np_pop = np.array(pop)
print(type(np_pop))
print(type(life_exp))
print(type(gdp_cap))

plt.scatter(x = gdp_cap,y = life_exp, s = np_pop * 2, c = col)

#Scatter Plot Customisations
plt.xscale('log')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.title('World Development in 2007')

plt.show()
