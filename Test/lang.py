import sys

def run(statement, env = {}):
    result_stored = []

    for i in range(len(statement)):
        temp_statement = statement[i]
        result = run_single_statement(temp_statement, env)
        env = result[1]
        result_stored = [result[0], result[1]]

    return result_stored

def run_single_statement(statement, env):
    if statement[0] == 'num':
        return [int(statement[1]), env]

    elif statement[0] == 'bool':
        if statement[1] == 'true':
            return [True, env]
        
        else:
            return [False, env]
        
    elif statement[0] == 'none':
        return [None, env]

    elif statement[0] == 'var':
        if statement[1] in env:
            return [env[statement[1]], env]
        else:
            return [None, env]
    
    elif statement[0] == 'let':
        env[statement[1][1]] = run_single_statement(statement[2], env)[0]
        return [None, env]
    
    elif statement[0] == 'if':
        if run_single_statement(statement[1], env)[0] == True:
            return run_single_statement(statement[2], env)
        
        else:
            return run_single_statement(statement[3], env)

    elif statement[0] == 'add':
        return [run_single_statement(statement[1], env)[0] + run_single_statement(statement[2], env)[0], env]

    elif statement[0] == 'equal':
        if run_single_statement(statement[1], env)[0] == run_single_statement(statement[2], env)[0]:
            return [True, env]
        
        else:
            return [False, env]

    elif statement[0] == 'greater':
        if run_single_statement(statement[1], env)[0] > run_single_statement(statement[2], env)[0]:
            return [True, env]
        
        else:
            return [False, env]

    elif statement[0] == 'less':
        if run_single_statement(statement[1], env)[0] < run_single_statement(statement[2], env)[0]:
            return [True, env]
        
        else:
            return [False, env]

def parse(text):
    stack = []
    stack_text = ''
    result = []

    for i in range(len(text)):
        if text[i] == ' ':
            if len(stack_text) > 0:
                stack.append(stack_text)
                stack_text = ''

        elif text[i] == '(':
            if len(stack_text) > 0:
                stack.append(stack_text)
                stack_text = ''

            stack.append('(')

        elif text[i] == ')':
            if len(stack_text) > 0:
                stack.append(stack_text)
                stack_text = ''

            temp_result = []

            while True:
                temp_result.insert(0, stack.pop())
                if stack[len(stack) - 1] == '(':
                    stack.pop()
                    stack.append(temp_result)
                    break

        elif text[i] == '|':
            result.append(stack[0])
            stack = []

        else:
            stack_text = stack_text + text[i]
    
    result.append(stack[0])
    stack = []
    return result

env = {}

def main():
    global env

    while True:
        a = input('> ')
        if a == 'exit':
            sys.exit()
        else:
            result = run(parse(a), env)
            print(result)
            env = result[1]

main()