try:
    import Tkinter as tk
except:
    import tkinter as tk


class test():
    m = 0
    otv = 0
    choice1 = [('A produce an energy-efficient design', 1), ('B adapt an existing energy-saving appliance', 2),
               ('C develop a new use for current technology', 3)]
    choice2 = [('A more appealing', 1), ('B more common', 2), ('C more economical', 3)]
    choice3 = [('A for decoration', 1), ('B to switch it on', 2), ('C to stop water escaping', 3)]
    check1 = [(' A the gym', 1), ('B the tracks', 2), ('C the indoor pool', 3), ('D the outdoor pool', 4),
              (' E the sports training for children', 5)]

    def __init__(self, otv, m):
        self.root = tk.Tk()
        self.root.title("English test")
        self.root.geometry("800x800")
        self.l1 = tk.Label(self.root, text="Введите цвет фона:")
        self.l1.grid(row=0, column=0, sticky='E')
        self.ent1 = tk.Entry(self.root, width=20)
        self.ent1.grid(row=0, column=1, sticky='W')
        self.row = 1
        self.b1 = tk.Button(self.root, text="Перекрасить окно", command=lambda: self.click1(str(self.ent1.get())))
        self.b1.grid(row=self.row, column=0, sticky='E')
        self.otv = otv
        self.m = m
        self.root.bind("<Control-s>", lambda e: self.my(str(self.ent1.get()), str(self.otv)))
        self.root.mainloop()

    def guga(self):
        self.root.destroy()

    def my(self, ent, pr):
        f = open('result.txt', 'w')
        sl = "Количество правильных ответов: " + pr + " из 5"
        for j in ent:
            f.write(j)
        f.write('\n')
        for i in sl:
            f.write(i)
        f.close()

    def select1(self, l):
        if l == 3:
            self.otv += 1

    def select2(self, l):
        if l == 1:
            self.otv += 1

    def select3(self, l):
        if l == 2:
            self.otv += 1

    def pressed(self, v):
        if v == 0 or v == 2:
            self.otv += 1

    def click1(self, smth):
        self.m += 1
        entry_text = tk.StringVar()
        if self.m == 1:
            self.root['bg'] = self.l1['bg'] = smth
            self.l1['text'] = "Введите цвет текста:"
            self.b1['text'] = "Перекрасить текст"
            self.ent1['textvariable'] = entry_text
        elif self.m == 2:
            self.b1['fg'] = self.l1['fg'] = smth
            self.l1['text'] = "Введите ФИО:"
            self.b1['text'] = "Начать тест "
            self.ent1['textvariable'] = entry_text
        elif self.m == 3:
            self.create_all()
            self.lbl['bg'] = self.lbl2['bg'] = self.lbl3['bg'] = self.lbl4['bg'] = self.sel3['bg'] = self.l1['bg']
            self.lbl['fg'] = self.lbl2['fg'] = self.lbl3['fg'] = self.lbl4['fg'] = self.sel3['fg'] = self.l1['fg']

    def click2(self, pr):
        self.sel3.config(text="Количество правильных ответов: " + pr + " из 5")

    def create_all(self):
        self.row += 2
        self.lbl = tk.Label(text=" Students entering the design competition have to")
        self.lbl.grid(row=2, column=0, sticky='W')

        language1 = tk.IntVar()

        for txt, val in self.choice1:
            tk.Radiobutton(text=txt, value=val, variable=language1, pady=10, padx=15,
                           command=lambda: self.select1(language1.get())) \
                .grid(row=self.row, sticky='W')
            self.row += 1

        self.lbl2 = tk.Label(text="John chose a dishwasher because he wanted to make dishwashers")
        self.lbl2.grid(row=self.row, column=0, sticky='W')
        self.row += 1
        language2 = tk.IntVar()
        for txt, val in self.choice2:
            tk.Radiobutton(text=txt, value=val, variable=language2, pady=10, padx=15,
                           command=lambda: self.select2(language2.get())) \
                .grid(row=self.row, sticky='W')
            self.row += 1

        self.lbl3 = tk.Label(text="The stone in John’s ‘Rockpool’ design is used")
        self.lbl3.grid(row=self.row, column=0, sticky='W')
        self.row += 1
        language3 = tk.IntVar()
        for txt, val in self.choice3:
            tk.Radiobutton(text=txt, value=val, variable=language3, pady=10, padx=15,
                           command=lambda: self.select3(language3.get())) \
                .grid(row=self.row, sticky='W')
            self.row += 1

        self.b2 = tk.Button(self.root, text="Проверить кол-во правильных ответов",
                            command=lambda: self.click2(str(self.otv))) \
            .grid(row=self.row, column=0, sticky='W')
        self.row += 1
        self.sel3 = tk.Label()
        self.sel3.grid(row=self.row, sticky='W')

        self.var = []
        x = 0
        while x < 5:
            self.var.append(tk.IntVar(None))
            x += 1

        row1 = 2
        self.lbl4 = tk.Label(text="Which TWO facilities at the leisure club have recently been improved? ")
        self.lbl4.grid(row=2, column=1, sticky='W')

        row1 += 1
        x = 0
        for txt, val in self.check1:
            tk.Checkbutton(text=txt, variable=self.var[x], pady=10, padx=15, onvalue=val, offvalue=0,
                           command=lambda v=x: self.pressed(v)).grid(row=row1, column=1, sticky='W')
            row1 += 1
            if x < 5:
                x += 1

# https://engexam.info/ielts-listening-practice-tests/ielts-listening-practice-test-1/2/

app = test(0, 0)
