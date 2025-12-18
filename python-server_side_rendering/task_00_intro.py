#!/usr/bin/python3
"""Module for generating personalized invitation files."""


def generate_invitations(template, attendees):
    """Generates personalized invitation files from a template."""
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template

        # Replace placeholders with values or "N/A" if missing
        name = attendee.get("name") if attendee.get("name") else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        output = output.replace("{name}", name)
        output = output.replace("{event_title}", event_title)
        output = output.replace("{event_date}", event_date)
        output = output.replace("{event_location}", event_location)

        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(output)
