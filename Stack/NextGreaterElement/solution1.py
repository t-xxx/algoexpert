def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []
    for idx in range(2 * len(array) - 1, -1, -1):
        circularIdx = idx % len(array)
        print(circularIdx)

        while len(stack) > 0:
            if stack[len(stack) - 1] <= array[circularIdx]:
                stack.pop()
            else:
                result[circularIdx] = stack[len(stack) - 1]
                break

        stack.append(array[circularIdx])
        print("stack", stack)
        print("result", result)

    print(result)
    return result
