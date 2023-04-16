class parent:
    import json

    def get_data(self):
        with open("src/data/currentAssets.json", "r") as file:
            self.currentAssets = self.json.load(file)
        with open("src/data/nonCurrentAssets.json", "r") as file:
            self.nonCurrentAssets = self.json.load(file)
        with open("src/data/nonCurrentLiabilities.json", "r") as file:
            self.nonCurrentLiablities = self.json.load(file)
        with open("src/data/currentLiabilities.json", "r") as file:
            self.currentLiabilties = self.json.load(file)
        with open("src/data/equity.json", "r") as file:
            self.equity = self.json.load(file)

    def check_columns(self):
        for i in [self.currentAssets, self.nonCurrentAssets, self.currentLiabilties, self.nonCurrentLiablities, self.equity]:
            columns = 0
            for j in i:
                if isinstance(i[j][0], str):
                    columns += 1
            print(columns)

e = parent()
e.get_data()
e.check_columns()