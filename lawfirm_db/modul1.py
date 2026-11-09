import sqlite3
import tkinter as tk
from tkinter import ttk


class LawFirmApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Юридическая фирма - Баянғазина Мадина")
    self.root.geometry("900x500")

    # Верхняя панель с кнопками выбора таблиц
    btn_frame = tk.Frame(root, bg="#000c6b", pady=10)
    btn_frame.pack(fill=tk.X)

    tk.Button(
        btn_frame,
        text="Клиенты",
        command=lambda: self.load_table("Clients"),
        width=15,
    ).pack(side=tk.LEFT, padx=10)
    tk.Button(
        btn_frame,
        text="Адвокаты",
        command=lambda: self.load_table("Lawyers"),
        width=15,
    ).pack(side=tk.LEFT, padx=10)
    tk.Button(
        btn_frame,
        text="Дела",
        command=lambda: self.load_table("Cases"),
        width=15,
    ).pack(side=tk.LEFT, padx=10)
    tk.Button(
        btn_frame,
        text="Платежи",
        command=lambda: self.load_table("Payments"),
        width=15,
    ).pack(side=tk.LEFT, padx=10)

    # Область для отображения таблицы
    self.tree_frame = tk.Frame(root)
    self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Загружаем таблицу Клиентов при старте
    self.load_table("Clients")

  def load_table(self, table_name):
    for widget in self.tree_frame.winfo_children():
      widget.destroy()

    try:
      # Подключаемся к вашей базе данных SQLite
      conn = sqlite3.connect("law_firm.db")
      cursor = conn.cursor()

      cursor.execute(f"SELECT * FROM {table_name}")
      columns = [description[0] for description in cursor.description]
      rows = cursor.fetchall()
      conn.close()

      # Создаем визуальную таблицу
      tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings")

      for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor=tk.CENTER)

      scrollbar = ttk.Scrollbar(
          self.tree_frame, orient=tk.VERTICAL, command=tree.yview
      )
      tree.configure(yscroll=scrollbar.set)

      tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
      scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

      for row in rows:
        tree.insert("", tk.END, values=row)

    except Exception as e:
      error_label = tk.Label(
          self.tree_frame, text=f"Ошибка загрузки: {e}", fg="red"
      )
      error_label.pack()


if __name__ == "__main__":
  root = tk.Tk()
  app = LawFirmApp(root)
  root.mainloop()