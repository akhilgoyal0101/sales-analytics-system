from utils.file_handler import read_sales_data, parse_transactions, validate_and_filter
from utils.data_processor import (
    calculate_total_revenue,
    region_wise_sales,
    top_selling_products,
    customer_analysis,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products
)
from utils.api_handler import (
    fetch_all_products,
    create_product_mapping,
    enrich_sales_data,
    save_enriched_data
)
from datetime import datetime


def generate_sales_report(transactions, enriched):
    with open('output/sales_report.txt', 'w', encoding='utf-8') as f:
        f.write("SALES ANALYTICS REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"Records Processed: {len(transactions)}\n\n")

        total = calculate_total_revenue(transactions)
        f.write(f"Total Revenue: ₹{total:,.2f}\n")
        f.write(f"Average Order Value: ₹{total / len(transactions):,.2f}\n\n")

        f.write("REGION-WISE PERFORMANCE\n")
        f.write("-" * 40 + "\n")
        for r, d in region_wise_sales(transactions).items():
            f.write(f"{r}: ₹{d['total_sales']:,.2f} ({d['percentage']}%)\n")

        f.write("\nTOP 5 PRODUCTS\n")
        for p in top_selling_products(transactions):
            f.write(f"{p[0]} | Qty: {p[1]} | ₹{p[2]:,.2f}\n")

        f.write("\nTOP 5 CUSTOMERS\n")
        customers = customer_analysis(transactions)
        for i, (c, d) in enumerate(list(customers.items())[:5], 1):
            f.write(f"{i}. {c} | ₹{d['total_spent']:,.2f} | Orders: {d['purchase_count']}\n")

        f.write("\nDAILY SALES TREND\n")
        for d, v in daily_sales_trend(transactions).items():
            f.write(f"{d} | ₹{v['revenue']:,.2f} | {v['transaction_count']} txns | {v['unique_customers']} customers\n")

        peak = find_peak_sales_day(transactions)
        f.write(f"\nPeak Sales Day: {peak[0]} | ₹{peak[1]:,.2f} | {peak[2]} txns\n")

        low = low_performing_products(transactions)
        if low:
            f.write("\nLow Performing Products:\n")
            for p in low:
                f.write(f"{p[0]} | Qty: {p[1]} | ₹{p[2]:,.2f}\n")

        success = sum(1 for t in enriched if t['API_Match'])
        f.write(f"\nAPI Enrichment Success Rate: {(success / len(enriched)) * 100:.2f}%\n")


def main():
    print("SALES ANALYTICS SYSTEM")

    raw = read_sales_data('data/sales_data.txt')
    parsed = parse_transactions(raw)

    valid, invalid = validate_and_filter(parsed)

    products = fetch_all_products()
    mapping = create_product_mapping(products)

    enriched = enrich_sales_data(valid, mapping)
    save_enriched_data(enriched)

    generate_sales_report(valid, enriched)

    print("Process completed successfully")


if __name__ == "__main__":
    main()
