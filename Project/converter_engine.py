class ConversionEngine:
    @staticmethod
    def convert(amount, currency_from, currency_to, rates_map):
        # validare
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if currency_from not in rates_map:
            raise ValueError(f"Currency {currency_from} not found.")

        if currency_to not in rates_map:
            raise ValueError(f"Currency {currency_to} not found.")

        # logica: convertim FROM -> RON -> TO
        rate_from = rates_map[currency_from]  # transform moneda de start in RON
        rate_to = rates_map[currency_to]  # transform acel RON in moneda finala

        # exemplu: 100 EUR to USD
        # 100 * 4.97 (RON value of EUR) = 497 RON
        # 497 / 4.50 (RON value of USD) = 110.44 USD

        val_in_ron = amount * rate_from
        final_val = val_in_ron / rate_to

        return round(final_val, 4)
