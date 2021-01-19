from tkinter import*
from tkinter import messagebox

main_window = Tk()

main_window.title('Kalkulator Kebutuhan Kalori')
main_window.geometry('800x450')
main_window.minsize(800, 450)

main_window.state('normal')
main_window.resizable(True, True)

photo = PhotoImage(file = 'amikom_logo.png')
main_window.iconphoto(False, photo)

class hitung_nilai:
    def __init__(self, nama, tinggi, berat, usia, level):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat
        self.usia = usia
        self.level = level
        lbl_text1.config(text = ('=>', self.nama))
    
    def pria(self):
        bmi = 66 + (13.7 * self.berat) + (5 * self.tinggi) - (6.8 * self.usia)
        kalori = bmi * self.level
        tampilkan(bmi, kalori)
                
    def wanita(self):
        bmi = 655 + (9.6 * self.berat) + (1.8 * self.tinggi) - (4.7 * self.usia)
        kalori = bmi * self.level
        tampilkan(bmi, kalori)
        
class tampilkan:
    def __init__(self, bmi, kalori):
        self.bmi = bmi
        self.kalori = kalori
        lbl_text2.config(text = 'BMR Anda adalah...')
        lbl_bmi.config(text = round(self.bmi, 2))
        lbl_text3.config(text = 'Ini adalah jumlah kalori MINIMAL setiap hari, \n supaya organ tubuh Anda bisa berfungsi. Namun...')
        lbl_text4.config(text = 'Kebutuhan kalori Anda setiap hari adalah...')
        lbl_kalori.config(text = round(self.kalori, 2))
        lbl_text5.config(text = 'Ini adalah jumlah kalori TOTAL yang Anda butuhkan \n untuk menjalani aktivitas sehari-hari.')
                    
def input_nilai():
    if var_level.get() == (list_level[1]):
        nilai_level = 1.2
    elif var_level.get() == (list_level[2]):
        nilai_level = 1.375
    elif var_level.get() == (list_level[3]):
        nilai_level = 1.55
    elif var_level.get() == (list_level[4]):
        nilai_level = 1.725
    elif var_level.get() == (list_level[5]):
        nilai_level = 1.9

    x = hitung_nilai(inp_nama.get(), float(inp_tinggi.get()), float(inp_berat.get()), float(inp_usia.get()), float(nilai_level))
    if var_jenis.get() == 1:
        x.pria()
    elif var_jenis.get() == 2:
        x.wanita()
    

def error_check():
    if var_jenis.get() == 0:
        messagebox.showerror("Error", "Mohon isi nama anda terlebih dahulu")
    else:
        if inp_nama.get() == '':
            messagebox.showerror("Error", "Mohon pilih jenis kelamin anda terlebih dahulu")
        else:
            if float(inp_tinggi.get()) == 0:
                messagebox.showerror("Error", "Mohon isi tinggi badan anda terlebih dahulu")
            else:
                if float(inp_berat.get()) == 0:
                    messagebox.showerror("Error", "Mohon isi berat badan anda terlebih dahulu")
                else:
                    if int(inp_usia.get()) == 0:
                        messagebox.showerror("Error", "Mohon isi usia anda terlebih dahulu")
                    else:
                        if var_level.get() == (list_level[0]):
                            messagebox.showerror("Error", "Mohon isi level aktivitas anda terlebih dahulu")
                        else:
                            return(input_nilai())

def reset():
    var_jenis.set(0)
    var_nama.set('')
    var_tinggi.set(0)
    var_berat.set(0)
    var_usia.set(0)
    var_level.set(list_level[0])
    lbl_text1.config(text = '')
    lbl_text2.config(text = '')
    lbl_bmi.config(text = '')
    lbl_text3.config(text = '')
    lbl_text4.config(text = '')
    lbl_kalori.config(text = '')
    lbl_text5.config(text = '')
   

font_label = 'Helvetica 16'
list_level = ['------------------------------------------',
              '1. -> Sangat jarang olahraga',
              '2. -> Jarang olahraga (1-3 hari/minggu)',
              '3. -> Normal olahraga (3-5 hari/minggu)',
              '4. -> Sering olahraga (6-7 hari/minggu)',
              '5. -> Sangat sering olahraga (setiap hari bisa dua kali dalam sehari)']

