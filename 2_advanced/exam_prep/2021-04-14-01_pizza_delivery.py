
'''
On the first line, you will receive a sequence of pizza orders.
Each order contains a different number of pizzas, separated by comma and space ", ".

On the second line, you will receive a sequence of employees with pizza-making
capacities (how much pizzas an employee could make), separated by comma and space ", ".

Your task is to check if all pizza orders are completed.

To do that, you should take the first order and the last employee and see:
 - If the number of pizzas in the order is less than or equal to the employee's pizza making capacity,
    the order is completed. Remove both the order and the employee.

 - If the number of pizzas in the order is greater than the employee's pizza making capacity,
    he remaining pizzas from the order are going to be made by the next employees until the order is completed.
    o If there are no more employees to finish the order, consider it not completed.

 - The restaurant does not take orders for more than 10 pizzas at once.
 - If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee.

You should keep track of the total pizzas that are being made.
'''


from collections import deque

pizza_orders = deque([int(i) for i in input().split(", ")])
pizza_employees = [int(i) for i in input().split(", ")]

total_pizzas = 0

while pizza_orders:
    if len(pizza_employees) > 0:
        pizza_order = pizza_orders[0]
        pizza_employee = pizza_employees[-1]

        # invalid order
        if pizza_order <= 0 or pizza_order > 10:
            pizza_orders.popleft()

        # complete order
        elif pizza_order <= pizza_employee:
            total_pizzas += pizza_order
            pizza_orders.popleft()
            pizza_employees.pop()

        # split order between employees
        elif pizza_order > pizza_employee:
            total_pizzas += pizza_employee
            pizza_orders[0] -= pizza_employee
            pizza_employees.pop()
    else:
        break

employees_left = [str(e) for e in pizza_employees]
orders_left = [str(p) for p in pizza_orders]

# if all orders have been completed, count total orders
if len(pizza_orders) == 0:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(employees_left)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(orders_left)}')
