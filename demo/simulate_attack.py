import random
from datetime import datetime, timezone


def simulate_attack(unauthorized=True):
    """
    Simulates a cloud key access event.
    Returns a dictionary representing the event.
    """

    caller_identities = [
        "service-account-a",
        "service-account-b",
        "service-account-c"
    ]

    key_owners = [
        "service-account-a",
        "service-account-b"
    ]

    caller_identity = random.choice(caller_identities)

    if unauthorized:
        key_owner = random.choice(
            [owner for owner in key_owners if owner != caller_identity]
        )
    else:
        key_owner = caller_identity

    event = {
        "caller_identity": caller_identity,
        "key_owner": key_owner,
        "resource": "kms-key-123",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "region": random.choice(["us-central1", "europe-west1"]),
        "authorized": not unauthorized
    }

    return event


if __name__ == "__main__":
    event = simulate_attack(unauthorized=True)
    print("Simulated Cloud Access Event:")
    for key, value in event.items():
        print(f"{key}: {value}")

