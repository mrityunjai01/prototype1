def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    try:
        res = requests.get("https://api.fixer.io/latest", params={"base": base, "symbols": other})
        if res.status_code != 200:
            raise Exception("ERROR:  requeAPIst unsuccessful.")
        data = res.json()
        rate = data["rates"][other]
        print(f"1 {base} is equal to {rate} {other}")
    except:
        print("Oops, seems there's an error")
    

if __name__ == "__main__":
    main()