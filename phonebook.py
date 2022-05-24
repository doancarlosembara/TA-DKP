from tkinter import *
import csv
from tkinter import messagebox

phonelist = []


def ReadCSVFile():
    global header
    with open('DataPengunjung.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            phonelist.append(row)
    set_select()
    print(phonelist)


def MenulisCSVFile(phonelist):
    with open('DataPengunjung.csv', 'w', newline='') as csv_file:
        writeobj = csv.writer(csv_file, delimiter=',')
        writeobj.writerow(header)
        for row in phonelist:
            writeobj.writerow(row)


def DataTerpilih():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror(
            "Error", "Mohon pilih data yang ingin dilihat")
    else:
        return int(select.curselection()[0])


def TambahDetail():
    if E_name.get() != "" and E_last_name.get() != "" and E_contact.get() != "":
        phonelist.append([E_name.get()+' '+E_last_name.get(), E_contact.get()])
        print(phonelist)
        MenulisCSVFile(phonelist)
        set_select()
        DataReset()
        messagebox.showinfo("Confirmation", "Berhasil Menambahkan Kontak!")

    else:
        messagebox.showerror("Error", "Mohon Masukan Informasi Detail")


def UpdateDetail():
    if E_name.get() and E_last_name.get() and E_contact.get():
        phonelist[DataTerpilih()] = [E_name.get()+' ' +
                                     E_last_name.get(), E_contact.get()]
        MenulisCSVFile(phonelist)
        messagebox.showinfo("Confirmation", "Kontak berhasil Diperbarui!")
        DataReset()
        set_select()

    elif not(E_name.get()) and not(E_last_name.get()) and not(E_contact.get()) and not(len(select.curselection()) == 0):
        messagebox.showerror("Error", "Silahkan Isi Informasinya")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror(
                "Error", "Mohon Pilih Data dan \n Tekan Button Load")
        else:
            message1 = """Untuk Menampilkan Semua Data, \n 
						  Silahkan Pilih Data dan Tekan Load\n.
						  """
            messagebox.showerror("Error", message1)


def DataReset():
    E_name_var.set('')
    E_last_name_var.set('')
    E_contact_var.set('')


def HapusData():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno(
            'Confirmation', 'Apakah Anda Ingin Menghapus Kontak\n Yang Anda pilih?')
        if result == True:
            del phonelist[DataTerpilih()]
            MenulisCSVFile(phonelist)
            set_select()
    else:
        messagebox.showerror("Error", 'Silahkan Pilih Kontak')


def MemuatData():
    name, phone = phonelist[DataTerpilih()]
    print(name.split(' '))
    E_name_var.set(name.split()[0])
    E_last_name_var.set(name.split()[1])
    E_contact_var.set(phone)


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i = 0
    for name, phone in phonelist:
        i += 1
        select.insert(END, f"{i}  |    {name}   |   {phone}")


window = Tk()

Frame1 = LabelFrame(window, text="Masukan Detail Kontak")
Frame1.grid(padx=15, pady=15)


Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0, column=0, padx=15, pady=15)
# ---------------------------------------------
l_name = Label(Inside_Frame1, text="Name")
l_name.grid(row=0, column=0, padx=5, pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1, width=30, textvariable=E_name_var)
E_name.grid(row=0, column=1, padx=5, pady=5)
# -----------------------------------------------
l_last_name = Label(Inside_Frame1, text="Last Name")
l_last_name.grid(row=1, column=0, padx=5, pady=5)
E_last_name_var = StringVar()
E_last_name = Entry(Inside_Frame1, width=30, textvariable=E_last_name_var)
E_last_name.grid(row=1, column=1, padx=5, pady=5)
# ---------------------------------------------------
l_contact = Label(Inside_Frame1, text="Contact")
l_contact.grid(row=2, column=0, padx=5, pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1, width=30, textvariable=E_contact_var)
E_contact.grid(row=2, column=1, padx=5, pady=5)
# ---------------------------------------------------
Frame2 = Frame(window)
Frame2.grid(row=0, column=1, padx=15, pady=15, sticky=E)
# <><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
Add_button = Button(Frame2, text="Add Detail", width=15,
                    bg="#f54865", fg="#FFFFFF", command=TambahDetail)
Add_button.grid(row=0, column=0, padx=8, pady=8)

Update_button = Button(Frame2, text="Update Detail", width=15,
                       bg="#f54865", fg="#FFFFFF", command=UpdateDetail)
Update_button.grid(row=1, column=0, padx=8, pady=8)


Reset_button = Button(Frame2, text="Reset", width=15,
                      bg="#f54865", fg="#FFFFFF", command=DataReset)
Reset_button.grid(row=2, column=0, padx=8, pady=8)
# ----------------------------------------------------------------------------

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1, column=0, padx=15, pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set, font=("Arial Bold", 10),
                 bg="#282923", fg="#E7C855", width=40, height=10, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
select.grid(row=0, column=0, sticky=W)
scroll.grid(row=0, column=1, sticky=N+S)


# -----------------------------------------------------------------------------------
ActionFrame = Frame(window)
ActionFrame.grid(row=1, column=1, padx=15, pady=15, sticky=E)

Delete_button = Button(ActionFrame, text="Delete", width=15,
                       bg="#D20000", fg="#FFFFFF", command=HapusData)
Delete_button.grid(row=0, column=0, padx=5, pady=5, sticky=S)

Loadbutton = Button(ActionFrame, text="Load", width=15,
                    bg="#00FF00", fg="#FFFFFF", command=MemuatData)
Loadbutton.grid(row=1, column=0, padx=5, pady=5)


ReadCSVFile()


window.mainloop()