var_jenis = IntVar()
var_nama = StringVar()
var_tinggi = IntVar()
var_berat = IntVar()
var_usia = IntVar()
var_level = StringVar(); var_level.set(list_level[0])

lbl_judul = Label(main_window, text = 'Silakan isi data di bawah ini.', font = 'Helvetica 16 bold')
lbl_nama = Label(main_window, text = 'Nama', font = font_label)
lbl_tinggi = Label(main_window, text = 'Tinggi badan (cm)', font = font_label)
lbl_berat = Label(main_window, text = 'Berat badan (kg)', font = font_label)
lbl_usia = Label(main_window, text = 'Usia', font = font_label)
lbl_level = Label(main_window, text = 'Level Aktivitas Fisik', font = font_label)

lbl_text0 = Label(main_window, text = 'Hasil Perhitungan', font = 'Helvetica 16')
lbl_text1 = Label(main_window, text = '', font = 'Helvetica 14 bold')
lbl_text2 = Label(main_window, text = '', font = 'Helvetica 10')
lbl_bmi = Label(main_window, text = '', font = 'Helvetica 20 bold')
lbl_text3 = Label(main_window, text = '', font = 'Helvetica 10')
lbl_text4 = Label(main_window, text = '', font = 'Helvetica 10')
lbl_kalori = Label(main_window, text = '', font = 'Helvetica 20 bold')
lbl_text5 = Label(main_window, text = '', font = 'Helvetica 10')

inp_pria = Radiobutton(main_window, text = 'Pria', variable = var_jenis, value = 1, font = font_label)
inp_wanita = Radiobutton(main_window, text = 'Wanita', variable = var_jenis, value = 2, font = font_label)
inp_nama = Entry(main_window, width = 25, textvariable = var_nama, font = 'Helvetica 14 bold')
inp_tinggi = Spinbox(main_window, width = 3, from_ = 0, to = 200, textvariable = var_tinggi, font = 'Helvetica 16 bold')
inp_berat = Spinbox(main_window, width = 3, from_ = 0, to = 150, textvariable = var_berat, font = 'Helvetica 16 bold')
inp_usia = Spinbox(main_window, width = 3, from_ = 0, to = 150, textvariable = var_usia, font = 'Helvetica 16 bold')
inp_level = OptionMenu(main_window, var_level, *list_level)
btn_hitung = Button(main_window, text = '=>', width = 5, font = font_label, command = error_check)
btn_reset = Button(main_window, text = '<=', width = 5, font = font_label, command = reset)

lbl_judul.place(relx = 0.05, rely = 0.1)
lbl_nama.place(relx = 0.05, rely = 0.2)
lbl_tinggi.place(relx = 0.05, rely = 0.4)
lbl_berat.place(relx = 0.05, rely = 0.55)
lbl_usia.place(relx = 0.05, rely = 0.7)
lbl_level.place(relx = 0.05, rely = 0.85)

lbl_text0.place(relx = 0.6, rely = 0.175)
lbl_text1.place(relx = 0.6, rely = 0.225)
lbl_text2.place(relx = 0.75, rely = 0.4, anchor = CENTER)
lbl_bmi.place(relx = 0.75, rely = 0.5, anchor = CENTER)
lbl_text3.place(relx = 0.75, rely = 0.6, anchor = CENTER)
lbl_text4.place(relx = 0.75, rely = 0.7, anchor = CENTER)
lbl_kalori.place(relx = 0.75, rely = 0.8, anchor = CENTER)
lbl_text5.place(relx = 0.75, rely = 0.9, anchor = CENTER)

inp_nama.place(relx = 0.05, rely = 0.26)
inp_pria.place(relx = 0.05, rely = 0.32)
inp_wanita.place(relx = 0.175, rely = 0.32)
inp_tinggi.place(relx = 0.05, rely = 0.46)
inp_berat.place(relx = 0.05, rely = 0.61)
inp_usia.place(relx = 0.05, rely = 0.76)
inp_level.place(relx = 0.05, rely = 0.91)
btn_hitung.place(relx = 0.45, rely = 0.3)
btn_reset.place(relx = 0.45, rely = 0.4)


main_window.mainloop()
