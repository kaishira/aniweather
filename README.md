# Aniweather

Aniweather is a simple console weather application that features cute ASCII art of an anime girl. It allows you to check the current weather for any city directly from your terminal.

This project is just for fun and was not developed carefully.

<img width="691" alt="Screenshot 2025-01-08 at 03 30 19" src="https://github.com/user-attachments/assets/04acbb81-213d-4081-a989-b4411b597ce9" />

# Prerequisites

You need to have the `requests` library installed. You can install it using pip. Run the following command in your terminal:

```bash
pip install requests
```

Make sure you have Python and pip installed on your system before running the command.

## Installation

To install Aniweather, follow these steps:

1. **Clone the repository:**

2. **Move the `aniweather.py` file to your `bin` directory:**

   ```bash
   mv aniweather.py ~/bin/
   ```

3. **Ensure your `bin` directory is in your system's `PATH`:**

   You can add it to your `~/.bashrc` or `~/.bash_profile`:

   ```bash
   echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
   ```

4. **Reload your shell configuration:**

   ```bash
   source ~/.bashrc
   ```

## Usage

You can now run Aniweather from anywhere in your terminal by simply typing:

```bash
aniweather.py <city>
```

Replace `<city>` with the name of the city you want to check the weather for.

## Features

- Simple and easy to use
- Displays current weather information
- Cute ASCII art of an anime girl

## Customization

Feel free to edit the `aniweather.py` script to modify the displayed information or ASCII art to suit your preferences.

## License

This project is open-source and available for anyone to use and modify. Please refer to the LICENSE file for more details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

- Inspired by various console weather applications
- ASCII art created by the community
