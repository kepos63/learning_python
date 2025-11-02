import tkinter
def comprehensive_pack_example():
    comp_window = Tk.Toplevel(root)
    comp_window.title("Comprehensive Pack Example")
    comp_window.geometry("500x400")

    # Виджет со всеми возможными параметрами pack
    comprehensive_label = Tk.Label(
        comp_window,
        text="Все параметры pack:\n"
             "side='left'\n"
             "fill='y'\n"
             "expand=True\n"
             "anchor='n'\n"
             "padx=10, pady=10\n"
             "ipadx=5, ipady=5",
        bg="lightgoldenrod",
        relief="ridge",
        borderwidth=2,
        font=("Arial", 10),
        width=20,
        height=10
    )

    comprehensive_label.pack(
        side="left",
        fill="y",
        expand=True,
        anchor="n",
        padx=10,
        pady=10,
        ipadx=5,
        ipady=5
    )

    # Дополнительные виджеты для демонстрации взаимодействия
    right_frame = tk.Frame(comp_window)
    right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Различные комбинации параметров
    combinations = [
        ("top", "x", False, "n", "Комбинация 1"),
        ("top", "both", True, "center", "Комбинация 2"),
        ("bottom", "x", False, "s", "Комбинация 3"),
        ("left", "y", True, "w", "Комбинация 4")
    ]

    colors = ["lightblue", "lightgreen", "lightcoral", "lightcyan"]

    for i, (side, fill, expand, anchor, text) in enumerate(combinations):
        lbl = tkinter.Tk.Label(right_frame, text=text, bg=colors[i])
        lbl.pack(
            side=side,
            fill=fill,
            expand=expand,
            anchor=anchor,
            padx=5,
            pady=5,
            ipadx=3,
            ipady=3
        )


# Кнопка для полного примера
comp_btn = Tk.Button(root, text="Полный пример Pack", command=comprehensive_pack_example)
comp_btn.pack(pady=10)

root.mainloop()