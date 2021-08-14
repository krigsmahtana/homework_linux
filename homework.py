import subprocess


ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
wiwod = list(ps.decode().split('\n'))
i = len(wiwod)
j=0
name_list = []
all_list=[]
all_memory = []
all_cpu = []
while j<i:
    all = list(filter(None, wiwod[j].split(" ")))
    all_list.append(all)
    j = j+1
j=1
while j<i:
    name = all_list[j][0]
    name_list.append(name)
    memory = all_list[j][3]
    all_memory.append(memory)
    cpu = all_list[j][2]
    all_cpu.append(cpu)
    j = j+1

unik_user = list(set(name_list))
number_uesr = len(unik_user)
j=0
summa = 0.0
summ_cpu = 0.0
user_pros = []
while j<number_uesr:
    text = name_list.count(unik_user[j])
    user_pros.append(text)
    j = j+1
j=0
i=len(all_memory)
while j<i:
    summa = summa + float(all_memory[j])
    summ_cpu = summ_cpu + float(all_cpu[j])
    j = j+1
#вывод в консоль
print("Пользователи системы: " + str(unik_user) +"\n"
      +"Процессов запущено:" + str(len(wiwod)-1) +"\n"
      + "Пользовательских процессов: ")
j=0
while j<number_uesr:
    print(unik_user[j] + " : " + str(user_pros[j]))
    j =j+1
print("Всего памяти используется, %: " + str(summa) +"\n"
      + "Всего CPU используется, %: " + str(summ_cpu) +"\n"
      + "Больше всего памяти использует: " + str(name_list[all_memory.index(max(all_memory))])+"\n"
      + "Больше всего CPU использует: " + str(name_list[all_cpu.index(max(all_cpu))]))
#вывод в файл
f = open('system_homework.txt', 'w')
f.write("Пользователи системы: " + str(unik_user)+ '\n'
        + "Процессов запущено:" + str(len(wiwod)-1)+ '\n'
        + "Пользовательских процессов: "+ '\n')
j=0
while j<number_uesr:
    f.write(unik_user[j] + " : " + str(user_pros[j])+ '\n')
    j =j+1
f.write("Всего памяти используется, %: " + str(summa)+ '\n'
        + "Всего CPU используется, %: " + str(summ_cpu)+ '\n'
        + "Больше всего памяти использует: " + str(name_list[all_memory.index(max(all_memory))])+ '\n'
        + "Больше всего CPU использует: " + str(name_list[all_cpu.index(max(all_cpu))])+ '\n')
f.close()
