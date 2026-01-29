def extract_features(packet):
    return [
        packet["size"],
        packet["proto"]
    ]
