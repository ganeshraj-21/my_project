import requests
def greet(name):
    return f"hello,{name}!"

if __name__ == "__main__" :
    print (greet("python class"))

r = requests.get("https://api.github.com")
print("Github Status:",r.status_code)