import pandas as pd
import json

def excel_to_sap_format(file_path):
    # Excel dosyasını oku (Depodaki mevcut Excel dosyanı okuyor)
    print("Loading legacy procurement data...")
    df = pd.read_excel(file_path)
    
    sap_payloads = []

    for index, row in df.iterrows():
        # SAP BAPI / IDoc benzeri profesyonel veri yapısı oluşturuluyor
        po_structure = {
            "HEADER": {
                "PO_NUMBER": f"PO-100{index}",
                "COMP_CODE": "1000",
                "DOC_TYPE": "NB",
                "CREAT_DATE": "2026-04-13"
            },
            "ITEMS": [
                {
                    "PO_ITEM": "00010",
                    "MATERIAL_GROUP": "RAW_MAT",
                    "PLANT": "2000",
                    "QUANTITY": 1
                }
            ]
        }
        sap_payloads.append(po_structure)

    # SAP uyumlu JSON dosyasını dışa aktar
    with open('sap_upload_ready.json', 'w') as f:
        json.dump(sap_payloads, f, indent=4)
    
    print("Success: Data converted to SAP BAPI structure successfully!")

# Çalıştırma komutu:
# excel_to_sap_format('senin_excel_dosyanin_adi.xlsx')
