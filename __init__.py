import datamangment

managger = datamangment.Datas("adatok.txt")

if __name__ == '__main__':
    managger.run(altalanos=False, mintavetel=35, max_karakterhossz=21)