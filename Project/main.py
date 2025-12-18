import tkinter as tk
from tkinter import ttk, messagebox
import threading
from rates_manager import RatesManager
from converter_engine import ConversionEngine


class CurrencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BNR Currency Converter")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # logica modulelor
        self.manager = RatesManager()
        self.engine = ConversionEngine()
        self.current_rates = {}

        # setup pt ui
        self._setup_ui()

        # auto-update la startup (background thread)
        self.status_var.set("Initializing data...")
        threading.Thread(target=self._initial_fetch, daemon=True).start()

    def _setup_ui(self):
        # styles
        style = ttk.Style()
        style.configure("TButton", padding=6)
        style.configure("TLabel", font=("Arial", 10))

        # main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # row 1: Amount
        ttk.Label(main_frame, text="Amount:").grid(row=0, column=0, sticky="w", pady=5)
        self.amount_entry = ttk.Entry(main_frame)
        self.amount_entry.grid(row=0, column=1, sticky="ew", pady=5)
        self.amount_entry.insert(0, "1")

        # row 2: From Currency
        ttk.Label(main_frame, text="From:").grid(row=1, column=0, sticky="w", pady=5)
        self.combo_from = ttk.Combobox(main_frame, state="readonly")
        self.combo_from.grid(row=1, column=1, sticky="ew", pady=5)

        # row 3: To Currency
        ttk.Label(main_frame, text="To:").grid(row=2, column=0, sticky="w", pady=5)
        self.combo_to = ttk.Combobox(main_frame, state="readonly")
        self.combo_to.grid(row=2, column=1, sticky="ew", pady=5)

        # row 4: Convert Button
        self.btn_convert = ttk.Button(main_frame, text="CONVERT", command=self.do_convert)
        self.btn_convert.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")

        # row 5: Result Display
        self.result_var = tk.StringVar(value="Result: -")
        lbl_result = ttk.Label(main_frame, textvariable=self.result_var, font=("Arial", 14, "bold"),
                               foreground="#2c3e50")
        lbl_result.grid(row=4, column=0, columnspan=2, pady=10)

        # separator
        ttk.Separator(main_frame, orient='horizontal').grid(row=5, column=0, columnspan=2, sticky="ew", pady=10)

        # row 6: Status & Refresh
        self.status_var = tk.StringVar(value="Waiting for data...")
        lbl_status = ttk.Label(main_frame, textvariable=self.status_var, font=("Arial", 8), foreground="gray")
        lbl_status.grid(row=6, column=0, sticky="w")

        btn_refresh = ttk.Button(main_frame, text="Refresh Rates", command=self.refresh_rates)
        btn_refresh.grid(row=6, column=1, sticky="e")

        # configurez grid weights
        main_frame.columnconfigure(1, weight=1)

    def _initial_fetch(self):
        # ruleaza cand pornim aplicatia
        rates, msg, is_error = self.manager.get_rates()
        # schedule UI update on main thread
        self.root.after(0, lambda: self._update_ui_after_fetch(rates, msg, is_error))

    def refresh_rates(self):
        # Ruleaza cand dam click pe refresh
        self.status_var.set("Fetching from BNR...")
        self.btn_convert.config(state="disabled")

        def worker():
            try:
                rates, msg, is_error = self.manager.force_refresh()
                self.root.after(0, lambda: self._update_ui_after_fetch(rates, msg, is_error))
            except Exception as e:
                self.root.after(0, lambda: self._update_ui_after_fetch({}, f"Error: {str(e)}", True))

        threading.Thread(target=worker, daemon=True).start()

    def _update_ui_after_fetch(self, rates, msg, is_error):
        # apelata de thread-uri pt update GUI safely"""
        self.btn_convert.config(state="normal")
        self.status_var.set(msg)

        if is_error and not rates:
            messagebox.showerror("Network Error", "Could not fetch rates and no cache found.")
            return

        self.current_rates = rates

        # populam comboboxes
        currency_list = sorted(list(rates.keys()))

        # salvam optiunile/setarile selectate inainte de a le sterge
        curr_from = self.combo_from.get()
        curr_to = self.combo_to.get()

        self.combo_from['values'] = currency_list
        self.combo_to['values'] = currency_list

        # defaults
        if not curr_from and "EUR" in currency_list:
            self.combo_from.set("EUR")
        elif curr_from in currency_list:
            self.combo_from.set(curr_from)

        if not curr_to and "RON" in currency_list:
            self.combo_to.set("RON")
        elif curr_to in currency_list:
            self.combo_to.set(curr_to)

    def do_convert(self):
        try:
            amt_str = self.amount_entry.get()
            if not amt_str:
                return

            try:
                amount = float(amt_str)
            except ValueError:
                messagebox.showwarning("Input Error", "Please enter a valid number.")
                return

            c_from = self.combo_from.get()
            c_to = self.combo_to.get()

            if not c_from or not c_to:
                return

            result = self.engine.convert(amount, c_from, c_to, self.current_rates)
            self.result_var.set(f"{amount} {c_from} = {result} {c_to}")

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Critical Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyApp(root)
    root.mainloop()
