## **Ranking Books App**
## **Overview**
RankingBooks is a Flask-based web application designed for managing and ranking a collection of books. Users can add, edit, or delete book entries and update their rankings through an intuitive and interactive interface.

## **Features**
Home Page: Displays all books with their titles, authors, and rankings.<br>
Add Book: Allows users to add new books by specifying the title, author, and ranking.<br>
Edit Book Ranking: Users can update the ranking of an existing book.<br>
Delete Book: Provides an option to remove a book from the list.<br>
 
## **Technologies Used**
<ins>Python (Flask)</ins>: Backend framework for managing routing and server-side logic.<br>
<ins>HTML</ins>: For the structure of web pages.<br>
<ins>Jinja2</ins>: Template engine for rendering dynamic content.<br>
<ins>CSS</ins>: For styling the application interface.<br>

## **File Structure**
app.py: Main Flask application file.<br>
templates/: Contains HTML templates.<br>
index.html: Displays the list of books.<br>
add.html: Form for adding new books.<br>
edit_ranking.html: Form for editing book rankings.<br>

## **Features in Detail**
<ins>Dynamic Routing:</ins>

/: Displays the list of books.<br>
/add: Provides a form to add new books.<br>
/edit/<id>: Enables editing of book rankings.<br>
/delete/<id>: Deletes a book by its ID.<br>

<ins>Interactive Forms:</ins>
Input forms are implemented using HTML and Flask request handling for user-friendly interactions.<br>

<ins>Data Management:</ins>
Simulated data is stored in a Python list for simplicity. For production, this can be replaced with a database (e.g., SQLite, PostgreSQL).<br>

## **Advanced Programming Features**
<ins>RESTful Routes:</ins> Implements clear and concise URL patterns for CRUD operations.<br>
<ins>Template Inheritance:</ins> Ensures modular and reusable HTML components with Jinja2.<br>
<ins>Dynamic Content Rendering:</ins> Leverages Flask and Jinja2 for rendering dynamic book details.<br>
<ins>Global Data Management:</ins> Uses a Python list to simulate a database for seamless demonstration.<br>

## **Future Enhancements**
Integrate a database for persistent storage.<br>
Add authentication to manage user-specific book lists.<br>
Enable sorting and filtering of books by ranking or author.<br>
Enhance UI/UX with Bootstrap or similar frameworks.<br>
