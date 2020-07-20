try:
    from datascience import Table
    print("The module `datascience` is installed on your project.")
except ModuleNotFoundError:
    import sys
    print("The module `datascience` is not installed.")
    print("To install it for your CoCalc project, use the [(+) New] menu to")
    print("open a Linux terminal.")
    print("Then copy-paste the line below into the terminal and hit [Enter].")
    print()
    print(f"{sys.executable} -m pip install --user datascience")