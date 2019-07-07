import numpy as np


def date_order(date):
    return int("".join(date))


def extract_timestamp(line):
    timestamp = line
    for c in ["[", "]", "-", ":", "#"]:
        timestamp = timestamp.replace(c, " ")

    date = timestamp.split()[:5]
    message = timestamp.split()[5:]

    return date, message


class GuardInput:

    def __init__(self, date, message):
        self.year = int(date[0])
        self.month = int(date[1])
        self.day = int(date[2])
        self.hour = int(date[3])
        self.minute = int(date[4])

        self.order = date_order(date)

        self.message = message


file = open("input.txt", "r")

g_inputs = []
for line in file:
    d, m = extract_timestamp(line)
    g_inputs.append(GuardInput(d, m))

g_inputs.sort(key=lambda g: g.order)

'''input ordinati...'''

schedule = {}  # per ogni guardia tutti gli array dei turni
i = 0
while i < len(g_inputs):

    guard_id = g_inputs[i].message[1]

    shift = np.zeros(shape=60, dtype=int)

    while i < len(g_inputs)-1 and g_inputs[i+1].message[0] != "Guard":
        shift[g_inputs[i+1].minute: g_inputs[i+2].minute] = 1
        i += 2  # to next nap or next guard shift

    if guard_id not in schedule:
        schedule[guard_id] = [shift]
    else:
        schedule[guard_id].append(shift)

    i += 1  # to next guard shift

nap_time_sched = {}  # per ogni guardia array contenente ogni minuto la somma dei sonnellini

total_nap = {}  # per ogni guardia il sonno totale (in minuti)

for id in schedule.keys():

    nap_time_sched[id] = np.zeros(60, int)

    for s in schedule[id]:
        nap_time_sched[id] = nap_time_sched[id] + s

    total_nap[id] = nap_time_sched[id].sum()

sleeper = max(total_nap, key=lambda k: total_nap[k])  # guardia che ha dormito di più

print("Guard: " + sleeper)

sleeper_minute = max(range(60), key=lambda index: nap_time_sched[sleeper][index])

print("Min: " + str(sleeper_minute))  # minuto in cui la guardia sleeper ha dormito di più

print("Answer 1 = " + str(int(sleeper)*sleeper_minute))

'''PARTE 2'''

max_naps = 0
sleeper_minute_2 = -1
sleeper_2 = ""

for k in nap_time_sched.keys():
    current_max = np.amax(nap_time_sched[k])

    if current_max > max_naps:
        sleeper_minute_2 = np.argmax(nap_time_sched[k])
        sleeper_2 = k
        max_naps = current_max

print("*********************")
print("Guard: " + sleeper_2)
print("Min: " + str(sleeper_minute_2))
print("Answer 2 = " + str(int(sleeper_2)*sleeper_minute_2))




