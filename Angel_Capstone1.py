######### Capstone Project 1 --> Penjualan Barang - Toko --> by Angel

def number_validation(a,b):
    global x
    while not x.isnumeric():
        print ('\n')
        print ('********** Masukkan Angka Saja ************')
        print ('\n')
        x = input(f'Silakan Pilih Menu ({a}-{b}): ').strip()
        print ('\n')
    while int(a) < 1 or int(x) > b :
        print ('\n')
        print (f'******* Hanya Masukkan Angka {a}-{b} **********')
        print ('\n')
        x = input(f'Silakan Pilih Menu ({a}-{b}): ').strip()
        print ('\n')
        while not x.isnumeric():
            print('\n')
            print ('********** Hanya Masukkan Angka ***********')
            print ('\n')
            x = input(f'Silakan Pilih Menu ({a}-{b}): ').strip()
            print ('\n')
    x = int(x)
def listnama ():
    global List
    List = []
    for i in range (len(list_item)):
        b = [list_item[i][0]]
        List = List + b
def change (MHST, IND) : 
    global list_item, List
    Nama = input ('Masukkan Nama Item : ').title().strip()
    print ('\n')
    listnama()
    while not Nama in List:
        print ('Masukkan Nama Item yang Sudah Terdaftar')
        print (f'Nama Item yang Telah Terdaftar Adalah : {List}')
        print ('\n')
        Nama = input ('Masukkan Nama Item : ').title().strip()
        print ('\n')
    New = input (f'Masukkan {MHST} Item Baru : ').strip()
    print ('\n')
    while not New.isnumeric :
        print ('Masukkan Angka Saja')
        print ('\n')
        New = input (f'Masukkan {MHST} Item Baru : ').strip()
        print ('\n')
    x = List.index(Nama)
    list_item [x][IND] = New
    print (f'{MHST} Item Telah Berhasil di ganti')
    print ('\n')
    print (tabulate([list_item [x]], headers=header_item, tablefmt='fancy_outline'))
def jual():
    global list_item, List, struk, SubTotal
    Nama = input('Masukan Nama Item : ').strip().title()
    print ('\n')
    listnama()
    while not Nama in List:
        print ('Masukkan Nama Item yang Terdaftar')
        print (f'Nama Item yang Terdaftar Adalah : {List}')
        print ('\n')
        Nama = input ('Masukkan Nama Item : ').strip().title()
        print ('\n')
    x = List.index(Nama)
    a = int(list_item [x][3])
    Jlh = input ('Masukkan Jumlah Item : ').strip()
    print ('\n')
    while not Jlh.isnumeric():
        print ('Masukkan Angka Saja')
        print ('\n')
        Jlh = input ('Masukkan Jumlah Item : ').strip()
        print ('\n')
    while int(Jlh) > a :
        print ('Stock Item Tidak Memadai')
        print (f'Sisa Stock Item {Nama} adalah {a}')
        print ('\n')
        Jlh = input ('Masukkan Jumlah Item : ').strip()
        print ('\n')
        while not Jlh.isnumeric():
            print ('Masukkan Angka Saja')
            print ('\n')
            Jlh = input ('Masukkan Jumlah Item : ').strip()
            print ('\n')
    Jlh = int(Jlh)
    Total = (int(list_item[x][2])*Jlh)
    struk = struk + [[(list_item[x][0]), (list_item[x][2]), Jlh] , ['', '', Total ]]
    sisa_stock = a - Jlh
    list_item [x][3] = sisa_stock
    a = int(list_item[x][4])
    terjual = a + Jlh
    list_item [x][4] = terjual
    SubTotal = SubTotal + Total
