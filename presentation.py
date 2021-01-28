from data import *
import tkinter as tk
import tkinter.ttk

class Aplication(object):
    global places
    places = getDataFromAPI
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x180')
        self.root.title("AirQuality")
        self.root.resizable(False, False)

        self.main_label = tk.Label(self.root, text="Wybierz jedną z dostępnych stacji,\n"
                                                   " w której chcesz sprawdzić jakość powietrza ", \
                                   font=('Arial', 15))
        self.main_label.pack(side=tk.TOP)
        # self.confirm=tk.Button(self.root, text="Zatwierdź",command=)
        self.station_select = tk.ttk.Combobox(self.root, width=60, height=5, state='readonly')
        self.station_select.pack()
        self.station_select.place(x=60, y=60)
        self.stations = self.get_stations()
        self.station_select['values'] = self.stations[1]
        self.station_select.bind("<<ComboboxSelected>>", self.choice_function)

        # self.station_select.current()



    def get_stations(self):
        station_names=()
        places_list=places.getStationData(self)
        for i in places_list:
            station_names +=  i.name,
        return places_list,station_names
    def destruct_labels(self):
        # labels = (station_name_label, check_time_label, air_q_text_label, air_q_SO2_label, \
        #           air_q_NO2_label, air_q_PM10_label, air_q_PM25_label, air_q_CO_label, \
        #           air_q_C6H6_label, air_q_O3_label)
        if 'station_name_label' in globals():
            station_name_label.destroy()
            del globals()['station_name_label']

        if 'check_time_label' in globals():
            check_time_label.destroy()
            del globals()['check_time_label']

        if 'air_q_text_label' in globals():
            air_q_text_label.destroy()
            del globals()['air_q_text_label']

        if 'air_q_SO2_label' in globals():
            air_q_SO2_label.destroy()
            del globals()['air_q_SO2_label']

        if 'air_q_NO2_label' in globals():
            air_q_NO2_label.destroy()
            del globals()['air_q_NO2_label']

        if 'air_q_PM10_label' in globals():
            air_q_PM10_label.destroy()
            del globals()['air_q_PM10_label']

        if 'air_q_PM25_label' in globals():
            air_q_PM25_label.destroy()
            del globals()['air_q_PM25_label']

        if 'air_q_CO_label' in globals():
            air_q_CO_label.destroy()
            del globals()['air_q_CO_label']

        if 'air_q_C6H6_label' in globals():
            air_q_C6H6_label.destroy()
            del globals()['air_q_C6H6_label']

        if 'air_q_O3_label' in globals():
            air_q_O3_label.destroy()
            del globals()['air_q_O3_label']









    def choice_function(self,event):
        font_size=10
        station = self.station_select.get()
        for i in self.stations[0]:
            if station == i.name:
                self.root.geometry('500x330')
                data = places.getStationProperties(self,i.id)
                self.destruct_labels()

                station_name = tk.StringVar()
                station_name.set(f"Wybrano: {i.name}")
                global station_name_label
                station_name_label = tkinter.Label(self.root, textvariable=station_name, font=("Arial", font_size))
                station_name_label.pack()
                station_name_label.place(x=60, y=90)

                check_time=tk.StringVar()
                check_time.set(f"Data pomiaru: {data.indexMain[0][:10]}")
                global check_time_label
                check_time_label = tkinter.Label(self.root, textvariable=check_time, font=("Arial", font_size))
                check_time_label.pack()
                check_time_label.place(x=60, y=110)

                air_q_text = tk.StringVar()
                air_q_text.set(f"Tekstowa ocena stanu powietrza: {data.indexMain[1]}")
                global air_q_text_label
                air_q_text_label = tkinter.Label(self.root, textvariable=air_q_text, font=("Arial", font_size))
                air_q_text_label.pack()
                air_q_text_label.place(x=60, y=130)
            #SO2
                air_q_SO2 = tk.StringVar()
                if len(data.indexSO2)==4:
                    info = f"PoziomSO2: {data.indexSO2[2]} µg/m3 Ocena tekstowa: {data.indexSO2[3]} Godzina: {data.indexSO2[1][12:16]}"
                else:
                    info="PoziomSO2: Ta stacja nie mierzy tej właściwości!"
                air_q_SO2.set(info)
                global air_q_SO2_label
                air_q_SO2_label = tkinter.Label(self.root, textvariable=air_q_SO2, font=("Arial", font_size))
                air_q_SO2_label.pack()
                air_q_SO2_label.place(x=30, y=170)
            #NO2
                air_q_NO2 = tk.StringVar()
                if len(data.indexNO2)==4:
                    info=f"PoziomNO2: {data.indexNO2[2]} µg/m3 Ocena tekstowa: {data.indexNO2[3]} Godzina: {data.indexNO2[1][12:16]}"
                else:
                    info="PoziomNO2: Ta stacja nie mierzy tej właściwości!"
                air_q_NO2.set(info)
                global air_q_NO2_label
                air_q_NO2_label = tkinter.Label(self.root, textvariable=air_q_NO2, font=("Arial", font_size))
                air_q_NO2_label.pack()
                air_q_NO2_label.place(x=30, y=190)
            #PM10
                air_q_PM10 = tk.StringVar()
                if len(data.indexPM10) == 4:
                    info = f"PoziomPM10: {data.indexPM10[2]} µg/m3 Ocena tekstowa: {data.indexPM10[3]} Godzina: {data.indexPM10[1][12:16]}"
                else:
                    info = "PoziomPM10: Ta stacja nie mierzy tej właściwości!"
                air_q_PM10.set(info)
                global air_q_PM10_label
                air_q_PM10_label = tkinter.Label(self.root, textvariable=air_q_PM10, font=("Arial", font_size))
                air_q_PM10_label.pack()
                air_q_PM10_label.place(x=30, y=210)
            #PM25
                air_q_PM25 = tk.StringVar()
                if len(data.indexPM25) == 4:
                    info = f"PoziomPM25: {data.indexPM25[2]} µg/m3 Ocena tekstowa: {data.indexPM25[3]} Godzina: {data.indexPM25[1][12:16]}"
                else:
                    info = "PoziomPM25: Ta stacja nie mierzy tej właściwości!"
                air_q_PM25.set(info)
                global air_q_PM25_label
                air_q_PM25_label = tkinter.Label(self.root, textvariable=air_q_PM25, font=("Arial", font_size))
                air_q_PM25_label.pack()
                air_q_PM25_label.place(x=30, y=230)
            #CO
                air_q_CO = tk.StringVar()
                if len(data.indexCO) == 4:
                    info = f"PoziomCO: {data.indexCO[2]} µg/m3 Ocena tekstowa: {data.indexCO[3]} Godzina: {data.indexCO[1][12:16]}"
                else:
                    info = "PoziomCO: Ta stacja nie mierzy tej właściwości!"
                air_q_CO.set(info)
                global air_q_CO_label
                air_q_CO_label = tkinter.Label(self.root, textvariable=air_q_CO, font=("Arial", font_size))
                air_q_CO_label.pack()
                air_q_CO_label.place(x=30, y=250)
            #C6H6
                air_q_C6H6 = tk.StringVar()
                if len(data.indexC6H6) == 4:
                    info = f"PoziomC6H6: {data.indexC6H6[2]} µg/m3 Ocena tekstowa: {data.indexC6H6[3]} Godzina: {data.indexC6H6[1][12:16]}"
                else:
                    info = "PoziomCO: Ta stacja nie mierzy tej właściwości!"
                air_q_C6H6.set(info)
                global air_q_C6H6_label
                air_q_C6H6_label = tkinter.Label(self.root, textvariable=air_q_C6H6, font=("Arial", font_size))
                air_q_C6H6_label.pack()
                air_q_C6H6_label.place(x=30, y=270)
            #O3
                air_q_O3 = tk.StringVar()
                if len(data.indexO3) == 4:
                    info = f"PoziomO3: {data.indexO3[2]} µg/m3 Ocena tekstowa: {data.indexO3[3]} Godzina: {data.indexO3[1][12:16]}"
                else:
                    info = "PoziomCO: Ta stacja nie mierzy tej właściwości!"
                air_q_O3.set(info)
                global air_q_O3_label
                air_q_O3_label = tkinter.Label(self.root, textvariable=air_q_O3, font=("Arial", font_size))
                air_q_O3_label.pack()
                air_q_O3_label.place(x=30, y=290)





    def run(self):
        self.root.mainloop()



class Main(object):
    Okno=Aplication()
    Okno.run()
