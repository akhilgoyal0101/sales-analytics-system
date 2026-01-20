from collections import defaultdict


def calculate_total_revenue(transactions):
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)


def region_wise_sales(transactions):
    data = defaultdict(lambda: {'total_sales': 0, 'transaction_count': 0})
    total_revenue = calculate_total_revenue(transactions)

    for t in transactions:
        region = t['Region']
        data[region]['total_sales'] += t['Quantity'] * t['UnitPrice']
        data[region]['transaction_count'] += 1

    result = {}
    for r, d in data.items():
        result[r] = {
            'total_sales': d['total_sales'],
            'transaction_count': d['transaction_count'],
            'percentage': round((d['total_sales'] / total_revenue) * 100, 2)
        }

    return dict(sorted(result.items(),
                       key=lambda x: x[1]['total_sales'],
                       reverse=True))


def top_selling_products(transactions, n=5):
    products = defaultdict(lambda: {'qty': 0, 'rev': 0})

    for t in transactions:
        p = t['ProductName']
        products[p]['qty'] += t['Quantity']
        products[p]['rev'] += t['Quantity'] * t['UnitPrice']

    sorted_products = sorted(products.items(),
                             key=lambda x: x[1]['qty'],
                             reverse=True)

    return [(p, d['qty'], d['rev']) for p, d in sorted_products[:n]]


def customer_analysis(transactions):
    customers = defaultdict(lambda: {'total': 0, 'count': 0, 'products': set()})

    for t in transactions:
        c = t['CustomerID']
        customers[c]['total'] += t['Quantity'] * t['UnitPrice']
        customers[c]['count'] += 1
        customers[c]['products'].add(t['ProductName'])

    result = {}
    for c, d in customers.items():
        result[c] = {
            'total_spent': d['total'],
            'purchase_count': d['count'],
            'avg_order_value': round(d['total'] / d['count'], 2),
            'products_bought': list(d['products'])
        }

    return dict(sorted(result.items(),
                       key=lambda x: x[1]['total_spent'],
                       reverse=True))


def daily_sales_trend(transactions):
    daily = defaultdict(lambda: {'revenue': 0, 'count': 0, 'customers': set()})

    for t in transactions:
        date = t['Date']
        daily[date]['revenue'] += t['Quantity'] * t['UnitPrice']
        daily[date]['count'] += 1
        daily[date]['customers'].add(t['CustomerID'])

    return {
        d: {
            'revenue': v['revenue'],
            'transaction_count': v['count'],
            'unique_customers': len(v['customers'])
        }
        for d, v in sorted(daily.items())
    }


def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)
    peak = max(daily.items(), key=lambda x: x[1]['revenue'])
    return peak[0], peak[1]['revenue'], peak[1]['transaction_count']


def low_performing_products(transactions, threshold=10):
    products = defaultdict(lambda: {'qty': 0, 'rev': 0})

    for t in transactions:
        p = t['ProductName']
        products[p]['qty'] += t['Quantity']
        products[p]['rev'] += t['Quantity'] * t['UnitPrice']

    return sorted(
        [(p, d['qty'], d['rev']) for p, d in products.items() if d['qty'] < threshold],
        key=lambda x: x[1]
    )
