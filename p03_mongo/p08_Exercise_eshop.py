"""Vytvořte aplikaci e-shop:
- Databáze bude obsahovat kolekce:
  - Customers (_id, name, surname, address)
  - Storage (_id, product, serial_number, count)
  - Order (_id, Customer, Product, count)
- přidejte do databáze několik zákazníků (Customers) (alespoň 3)
- přidejte do databáze několik produktů do skladu (Storage) (alespoň 3)
- vytvořte konzolovou aplikaci, která umožní:
  - výpis všech produktů
  - výpis zákazníků
  - přidání nového zákazníka (simulujeme registraci nového zákazníka)
  - smazání zákazníka
  - zvolení zákazníka (simulujeme přihlášení do e-shopu)
    - zákazník si může vypsat všechny produkty
    - zákazník může vyhledávat produkt podle jména nebo výrobního čísla
    - zákazník může vložit produkt do objednávky (Order)
  - výpis všech objednávek
"""