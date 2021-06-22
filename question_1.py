# -- a --

customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']

salary = [155000, 755000,  455000, 1255000, 635000, 575000]

taxes = [55800, 317100, 182000, 451800, 171450, 71400]

for i, val in enumerate(salary):
    
    if val > 555000:
        
        tax_rate = taxes[i]/salary[i]
        
        if tax_rate < 0.3:
            
            print(customers[i])