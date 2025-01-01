## **Ranking Books App**
## **Overview**
RankingBooks is a Flask-based web application designed for managing and ranking a collection of books. Users can add, edit, or delete book entries and update their rankings through an intuitive and interactive interface.

## **Features**
Home Page: Displays all books with their titles, authors, and rankings.
Add Book: Allows users to add new books by specifying the title, author, and ranking.
Edit Book Ranking: Users can update the ranking of an existing book.
Delete Book: Provides an option to remove a book from the list.

## **Technologies Used**
Python (Flask): Backend framework for managing routing and server-side logic.
HTML: For the structure of web pages.
Jinja2: Template engine for rendering dynamic content.
CSS: For styling the application interface.
How to Run the Application
Clone the Repository:

## **File Structure**
app.py: Main Flask application file.
templates/: Contains HTML templates:
index.html: Displays the list of books.
add.html: Form for adding new books.
edit_ranking.html: Form for editing book rankings.

## **Features in Detail**
Dynamic Routing:

/: Displays the list of books.
/add: Provides a form to add new books.
/edit/<id>: Enables editing of book rankings.
/delete/<id>: Deletes a book by its ID.

Interactive Forms:
Input forms are implemented using HTML and Flask request handling for user-friendly interactions.

Data Management:
Simulated data is stored in a Python list for simplicity. For production, this can be replaced with a database (e.g., SQLite, PostgreSQL).

## **Advanced Programming Features**
RESTful Routes: Implements clear and concise URL patterns for CRUD operations.
Template Inheritance: Ensures modular and reusable HTML components with Jinja2.
Dynamic Content Rendering: Leverages Flask and Jinja2 for rendering dynamic book details.
Global Data Management: Uses a Python list to simulate a database for seamless demonstration.

## **Future Enhancements**
Integrate a database for persistent storage.
Add authentication to manage user-specific book lists.
Enable sorting and filtering of books by ranking or author.
Enhance UI/UX with Bootstrap or similar frameworks.
