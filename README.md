# Personal Website README

Welcome to my personal website! This blog, powered by Wagtail CMS, deployed on Fly.io, and utilizing a PostgreSQL database, is designed to provide a genuine and uncluttered experience, fostering creativity and stimulating indie developers. Below, you'll find information on how to set up, run, and contribute to this project.

## Table of Contents

-   [Features](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#features)
-   [Installation](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#installation)
-   [Deployment](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#deployment)
-   [Technology Stack](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#technology-stack)
-   [Why Wagtail?](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#why-wagtail)
-   [Contributing](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#contributing)
-   [License](https://chat.openai.com/c/bca79cba-014c-46f1-a4f1-86b2359d9432#license)

## Features

-   **Unified Blog and Personal Posts:** Share a mix of thoughts, experiences, updates, and personal stories.
-   **Media Galleries:** Showcase personal photos and favorite songs in dedicated galleries.

## Installation

1.  **Clone the Repository:**

    bashCopy code

    `git clone https://github.com/your-username/your-repo.git
    cd your-repo`

2.  **Create Virtual Environment:**

    bashCopy code

    `python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    # OR
    .\venv\Scripts\activate  # For Windows`

3.  **Install Dependencies:**

    bashCopy code

    `pip install -r requirements.txt`

4.  **Database Setup:**

    -   Create a PostgreSQL database.
    -   Update the database settings in `your_project/settings/base.py`.
5.  **Apply Migrations:**

    bashCopy code

    `python manage.py migrate`

6.  **Create Superuser (Admin):**

    bashCopy code

    `python manage.py createsuperuser`

7.  **Run the Development Server:**

    bashCopy code

    `python manage.py runserver`

    Visit `http://127.0.0.1:8000` in your browser to access the local development server.


## Deployment

This blog is designed for easy deployment on platforms like Fly.io. Configure the necessary environment variables for production settings. Consult the platform's documentation for deployment instructions.

## Technology Stack

-   **Wagtail CMS:** Empowering creativity with a Django-based CMS, providing an amazing Python experience.
-   **Fly.io:** A modern platform for deploying and running applications globally.
-   **PostgreSQL:** A robust relational database for secure and scalable data storage.

## Why Wagtail?

Wagtail is not just a CMS; it's a Django-based powerhouse that lets you focus on content creation. With its intuitive admin interface and flexibility, Wagtail empowers indie developers to build unique and compelling websites. The seamless integration with Django, coupled with the elegance of the Python language, makes it a delightful choice for those who value simplicity and power in their projects.

## Contributing

If you find a bug, have a feature request, or would like to contribute, please open an issue or submit a pull request. Your contributions are highly welcome!

## License

This project is licensed under the [MIT License](https://chat.openai.com/c/LICENSE.md).

Feel free to reach out if you have any questions or need further assistance. Enjoy exploring the blog! 🚀
