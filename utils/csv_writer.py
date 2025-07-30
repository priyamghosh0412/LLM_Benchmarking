import csv

def write_csv(results, filename="benchmark_results.csv"):
    headers = [
        "model", "load_time", "first_token", "avg_token",
        "tokens_per_min", "verdict", "runnable"
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:  # <-- fix here
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(results)
