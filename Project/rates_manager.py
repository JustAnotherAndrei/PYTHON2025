import requests
import xml.etree.ElementTree as ET
import json
import os
import datetime

# config
BNR_URL = "https://www.bnr.ro/nbrfxrates.xml"
CACHE_FILE = "rates_cache.json"


class RatesManager:
    def __init__(self):
        self.rates = {}
        self.last_updated = None
        self.data_date = None

    def get_rates(self):
        # 1. dam load la cache mai intai
        cache_data = self._load_cache()

        should_fetch = True
        if cache_data:
            # verificam daca cache-ul e mai recent decat 24h
            last_fetch_ts = cache_data.get("timestamp", 0)
            if datetime.datetime.now().timestamp() - last_fetch_ts < 86400:  # 24 hours
                should_fetch = False
                self.rates = cache_data["rates"]
                self.data_date = cache_data.get("date_str", "Unknown")
                return self.rates, f"Loaded from cache ({self.data_date})", False

        # 2. facem 'fetch' din web daca e trebuie
        if should_fetch:
            try:
                print("Fetching live rates from BNR...")
                return self.force_refresh()
            except Exception as e:
                # 3. fallback: daca web-ul crapa, folosim cache-ul chiar daca e vechi
                if cache_data:
                    self.rates = cache_data["rates"]
                    self.data_date = cache_data.get("date_str", "Unknown")
                    return self.rates, f"Offline: Using cached rates ({self.data_date})", True
                else:
                    return {}, "Error: No internet and no cache available.", True

        return self.rates, "Ready", False

    def force_refresh(self):
        try:
            response = requests.get(BNR_URL, timeout=5)
            response.raise_for_status()

            # parsam XML-ul
            rates, date_str = self._parse_bnr_xml(response.content)

            # actualizam starea interna
            self.rates = rates
            self.data_date = date_str

            # salvam in cache
            self._save_cache(rates, date_str)

            return rates, f"Updated live ({date_str})", False
        except Exception as e:
            raise e

    def _parse_bnr_xml(self, xml_content):
        root = ET.fromstring(xml_content)

        # BNR XML foloseste de obicei un namespace, e.g. {http://www.bnr.ro/xsd}
        # din simplitate, vom ignora namespace-urile, uitandu-ne doar la tagurile locale

        rates = {"RON": 1.0}  # Pivot currency
        date_str = datetime.date.today().strftime("%Y-%m-%d")

        # cautam Cube-ul cu data
        for child in root:
            if "Body" in child.tag:
                for cube in child:
                    if "Cube" in cube.tag:
                        date_str = cube.get("date", date_str)
                        for rate_node in cube:
                            if "Rate" in rate_node.tag:
                                currency = rate_node.get("currency")
                                multiplier = int(rate_node.get("multiplier", "1"))
                                value = float(rate_node.text)

                                # normalizam: stocam o valoare de unitate
                                normalized_rate = value / multiplier
                                rates[currency] = normalized_rate
        return rates, date_str

    def _save_cache(self, rates, date_str):
        data = {
            "timestamp": datetime.datetime.now().timestamp(),
            "date_str": date_str,
            "rates": rates
        }
        with open(CACHE_FILE, "w") as f:
            json.dump(data, f)

    def _load_cache(self):
        if not os.path.exists(CACHE_FILE):
            return None
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except:
            return None
