class parent:
    import json

    def get_data(self):
        with open("src/data/currentAssets.json", "r") as file:
            self.current_assets = self.json.load(file)
        with open("src/data/nonCurrentAssets.json", "r") as file:
            self.non_current_assets = self.json.load(file)
        with open("src/data/nonCurrentLiabilities.json", "r") as file:
            self.non_current_liablities = self.json.load(file)
        with open("src/data/currentLiabilities.json", "r") as file:
            self.current_liabilties = self.json.load(file)
        with open("src/data/equity.json", "r") as file:
            self.equity = self.json.load(file)

    def check_columns(self):
        pass
