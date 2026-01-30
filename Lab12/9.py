import logging

logging.basicConfig(
    filename='parser.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

def przetworz_logi(linie):
    for linia in linie:
        if linia.startswith("INFO:"):
            logging.info(linia[5:].strip())
        elif linia.startswith("DEBUG:"):
            logging.debug(linia[6:].strip())
        elif linia.startswith("WARNING:"):
            logging.warning(linia[8:].strip())
        elif linia.startswith("ERROR:"):
            logging.error(linia[6:].strip())
        else:
            logging.warning(f"Nierozpoznana linia: {linia}")

linie = [
    "INFO: Start systemu.",
    "DEBUG: Sprawdzanie.",
    "ERROR: Awaria!",
    "Nieznany format"
]

przetworz_logi(linie)