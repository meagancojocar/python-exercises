def compareStrings(input, output):
    if input.lower() == output.lower():
        return input.lower()
    return ':('

print(compareStrings('Marc LOVES hanging off the sideof buildings','marc loves hanging off the sideof buildings'))
print(compareStrings('James is writing his FIRST react app','james is writing a react app'))