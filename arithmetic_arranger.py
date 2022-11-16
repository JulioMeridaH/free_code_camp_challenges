def arranger(operation_strings,want_solution=False):
    number_operations=len(operation_strings)
    if number_operations>5:
        return "Error: Too many problems."

    operators=[]
    operands_up=[]
    operands_down=[]
    dashes=[]
    results=[]

    for i in range(0,number_operations):
        operators.append(single_arranger(operation_strings[i],want_solution))
        if single_arranger(operation_strings[i],want_solution)=="Error: Operator must be '+' or '-'.":
            return "Error: Operator must be '+' or '-'."
        elif single_arranger(operation_strings[i],want_solution)=="Error: Numbers cannot be more than four digits.":
            return "Error: Numbers cannot be more than four digits."
        elif single_arranger(operation_strings[i],want_solution)=="Error: Numbers must only contain digits.":
            return "Error: Numbers must only contain digits."

    for i in range(0,number_operations):
        operands_up.append(operators[i][0])
        operands_down.append(operators[i][1])
        dashes.append(operators[i][2])
        if want_solution:
            results.append(operators[i][3])
        if i==number_operations-1:
            break
        else:
            operands_up.append("    ")
            operands_down.append("    ")
            dashes.append("    ")
            if want_solution:
                results.append("    ")

    up_line=''.join(operands_up)
    down_line=''.join(operands_down)
    dashes_line=''.join(dashes)
    if want_solution:
        result_line=''.join(results)

    if want_solution:
        return up_line + "\n" + down_line + "\n" + dashes_line + "\n" + result_line
    else:
        return up_line + "\n" + down_line + "\n" + dashes_line

    

def single_arranger(operation_string,want_solution):
    splited=operation_string.split()
    if splited[1]!="+" and splited[1]!="-":
        return "Error: Operator must be '+' or '-'."
    try:
        if int(splited[0])>10000:
            return "Error: Numbers cannot be more than four digits."
        elif int(splited[2])>10000:
            return "Error: Numbers cannot be more than four digits."
    except:
        return "Error: Numbers must only contain digits."
        
    if int(splited[0])>int(splited[2]):
        length=len(splited[0])
        space_up="  "
        space_down=""
        dashes="--"
        length_dif=len(splited[0])-len(splited[2])
        for i in range(0,length_dif+1):
            space_down=space_down+" "
        for i in range(0,len(splited[0])):
            dashes=dashes+"-"
    else:
        length=len(splited[2])
        space_up="  "
        space_down=" "
        dashes="--"
        length_dif=len(splited[2])-len(splited[0])
        for i in range(0,length_dif):
            space_up=space_up+" "
        for i in range(0,len(splited[2])):
            dashes=dashes+"-"
        
    if splited[1]=="+":
        solution=int(splited[0])+ int(splited[2])
    elif splited[1]=="-":
        solution=int(splited[0])- int(splited[2])
   
    if want_solution:
        space_solution=""
        for i in range(0,len(dashes)-len(str(solution))):
            space_solution=space_solution + " "

        operators=(space_up + splited[0]+ "\n" + splited[1] + space_down + splited[2]+"\n"+dashes +"\n" + space_solution + str(solution)).split("\n")
        return operators
    else:
        operators=(space_up + splited[0]+ "\n" + splited[1] + space_down + splited[2]+"\n"+dashes).split("\n")
        return operators

if __name__ == '__main__':
    arranger(['44 * 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40'])
    print(arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40']))