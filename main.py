import os
from tkinter.filedialog import askdirectory

source_folder = askdirectory(title="Source Folder")
destination_folder = askdirectory(title="Destination Folder")

file_rules = {
    "jan": "Janeiro",
    "fev": "Fevereiro",
    "mar": "Março",
    "abr": "Abril",
    "mai": "Maio",
    "jun": "Junho",
    "jul": "Julho",
    "ago": "Agosto",
    "set": "Setembro",
    "out": "Outubro",
    "nov": "Novembro",
    "dez": "Dezembro",

}

file_list = os.listdir(source_folder)

for file_name in file_list:
    for key in file_rules.keys():
        if key in file_name:
            new_folder = file_rules[key]
            original_full_name = os.path.join(source_folder, file_name)
            final_full_name = os.path.join(destination_folder, new_folder, file_name)
            "C://Users/wladsonramos/Downloads/arquivos/vendas_jan.txt"
            "C://Users/wladsonramos/Downloads/arquivos/Janeiro/vendas_jan.txt"
            new_folder_path = os.path.join(destination_folder, new_folder)
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            os.rename(original_full_name, final_full_name)
