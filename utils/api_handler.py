import requests


def fetch_all_products():
    try:
        response = requests.get('https://dummyjson.com/products?limit=100')
        return response.json()['products']
    except:
        return []


def create_product_mapping(products):
    return {
        p['id']: {
            'category': p['category'],
            'brand': p['brand'],
            'rating': p['rating']
        }
        for p in products
    }


def enrich_sales_data(transactions, mapping):
    enriched = []

    for t in transactions:
        t = t.copy()
        try:
            pid = int(t['ProductID'][1:])
            api = mapping.get(pid)

            if api:
                t.update({
                    'API_Category': api['category'],
                    'API_Brand': api['brand'],
                    'API_Rating': api['rating'],
                    'API_Match': True
                })
            else:
                raise ValueError
        except:
            t.update({
                'API_Category': None,
                'API_Brand': None,
                'API_Rating': None,
                'API_Match': False
            })

        enriched.append(t)

    return enriched


def save_enriched_data(enriched, filename='data/enriched_sales_data.txt'):
    headers = enriched[0].keys()

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('|'.join(headers) + '\n')
        for t in enriched:
            row = [str(t[h]) if t[h] is not None else '' for h in headers]
            f.write('|'.join(row) + '\n')