def menu_utama() :
    global x, list_item
    print ('\n')
    print (('=' * 10) ,' \033[1mData Barang Toko Kue\033[0m ' ,('=' * 10))
    print ('\n')
    menu_utama = [
        ['No.', 'Pilihan Menu Utama'],
        ['1. ', 'Daftar Item Toko Kue'],
        ['2. ', 'Menambahkan Item Baru'],
        ['3. ', 'Mengubah Detail Item'],
        ['4. ', 'Menambahkan Stock Item'],
        ['5. ', 'Menghapus Item'],
        ['6. ', 'Mencetak Struk Penjualan'],
        ['7. ', 'Laporan Penjualan'],
        ['8. ', 'Exit']]
    print (tabulate(menu_utama, headers="firstrow" ,tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu Utama (1-8): ').strip()
    print ('\n')
    number_validation(1,8)
    if x == 1 :
        menu_1()
    elif x == 2 :
        menu_2()
    elif x == 3 :
        menu_3()
    elif x == 4 :
        menu_4()
    elif x == 5 :
        menu_5()
    elif x == 6 :
        menu_6()
    elif x ==7 :
        menu_7()
    else :
        print ('\n')
        print (('=' * 5) ,' \033[1mThank you And Have a Nice Day\033[0m ' ,('=' * 6))
        print ('\n')
def menu_1():
    global x, list_item, List
    print ('\n')
    print (('=' * 10) ,' \033[1mDaftar Item Toko\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [['No.', 'Daftar Item Toko'],
        ['1. ', 'Semua Daftar Item Toko Kue'],
        ['2, ', 'Daftar Item Berdasarkan Nama'],
        ['3. ', 'Kembali ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-3): ').strip()
    print ('\n')
    number_validation(1,3)
    if x == 1 :
        if len(list_item) == 0:
            print ('Toko Belum Mempunyai Daftar Item')
            print ('Anda Dapat Menambah Item Di Menu 2 Pada Halaman Menu Utama')
            menu_1()
        else :
            print (tabulate(list_item, headers=header_item, tablefmt='fancy_outline'))
            menu_1()
    elif x == 2 :
        Nama = input ('Masukkan Nama Item : ').strip().capitalize()
        print('\n')
        listnama()
        while not Nama in List:
            print ('Nama Item Yang Dimasukkan Tidak Terdaftar')
            print ('Masukkan Nama Item yang Telah Terdaftar')
            print (f'Nama Item yang Telah Terdaftar Adalah : {List}')
            print ('\n')
            Nama = input ('Masukkan Nama Item : ').capitalize().strip()
            print ('\n')
        x = List.index(Nama)
        print (tabulate([list_item[x]], headers=header_item, tablefmt='fancy_outline'))
        menu_1()
    else :
        menu_utama()
def menu_2():
    global x, list_item, List
    print ('\n')
    print (('=' * 10) ,' \033[1mMenambahkan Item Toko\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [
        ['No.', 'Menambahkan Item Toko'],
        ['1. ', 'Menambahkan Item Baru'],
        ['2. ', 'Kembali ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-2): ').strip()
    print ('\n')
    number_validation(1,2)
    if x == 1:
        a = input('Masukkan Nama Item Baru : ').strip().title()
        print ('\n')
        while len(a) == 0 :
            print ('Masukkan Nama Item, Nama Item Tidak Bisa Kosong')
            a = input('Masukkan Nama Item Baru : ').strip().title()
            print ('\n')
        listnama()
        while a in List:
            print ('Nama Item Yang Anda Masukkan Sudah Terdaftar')
            print (f'Nama Item yang Telah Terdaftar Adalah : {List}')
            print ('Mohon Masukkan Nama Item Yang Belom Terdaftar')
            print ('\n')
            a = input('Masukkan Nama Item Baru : ').strip().title()
            print ('\n')
        b = input ('Masukkan Modal Item : ').strip()
        print ('\n')
        while not b.isnumeric() :
            print ('Masukkan Angka Saja')
            print ('\n')
            b = input ('Masukkan Modal Item : ').strip()
            print ('\n')
        c = input ('Masukkan Harga Jual Item : ').strip()
        print ('\n')
        while not c.isnumeric() :
            print ('Masukkan Angka Saja')
            print ('\n')
            c = input ('Masukkan Harga Jual Item : ').strip()
            print ('\n')
        while int(b) > int(c):
            print ('Harga Jual Tidak Boleh Kurang dari Harga Modal')
            print (f'Harga Modal yang Telah Dimasukkan Adalah : {b}')
            c = input ('Masukkan Harga Jual Item : ').strip()
            print ('\n')
            while not c.isnumeric() :
                print ('Masukkan Angka Saja')
                print ('\n')
                c = input ('Masukkan Harga Jual Item : ').strip()
                print ('\n')
        d = input ('Masukkan Jumlah Stock Item : ').strip()
        print ('\n')
        while not d.isnumeric() :
            print ('Masukkan Angka Saja')
            print ('\n')
            d = input ('Masukkan Jumlah Stock Item : ').strip()
            print ('\n')
        list_item.append([a, b, c, d, 0])
        print ('Data Anda Sudah Berhasil Di Tambahkan')
        menu_2()
    else :
        menu_utama()
def menu_3():
    global x, list_item, List
    print ('\n')
    print (('=' * 10) ,' \033[1mMenangubah Detail Item\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [
        ['No.', 'Mengubah Detail Item'],
        ['1. ', 'Mengubah Nama Item'],
        ['2. ', 'Mengubah Modal Item'],
        ['3. ', 'Mengubah Harga Item'],
        ['4. ', 'Mengubah Stock Item'],
        ['5. ', 'Mengubah Penjualan Item'],
        ['6. ', 'Kembali Ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-6): ').strip()
    print ('\n')
    number_validation(1,6)
    if x == 1:
        Nama = input ('Masukkan Nama Item : ').title().strip()
        print ('\n')
        listnama()
        while not Nama in List:
            print ('Masukkan Nama Item yang Sudah Terdaftar')
            print (f'Nama Item yang Telah Terdaftar Adalah : {List}')
            print ('\n')
            Nama = input ('Masukkan Nama Item : ').title().strip()
            print ('\n')
        NamaBaru = input ('Masukkan Nama Item Baru : ').title().strip()
        print ('\n')
        while NamaBaru in List:
            print ('Masukkan Nama Item yang Belom Terdaftar')
            print (f'Nama Item yang Sudah Terdaftar Adalah : {List}')
            print ('\n')
            NamaBaru = input ('Masukkan Nama Item Baru : ').title().strip()
            print ('\n')
        x = List.index(Nama)
        list_item [x][0] = NamaBaru
        print ('Nama Item Telah Berhasil di ganti')
        print ('\n')
        print (tabulate([list_item [x]], headers=header_item, tablefmt='fancy_outline'))
        menu_3()
    elif x == 2:
        change ('Modal', 1)
        menu_3()
    elif x == 3:
        change ('Harga Jual', 2)
        menu_3()
    elif x == 4:
        change ('Stock', 3)
        menu_3()
    elif x == 5:
        change ('Terjual', 4)
        menu_3()
    else :
        menu_utama()
def menu_4():
    global x, list_item, List
    print ('\n')
    print (('=' * 10) ,' \033[1mMenambahkan Stock Item\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [
        ['No.', 'Menambahkan Stock Item'],
        ['1. ', 'Menambahkan Stock Item'],
        ['2. ', 'Kembali Ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-2): ').strip()
    print ('\n')
    number_validation(1,2)
    if x == 1: 
        print ('Masukkan Detail Item yang Masuk.')
        print ('\n')
        Nama = input('Masukan Nama Item : ').strip().title()
        print ('\n')
        listnama()
        while not Nama in List:
            print ('Masukkan Nama Item yang Terdaftar')
            print (f'Nama Item yang Terdaftar Adalah : {List}')
            print ('\n')
            Nama = input ('Masukkan Nama Item : ').strip().title()
            print ('\n')
        x = List.index(Nama)
        a = int(list_item [x][3])
        New = input ('Masukkan Jumlah Stock Item Yang Masuk : ').strip()
        print ('\n')
        while not New.isnumeric() :
            print ('Masukkan Angka Saja')
            New = input ('Masukkan Jumlah Stock Item Yang Masuk : ').strip()
            print ('\n')
        list_item [x][3] = a + int(New)
        print ('Stock Telah Berhasil Di Update.')
        print ('\n')
        print (tabulate([list_item [x]], headers=header_item, tablefmt='fancy_outline'))
        menu_4()
    else :
        menu_utama()
def menu_5():
    global x, list_item, List
    print ('\n')
    print (('=' * 10) ,' \033[1mMenghapus Item\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [
        ['No.', 'Menghapus Item'],
        ['1. ', 'Menghapus Seluruh Data'],
        ['2. ', 'Menghapus Item Berdasarkan Nama'],
        ['3. ', 'Kembali Ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-3): ').strip()
    print ('\n')
    number_validation(1,3)
    if x == 1:
        print ('Apakah Anda Yakin Ingin Menghapus Seluruh Data?')
        print ('Data Yang Telah Dihapus Tidak Dapat Di Akses atau Di Kembalikan Lagi.')
        print ('\n')
        print ('Jika Ya, Pilih 1, Jika Tidak, Pilih 2 : ')
        print ('\n')
        menu1 = [
            ['1. ', 'Ya'],
            ['2. ', 'Tidak']]
        print (tabulate(menu1, tablefmt='simple'))
        print ('\n')
        x = input('Silakan Pilih Menu (1-2): ').strip()
        print ('\n')
        number_validation(1,2)
        if x == 1:
            list_item.clear()
            print ('Semua Data Telah Dihapus')
            menu_5()
        else :
            print ('Data Item TIDAK di Hapus')
            menu_5()    
    elif x == 2:
        if len(list_item) == 0:
            print ('Toko Belum Mempunyai Daftar Item')
            print ('Anda Dapat Menambah Item Di Menu 2 Pada Halaman Menu Utama')
            menu_5()
        Nama = input ('Masukkan Nama Item : ').title().strip()
        print ('\n')
        listnama()
        while not Nama in List:
            print ('Masukkan Nama Item yang Sudah Terdaftar')
            print (f'Nama Item yang Telah Terdaftar Adalah : {List}')
            print ('\n')
            Nama = input ('Masukkan Nama Item : ').title().strip()
            print ('\n')
        print ('Apakah Anda Yakin Ingin Menghapus Data Ini?')
        print ('Data Yang Telah Dihapus Tidak Dapat Di Akses atau Di Kembalikan Lagi.')
        print ('\n')
        print ('Jika Ya, Pilih 1, Jika Tidak, Pilih 2 : ')
        print ('\n')
        menu1 = [
            ['1. ', 'Ya'],
            ['2. ', 'Tidak']]
        print (tabulate(menu1, tablefmt='simple'))
        print ('\n')
        x = input('Silakan Pilih Menu (1-2): ').strip()
        print ('\n')
        number_validation(1,2)
        if x == 1: 
            x = List.index(Nama)
            del list_item [x]
            print ('Data Item Telah Berhasil di Hapus')
            menu_5()
        else :
            print ('Data Item TIDAK di Hapus')
            menu_5()
    else:
        menu_utama()
def menu_6():
    global x, list_item, List, struk, SubTotal
    print ('\n')
    print (('=' * 10) ,' \033[1mMencetak Struk Penjualan\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [
        ['No.', 'Struk Penjualan'],
        ['1. ', 'Mencetak Struk'],
        ['2. ', 'Kembali Ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-2): ').strip()
    print ('\n')
    number_validation(1,2)
    header_struk = ['Nama Item', 'Harga', 'Qty']
    struk = [['','','']]
    SubTotal = 0
    if x == 1: 
        print ('Masukkan Detail Item yang Terjual.')
        print ('\n')
        jual()
        print ('Apakah Ada Tambahan?')
        menu1 = [
            ['1. ', 'Ya'],
            ['2. ', 'Tidak']]
        print (tabulate(menu1, tablefmt='simple'))
        print ('\n')
        x = input('Silakan Pilih Menu (1-2): ').strip()
        print ('\n')
        number_validation(1,2)
        while x == 1: 
            print ('Masukkan Detail Item yang Terjual.')
            print ('\n')
            jual()
            print ('Apakah Ada Tambahan?')
            menu1 = [
                ['1. ', 'Ya'],
                ['2. ', 'Tidak']]
            print (tabulate(menu1, tablefmt='simple'))
            print ('\n')
            x = input('Silakan Pilih Menu (1-2): ').strip()
            print ('\n')
            number_validation(1,2)
        if x == 2:
            print (('=' * 5) ,' \033[1mStruk Belanja\033[0m ' ,('=' * 6))
            print ('\n')
            struk = struk + [['','',''],['SubTotal', '', SubTotal ]]
            print (tabulate(struk, headers = header_struk))
            menu_6()
    else :
        menu_utama()
def menu_7():
    global x, list_item, List, struk, SubTotal
    print ('\n')
    print (('=' * 10) ,' \033[1mLaporan Penjualan\033[0m ' ,('=' * 10))
    print ('\n')
    menu1 = [
        ['No.', 'Laporan Penjualan'],
        ['1. ', 'Hasil Penjualan'],
        ['2. ', 'Laporan Item Terjual'],
        ['3. ', 'Profit Margin Item'],
        ['4. ', 'Kembali Ke Menu Utama']]
    print (tabulate(menu1, headers="firstrow", tablefmt='simple'))
    print ('\n')
    x = input('Silakan Pilih Menu (1-4): ').strip()
    print ('\n')
    number_validation(1,4)
    if x == 1:
        print ('Hasil Penjualan Pada Periode ini Adalah : ')
        print ('\n')
        O = 0
        for i in range(len(list_item)):
           x = int(list_item[i][2]) * int (list_item[i][4])
           O = O + x
        M = 0
        for i in range(len(list_item)):
           Item = int(list_item[i][3]) + int (list_item[i][4])
           x = int(list_item[i][1]) * Item
           M = M + x
        PO = 0
        for i in range(len(list_item)):
           Item = int(list_item[i][3]) + int (list_item[i][4])
           x = int(list_item[i][2]) * Item
           PO = PO + x
        menu1 = [
            ['Omset', f'Rp {O}'],
            ['Modal', f'Rp {M}'],
            ['Potensi Omset', f'Rp {PO}']]
        print (tabulate(menu1, tablefmt='simple'))
        menu_7()
    elif x == 2 :
        print ('Data Laporan Item Terlaris Adalah : ')
        print ('\n')
        T = []
        for i in range(len(list_item)):
            x = list_item[i][4]
            T = T + [int(x)]
        t = T.copy()
        t.sort(reverse=True)
        order = []
        for i in t:
            x = T.index(i)
            order = order + [x]
        newlist = [['Nama Item', 'Terjual']]
        for i in order:
            x = list_item[i][0], list_item [i][4]
            newlist = newlist + [x]
        print (tabulate(newlist, headers='firstrow', tablefmt='fancy_outline'))
        menu_7()
    elif x == 3:
        print ('Profit Margin Pada Periode ini Adalah : ')
        print ('\n')
        O = 0
        for i in range(len(list_item)):
           x = int(list_item[i][2]) * int (list_item[i][4])
           O = O + x
        M = 0
        for i in range(len(list_item)):
           x = int(list_item[i][1]) * int (list_item[i][4])
           M = M + x
        menu1 = [['profit', f'{(O-M)}']]
        print ('Profit Margin Setiap Item')
        print ('\n')
        Margin = [['Nama Item', 'Margin/Item', 'Profit']]
        for i in range(len(list_item)):
            x = list_item[i][0]
            y = int(list_item[i][2])-int(list_item[i][1])
            z = int(list_item[i][4])*y
            Margin = Margin + [[x,y,z]]
        print (tabulate(Margin, headers='firstrow', tablefmt='fancy_outline'))
        menu_7()
    else:
        menu_utama()
from tabulate import tabulate
header_item = ['Nama Item', 'Modal', 'Harga Jual', 'Stock', 'Terjual']
list_item =[['Tepung', '8500', '10000', '5', '8'], 
            ['Gula', '9000', '11000', '10', '2'], 
            ['Mentega', '13500', '15000', '8', '3'], 
            ['Telur', '1400', '1500', '50', '20']]
menu_utama()