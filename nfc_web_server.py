import machine
import utime
import ujson
from pico_nfc import PN532_SPI
from machine import Pin, SoftSPI
from micropython import const
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Configurazione NFC
spi = SoftSPI(sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs_pin = Pin(17)
sda_pin = Pin(21)
irq_pin = Pin(20)
reset_pin = Pin(22)

nfc = PN532_SPI(spi, cs_pin, reset_pin, irq_pin)

# Configurazione web server
log_filename = "log.csv"

class NFCServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/download':
            with open(log_filename, 'rb') as log_file:
                self.send_response(200)
                self.send_header('Content-Type', 'text/csv')
                self.send_header('Content-Disposition', 'attachment; filename="log.csv"')
                self.end_headers()
                self.wfile.write(log_file.read())
                log_file.close()
                # Cancella i dati del file log.csv
                with open(log_filename, 'w') as log_file:
                    log_file.write('')
        else:
            super().do_GET()

def read_uid():
    uid = nfc.read_passive_target()
    if uid:
        uid_str = ':'.join(format(x, '02x') for x in uid)
        return uid_str
    return None

def find_name(uid, database_filename):
    try:
        with open(database_filename, 'r') as db_file:
            for line in db_file:
                uid_db, nome, cognome = line.strip().split(',')
                if uid_db == uid:
                    return f"{nome} {cognome}"
    except Exception as e:
        print("Errore nella ricerca nel database:", e)
    return None

def log_entry(data):
    with open(log_filename, 'a') as log_file:
        log_file.write(data + '\n')

def main():
    while True:
        uid = read_uid()
        if uid:
            nome_completo = find_name(uid, "database.csv")
            if nome_completo:
                ora_attuale = utime.localtime()
                data_ora = utime.strftime("%Y-%m-%d %H:%M:%S", ora_attuale)
                log_entry(f"{nome_completo},{data_ora}")
                print(f"UID rilevato: {uid}, Nome: {nome_completo}, Data e Ora: {data_ora}")
        utime.sleep(1)

if __name__ == "__main__":
    http_server = HTTPServer(('', 80), NFCServer)
    print("Server avviato sulla porta 80")
    try:
        main()
    except KeyboardInterrupt:
        print("\nChiusura del server NFC")
