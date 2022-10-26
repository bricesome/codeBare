import barcode
from barcode.writer import ImageWriter


def code(nbr,lot):
     hr = barcode.get_barcode_class('ean13')
     for i in range(nbr):
         H=hr('122326923789',writer=ImageWriter())
         qt = H.save(str(lot)+"code"+str(i))

#code(4,"lot1")

def code1(nbr,lot):
    hr = barcode.get_barcode_class('code39')
    for i in range(nbr):
        H = hr('yr22326923789', writer=ImageWriter())
        qt = H.save(str(lot) + "code" + str(i))

#code1(2,"lot3")

def code2(nbr,lot):
    hr = barcode.get_barcode_class('code128')
    for i in range(nbr):
        H = hr('BISCUITS FARINE DE MAIS+FARINE DE BLE SALE SANS ADDITIFS-Tel:77547754'+str(i), writer=ImageWriter())
        qt = H.save(str(lot) + "code" + str(i))

def code3(nbr,lot):
    hr = barcode.get_barcode_class('code128')
    for i in range(nbr):
        H = hr('BISCUITS FARINE DE MAIS+FARINE DE BLE SUCRE SANS ADDITIFS-Tel:77547754'+str(i), writer=ImageWriter())
        qt = H.save(str(lot) + "code" + str(i))

def code4(nbr,lot):
    hr = barcode.get_barcode_class('code128')
    for i in range(nbr):
        H = hr('BISCUITS FARINE DE SORGHO ROUGE+FARINE DE BLE SALE SANS ADDITIFS-Tel:77547754'+str(i), writer=ImageWriter())
        qt = H.save(str(lot) + "code" + str(i))


code2(34,"lot1")
code3(33,"lot2")
code2(33,"lot3")

# def code3(nbr,lot):
#     hr = barcode.get_barcode_class("gs1128UCCean128")
#     for i in range(nbr):
#         H = hr('yr223-26923789_salut', writer=ImageWriter())
#         qt = H.save(str(lot) + "code" + str(i))
#
# code3(2,"lot2")