# sarthi_rest_api
Sarthi.ai assignment to develop a book api with CRUD operation using Django framework

Download link -  https://github.com/PratyushPratapSingh/sarthi_rest_api.git

Pay special attention for isbn of books because it shoud be uniquely defined not every 3 digit with 10 digit separated is isbn number.

1.  I have developed my own api and use insert book using CRUD operation and you can access using adding "/api/"

2.  To check the api visit my hosted book-api on Heroku - https://sarthibookapi.herokuapp.com

3.  After visit the site add "  '/api/' to  the existing URL" check the working 

4.  for different condition as mention my project not exactly the same detto 

5.  you can check this api for different book id like adding "/api/1"   or "/api/2" depending on the inserted books if book is not available it shows we can't found book with id "4" because I have inserted only two books

6.  After visiting let say "https://sarthibookapi.herokuapp.com/api/1" you can update and delete the book

7. On testing on local machine please install the specific version of the libraries to work smoothly because some of the latest one is not work properly like in my case waitress==2.0.0 is not working but waitress==1.4.4 is working smoothly











Enjoy Testing the Api :)

Introduction
This is a short coding assignment, in which you will implement a REST API that calls an external API service to get information about books. Additionally, you will implement a simple CRUD (Create, Read, Update, Delete) API with a local database of your choice.
The external API that will be used here is the Ice And Fire API. This API requires no sign up / authentication on your part. 
Ground Rules
You may use any python framework you like or no framework at all.
You may use any web server you like.
Your solution should be submitted as a link to a GitHub repository containing a README file written in English.
We should be able to verify your submission by cloning your repository, configure the environment and running the application. Please document all details about project setup in the README file.
We estimate that this test should take roughly 4-5 hours to complete.
Requirements to Implement
Your solution should provide an implementation for each of the following requirements. The tasks will be tested with the specified endpoints while expecting the specified JSON.
Requirement 1
When the endpoint:
GET http://localhost:8080/api/external-books?name=:nameOfABook
is requested, your application should query the Ice And Fire API and use the data received to respond with precisely the following JSON if there are results:
[
    "status_code": 200,
    "status": "success",
    "data": [
        {
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1996-08-01",
        },
        {
            "name": "A Clash of Kings",
            "isbn": "978-0553108033",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 768,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1999-02-02",
        }
    ]
]
or precisely this JSON if the Ice and Fire API returns no results:
{
    "status_code": 200,
    "status": "success",
    "data": []
}


where :nameOfABook is a variable. Example value for :nameOfABook can be A Game Of Thrones.
Note that the JSON property names that Ice And Fire uses don't quite match the ones in the required output that your application needs to deliver, so pay attention to this. Also, not all of the output from Ice And Fire is required in your application's output - you may need to suppress some field(s).
Requirement 2
Create
When the endpoint:
POST http://localhost:8080/api/v1/books
is requested with the following data:
name
isbn
authors
country
number_of_pages
publisher
release_date
a book should be created in the local database and the following response should be returned:
[
    "status_code": 201,
    "status": "success",
    "data": [
        "book": {
            "name": "My First Book",
            "isbn": "123-3213243567",
            "authors": [
                "John Doe"
            ],
            "number_of_pages": 350,
            "publisher": "Acme Books",
            "country": "United States",
            "release_date": "2019-08-01",
        },
    ]
]
Read
When the endpoint:
GET http://localhost:8080/api/v1/books
is requested, your solution will return a list of books from the local database using the following response:
[
    "status_code": 200,
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 694,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1996-08-01",
        },
        {
            "id": 2,
            "name": "A Clash of Kings",
            "isbn": "978-0553108033",
            "author": [
                "George R. R. Martin"
            ],
            "number_of_pages": 768,
            "publisher": "Bantam Books",
            "country": "United States",
            "release_date": "1999-02-02",
        }
    ]
]
or precisely this JSON if the Books API returns no results:
{
    "status_code": 200,
    "status": "success",
    "data": []
}
The Books API should be searchable by name (string), country (string), publisher (string) and release date (year, integer).
Update
When the endpoint:
PATCH http://localhost:8080/api/v1/books/:id
is requested with any of the following form data:
name
isbn
authors
country
number_of_pages
publisher
release_date
and a specific :id in the URL, where :id is a placeholder variable for an integer (for example 1), the specific book should be updated in the database and the following response should be returned:
[
    "status_code": 200,
    "status": "success",
    "message": "The book My First Book was updated successfully",
    "data": {
        "id": 1,
        "name": "My First Updated Book",
        "isbn": "123-3213243567",
        "authors": [
            "John Doe"
        ],
        "number_of_pages": 350,
        "publisher": "Acme Books Publishing",
        "country": "United States",
        "release_date": "2019-01-01",
    }
]
An alternative endpoint for updating books if you are not using a framework should be:
POST http://localhost:8080/api/v1/books/:id/update
Delete
When the endpoint:
DELETE http://localhost:8080/api/v1/books/:id
is requested with a specific :id in the URL, where :id is a placeholder variable for an integer (for example 1), the specific book should be deleted from the database and the following response will be returned:
[
    "status_code": 204,
    "status": "success",
    "message": "The book My First Book was deleted successfully",
    "data": []
]
An alternative endpoint for deleting a book could be:
POST http://localhost:8080/api/v1/books/:id/delete
Show
When the endpoint:
GET http://localhost:8080/api/v1/books/:id
is requested with a specific :id in the URL, where :id is a placeholder variable for an integer (for example 1), it should show the specific book and the following response will be returned:
[
    "status_code": 200,
    "status": "success",
    "data": {
        "id": 1,
        "name": "My First Book",
        "isbn": "123-3213243567",
        "authors": [
            "John Doe"
        ],
        "number_of_pages": 350,
        "publisher": "Acme Books Publishing",
        "country": "United States",
        "release_date": "2019-01-01",
    }
]
