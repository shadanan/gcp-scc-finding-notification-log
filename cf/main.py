#!/usr/bin/env python3
import base64
import json


def process_notification(event, context):
    """Process the finding notification."""
    pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
    finding = json.loads(pubsub_message)["finding"]
    print(f"Encoded Finding: {event['data']}")
    print(f"Decoded Finding: {finding}")
