#make 2 seperate fastq files as 1 interleaved file
import time
start_time = time.time()

import sys
input1_path  = sys.argv[1]
input2_path  = sys.argv[2]
output_path  = sys.argv[3]

newfile = open(output_path,'w')
with open(input1_path, 'r') as input1, open(input2_path, 'r') as input2:
    while True:
        record_1 = list(input1.readline()[:-1] for index in range(4))
        record_2 = list(input2.readline()[:-1] for index in range(4))
        if len(record_1[0]) == 0:
            break
        if 'BC:' in record_1[0]:
            newfile.write("\n".join(record_1))
            newfile.write("\n")
            newfile.write("\n".join(record_2))
            newfile.write("\n")

newfile.close()

print("merged ---%s seconds ---" % (time.time() - start_time))

