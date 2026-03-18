def isCorrect(system, student):
    if (system == student):
        return True
    elif(system == 1 and student != 1):
        return False
    elif(system != 1 and student == 1):
        return False
    else:
        return True


system = int(input())
student = int(input())

if(isCorrect(system, student)):
    print("YES")
else:
    print("NO")