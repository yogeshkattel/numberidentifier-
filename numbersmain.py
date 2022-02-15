import csv
import xlsxwriter

def valiation(data):
   number = str(data)
   array = []

   for i in number:
      array.append(i)
   
   if len(array) <10 or len(array) >13:
      return 'Number cant be less than 10 digits or greater than 13 digits'
   
   if str(''.join(array[0:3])) == '977':
      del array[0:3]
   
   indexes = int(''.join(array[0:3]))

   if array[0:3] != 977 and len(array) >10:
      return 'Invalid number'
   
   sim = seprator(indexes)

   return { 'number':number, 'sim':sim}
   
def seprator(data):
   ary = {984:'Namaste GSM', 985:'Namaste GSM', 986:'Namaste GSM', 974:'NTC CDMA', 975:'NTC CDMA', 961:'smart cell', 962:'smart cell', 988:'smart cell', 980:'Ncell', 981:'Ncell', 982:'Ncell', 972:'UTL', 963:'hello mobile'}

   if data in ary:
      # print(data)
      # print(ary[data])
      return ary[data]
   


# valiation(data=9779806033057ls)

# print(valiation(data=9806033057))

with open('numbers.csv', newline='') as csvfile:
   reader = csv.reader(csvfile, delimiter=',')
   reader.__next__()
   line_count = 0
   for row in reader:
      data = valiation(data=row[1])
      print(data['sim'])
      if data['sim'] == 'Ncell':

         with open('ncell.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([row[0],data['number']])
      else:
         with open('ntc.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([row[0],data['number']])

      # print(data['number'],data['sim'], row[0])
      

# with open()

   


