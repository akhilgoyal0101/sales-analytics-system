def read_sales_data(filename):
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(filename, 'r', encoding=enc) as f:
                lines = f.readlines()
            # skip header and empty lines
            return [line.strip() for line in lines[1:] if line.strip()]
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print("File not found:", filename)
            return []
    return []


def parse_transactions(raw_lines):
    transactions = []

    for line in raw_lines:
        parts = line.split('|')
        if len(parts) != 8:
            continue

        tid, date, pid, pname, qty, price, cid, region = parts

        try:
            pname = pname.replace(',', ' ')
            qty = int(qty)
            price = float(price.replace(',', ''))

            transactions.append({
                'TransactionID': tid,
                'Date': date,
                'ProductID': pid,
                'ProductName': pname,
                'Quantity': qty,
                'UnitPrice': price,
                'CustomerID': cid,
                'Region': region
            })
        except:
            continue

    return transactions


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid = []
    invalid = 0
    regions = set()
    amounts = []

    for t in transactions:
        try:
            if not t['TransactionID'].startswith('T'):
                raise ValueError
            if not t['ProductID'].startswith('P'):
                raise ValueError
            if not t['CustomerID'].startswith('C'):
                raise ValueError
            if t['Quantity'] <= 0 or t['UnitPrice'] <= 0:
                raise ValueError
            if not t['Region']:
                raise ValueError

            amount = t['Quantity'] * t['UnitPrice']
            regions.add(t['Region'])
            amounts.append(amount)

            if region and t['Region'] != region:
                continue
            if min_amount and amount < min_amount:
                continue
            if max_amount and amount > max_amount:
                continue

            valid.append(t)

        except:
            invalid += 1

    print("Available Regions:", ', '.join(sorted(regions)))
    print(f"Transaction Amount Range: ₹{min(amounts):,.2f} - ₹{max(amounts):,.2f}")
    print(f"Total records parsed: {len(transactions)}")
    print(f"Invalid records removed: {invalid}")
    print(f"Valid records after cleaning: {len(valid)}")

    return valid, invalid
