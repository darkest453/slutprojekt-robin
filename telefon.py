import json
import os

DATAFIL = "Kontakter.json"

def ladda_kontakter():
    if os.path.exists(DATAFIL):
        with open(DATAFIL, "r", encoding="utf-8") as f:
            return json.load(f)
        
    return{}

def spara_kontakter(kontakter):
    with open (DATAFIL, "w", encoding="utf-8") as f:
        json.dump(kontakter, f,  ensure_ascii=False, indent=2)
    print("✅ Kontakter sparade.")
    
def visa_meny():
    print("\n" + "═" * 40)
    print("        📞  TELEFONKATALOG")
    print("═" * 40)
    print("  1. Lägg till kontakt")
    print("  2. Sök kontakt")
    print("  3. Visa alla kontakter")
    print("  4. Redigera kontakt")
    print("  5. Ta bort kontakt")
    print("  6. Avsluta")
    print("═" * 40)
    
    
def lägg_till(kontakter):
    pass
    
def sök(kontakter): 
    pass


def visa_alla(kontakter):
    pass

def skriv_ut_kontakt(namn, info):
    pass

def redigera(kontakter):
    pass

def ta_bort(kontakter):
    pass

def main():
    kontakter = ladda_kontakter()
    print("Det här är din telefonkatalogen")
    
    välj_map = {
        
        "1": lägg_till,
        "2": sök,
        "3": visa_alla,
        "4": redigera,
        "5": ta_bort,
    }
    
    while True:
        visa_meny
        val = input("välj (1-6): ").strip() #removes leading and trailing spaces to return a copy of the original string
        if val == "6":
            print("program avlustas")
            break
        elif val in välj_map:
            if val == "3":
                 välj_map[val](kontakter)
            else:
                välj_map[val](kontakter)
        else:
            print("❌ Ogiltigt val, försök igen.")
 
 
if __name__ == "__main__":
    main()



  
  
    
