"""
Contact Book

Tavsif:
    Bu dastur kontaktlar bilan ishlaydi — qoshish, ko‘rish, qidirish va
    email bo‘yicha filtrlash. Har bir kontakt "Ism|Telefon|Email" formatida
    list ichida string sifatida saqlanadi.
"""

from typing import List


def show_menu() -> None:
    """Konsolda foydalanuvchi uchun menyuni chiqaradi."""
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. ➕ Yangi kontakt qo‘shish")
    print("2. 📄 Barcha kontaktlarni ko‘rish")
    print("3. 🔍 Kontaktni ism bo‘yicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni ko‘rish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact: str) -> bool:
    """
    Kontakt formati to‘g‘ri yoki noto‘g‘ri ekanligini aniqlaydi.

    Args:
        contact (str): Kontakt string (masalan, "Ali|99890...|ali@gmail.com").

    Returns:
        bool: To‘g‘ri format bo‘lsa True, aks holda False.
    """
    
    pass


def add_contact(contact_list: List[str]) -> None:
    """
    Yangi kontakt qo‘shadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def list_contacts(contact_list: List[str]) -> None:
    """
    Kontaktlar ro‘yxatini konsolga chiqaradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def search_contact(contact_list: List[str]) -> None:
    """
    Foydalanuvchi kiritgan ism bo‘yicha kontaktlarni qidiradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def filter_gmail_contacts(contact_list: List[str]) -> None:
    """
    Faqat @gmail.com domeniga ega kontaktlarni ko‘rsatadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    pass


def main() -> None:
    """
    Dasturning asosiy ishga tushirish funksiyasi.
    Menyu orqali foydalanuvchi tanlovini boshqaradi.
    """
    contacts: List[str] = []

    while True:
        show_menu()
        choice = input("Tanlov (1–5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("❗️Noto‘g‘ri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")


main()
