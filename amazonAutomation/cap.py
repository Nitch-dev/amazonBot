import capsolver

capsolver.api_key = "CAP-809E511AAF26049F3BFFF873D2376616"

def solveC():
    solution = capsolver.solve({
        "type":"ImageToTextTask",
        "websiteURL":"https://www.amazon.com/errors/validateCaptcha"
    })
    return solution


print("starting to solve")
s = solveC()
print(s)