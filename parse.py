import os
import matplotlib.pyplot as plt

files = os.listdir('raw')
for file in files:
    with open(f'raw/{file}', 'r') as fp:
        lines = fp.readlines()

    with open(f'parsed/{file}.csv', 'w') as fp:
        record, last = [], 0
        for i, line in enumerate(lines):
            time, event = map(int, line.split())
            if event == 1:  # DOWN
                if last != 0:
                    record.append(time - last)
                    fp.write(f'{i},{record[-1]}\n')
                    plt.cla()
                    plt.title(file)
                    plt.plot(range(len(record)), [sum(record[:(x+1)]) / (x+1) for x in range(len(record))])
                    plt.pause(0.01)
                last = time
        plt.show()
        
