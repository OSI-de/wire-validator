import csv
from wire import Wire
def load_wires(filename):
        wires=[]
        try:  
            with open(filename,encoding="utf-8-sig") as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    wires.append(Wire(row["wire"], row["section"]))        
        except FileNotFoundError:
             print(f'File not found: {filename} \nValidation aborted.')     
        except KeyError as e:  
             print(f'Please check the CSV File, column {e} is missing in the header.')  
        except ValueError as e:
             print(f'Please check the CSV File, there is a value error: {e}')
        return wires