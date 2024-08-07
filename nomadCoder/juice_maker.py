#juice_maker 240708
def make_juice(a):
  return f"{a}+🥤"
  
def add_ice(a):
  return f"{a}+🧊"

def add_sugar(a):
  return f"{a}+🍭"

juice = make_juice("🍎")

cold_juice = add_ice(juice)
perfect_cold_juice = add_sugar(cold_juice)

print(perfect_cold_juice)