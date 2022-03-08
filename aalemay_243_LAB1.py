# Greet the user with the message, "Sage’s Wedding Cake Price Calculator"
print("Sage's Wedding Cake Price Calculator")
# Ask the user: Total People Attending:
guest_num = input("Total people attending:")
print("----------------------------------------")
# Compute and output the labor cost to make Cake A
x_value = int(guest_num) / 30
baker_salaryA = x_value * 225
cons_salaryA = x_value * 12.50
labor_costA = baker_salaryA + cons_salaryA
# labor_costA = "${:,.2f}".format()
# Compute and output the total cost to make Cake A
ingreA = x_value * 35
cost_to_makeA = labor_costA + ingreA
# Compute and output the total to charge the customer for Cake A
charge_customerA = (cost_to_makeA / 90) * 100
print("Cake A")
# how do i add the dollar sign without the space?
labor_costA = f'${labor_costA:.2f}'
cost_to_makeA = f'${cost_to_makeA:.2f}'
charge_customerA = f'${charge_customerA:.2f}'
print("Labor cost:     ", labor_costA)
print("Cost to make:   ", cost_to_makeA)
print("Charge Customer:", charge_customerA)
# Compute and output the labor cost to make Cake B
baker_salaryB = x_value * 210
cons_salaryB = x_value * 25
labor_costB = baker_salaryB + cons_salaryB
# Compute and output the total cost to make Cake B
ingreB = x_value * 30
cost_to_makeB = labor_costB + ingreB
# Compute and output the total to charge the customer for Cake B
charge_customerB = (cost_to_makeB / 90) * 100
labor_costB = f'${labor_costB:.2f}'
cost_to_makeB = f'${cost_to_makeB:.2f}'
charge_customerB = f'${charge_customerB:.2f}'
print("----------------------------------------")
print("Cake B")
print("Labor Cost:     ", labor_costB)
print("Cost to make:   ", cost_to_makeB)
print("Charge Customer:", charge_customerB)
# Compute and output the labor cost to make Cake C
baker_salaryC = x_value * 240
cons_salaryC = x_value * 18.75
labor_costC = baker_salaryC + cons_salaryC
# Compute and output the total cost to make Cake C
ingreC = x_value * 40
cost_to_makeC = labor_costC + ingreC
# Compute and output the total to charge the customer for Cake C
charge_customerC = (cost_to_makeC / 90) * 100
print("----------------------------------------")
print("Cake C")
print("Labor Cost:     ", labor_costC)
print("Cost to make:   ", cost_to_makeC)
print("Charge Customer:", charge_customerC)
# str. format (number) with "{:. 2f}"
# the outputs depend on where you put in the string and floets
# to get terminal interaction type in python3 -i myproject.py
# formatted_float = "${:,.2f}".format(1500.2)
