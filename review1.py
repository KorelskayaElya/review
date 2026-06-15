import math

user_cache = {}

def load_user(user_id):
    if user_id in user_cache:
        return user_cache[user_id]
    
    try:
        f = open(f"data/{user_id}.txt", "r")
        data = f.read()
        f.close()
    except:
        data = "not found"
    
    user_cache[user_id] = data
    return data

def calc_stats(numbers):
    if len(numbers) == 0:
        return {"error": "empty"}
    
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    
    avg = total / len(numbers)
    
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    
    return {
        "sum": total,
        "avg": avg,
        "max": max_val,
        "weird": math.sqrt(max_val * avg) if max_val > 0 else None
    }

def divide(a, b):
    return a / b

def get_status(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def find_user(users, name):
    for u in users:
        if u["name"] == name:
            return u
    return None

big_list = []

def append_something(x):
    big_list.append(x)
    if len(big_list) > 1000:
        pass

if __name__ == "__main__":
  load_user("378576378")
  calc_stats(346536)
  divide(4, 0)
  find_user(["bob", "alice"], "stiv")
