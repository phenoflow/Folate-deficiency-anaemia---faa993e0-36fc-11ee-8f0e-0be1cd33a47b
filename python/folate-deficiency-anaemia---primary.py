# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"D012100","system":"readv2"},{"code":"D012111","system":"readv2"},{"code":"D012200","system":"readv2"},{"code":"D012300","system":"readv2"},{"code":"D012400","system":"readv2"},{"code":"D012z00","system":"readv2"},{"code":"D013000","system":"readv2"},{"code":"Dyu0300","system":"readv2"},{"code":"22715","system":"med"},{"code":"24870","system":"med"},{"code":"36634","system":"med"},{"code":"37082","system":"med"},{"code":"4078","system":"med"},{"code":"4080","system":"med"},{"code":"42117","system":"med"},{"code":"53783","system":"med"},{"code":"55481","system":"med"},{"code":"56114","system":"med"},{"code":"98709","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('folate-deficiency-anaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["folate-deficiency-anaemia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["folate-deficiency-anaemia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["folate-deficiency-anaemia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
