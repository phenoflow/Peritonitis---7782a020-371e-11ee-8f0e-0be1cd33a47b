# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J552000","system":"readv2"},{"code":"J552100","system":"readv2"},{"code":"J552200","system":"readv2"},{"code":"J552300","system":"readv2"},{"code":"J552400","system":"readv2"},{"code":"J552500","system":"readv2"},{"code":"J552600","system":"readv2"},{"code":"J552700","system":"readv2"},{"code":"J552800","system":"readv2"},{"code":"J552900","system":"readv2"},{"code":"J552A00","system":"readv2"},{"code":"J552B00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peritonitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peritonitis-abscess---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peritonitis-abscess---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peritonitis-abscess---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)