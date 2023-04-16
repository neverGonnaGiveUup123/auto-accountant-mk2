class readTrialBalance:
    import pytesseract
    from PIL import Image
    import json
    import os

    pytesseract.pytesseract.tesseract_cmd = (
        "C:\Program Files\Tesseract-OCR/tesseract.exe"
    )

    def __init__(self, img) -> None:
        self.trial_balance_img = self.Image.open(img)

    @classmethod
    def get_pytesseract_version(cls):
        return cls.pytesseract.get_tesseract_version()

    def get_classifications(self):
        with open("src/data/currentAssets.json", "r") as file:
            self.currentAssetsJson = self.json.load(file)
            # [self.currentAssetsJson.update({i, (0,0,0)}) for i in self.currentAssetsJson.keys()]
        self.os.remove("src/data/currentAssets.json")

        with open("src/data/nonCurrentAssets.json", "r") as file:
            self.non_current_assets = self.json.load(file)
        self.os.remove("src/data/nonCurrentAssets.json")

        with open("src/data/nonCurrentLiabilities.json", "r") as file:
            self.non_current_liablities = self.json.load(file)
        self.os.remove("src/data/nonCurrentLiabilities.json")

        with open("src/data/currentLiabilities.json", "r") as file:
            self.current_liabilties = self.json.load(file)
        self.os.remove("src/data/currentLiabilities.json")

        with open("src/data/equity.json", "r") as file:
            self.equity = self.json.load(file)
        self.os.remove("src/data/equity.json")

    def check_errors(self):
        self.string_trial_balance = self.pytesseract.image_to_string(
            self.trial_balance_img
        )
        self.string_trial_balance = self.string_trial_balance.replace("|", " ")
        self.string_trial_balance = self.string_trial_balance.replace("(", " ")
        self.string_trial_balance = self.string_trial_balance.replace(")", " ")
        self.string_trial_balance = self.string_trial_balance.replace("[", " ")
        self.string_trial_balance = self.string_trial_balance.replace("]", " ")
        self.string_trial_balance = self.string_trial_balance.replace(".", "")
        self.string_trial_balance = self.string_trial_balance.replace(",", "")
        print(self.string_trial_balance)

    def assign_money(self):
        for j in [
            self.currentAssetsJson,
            self.non_current_assets,
            self.current_liabilties,
            self.non_current_liablities,
            self.equity,
        ]:
            for x in j.keys():
                j[x] = [0,0,0]
            exceptions_list = []
            [exceptions_list.append(i) for i in j.keys()]
            temp_list = []
            for words in self.string_trial_balance.split():
                temp_list.append(words)
            # print(temp_list)
            loop_list = [4, 3, 2, 1]

            if exceptions_list[0] != "Loan":
                for words in temp_list:
                    for items in j.keys():
                        for i in loop_list:
                            if (
                                words.title() == items.title()
                                and temp_list[temp_list.index(words) + i].isdigit()
                            ):
                                j[items][0] = temp_list[temp_list.index(words) + i]
            else:
                for words in temp_list:
                    for items in j.keys():
                        for i in loop_list:
                            if (
                                words.title() == items.title()
                                and temp_list[temp_list.index(words) + i][-1] == "0"
                            ):
                                j[items][0] = temp_list[temp_list.index(words) + i]

            print("***")
            print(j)
        for object, path in [
            (self.currentAssetsJson, "src/data/currentAssets.json"),
            (self.non_current_assets, "src/data/nonCurrentAssets.json"),
            (self.current_liabilties, "src/data/currentLiabilities.json"),
            (self.non_current_liablities, "src/data/nonCurrentLiabilities.json"),
            (self.equity, "src/data/equity.json"),
        ]:
            with open(path, "w") as file:
                self.json.dump(object, file)
