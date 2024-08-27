# PROST Command Documentation

## Overview

The `prost` command is a fun and interactive tool that allows you to virtually share a beer with others from your command line. Whether you're celebrating, catching up, or just want to unwind, `cheers` makes it easy to share a moment, no matter where you are.

## Install instructions

The following examples are for POSIX systems, but you can look up further
information for Windows, or different shells at the Python [docs](https://docs.python.org/3/library/venv.html)

Ensure you have Python 3.6+ installed on your system. You can check your Python version with:

```sh
python --version
```

Clone the repository

```sh
git clone https://github.com/exocomet/prost.git
cd prost
```

It is recommended to create virtual enviroment.

```sh
python -m venv .venv
```

Then activate it:

```sh
source .venv/bin/activate
```

Then you can install `prost` within this venv.

```
pip install .
```

Prost!

```sh
prost -rf
```

## Basic Usage

The simplest way to use the `prost` command is to just type:

```bash
prost -f
```

This will generate a default toast message and simulate the sound of clinking glasses.

## Command Structure

```bash
prost [options]
```

### Common Flags

- `-u, --user <name>`: Specifies the user you want to have a beer with. You can use this flag multiple times to include multiple users.

  ```bash
  prost -u Alice -u Bob
  ```

- `-r, --random`: Generates a random toast message. Perfect for when you don't know what to say!

  ```bash
  prost -r
  ```

- `-m, --message <message>`: Allows you to customize the toast message.

  ```bash
  prost -m "Here's to new beginnings!"
  ```

- `-f, --force`: Forces the command to execute even if certain conditions are not met (e.g., no users specified, sound device not available).

  ```bash
  prost -f
  ```

- `-n, --no-sound`: Disables the clinking glass sound effect. Use this if you’re in a quiet environment.

  ```bash
  prost -n
  ```

- `-v, --version`: Displays the current version of the `prost` command.

  ```bash
  prost -v
  ```

- `-h, --help`: Displays help information about the `prost` command.

  ```bash
  prost -h
  ```

## Examples

### Example 1: Toasting with Users

To send a toast message to specific users, Alice and Bob:

```bash
prost -u Alice -u Bob -m "prost to a great weekend!"
```

### Example 2: Random Toast with No Sound

For a random toast message without the sound effect:

```bash
prost -r -n
```

### Example 3: Force Execution

To force the prost command to run even if no users are specified or other conditions are not met:

```bash
prost -f
```

### Example 4: Checking Version

To check the version of the `prost` command you are using:

```bash
prost -v
```

## Advanced Options

- `-c, --prost-type <type>`: Specifies the type of prost. Options include `beer`, `wine`, `cocktail`, etc. Default is `beer`.

  ```bash
  prost -u Alice -c wine
  ```

- `-l, --location <location>`: Adds a location to your prost, making it feel more immersive.

  ```bash
  prost -u Bob -l "on the beach"
  ```

- `-t, --time <time>`: Schedules a toast for a later time. Use a format like `10m` for 10 minutes, `2h` for 2 hours, etc.

  ```bash
  prost -u Alice -t 1h
  ```

## Exit Status

The `prost` command will exit with one of the following statuses:

- `0`: Success.
- `1`: Error in the command usage (e.g., invalid flag, missing argument).
- `2`: Command was interrupted (e.g., canceled by the user).

## Troubleshooting

If you encounter issues while using the `prost` command, here are some common solutions:

- Ensure you are using the correct flags and options.
- Use the `-h` flag to see help and understand the command better.
- Check if the `prost` command is installed properly and is in your `$PATH`.

## Conclusion

The `prost` command is a light-hearted way to stay connected with others. Whether it's a simple toast or a grand celebration, it adds a bit of fun to your terminal. So, the next time you need to raise a glass, just type `prost`!