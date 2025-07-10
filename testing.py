import requests
import time
from collections import Counter
from statistics import mean

# Endpoints
PRODUCTS_URL = "http://192.168.49.2:31066/products"
USERS_URL = "http://192.168.49.2:31728/users"

# Number of requests to send to each endpoint
NUM_REQUESTS = 5000

def test_endpoint(endpoint):
    print(f"\n🔍 Testing endpoint: {endpoint}\n{'='*50}")
    responses = []
    latencies = []
    failures = 0

    for i in range(NUM_REQUESTS):
        try:
            start = time.time()
            response = requests.get(endpoint, timeout=5)
            duration = round((time.time() - start) * 1000, 2)  # in ms

            if response.status_code == 200:
                responses.append(response.text.strip())
                latencies.append(duration)
                print(f"✅ {i+1:02d}: Success ({duration} ms)")
            else:
                failures += 1
                print(f"⚠️ {i+1:02d}: Non-200 ({response.status_code})")
        except requests.exceptions.RequestException as e:
            failures += 1
            print(f"❌ {i+1:02d}: Request failed - {e}")

        time.sleep(0.1)  # Small delay between requests

    # Analyze
    print(f"\n📊 Summary for {endpoint}")
    print(f"Total Requests: {NUM_REQUESTS}")
    print(f"Success: {NUM_REQUESTS - failures}")
    print(f"Failures: {failures}")
    if latencies:
        print(f"Average Response Time: {mean(latencies):.2f} ms")
        print(f"Min Response Time: {min(latencies):.2f} ms")
        print(f"Max Response Time: {max(latencies):.2f} ms")

    count = Counter(responses)
    print(f"\nTop 5 unique responses:")
    for i, (key, val) in enumerate(count.most_common(5), start=1):
        print(f"{i}. [{val} times] → {key}")

    print("\n" + "-"*60 + "\n")

# Run the test
test_endpoint(PRODUCTS_URL)
test_endpoint(USERS_URL)




