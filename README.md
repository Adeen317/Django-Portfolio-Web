# Django-Portfolio-Web
Certainly, here are the steps to create a folder, set up a virtual environment, install Django, create a Django project, and run the development server:

1. **Create a Folder**: First, create a new directory for your Django project. You can do this by opening your file explorer and right-clicking to create a new folder. Name it something relevant to your project.

2. **Open Command Prompt in the Folder**: Now, navigate to the folder you just created in Command Prompt. You can do this by opening Command Prompt, using the 'cd' command to change directories to your project folder, or you can use the 'cd' command followed by the folder's path.

3. **Set Up a Virtual Environment**: In your Command Prompt, use the following command to create a virtual environment named 'my_env':
   
   ```
   python -m venv my_env
   ```

   Activate the virtual environment:
   
   ```
   my_env\Scripts\activate
   ```

4. **Install Django**: With the virtual environment activated, install Django using pip:

   ```
   pip install django
   ```

5. **Create a Django Project**: To start a new Django project, run the following command, replacing 'my_project' with your desired project name:

   ```
   django-admin startproject my_project
   ```

6. **Navigate to Your Project Folder**: Change to the project directory using the 'cd' command:

   ```
   cd my_project
   ```

7. **Run the Development Server**: Finally, start the Django development server:

   ```
   python manage.py runserver
   ```

   This will display a URL, typically `http://127.0.0.1:8000/`, in the command prompt.

8. **Access the Development Server**: Copy the URL displayed in the command prompt and paste it into your web browser to access your Django project.

These steps will help you create a clean development environment and get your Django project up and running professionally.
![My Portfolio](https://github.com/Adeen317/Django-Portfolio-Web/assets/112985225/f2048cb8-4c79-4895-ae4a-f1047c63d753)
