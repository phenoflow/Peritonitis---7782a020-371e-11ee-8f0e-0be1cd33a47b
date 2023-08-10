# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"A32y200","system":"readv2"},{"code":"J55..00","system":"readv2"},{"code":"J550400","system":"readv2"},{"code":"J551.00","system":"readv2"},{"code":"J555.00","system":"readv2"},{"code":"J557.00","system":"readv2"},{"code":"J558.00","system":"readv2"},{"code":"J55y100","system":"readv2"},{"code":"J55y300","system":"readv2"},{"code":"J55y400","system":"readv2"},{"code":"J55y500","system":"readv2"},{"code":"J55z.00","system":"readv2"},{"code":"J574A00","system":"readv2"},{"code":"100357.0","system":"med"},{"code":"101301.0","system":"med"},{"code":"102177.0","system":"med"},{"code":"104496.0","system":"med"},{"code":"104722.0","system":"med"},{"code":"105518.0","system":"med"},{"code":"105575.0","system":"med"},{"code":"105579.0","system":"med"},{"code":"105660.0","system":"med"},{"code":"105831.0","system":"med"},{"code":"105959.0","system":"med"},{"code":"106330.0","system":"med"},{"code":"106340.0","system":"med"},{"code":"110244.0","system":"med"},{"code":"110756.0","system":"med"},{"code":"11104.0","system":"med"},{"code":"11143.0","system":"med"},{"code":"1126.0","system":"med"},{"code":"14671.0","system":"med"},{"code":"14942.0","system":"med"},{"code":"15032.0","system":"med"},{"code":"15784.0","system":"med"},{"code":"15979.0","system":"med"},{"code":"16040.0","system":"med"},{"code":"16716.0","system":"med"},{"code":"17014.0","system":"med"},{"code":"18324.0","system":"med"},{"code":"1999.0","system":"med"},{"code":"2179.0","system":"med"},{"code":"23087.0","system":"med"},{"code":"2541.0","system":"med"},{"code":"26219.0","system":"med"},{"code":"26230.0","system":"med"},{"code":"27298.0","system":"med"},{"code":"27305.0","system":"med"},{"code":"28366.0","system":"med"},{"code":"28895.0","system":"med"},{"code":"28918.0","system":"med"},{"code":"31409.0","system":"med"},{"code":"31430.0","system":"med"},{"code":"32899.0","system":"med"},{"code":"35656.0","system":"med"},{"code":"35800.0","system":"med"},{"code":"36165.0","system":"med"},{"code":"36461.0","system":"med"},{"code":"37588.0","system":"med"},{"code":"37620.0","system":"med"},{"code":"37643.0","system":"med"},{"code":"37813.0","system":"med"},{"code":"38941.0","system":"med"},{"code":"39736.0","system":"med"},{"code":"4130.0","system":"med"},{"code":"41484.0","system":"med"},{"code":"42334.0","system":"med"},{"code":"42568.0","system":"med"},{"code":"42866.0","system":"med"},{"code":"45146.0","system":"med"},{"code":"45304.0","system":"med"},{"code":"47355.0","system":"med"},{"code":"4745.0","system":"med"},{"code":"47775.0","system":"med"},{"code":"48173.0","system":"med"},{"code":"48589.0","system":"med"},{"code":"48730.0","system":"med"},{"code":"48819.0","system":"med"},{"code":"48927.0","system":"med"},{"code":"49066.0","system":"med"},{"code":"50313.0","system":"med"},{"code":"53336.0","system":"med"},{"code":"5521.0","system":"med"},{"code":"5558.0","system":"med"},{"code":"56749.0","system":"med"},{"code":"58070.0","system":"med"},{"code":"59056.0","system":"med"},{"code":"64111.0","system":"med"},{"code":"65685.0","system":"med"},{"code":"657.0","system":"med"},{"code":"66822.0","system":"med"},{"code":"6786.0","system":"med"},{"code":"69918.0","system":"med"},{"code":"70431.0","system":"med"},{"code":"71130.0","system":"med"},{"code":"71403.0","system":"med"},{"code":"71881.0","system":"med"},{"code":"71897.0","system":"med"},{"code":"8044.0","system":"med"},{"code":"93436.0","system":"med"},{"code":"94397.0","system":"med"},{"code":"94998.0","system":"med"},{"code":"96622.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('peritonitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["peritonitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["peritonitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["peritonitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
