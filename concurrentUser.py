# ThreadPoolExecutor

import requests
import time
from collections import Counter
from statistics import mean
from concurrent.futures import ThreadPoolExecutor, as_completed

PRODUCTS_URL = "http://192.168.49.2:31066/products"
USERS_URL = "http://192.168.49.2:31728/users"

NUM_REQUESTS = 5000
MAX_WORKERS = 200  # Number of concurrent threads

def make_request(endpoint):
    try:
        start = time.time()
        response = requests.get(endpoint, timeout=5)
        duration = round((time.time() - start) * 1000, 2)
        if response.status_code == 200:
            return (response.text.strip(), duration, None)
        else:
            return (None, duration, f"Non-200 ({response.status_code})")
    except Exception as e:
        return (None, None, str(e))

def test_endpoint(endpoint):
    print(f"\n🔍 Testing endpoint: {endpoint} with {NUM_REQUESTS} concurrent requests")

    responses = []
    latencies = []
    errors = Counter()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(make_request, endpoint) for _ in range(NUM_REQUESTS)]
        for i, future in enumerate(as_completed(futures), 1):
            result, duration, error = future.result()
            if result:
                responses.append(result)
                latencies.append(duration)
                if i % 100 == 0:
                    print(f"✅ {i}: OK ({duration} ms)")
            else:
                errors[error] += 1
                if i % 100 == 0:
                    print(f"❌ {i}: Failed ({error})")

    # Summary
    print(f"\n📊 Summary for {endpoint}")
    print(f"Total Requests: {NUM_REQUESTS}")
    print(f"Success: {len(responses)}")
    print(f"Failures: {NUM_REQUESTS - len(responses)}")
    if latencies:
        print(f"Average Latency: {mean(latencies):.2f} ms")
        print(f"Min Latency: {min(latencies):.2f} ms")
        print(f"Max Latency: {max(latencies):.2f} ms")

    print(f"\nTop 5 Responses:")
    for i, (resp, count) in enumerate(Counter(responses).most_common(5), 1):
        print(f"{i}. [{count} times] → {resp}")

    if errors:
        print(f"\nErrors Breakdown:")
        for err, count in errors.items():
            print(f"{err}: {count}")

    print("\n" + "-"*60 + "\n")

# Run the test
test_endpoint(PRODUCTS_URL)
test_endpoint(USERS_URL)



# In load testing, latency refers to the delay between a user's request and the system's response

# 📊 Summary for http://192.168.49.2:31066/products
# Total Requests: 5000
# Success: 5000
# Failures: 0
# Average Latency: 261.45 ms
# Min Latency: 4.07 ms
# Max Latency: 1278.54 ms