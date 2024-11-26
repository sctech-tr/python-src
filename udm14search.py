import webbrowser

input_str = input("please enter a search query: ")
if input_str is None:
    print("please enter a valid search query.")
else:
    print(f"searching for {input_str}...")
    final_query = input_str.replace(" ", "+")
    url = f"https://www.google.com/search?q={final_query}&udm=14"
    webbrowser.open(url)

