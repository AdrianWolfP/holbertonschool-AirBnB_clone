
<h1> Holbertonschool AirBnB Clone - The Console </h1>

<p>
    <img src="https://miro.medium.com/v2/resize:fit:828/0*NChTo-XqLOxLabIW" alt="Logo_Airbnb" loading="lazy" style="" />
</p>


<h3>Description</h3>

<p>A first step with a command interpreter to manage our AirBnB objects. Working towards building our first web application. HTML/CSS templating, datebase storage, API, front-end intergration.</p>

<p>About</p>

<ul>
<li>Parent class(<code>BaseModel</code>) will be doing the initialization, serialization and deserialization of your future instances</li>
<li>A flow of serialization/deserialization: Instance, Dictionary, JSON string, file</li>
<li>All classed made for AirBnB (<code>User</code>), <code>State</code>, <code>City</code>, <code>Place</code> that inherit from <code>BaseModel</code></li>
<li>An abstracted storage engine is made (<code>FileStorage</code>)</li>
<li>Unittest are made to vaildate all the classes and storage engine</li>
</ul>


<h3>Diagram AirBnB clone (The Console)</h3>

<p>
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230615%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230615T210513Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=067d0a1d183e0e3f2cfc218292f4a1339cc1bb3850dcc100b5ab9c3ac17801b8" alt="console_Airbnb" loading="lazy" style="" />
</p>


<h3>Files in the Repositry</h3>

| No. | File               | File Hierarchy                          | Description                                    |
|-----|--------------------|-----------------------------------------|------------------------------------------------|
| 1   | console.py         |                                         | The main console, command interpreter (EOF, all, create, destroy, help, quit, show, update.) |
| 2   | Authors            |                                         | File with the name of Authors                  |                          
| 3   | README.md          |                                         | Readme file proyect                            |
| 4   | '__init__.py'        | models/__init__.py                      | File to mark a directory as a package          |
| 5   | amenity.py         | models/amenity.py                       | The amenity subclass                           |
| 6   | base_model.py      | models/base_model.py                    | Defines all common attributes/methods for other classes |
| 7   | city.py            | models/city.py                           | The city subclass                              |
| 8   | place.py           | models/place.py                          | The place subclass                             |
| 9   | review.py          | models/review.py                         | The review subclass                            |
| 10  | state.py           | models/state.py                          | The state subclass                             |
| 11  | user.py            | models/user.py                           | The user subclass                              |
| 12  | __init__.py        | models/engine/__init__.py                | File to mark a directory as a package          |
| 13  | file_storage.py    | models/engine/file_storage.py            | The file storage class                         |
| 14  | test_amenity.py    | tests/test_models/test_amenity.py        | The unittest module for amenity                |
| 15  | test_base_model.py | tests/test_models/base_model.py          | The unittest module for base model             |
| 16  | test_city.py       | tests/test_models/city.py                | The unittest module for city                   |
| 17  | test_place.py      | tests/test_models/place.py               | The unittest module for place                  |
| 18  | test_review.py     | tests/test_models/review.py              | The unittest module for review                 |
| 19  | test_state.py      | tests/test_models/state.py               | The unittest module for state                  |
| 20  | test_user.py       | tests/test_models/user.py                | The unittest module for user                   |
| 21  | '__init__.py'        | tests/test_models/test_engine/__init__.py | File to mark a directory as a package         |
| 22  | test_file_storage.py| tests/test_models/test_engine/test_file_storage.py | The unittest module for file storage   |

## Commands in terminal

Instructions navigating the application are listed as

| Command | Description |
| ------ | ------|
| Quit | Quits the prompt |
| Help | Display help console |
| Create | Create new object |
| Show | Display info object |
| All | Display all objects |
| Update | Updates object |
| Destroy | Destroy objects |

## AUTHORS

<br>Fox Galileo <5544@holbertonstudents.com>
<br>Wolfgang Pendergrass <6130@holbertonstudents.com>