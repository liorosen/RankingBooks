## **Ranking Books App**
## **Overview**
RankingBooks is a Flask-based web application designed for managing and ranking a collection of books. Users can add, edit, or delete book entries and update their rankings through an intuitive and interactive interface.

## **Features**
Home Page: Displays all books with their titles, authors, and rankings.<br>
Add Book: Allows users to add new books by specifying the title, author, and ranking.<br>
Edit Book Ranking: Users can update the ranking of an existing book.<br>
Delete Book: Provides an option to remove a book from the list.<br>

## **Technologies Used**
Python (Flask): Backend framework for managing routing and server-side logic.<br>
HTML: For the structure of web pages.<br>
Jinja2: Template engine for rendering dynamic content.<br>
CSS: For styling the application interface.<br>

## **File Structure**
app.py: Main Flask application file.<br>
templates/: Contains HTML templates.<br>
index.html: Displays the list of books.<br>
add.html: Form for adding new books.<br>
edit_ranking.html: Form for editing book rankings.<br>

## **Features in Detail**
Dynamic Routing:

/: Displays the list of books.<br>
/add: Provides a form to add new books.<br>
/edit/<id>: Enables editing of book rankings.<br>
/delete/<id>: Deletes a book by its ID.<br>

Interactive Forms:
Input forms are implemented using HTML and Flask request handling for user-friendly interactions.<br>

Data Management:
Simulated data is stored in a Python list for simplicity. For production, this can be replaced with a database (e.g., SQLite, PostgreSQL).<br>

## **Advanced Programming Features**
RESTful Routes: Implements clear and concise URL patterns for CRUD operations.<br>
Template Inheritance: Ensures modular and reusable HTML components with Jinja2.<br>
Dynamic Content Rendering: Leverages Flask and Jinja2 for rendering dynamic book details.<br>
Global Data Management: Uses a Python list to simulate a database for seamless demonstration.<br>

## **Future Enhancements**
Integrate a database for persistent storage.<br>
Add authentication to manage user-specific book lists.<br>
Enable sorting and filtering of books by ranking or author.<br>
Enhance UI/UX with Bootstrap or similar frameworks.<br>
