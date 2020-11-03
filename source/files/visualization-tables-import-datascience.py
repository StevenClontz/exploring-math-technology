try:
    from datascience import Table
    print("The module `datascience` is installed on your project.")
except ModuleNotFoundError:
    import sys
    print("The module `datascience` is not installed.")
    print("To install it for your CoCalc project, do the following:"
    print("1. Use the [(+) New] menu to open a Linux terminal.")
    print("2. Copy-paste the line below into the terminal and hit [Enter].")
    print()
    print(f"{sys.executable} -m pip install --user datascience")
    print()
    print("3. Return to this notebook and \"Restart Kernel\".")
    print("4. Re-run this Code cell.")