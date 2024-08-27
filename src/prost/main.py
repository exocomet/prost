#!/usr/bin/env python3

import argparse
import random
import time
import sys

# Sample random messages
random_messages = [
    "Prost",
    "Cheers to good health!",
    "Here's to great friends and even better times!",
    "May your drinks be cold and your conversations warm!",
    "To a night we won't remember, with friends we'll never forget!",
    "Raise your glass to new adventures!",
    "Skål!",
    "Das Flüssige muss ins Durstige.",
]

def cheers(users=None, message=None, random_message=False, force=False, no_sound=False, cheers_type="beer", location=None, schedule=None):
    if random_message:
        message = random.choice(random_messages)
    
    message = message or random_messages[0]

    if schedule:
        try:
            delay = int(schedule[:-1])
            if schedule.endswith('m'):
                delay *= 60
            elif schedule.endswith('h'):
                delay *= 3600
            print(f"Scheduling toast in {schedule}...")
            time.sleep(delay)
        except ValueError:
            print("Invalid time format. Please use 'm' for minutes or 'h' for hours.")
            sys.exit(1)

    # Display the cheers message
    if users:
        user_str = ', '.join(users)
        print(f"{message} to {user_str}!")
    else:
        if not force:
            print("No users specified. Use -f to force a toast without specifying users.")
            sys.exit(1)
        print(message)

    if location:
        print(f"Location: {location}")

    print(f"Cheers with a {cheers_type}!")

    if not no_sound:
        print("*Clink*")

def main():
    parser = argparse.ArgumentParser(description="Have a virtual beer with others.")
    
    parser.add_argument('-u', '--user', action='append', help="Specify users to toast with.")
    parser.add_argument('-m', '--message', help="Customize your toast message.")
    parser.add_argument('-r', '--random', action='store_true', help="Generate a random toast message.")
    parser.add_argument('-f', '--force', action='store_true', help="Force the toast even if no users are specified.")
    parser.add_argument('-n', '--no-sound', action='store_true', help="Disable the clinking sound.")
    parser.add_argument('-c', '--cheers-type', default="beer", help="Specify the type of drink (default: beer).")
    parser.add_argument('-l', '--location', help="Add a location to your cheers.")
    parser.add_argument('-t', '--time', help="Schedule the toast for later (e.g., 10m, 2h).")
    parser.add_argument('-v', '--version', action='version', version='cheers 1.0', help="Show the version of the cheers command.")

    args = parser.parse_args()
    
    cheers(users=args.user,
           message=args.message,
           random_message=args.random,
           force=args.force,
           no_sound=args.no_sound,
           cheers_type=args.cheers_type,
           location=args.location,
           schedule=args.time)

if __name__ == "__main__":
    main()
