from core.readTrialBalance import readTrialBalance

trial_balance = readTrialBalance("testTB2.png")
trial_balance.get_pytesseract_version()
trial_balance.get_classifications()
trial_balance.check_errors()
trial_balance.assign_money()