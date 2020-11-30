def arithmetic_arranger(problems, ans = False):
    arranged_problems = ""
    # check if there are too many problems. The limit is 5
    if len(problems) > 5:
         return "Error: Too many problems."
    for i in range(len(problems)):
        problems[i] = problems[i].split()
        problem = problems[i]
        operator = problem[1]
        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."
        first_operand = problem[0]
        second_operand = problem[2]
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        num_dash = len(first_operand) + 2 if (len(first_operand) > len(second_operand)) else len(second_operand) + 2
        problem.append(num_dash)
        try:
            problem[0] = int(first_operand)
            problem[2] = int(second_operand)
            answer = problem[0] + problem[2] if operator == '+' else problem[0] - problem[2]
            problem.append(answer)
        except ValueError:
            return "Error: Numbers must only contain digits."
        
    # For now, each problem is a list of [first_operand, operator, second_operand, num_dash, answer]
    # deal with first operand first
    for i in range(len(problems)):
        first_operand = str(problems[i][0])
        num_dash = problems[i][3]
        num_spaces = num_dash - len(first_operand)
        arranged_problems += (" " * num_spaces) + first_operand
        if i != (len(problems) - 1):
            arranged_problems += " " * 4
        else:
            arranged_problems += '\n'

    # deal with second operand 
    for i in range(len(problems)):
        second_operand = str(problems[i][2])
        operator = problems[i][1]
        num_dash = problems[i][3]
        arranged_problems += operator
        num_spaces = num_dash - 1 - len(second_operand)
        arranged_problems += (" " * num_spaces) + second_operand
        if i != (len(problems) - 1):
            arranged_problems += " " * 4
        else:
            arranged_problems += '\n'

    # deal with dashes 
    for i in range(len(problems)):
        num_dash = problems[i][3]
        arranged_problems += ("-" * num_dash)
        if i != (len(problems) - 1):
            arranged_problems += " " * 4
        elif ans is True:
            arranged_problems += '\n'
            
    # deal with answers if ans is True
    if ans is True:
        for i in range(len(problems)):
            answer = str(problems[i][4])
            num_dash = problems[i][3]
            num_spaces = num_dash - len(answer)
            arranged_problems += (" " * num_spaces) + answer
            if i != (len(problems) - 1):
                arranged_problems += " " * 4
        

    return arranged_problems

