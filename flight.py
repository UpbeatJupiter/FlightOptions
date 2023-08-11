from datetime import datetime

with open('flightList.txt','r') as filestream:
    depart_from = input('Depart from: ')
    arrive_to = input('Arrive to: ')
    transfer_stop = " "
    cost_counter = 0
    for line in filestream:
        row = line.split(",")
        if depart_from == row[2] and arrive_to == row[4]:          #Direct flights
            start_time = datetime.strptime(row[1], '%H:%M')        
            end_time = datetime.strptime(row[3], '%H:%M')
            delta = end_time - start_time                          #Travel time
            print(f'\nDirect flights: \n{row[0]}  {row[1]}  {row[2]}  ->  {row[3]}  {row[4]} \nTraveling Time: {delta} \nCost: {row[5]} ')            
with open('flightList.txt','r') as filestream2:
    stop_counter = 0
    for lines in filestream2:
        row1 = lines.split(",")
        if depart_from == row1[2] and arrive_to != row1[4]:     #Depart Torino , Arrive -> ?
            transfer_stop = row1[4]                            #Transfer noktası  -> Catania
            cost_counter = int(row1[5])
            stop_counter += 1
            start_time1 = datetime.strptime(row[1], '%H:%M')
            firstTransferInfo = [row1[0],row1[1],row1[2],row1[3],row1[4],row1[5]]  #ilk transfer noktasının bilgilerinin olduğu liste
            filestream2.seek(0)
            for line2 in filestream2:   
                row2 = line2.split(",")
                if row2[2] == transfer_stop and row2[4] == arrive_to:      #transfer stop ve user input taki arrive lokasyonu aynı ise
                    end_time2 = datetime.strptime(row2[3], '%H:%M')
                    delta = end_time2 - start_time1                       #travel time
                    cost_counter += int(row2[5]) 
                    print(f'\n1 Stop Option {stop_counter} \n{firstTransferInfo[0]}  {firstTransferInfo[1]}  {firstTransferInfo[2]}  ->  {firstTransferInfo[3]}  {firstTransferInfo[4]} ')             
                    print(f'{row2[0]}  {row2[1]}  {row2[2]}  ->  {row2[3]}  {row2[4]} \nTraveling Time: {delta} \nCost: {cost_counter} ')
                    break
                  
                    
    