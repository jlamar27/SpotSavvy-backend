# Spot Savvy
Spot Savvy is a web application that aims to provide users with a platform to discover and review businesses and restaurants in their area. This README will provide an overview of our goals and stretch goals, helping you understand the key features and functionalities of the application.

## Wire Frames

**Login Page**
![image](./images/log%20in%20page.png)

**Home Page**
![image](./images/home%20page.png)

## Backend Deployed Link

https://spot-savvy-backend-5923f47503b2.herokuapp.com/api


## How to work on this App
this app let users create their own account. Once an account is created the user will be able to look for a restaurant that they like and can leave a review on the restraurant , bars and shopping locations. The user will be able to delete , update the review when needed.

## Technologies Used


![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## API Endpoints

### Authentication and CSRF
- **GET** `/get-csrf-token/`: Retrieve a CSRF token.
- **POST** `/signup/`: Register a new user.
- **POST** `/login/`: Authenticate a user.
- **POST** `/logout/`: Log out the user.

### Reviews
- **GET** `/reviews/<str:restaurant_id>/`: Get reviews for a restaurant.
- **POST** `/review/create/`: Create a new review.
- **PUT** `/review/edit/<uuid:pk>/`: Edit a review.
- **DELETE** `/review/delete/<uuid:pk>/`: Delete a review.

### User Schema
- **ID**: Integer (Auto-generated primary key)
- **Username**: String (Inherited from `AbstractUser`)
- **Password**: String (Inherited from `AbstractUser`, encrypted representation of the user password)
- **Location**: String (User's location)

```python
class User(AbstractUser):
    location = models.CharField(max_length=100)

### Review Schema
- **ID**: UUID (Unique identifier for the review)
- **Restaurant_ID**: String (Identifier for the restaurant being reviewed)
- **User**: ForeignKey (Reference to the user who wrote the review)
- **Rating**: Integer (Rating given to the restaurant)
- **Text**: String (Review text/content)
- **Date**: DateTime (Date when the review was created)

```python
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_id = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

## MVP Goals
### 1. User Registration
- Users can create a new account by providing their username, password, and location.
- Personalized user accounts allow for a tailored experience within the app.
### 2. User Authentication
- Registered users can log in with their username and password to access their accounts.
- Authentication ensures that user data remains secure and private.
### 3. Business/Restaurant Search
- Users can search for businesses or restaurants based on specific criteria.
- Search functionality helps users find relevant listings quickly.
### 4. Business/Restaurant Details
- Users can view detailed information about a selected business or restaurant.
- Information includes the business's name, address, phone number, website, and user reviews.
### 5. User Reviews
- Users can read reviews written by other users about a particular business or restaurant.
- Access to reviews helps users make informed decisions about where to visit.
### 6. User Review Submission
- Users can write and submit their own reviews for businesses or restaurants.
- Allows users to contribute their opinions and experiences to the platform.
### 7. Rating System
- Users can rate businesses or restaurants on a scale from 1 to 5 stars.
- Ratings provide a quick summary of user satisfaction.
### 8. Review Management
- Users can create, read, update, and delete their own reviews.
- Ensures that users have control over their contributions.
## Stretch Goals/Icebox
### 1. Favorites List
- Users can save their favorite businesses or restaurants to a "Favorites" list.
- Convenient access to preferred places for future visits.
### 2. GPS Navigation
- Users can get directions to a business or restaurant using integrated map and GPS navigation features.
- Enhances user experience when visiting new places.
### 3. Recommendation Engine
- Users receive personalized recommendations for businesses or restaurants based on their previous reviews and ratings.
- Helps users discover new places that match their preferences.
### 4. Search Enhancements
- Implement autocomplete and suggestions in the search bar to streamline the search process.
- Provides a user-friendly and efficient search experience.
## Getting Started
To get started with YelpClone, follow these steps:
1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Set up your database and apply migrations using `python manage.py migrate`.
4. Create a superuser account for admin access with `python manage.py createsuperuser`.
5. Start the development server with `python manage.py runserver`.
## Usage
1. Visit the application in your web browser.
2. Register or log in to your account.
3. Search for businesses or restaurants based on your preferences.
4. Explore detailed listings and read reviews.
5. Write and submit your own reviews and ratings.
6. Manage your reviews through the user-friendly interface.

## Contributors
- [Zubin Sood](https://www.linkedin.com/in/zubinsood/)
- [Tenzing Lhagyal](https://www.linkedin.com/in/tenzing-lhagyal/)
- [Josh Morgan](https://www.linkedin.com/in/joshmorgan1992/)
- [Juan Lamar](https://www.linkedin.com/in/juanlamar/)
- [Naischa Suriel](https://www.linkedin.com/in/naischa-suriel/)
- [Emre Surmeli](https://www.linkedin.com/in/emresurmeli/)
- [Gregorio Moreta](https://www.linkedin.com/in/gregorio-moreta/)
- [Santiago Dimaren](https://www.linkedin.com/in/santiago-dimaren/)
## Acknowledgments
- This project is inspired by Yelp, a popular platform for discovering and reviewing local businesses.

