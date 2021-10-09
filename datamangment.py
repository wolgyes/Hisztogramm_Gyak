from pathlib import Path
from math import sqrt


class Datas:
    def __init__(self, datas_path):
        self.datas = []
        try:
            with open(Path(datas_path)) as file:
                for line in file.readlines():
                    try:
                        for data in line.strip().split(" "):
                            self.datas.append(float(data))
                    except:
                        print("Adatfeldolgozasi hiba, kerjuk ellenorizze a fajlt")
                        self.datas_gotcha = False
                self.datas_gotcha = True
        except:
            print("Fajlolvasasi hiba")
            self.datas_gotcha = False

        if self.datas_gotcha:
            self._max()
            self._min()
            self._sum()
            self._len()
            self._avg()
            self._terj()
            self._szoras()

    @property
    def _datas_in_one(self):
        return [sor for sor in self.datas]

    def _max(self):
        self.max = max(self._datas_in_one)

    def _min(self):
        self.min = min(self._datas_in_one)

    def _terj(self):
        self.terj = self.max - self.min

    def _len(self):
        self.len = len(self._datas_in_one)

    def _sum(self):
        self.sum = sum(self._datas_in_one)

    def _avg(self):
        self.avg = self.sum / self.len

    def _szoras(self):
        to_sqrt = 0
        for data in self._datas_in_one:
            to_sqrt += pow(data - self.avg, 2)
        self.szoras = sqrt(to_sqrt / self.len)

    def _felosztas(self, oszlopok_szama, maximum_meret):
        oszlopok = {}
        oszlop_ertekek = []
        skala_param = (self.max - self.min) / oszlopok_szama
        for i in range(oszlopok_szama):
            i += 1
            oszlopok[i] = skala_param * i
            oszlop_ertekek.append(0)

        for ertek in self._datas_in_one:
            for oszlop_szam, oszlop_max in oszlopok.items():
                if ertek < oszlop_max:
                    oszlop_ertekek[oszlop_szam - 1] += 1
                    break

        modoszto = max(oszlop_ertekek) / maximum_meret

        hisztogramm = []
        for oszlop_ertek in oszlop_ertekek:
            hisztogramm.append("*" * int(oszlop_ertek // modoszto))

        return hisztogramm

    def _hisztogramm_draw(self, oszlopok_szama, maximum_meret):
        print("\nHisztogramm:")
        hisztogramm = self._felosztas(oszlopok_szama, maximum_meret)
        counter = 0
        kirajzolt = 0
        for sor in hisztogramm:
            if "*" in sor:
                print(sor.strip())
                kirajzolt += 1
            else:
                counter += 1

        print("Kirajzolt oszlopok szama: ", kirajzolt)
        if counter > 0:
            print("Illetve tovabbi " + str(counter) + "db oszlop kerult volna kirajzolasra de tul pici gyakorisaggal szerepeltek.")

    def run(self, altalanos=True, mintavetel=50, max_karakterhossz=100, ):
        if self.datas_gotcha:
            if altalanos:
                print("A tomb:")
                print("\tMinimuma:", self.min)
                print("\tMaximuma:", self.max)
                print("\tTerjedelme:", self.terj)
                print("\tAtlaga:", self.avg)
                print("\tOsszege:", self.sum)
                print("\tElemszama:", self.len)
                print("\tSzorasa:", self.szoras)

            self._hisztogramm_draw(mintavetel, max_karakterhossz)
