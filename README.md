# Fantalega Project

Fantalega is a web application built using Django, designed to manage and enhance the experience of fantasy leagues. This README provides an overview of the project, setup instructions, and usage guidelines.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fantalega
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file in the root directory and add your configuration settings.

5. Run database migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. You can create and manage fantasy leagues, users, trophies, and payments through the web interface.

## Project Structure

```
fantalega/
├── .env
├── manage.py
├── requirements.txt
├── README.md
├── fantalega/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   ├── trophies/
│   ├── payments/
│   └── media/
├── templates/
│   └── base.html
└── static/
    ├── css/
    ├── js/
    └── fonts/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.