def print_report(errors):
    error_count = 0
    print("===== Prüfbericht =====")
    for error in errors:
        if "hat einen kleinen Leitungsquerschnitt." not in error:
            print(f'⚠  {error}')
            error_count +=1
    print(f'=======================\nFehler: {error_count}')