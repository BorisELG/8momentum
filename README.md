# 8momentum website

Welcome to my personal website, 8momentum.

## Table of Contents

-   [Features](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#features)
-   [Installation](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#installation)
-   [Deployment](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#deployment)
-   [Technology Stack](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#technology-stack)
-   [Why Wagtail?](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#why-wagtail)
-   [Contributing](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#contributing)
-   [License](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#license)

## Features

-   **Blog:** blog with chaotic blog posts.
-   **Media gallery:** photos and songs in dedicated galleries.

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2.  **Create Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create Superuser (Admin):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000` in your browser to access the local development server.


## Deployment

This blog is hosted on a bare metal server (DietPi) and served via Caddy.

## Technology Stack

-   **Wagtail CMS:** Empowering creativity with a Django-based CMS, providing an amazing Python experience.
-   **DietPi & Caddy:** Hosted on a lightweight Debian-based OS with Caddy as the web server.
-   **PostgreSQL:** A robust relational database for secure and scalable data storage.

## Why Wagtail?

Wagtail is not just a CMS; it's a Django-based powerhouse that lets you focus on content creation. With its intuitive admin interface and flexibility, Wagtail empowers indie developers to build unique and compelling websites. The seamless integration with Django, coupled with the elegance of the Python language, makes it a delightful choice for those who value simplicity and power in their projects.

## Contributing

If you find a bug, have a feature request, or would like to contribute, please open an issue or submit a pull request. Your contributions are highly welcome!

## License

This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE.md).

Feel free to reach out if you have any questions or need further assistance. Enjoy exploring the blog! 🚀
