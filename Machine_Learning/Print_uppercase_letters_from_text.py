import requests
from bs4 import BeautifulSoup

def print_grid(url: str):
    """
    Fetches a published Google Doc, parses the character grid table,
    and prints the hidden uppercase letter message.
    """
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # --- Parse the table ---
    grid = {}

    table = soup.find("table")
    if not table:
        print("No table found in the document.")
        return

    rows = table.find_all("tr")

    for row in rows[1:]:  # Skip header row (x-coordinate | Character | y-coordinate)
        cols = row.find_all("td")
        if len(cols) >= 3:
            x_text = cols[0].get_text(strip=True)
            char   = cols[1].get_text(strip=True)
            y_text = cols[2].get_text(strip=True)

            # Skip rows where values aren't integers (e.g. empty rows)
            if not x_text.isdigit() or not y_text.isdigit():
                continue

            x = int(x_text)
            y = int(y_text)

            grid[(x, y)] = char if char else " "

    if not grid:
        print("No grid data found.")
        return

    # --- Determine grid dimensions ---
    max_x = max(x for x, y in grid)
    max_y = max(y for x, y in grid)

    # --- Print the grid ---
    # y increases downward (row), x increases rightward (column)
    for y in range(max_y + 1):
        row_str = ""
        for x in range(max_x + 1):
            row_str += grid.get((x, y), " ")  # fill blanks with space
        print(row_str)


# --- Run it ---
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_grid(url)