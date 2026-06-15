import math

user_cache = {}
big_list = []
# не поятно, почему эти функции в одном файле находятся
# нет комментриев, не понятно, что функции делают
# читаемость кода отсутствует
# название перепменных не понятны
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

def calc_stats(numbers): # нет комментария
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
    if b != 0:
        return a / b
    else:
        return "Деление на ноль"
# не понятно, что за статус тут дается
def get_status(score): # дает результат за баллы 
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

def find_user(users, name):
    for u in users:
        if u["name"] == name:
            return u
    return None

def append_something(x): # необходим комментрий, что эта функция делает
    big_list.append(x)
    if len(big_list) > 1000:
        print("Действие")
    else:
        print("недостаточно элементов для X дейстивия")

if __name__ == "__main__":
  load_user("378576378")
  calc_stats(346536)
  div = divide(4, 0)
  print(div)
  name = find_user(["bob", "alice"], "stiv")
  print(name)
  append_something(1)
