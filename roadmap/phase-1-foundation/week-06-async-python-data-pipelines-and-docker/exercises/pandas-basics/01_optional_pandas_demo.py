"""
Week 06 - Optional Pandas Demo

This file is optional because Pandas may not be installed in every environment.
"""


def main():
    """Try a tiny Pandas example if the library is available."""
    try:
        import pandas as pd
    except ImportError:
        print("Pandas is not installed in this environment.")
        print("If you want to try this demo, install pandas and run the file again.")
        return

    data_frame = pd.DataFrame(
        [
            {"user_name": "Asha", "minutes": 15},
            {"user_name": "Ravi", "minutes": 30},
            {"user_name": "Asha", "minutes": 20},
        ]
    )

    grouped = data_frame.groupby("user_name", as_index=False)["minutes"].sum()
    print(grouped)


if __name__ == "__main__":
    main()
