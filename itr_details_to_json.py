import pdftotext
import os


path = os.getcwd()
pdf_path = path + '/Downloads/itr_details.pdf'

with open(pdf_path, 'rb') as f:
    pdf = pdftotext.PDF(f)


with open('output.txt', 'w') as f:
    f.write('\n\n'.join(pdf))

with open('output.txt', 'rb') as file:
    data = file.read().decode('utf-8')

#preprocessing data

a_list = data.strip('\n').split('  ')

without_empty_strings = []

for item in a_list:
    if item != '':
        without_empty_strings.append(item)

new_items = [ item.strip() for item in without_empty_strings ]
#dictionary objects

heading = new_items[8][11:] +' ' + new_items[17] + ' ' +new_items[27]

a_dict = {}


page_title = {
    'Title' : new_items[0],
    'Description' : new_items[2:4],
     new_items[1] :  new_items[4]

}


a_dict[new_items[5]] = new_items[7]
a_dict[new_items[6]] = new_items[8][0:10]
a_dict[new_items[9]] = new_items[12]
a_dict[new_items[10]] = None
form_no = new_items[11] +' '+ new_items[13]+ ' '  +new_items[14]+ ' ' + new_items[16]
a_dict[form_no] = new_items[15]
a_dict[new_items[18]] = new_items[20]
a_dict[new_items[19]] = new_items[21]
a_dict[new_items[23]] = new_items[22]
a_dict[new_items[24]] = new_items[28]
a_dict[new_items[25]] = new_items[29]
a_dict[new_items[26][:11]] = new_items[30]
a_dict[new_items[26][11:]] = None
a_dict[new_items[31][:30]] = new_items[31][30:]
a_dict[new_items[32][:19]] = new_items[32][20:]
a_dict[new_items[33]] = new_items[34]
a_dict[new_items[35]] = new_items[36]
category1 = {
    'category':heading,
    'info':a_dict
}


new_string = new_items[48][7:] + ' ' + new_items[54]

b_dict = {}
b_dict[new_items[38]] = new_items[40]
b_dict[new_items[42]] = new_items[44]
b_dict[new_items[46]] = new_items[48][:5]

current_year = {
    new_items[49][3:] : new_items[51]
}
b_dict[new_items[56]] = new_items[53]
b_dict[new_items[58]] = new_items[60]
b_dict[new_items[62]] = new_items[64]
b_dict[new_items[70]] = {
                        new_items[66]:new_items[68],
                        new_items[72]:new_items[74],
                        new_items[76]:new_items[78],
                        new_items[80]:new_items[82],
                        new_items[84]:new_items[86]

}

b_dict[new_items[88]] = new_items[90]
b_dict[new_items[92]] = new_items[94]
b_dict[new_items[98]] = None

category2 = {
    'category2' : new_string,
    'info2' : b_dict
}

c_dict = {
    new_items[99][7:] : new_items[100],
    new_items[101] : new_items[102][:8],
             new_items[102][10:] : new_items[103],
             new_items[104][:15] : new_items[104][16:],
             new_items[106][:2]: new_items[106][3:],
             new_items[105][:2]: new_items[105][3:]

}



_dict = {**page_title, **category1, **category2, **c_dict}

#dumping dictionary objects
import json
json_obj = json.dumps(_dict, indent=4)
#print(json_obj)



#writing to json file

with open('itr_details.json', 'w') as op_file:
    op_file.write(json_obj)
