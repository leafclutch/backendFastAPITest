@app.get("/print-name/{name}")
def print_name(name: str):
    print(f"User name is: {name}")
    return {"name": name}