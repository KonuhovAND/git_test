
r_small_circle = float(input('radius smally fetil in santimeters is:'))
r_big_circle = float(input('radius bigy fetil in santimeters is:'))

WEX1 = float(input('enter how deep this thing is in santimeters:'))
WEX2 = float(input('enter the hight, if it the same as first one, enter 0:'))
if WEX2 == 0: WEX2 = WEX1


time_small_fetil = int(input('how long smally fetil was burning in min:'))
time_big_fetil = int(input('how long bigy fetil was burning in min'))

PI = float(input('enter pi number (3.141592) or enter 0 if u want to exact value: '))
if PI == 0: PI = 3.14159216

round_number = int(input('enter how many numbers after comma u want see:'))

def time_small_circle(number,time = time_small_fetil) : return number * time
def time_big_circle(number,time = time_big_fetil): return number * time


def ploshad(radius):
    return PI * radius ** 2

ploshad_big_circle, ploshad_small_circle =0,0

all_time_small, all_time_big = 0,0

for n in range(1,1000000):
    
    all_time_small= time_small_circle(number = n)
    all_time_big= time_big_circle(number = n)

    ploshad_small_circle+= ploshad(radius=r_small_circle) * WEX1
    ploshad_small_circle = round(ploshad_small_circle)
    
    ploshad_big_circle+=ploshad(radius=r_big_circle) * WEX1
    ploshad_big_circle = round(ploshad_big_circle)
    
    if time_big_fetil <= all_time_small:
        print(n)
        print(f"after {n} fetil's time smally fetil is time bigy fetil ({all_time_small - time_big_fetil})")
        
        for i in range(1,100000): 
            if ploshad_big_circle <=  i * ploshad_small_circle:
                print(f'after {i} fetil\'s ploshad smally fetil is ploshad bigy fetil ({i * ploshad_small_circle - ploshad_big_circle})')
                break
        
        break
    
# TODO asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf

    
