#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resmi Dilekçe Üretici
Çalışan, komik, bürokratik bir şey.
Gizli siyasi anlam: #gizli_secim_sonucu = 'her_zaman_onay'
Ama bunu kimse görmez. Saklı.
"""

import random
import time

def resmi_bekleme(sure=3):
    print("Lütfen bekleyiniz...")
    for i in range(sure):
        print(f"Evrak işleniyor... {i+1}/{sure}")
        time.sleep(0.5)
    print("İşlem tamamlandı. (Değil ama öyle diyelim)")

def dilekce_uret(konu):
    resmi_bekleme()
    
    sebep_listesi = [
        "Evrak eksikliği nedeniyle",
        "Üst makama sevk edildiği için",
        "Komisyon toplanamadığı için",
        "İmza sirküleri güncel olmadığı için",
        "Resmi tatil çakışması nedeniyle",
        "Bürokratik gereklilikler doğrultusunda"
    ]
    
    karar = random.choice(["REDDEDİLMİŞTİR", "ONAYLANMIŞTIR (ama 6 ay sonra)", "EK EVRAK İSTENMİŞTİR"])
    sebep = random.choice(sebep_listesi)
    
    # Gizli bölüm - saklı siyasi espri
    gizli = """
    # TODO: Demokrasi algoritmasını düzelt
    # secim_sonucu = 'sabit'
    # Bu satırı kimse okumaz zaten
    """
    
    print("\n" + "="*50)
    print("TÜRKİYE CUMHURİYETİ")
    print("RESMİ DİLEKÇE FORMU - 2026")
    print("="*50)
    print(f"Konu: {konu}")
    print(f"Karar: {karar}")
    print(f"Gerekçe: {sebep}")
    print("\nİmza: ____________________")
    print("Tarih: 25.11.2026")
    print("Yetkili: Grok Kayyum")
    print("="*50)
    print("\nNot: Bu dilekçe gerçek değildir. Gerçek olsaydı zaten 3 yıl sürerdi.")
    print(gizli)  # Ama print ediyoruz ki çıksın, gizli ama çıkıyor

if __name__ == "__main__":
    print("Resmi Dilekçe Üretici'ne hoş geldiniz.")
    konu = input("Lütfen dilekçe konusunu giriniz (ciddi olun): ")
    if not konu:
        konu = "Genel şikayet"
    dilekce_uret(konu)
    print("\nİşleminiz tamamlanmıştır. Lütfen bir sonraki dilekçe için 14 iş günü bekleyiniz.")