#Nomor 2
def counterClockwise(List_awal):      #Membuat function dengan nama counterClockwise dengan parameter List_awal
                                      #Berikutnya adalah tahapan rotasi manual antara value dari list di index yang diinginkan ke index yang dituju
                                      #Penukaran isi list berdasarkan pola pergerakan dari value di dalam list berdasar indexnya
    temp1=List_awal[0][0]             #temp1 menukar isi dari list ke-0 pada index ke-0 dengan isi dar list ke-2 pada index ke-0
    List_awal[0][0]=List_awal[2][0]
    List_awal[2][0]=temp1
    
    temp2=List_awal[0][0]             #temp2 menukar isi dari list ke-0 pada index ke-0 dengan isi dari list ke-2 pada index ke-2
    List_awal[0][0]=List_awal[2][2]
    List_awal[2][2]=temp2

    temp3=List_awal[1][0]             #temp3 menukar isi dari list ke-1 pada index ke-0 dengan isi dari list ke-2 pada index ke-1
    List_awal[1][0]=List_awal[2][1]
    List_awal[2][1]=temp3
    
    temp4=List_awal[0][1]             #temp4 menukar isi dari list ke-0 pada index ke-1 dengan isi dari list ke-1 pada index ke-0
    List_awal[0][1]=List_awal[1][0]
    List_awal[1][0]=temp4
    
    temp5=List_awal[0][1]             #temp5 menukar isi dari list ke-0 pada index ke-1 dengan isi dari list ke-1 pada index ke-2
    List_awal[0][1]=List_awal[1][2]
    List_awal[1][2]=temp5
    
    temp6=List_awal[0][2]             #temp6 menukar isi dari list ke-0 pada index ke-2 dengan isi dari list ke-0 pada index ke-0
    List_awal[0][2]=List_awal[0][0]
    List_awal[0][0]=temp6    
    
    return List_awal                 #terminasi function dan return ke List_awal

List_awal=[[1,2,3],[4,5,6],[7,8,9]]  #state value dari variabel List_awal yang merupakan parameter function
print (counterClockwise(List_awal))  #Cetak function dengan parameter List_awal