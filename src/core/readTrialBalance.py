class readTrialBalance:
    import pytesseract
    from PIL import Image
    import json
    from core.assignMoney import assign_money

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
            self.current_assets = self.json.load(file)

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

    def assign_values(self):
        self.assign_money(data=self.current_assets, iterable=self.string_trial_balance)