import pandas as pd
import json

def excel_to_sap_format(file_path):
    print(f"'{file_path}' dosyasındaki veriler okunuyor...")
    
    # Dosyanı okuyoruz (Excel veya CSV olmasına karşı iki ihtimali de koyduk)
    try:
        df = pd.read_excel(file_path)
    except:
        df = pd.read_csv(file_path)
    
    sap_payloads = []

    # Senin dosyasındaki her bir satırı (siparişi) tek tek SAP şablonuna oturtuyoruz
    for index, row in df.iterrows():
        po_structure = {
            "HEADER": {
                "PO_NUMBER": str(row.get('Order_ID', f"PO-{index}")), # Senin Order ID'n
                "COMP_CODE": "1000",
                "DOC_TYPE": "NB",
                "CREAT_DATE": str(row.get('Date', '2026-04-13')) # Senin Tarihin
            },
            "ITEMS": [
                {
                    "PO_ITEM": "00010",
                    "SUPPLIER_ID": str(row.get('Supplier_ID', 'TEDARIKCI_1')), # Senin Tedarikçin
                    "MATERIAL_GROUP": str(row.get('Category', 'MAT_1')), # Hammadde, Plastik vs.
                    "QUANTITY": float(row.get('Order_Quantity', 1)), # Sipariş Adedi
                    "TOTAL_AMOUNT": float(row.get('Order_Amount', 0)) # Sipariş Tutarı
                }
            ]
        }
        sap_payloads.append(po_structure)

    # SAP için hazır olan JSON dosyasını oluşturuyoruz
    with open('sap_upload_ready.json', 'w', encoding='utf-8') as f:
        json.dump(sap_payloads, f, indent=4, ensure_ascii=False)
    
    print("MÜKEMMEL! Veriler SAP BAPI (JSON) formatına başarıyla dönüştürüldü!")

# İŞTE BURASI ÇALIŞTIRMA KOMUTU (Başı açık, direkt çalışır)
# Sol taraftaki dosya adın "Supply Chain.xlsx" ise böyle kalsın, uzun csv ise adını buraya kopyala.
excel_to_sap_format('Supply Chain.xlsx')
