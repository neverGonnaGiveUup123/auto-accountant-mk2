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
    
    def dump_data(self):
        for object, path in [
            (self.currentAssets, "src/data/currentAssets.json"),
            (self.nonCurrentAssets, "src/data/nonCurrentAssets.json"),
            (self.currentLiabilties, "src/data/currentLiabilities.json"),
            (self.nonCurrentLiablities, "src/data/nonCurrentLiabilities.json"),
            (self.equity, "src/data/equity.json"),
        ]:
            with open(path, "w") as file:
                self.json.dump(object, file)

    def check_columns(self):
        for data in [self.currentAssets, self.nonCurrentAssets, self.currentLiabilties, self.nonCurrentLiablities, self.equity]:
            columns = 0
            for items in data:
                if isinstance(data[items][0], str):
                    columns += 1
            
            if columns <= 1:
                for items in data:
                    data[items][1] = data[items][0]
                    data[items][0] = 0
            print(columns)
            print(data)

e = parent()
e.get_data()
e.check_columns()
e.dump_data()