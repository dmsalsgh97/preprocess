#reformat fastq file format
import time
start_time = time.time()

import sys
input_path  = sys.argv[1]
output_path = sys.argv[2]

newfile = open(output_path,'w')
with open(input_path, 'r') as handle:
    while True:
        record = list(handle.readline()[:-1] for index in range(4))
        if len(record[0]) == 0:
            break
        read_name,seqeunce,_,quality = record
        read_name = read_name[: -11]
        args = read_name.split(' ')
        del args[0]
        read_name = " ".join(args)
        read_name = "@{0}".format(read_name)
        read_name = read_name.replace('_',"\tBC:Z:") + '-1'
        newfile.write("\n".join([read_name,seqeunce,"+",quality]))
        newfile.write("\n")

newfile.close()

print("splited ---%s seconds ---" % (time.time() - start_time))
