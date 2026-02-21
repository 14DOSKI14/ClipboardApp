# =============================================================================
# MAIN.PY - Clipboard History Manager
# =============================================================================
# HVA: Terminal-stil app som lagrer alt du kopierer
# HVORFOR: Mac har bare 1 clipboard - denne husker alt!
# HVORDAN: Overvåker clipboard, kategoriserer automatisk, viser i liste
#
# OPPGAVEKRAV:
#   - Arrays (numpy i categories.py)
#   - Vektoriserte beregninger (numpy arrays)
#   - If/else-tester (kategorisering, validering)
#   - For-løkker (vise historikk)
#   - Lese fra fil (JSON)
#   - Skrive til fil (JSON)
#   - Egendefinerte funksjoner
# =============================================================================

from data_handler import load_data, add_clip, clear_data, get_category
from categories import categorize

import tkinter as tk
from tkinter import messagebox


class ClipboardApp:
    """Hovedklasse for clipboard-appen"""

    def __init__(self, root):
        """Initialiserer appen"""
        self.root = root
        self.root.title("clipboard")
        self.root.geometry("850x550")
        self.root.resizable(False, False)
        self.root.configure(bg='#1e1e1e')

        # Last inn lagret data
        self.data = load_data()
        self.last_clip = ""

        # Bygg GUI og start overvåking
        self.build_gui()
        self.monitor_clipboard()

    def build_gui(self):
        """Bygger brukergrensesnittet"""

        # === HEADER ===
        header = tk.Frame(self.root, bg='#1e1e1e')
        header.pack(fill='x', padx=15, pady=10)

        tk.Label(
            header, text="clipboard-history",
            font=('Menlo', 13), fg='#ffffff', bg='#1e1e1e'
        ).pack(side='left')

        self.status = tk.Label(
            header, text="watching",
            font=('Menlo', 10), fg='#666666', bg='#1e1e1e'
        )
        self.status.pack(side='right')

        # === LISTE MED SCROLLBAR ===
        list_frame = tk.Frame(self.root, bg='#1e1e1e')
        list_frame.pack(fill='both', expand=True, padx=15, pady=5)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side='right', fill='y')

        self.text_widget = tk.Text(
            list_frame,
            font=('Menlo', 11),
            bg='#1e1e1e',
            fg='#e0e0e0',
            highlightthickness=0,
            borderwidth=0,
            wrap='none',
            cursor='arrow',
            yscrollcommand=self.scrollbar.set,
            state='disabled'
        )
        self.text_widget.pack(side='left', fill='both', expand=True)
        self.scrollbar.config(command=self.text_widget.yview)

        # === FOOTER ===
        footer = tk.Frame(self.root, bg='#1e1e1e')
        footer.pack(fill='x', padx=15, pady=10)

        clear_btn = tk.Label(
            footer, text="clear",
            font=('Menlo', 10), fg='#ff5f56', bg='#1e1e1e'
        )
        clear_btn.pack(side='left')
        clear_btn.bind('<Button-1>', lambda e: self.clear_all())

        tk.Label(
            footer, text="klikk=kopier   dobbeltklikk=vis alt",
            font=('Menlo', 9), fg='#444444', bg='#1e1e1e'
        ).pack(side='left', padx=20)

        self.counter = tk.Label(
            footer, text="",
            font=('Menlo', 10), fg='#666666', bg='#1e1e1e'
        )
        self.counter.pack(side='right')

        self.refresh_display()

    def refresh_display(self):
        """Oppdaterer listen med kopieringer"""

        self.text_widget.config(state='normal')
        self.text_widget.delete('1.0', tk.END)

        for i, clip in enumerate(self.data["history"]):
            self.create_clip_entry(clip, i)

        self.text_widget.config(state='disabled')

        cmd = len(get_category(self.data, "command"))
        code = len(get_category(self.data, "code"))
        txt = len(get_category(self.data, "text"))
        self.counter.config(text=f"{cmd} cmd   {code} code   {txt} txt")

    def create_clip_entry(self, clip, index):
        """Lager en enkelt klipp-rad"""

        cat = clip["category"]

        if cat == "command":
            cat_color = "#ff9500"
            cat_label = "cmd "
        elif cat == "code":
            cat_color = "#00aaff"
            cat_label = "code"
        else:
            cat_color = "#ffffff"
            cat_label = "text"

        preview = clip["text"].replace('\n', ' ')[:60]
        if len(clip["text"]) > 60:
            preview += "..."

        # Innhold
        self.text_widget.insert('end', f" [{cat_label}]", f'cat_{index}')
        self.text_widget.insert('end', "  ")

        padded_preview = preview.ljust(62)
        self.text_widget.insert('end', padded_preview, f'clip_{index}')

        self.text_widget.insert('end', f" {clip['time']} ", 'time')
        self.text_widget.insert('end', " copy ", f'copy_{index}')
        self.text_widget.insert('end', "\n")

        # Tynn linje
        self.text_widget.insert('end', " " + "─" * 95 + "\n", 'line')

        # Tags
        self.text_widget.tag_config('line', foreground='#2d2d2d')
        self.text_widget.tag_config('time', foreground='#555555')
        self.text_widget.tag_config(f'cat_{index}', foreground=cat_color)
        self.text_widget.tag_config(f'clip_{index}', foreground='#e0e0e0')
        self.text_widget.tag_config(f'copy_{index}', foreground='#27c93f')

        # Klikk = kopier
        self.text_widget.tag_bind(f'copy_{index}', '<Button-1>',
                                  lambda e, t=clip["text"]: self.copy_clip(t))
        self.text_widget.tag_bind(f'clip_{index}', '<Button-1>',
                                  lambda e, t=clip["text"]: self.copy_clip(t))
        self.text_widget.tag_bind(f'cat_{index}', '<Button-1>',
                                  lambda e, t=clip["text"]: self.copy_clip(t))

        # Dobbeltklikk = vis alt
        self.text_widget.tag_bind(f'clip_{index}', '<Double-Button-1>',
                                  lambda e, c=clip: self.show_full_text(c))
        self.text_widget.tag_bind(f'cat_{index}', '<Double-Button-1>',
                                  lambda e, c=clip: self.show_full_text(c))

    def show_full_text(self, clip):
        """Viser hele teksten i popup"""

        popup = tk.Toplevel(self.root)
        popup.title(f"{clip['category']} - {clip['time']}")
        popup.geometry("600x400")
        popup.configure(bg='#1e1e1e')
        popup.resizable(False, False)

        frame = tk.Frame(popup, bg='#1e1e1e')
        frame.pack(fill='both', expand=True, padx=15, pady=15)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')

        text = tk.Text(
            frame,
            font=('Menlo', 11),
            bg='#2d2d2d',
            fg='#e0e0e0',
            wrap='word',
            padx=12,
            pady=12,
            yscrollcommand=scrollbar.set
        )
        text.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=text.yview)

        text.insert('1.0', clip["text"])
        text.config(state='disabled')

        btn = tk.Button(
            popup, text="kopier og lukk",
            font=('Menlo', 11),
            bg='#2d2d2d',
            fg='#27c93f',
            command=lambda: self.copy_and_close(clip["text"], popup)
        )
        btn.pack(pady=(0, 15))

    def copy_and_close(self, text, popup):
        """Kopierer og lukker popup"""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.last_clip = text
        popup.destroy()

        self.status.config(text="copied", fg='#27c93f')
        self.root.after(1000, lambda: self.status.config(
            text="watching", fg='#666666'
        ))

    def copy_clip(self, text):
        """Kopierer tekst til clipboard"""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.last_clip = text

        self.status.config(text="copied", fg='#27c93f')
        self.root.after(1000, lambda: self.status.config(
            text="watching", fg='#666666'
        ))

    def monitor_clipboard(self):
        """Overvåker clipboard for nytt innhold"""
        try:
            current = self.root.clipboard_get()

            if current and current != self.last_clip:
                self.last_clip = current
                category = categorize(current)

                if category:
                    self.data = add_clip(self.data, current, category)
                    self.refresh_display()

                    self.status.config(text="saved", fg='#27c93f')
                    self.root.after(800, lambda: self.status.config(
                        text="watching", fg='#666666'
                    ))
        except:
            pass

        self.root.after(500, self.monitor_clipboard)

    def clear_all(self):
        """Sletter all historikk"""
        if messagebox.askyesno("bekreft", "slette all historikk?"):
            self.data = clear_data()
            self.refresh_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardApp(root)
    root.mainloop()